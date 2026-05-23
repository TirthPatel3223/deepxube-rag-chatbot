"""
DeepXube documentation extractor — v1.0

Produces, from a list of .py files:
  docs/functions/<module>/<Class>/<func>.md   (one per non-trivial function/method)
  docs/classes/<module>/<Class>.md            (one per class)
  docs/modules/<module>.md                    (one per module)
  docs/graph.json                             (merged knowledge graph)
  docs/cli_flags.json                         (factory keys + dispatch rules)
  docs/missing_docstrings.md                  (gap report)
  docs/skipped_trivial.md                     (skipped-function log)

Run from deepxube-main/:
    python docs/extractor/extract.py --scope docs/extractor/poc_scope.txt
"""

from __future__ import annotations

import argparse
import ast
import builtins as _builtins
import json
import os
import sys
import textwrap
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

SCHEMA_VERSION = "1.0"

BUILTIN_NAMES: Set[str] = set(dir(_builtins)) | {
    "print", "len", "range", "enumerate", "zip", "min", "max", "sum", "abs",
    "round", "sorted", "reversed", "map", "filter", "any", "all", "iter", "next",
    "isinstance", "issubclass", "type", "id", "hash", "hasattr", "getattr",
    "setattr", "delattr", "callable", "repr", "format", "vars", "dir",
    "str", "int", "float", "bool", "list", "tuple", "dict", "set", "frozenset",
    "bytes", "bytearray", "complex", "object", "super",
}


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Param:
    name: str
    annotation: Optional[str]
    default: Optional[str]


@dataclass
class CalleeRef:
    target: Optional[str]          # resolved node id, or None if unresolved
    expr: str                      # original source expression
    call_sites: List[int] = field(default_factory=list)


@dataclass
class RaiseRef:
    exception: str                 # exception class name
    call_sites: List[int] = field(default_factory=list)


@dataclass
class FunctionInfo:
    id: str
    kind: str                      # function | method | staticmethod | classmethod
    name: str
    qualified_name: str
    module: str
    file: str
    line_start: int
    line_end: int
    class_name: Optional[str]
    visibility: str                # public | private | dunder
    is_abstract: bool
    is_generator: bool
    is_async: bool
    decorators: List[str]
    parameters: List[Param]
    returns: Optional[str]
    docstring: Optional[str]
    docstring_source: str          # present | missing
    source: str
    callees: List[CalleeRef] = field(default_factory=list)
    raises: List[RaiseRef] = field(default_factory=list)
    reads_attrs: List[str] = field(default_factory=list)
    writes_attrs: List[str] = field(default_factory=list)
    trivial: bool = False
    trivial_reason: Optional[str] = None


@dataclass
class ClassInfo:
    id: str
    name: str
    qualified_name: str
    module: str
    file: str
    line_start: int
    line_end: int
    is_abstract: bool
    is_dataclass: bool
    decorators: List[str]
    generic_parameters: List[str]
    bases: List[Dict[str, Optional[str]]]   # [{name, resolved_id}]
    methods: List[str] = field(default_factory=list)  # method ids
    attributes: List[Dict[str, Optional[str]]] = field(default_factory=list)
    factory_registrations: List[Dict[str, str]] = field(default_factory=list)
    docstring: Optional[str] = None
    docstring_source: str = "missing"
    source: str = ""


@dataclass
class ModuleInfo:
    id: str
    name: str
    qualified_name: str
    file: str
    line_count: int
    docstring: Optional[str]
    docstring_source: str
    imports: List[Dict[str, object]]
    classes: List[str]
    module_level_functions: List[str]
    module_level_constants: List[Dict[str, Optional[str]]]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def rel_posix(path: Path, base: Path) -> str:
    return path.resolve().relative_to(base.resolve()).as_posix()


def ann_to_str(node: Optional[ast.AST]) -> Optional[str]:
    if node is None:
        return None
    try:
        return ast.unparse(node)
    except Exception:
        return None


def path_to_module(file_rel: str) -> str:
    # e.g. "deepxube/base/updater.py" -> "deepxube.base.updater"
    assert file_rel.endswith(".py")
    return file_rel[:-3].replace("/", ".")


def visibility_of(name: str) -> str:
    if name.startswith("__") and name.endswith("__"):
        return "dunder"
    if name.startswith("_"):
        return "private"
    return "public"


def get_docstring(node: ast.AST) -> Optional[str]:
    return ast.get_docstring(node)


def extract_decorators(decorators: List[ast.expr]) -> List[str]:
    out: List[str] = []
    for dec in decorators:
        try:
            out.append("@" + ast.unparse(dec))
        except Exception:
            out.append("@<unparseable>")
    return out


def extract_params(args: ast.arguments) -> List[Param]:
    # positional + vararg + kwonly + kwarg, with defaults
    params: List[Param] = []

    pos_args = args.posonlyargs + args.args
    defaults = [None] * (len(pos_args) - len(args.defaults)) + args.defaults
    for a, d in zip(pos_args, defaults):
        params.append(
            Param(
                name=a.arg,
                annotation=ann_to_str(a.annotation),
                default=(ast.unparse(d) if d is not None else None),
            )
        )
    if args.vararg:
        params.append(
            Param(
                name="*" + args.vararg.arg,
                annotation=ann_to_str(args.vararg.annotation),
                default=None,
            )
        )
    for a, d in zip(args.kwonlyargs, args.kw_defaults):
        params.append(
            Param(
                name=a.arg,
                annotation=ann_to_str(a.annotation),
                default=(ast.unparse(d) if d is not None else None),
            )
        )
    if args.kwarg:
        params.append(
            Param(
                name="**" + args.kwarg.arg,
                annotation=ann_to_str(args.kwarg.annotation),
                default=None,
            )
        )
    return params


def get_source_segment(src_lines: List[str], lineno: int, end_lineno: int) -> str:
    return "\n".join(src_lines[lineno - 1 : end_lineno])


# ---------------------------------------------------------------------------
# Import index — per-file map name -> dotted target
# ---------------------------------------------------------------------------

class ImportIndex:
    """For a single module, resolve a bare name to its imported origin."""

    def __init__(self, module_qname: str):
        self.module_qname = module_qname
        # short_name -> full dotted target (e.g. "np" -> "numpy")
        # and for "from X import Y", Y -> "X.Y"
        self.name_to_target: Dict[str, str] = {}
        self.imports_raw: List[Dict[str, object]] = []

    def visit(self, node: ast.AST) -> None:
        for n in ast.iter_child_nodes(node):
            if isinstance(n, ast.Import):
                for alias in n.names:
                    key = alias.asname or alias.name.split(".")[0]
                    self.name_to_target[key] = alias.name
                    self.imports_raw.append(
                        {"kind": "import", "module": alias.name, "alias": alias.asname}
                    )
            elif isinstance(n, ast.ImportFrom):
                src_mod = n.module or ""
                names = []
                for alias in n.names:
                    key = alias.asname or alias.name
                    target = f"{src_mod}.{alias.name}" if src_mod else alias.name
                    self.name_to_target[key] = target
                    names.append({"name": alias.name, "alias": alias.asname})
                self.imports_raw.append(
                    {"kind": "from", "module": src_mod, "names": names}
                )

    def resolve(self, name: str) -> Optional[str]:
        return self.name_to_target.get(name)


# ---------------------------------------------------------------------------
# Per-file extraction
# ---------------------------------------------------------------------------

# Globals across files (populated during scan)
MODULES: Dict[str, ModuleInfo] = {}
CLASSES: Dict[str, ClassInfo] = {}                  # qualified_name -> ClassInfo
FUNCTIONS: Dict[str, FunctionInfo] = {}             # id -> FunctionInfo
FACTORY_REGISTRATIONS: List[Dict[str, str]] = []
FACTORY_OBJECTS: Dict[str, Dict[str, object]] = {}  # dotted path -> info


def find_factory_instances(tree: ast.Module, module_qname: str) -> None:
    """Find `updater_factory: Factory[Update] = Factory[Update]("Update")` style lines."""
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            ann = ann_to_str(node.annotation) or ""
            if ann.startswith("Factory["):
                dotted = f"{module_qname}.{node.target.id}"
                class_type = ann[len("Factory[") : -1] if ann.endswith("]") else None
                FACTORY_OBJECTS[dotted] = {
                    "id": f"factory:{dotted}",
                    "name": node.target.id,
                    "module": module_qname,
                    "class_type": class_type,
                    "registered_keys": [],
                    "key_to_class": {},
                }
        elif isinstance(node, ast.Assign):
            # fallback without annotation
            if (
                len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and isinstance(node.value, ast.Call)
            ):
                func = node.value.func
                func_str = ann_to_str(func) or ""
                if func_str.startswith("Factory"):
                    dotted = f"{module_qname}.{node.targets[0].id}"
                    FACTORY_OBJECTS.setdefault(
                        dotted,
                        {
                            "id": f"factory:{dotted}",
                            "name": node.targets[0].id,
                            "module": module_qname,
                            "class_type": None,
                            "registered_keys": [],
                            "key_to_class": {},
                        },
                    )


def decorator_is_factory_register(
    dec: ast.expr, imports: ImportIndex
) -> Optional[Tuple[str, str]]:
    """If dec is `@X.register_class("name")`, return (factory_dotted, key)."""
    if not isinstance(dec, ast.Call):
        return None
    func = dec.func
    if not isinstance(func, ast.Attribute) or func.attr != "register_class":
        return None
    # target is the name before .register_class
    base = func.value
    if not isinstance(base, ast.Name):
        return None
    # Resolve the factory name via imports
    factory_import = imports.resolve(base.id)
    if factory_import is None:
        # factory defined in same module
        factory_dotted = f"{imports.module_qname}.{base.id}"
    else:
        factory_dotted = factory_import
    if not dec.args or not isinstance(dec.args[0], ast.Constant):
        return None
    key = dec.args[0].value
    if not isinstance(key, str):
        return None
    return factory_dotted, key


def decorator_is_abstract(dec: ast.expr) -> bool:
    expr = ann_to_str(dec) or ""
    return expr == "abstractmethod" or expr.endswith(".abstractmethod")


def decorator_is_dataclass(dec: ast.expr) -> bool:
    expr = ann_to_str(dec) or ""
    return expr == "dataclass" or expr.endswith(".dataclass")


def decorator_is_staticmethod(dec: ast.expr) -> bool:
    return (ann_to_str(dec) or "") == "staticmethod"


def decorator_is_classmethod(dec: ast.expr) -> bool:
    return (ann_to_str(dec) or "") == "classmethod"


# ---------------------------------------------------------------------------
# Function body analysis: callees, raises, attrs, trivial
# ---------------------------------------------------------------------------

class BodyAnalyzer(ast.NodeVisitor):
    def __init__(self, imports: ImportIndex, module_qname: str, class_name: Optional[str]):
        self.imports = imports
        self.module_qname = module_qname
        self.class_name = class_name
        self.callees: List[CalleeRef] = []
        self.raises: List[RaiseRef] = []
        self.reads_attrs: Set[str] = set()
        self.writes_attrs: Set[str] = set()
        self.stmt_count = 0
        self.has_control_flow = False
        self._in_assign_target = False
        # attributes used as the func of a Call (`self.foo(...)`) — exclude from reads_attrs
        self._attrs_as_call_target: Set[str] = set()

    def _resolve_call_target(self, func: ast.expr) -> Tuple[Optional[str], str]:
        expr = ann_to_str(func) or "<?>"

        # self.method() / cls.method()
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            if func.value.id in ("self", "cls") and self.class_name is not None:
                return f"func:{self.module_qname}.{self.class_name}.{func.attr}", expr

            # <imported_or_local>.method()
            resolved_module = self.imports.resolve(func.value.id)
            if resolved_module is not None:
                # resolved_module could be a module (e.g. "numpy") or a class (e.g. "deepxube.X.Foo")
                # We produce a best-effort id; the graph-build step will decide class vs func.
                return f"ref:{resolved_module}.{func.attr}", expr
            else:
                # local name — could be module-level function in same file
                candidate = f"func:{self.module_qname}.{func.attr}"
                if func.value.id == self.module_qname.split(".")[-1]:
                    return candidate, expr
                # Unknown — likely a local variable's method. Leave unresolved.
                return None, expr

        # bareword() -> module-level function or imported
        if isinstance(func, ast.Name):
            # skip builtins — they're not project functions
            if func.id in BUILTIN_NAMES:
                return None, expr
            resolved = self.imports.resolve(func.id)
            if resolved is not None:
                return f"func:{resolved}", expr
            # same-module function
            return f"func:{self.module_qname}.{func.id}", expr

        # anything else (chained, subscript, etc.) -> unresolved
        return None, expr

    def _add_call(self, func: ast.expr, lineno: int) -> None:
        target, expr = self._resolve_call_target(func)
        # collapse duplicates by (target, expr)
        for c in self.callees:
            if c.target == target and c.expr == expr:
                if lineno not in c.call_sites:
                    c.call_sites.append(lineno)
                return
        self.callees.append(CalleeRef(target=target, expr=expr, call_sites=[lineno]))

    def generic_visit(self, node: ast.AST) -> None:
        # count statements at any nesting for triviality
        if isinstance(node, ast.stmt) and not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            self.stmt_count += 1
        if isinstance(node, (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.With, ast.AsyncWith, ast.Match)):
            self.has_control_flow = True
        super().generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        self._add_call(node.func, node.lineno)
        # Track self.foo attribute access that is actually a method call, so we
        # can exclude it from reads_attrs.
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
            self._attrs_as_call_target.add(f"self.{node.func.attr}")
        self.generic_visit(node)

    def visit_Raise(self, node: ast.Raise) -> None:
        exc = node.exc
        exc_name = "Exception"
        if isinstance(exc, ast.Call) and isinstance(exc.func, ast.Name):
            exc_name = exc.func.id
        elif isinstance(exc, ast.Name):
            exc_name = exc.id
        # dedupe
        for r in self.raises:
            if r.exception == exc_name:
                if node.lineno not in r.call_sites:
                    r.call_sites.append(node.lineno)
                self.generic_visit(node)
                return
        self.raises.append(RaiseRef(exception=exc_name, call_sites=[node.lineno]))
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        # self.foo reads
        if isinstance(node.value, ast.Name) and node.value.id == "self":
            self.reads_attrs.add(f"self.{node.attr}")
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        for tgt in node.targets:
            if isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name) and tgt.value.id == "self":
                self.writes_attrs.add(f"self.{tgt.attr}")
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if isinstance(node.target, ast.Attribute) and isinstance(node.target.value, ast.Name) and node.target.value.id == "self":
            self.writes_attrs.add(f"self.{node.target.attr}")
        self.generic_visit(node)


def is_trivial(fn: FunctionInfo) -> Tuple[bool, Optional[str]]:
    """Trivial iff: ≤3 stmts AND no control flow AND no calls to project functions.
    Calls to builtins + self.<attr> access don't disqualify. We approximate:
    trivial = no callees whose target starts with 'func:' or 'ref:'.
    """
    # find function body analyzer info via attached fields
    reasons = []
    if fn.name in ("__repr__", "__str__", "__hash__", "__eq__") and fn.line_end - fn.line_start <= 3:
        return True, "dunder one-liner"
    # we expect analyzer-attached stmt_count / has_control_flow / project_callees -
    # stored as synthetic attrs on fn
    stmt_count = getattr(fn, "_stmt_count", 999)
    cf = getattr(fn, "_has_cf", True)
    project_callees = [c for c in fn.callees if c.target is not None]
    if stmt_count <= 3 and not cf and not project_callees:
        return True, f"≤3 stmts, no control flow, no project calls"
    return False, None


# ---------------------------------------------------------------------------
# File walker
# ---------------------------------------------------------------------------

def process_file(py_path: Path, repo_root: Path) -> None:
    file_rel = rel_posix(py_path, repo_root)
    module_qname = path_to_module(file_rel)
    src = py_path.read_text(encoding="utf-8")
    src_lines = src.splitlines()
    tree = ast.parse(src, filename=str(py_path))

    imports = ImportIndex(module_qname)
    imports.visit(tree)

    find_factory_instances(tree, module_qname)

    # Module info
    mod_doc = get_docstring(tree)
    module = ModuleInfo(
        id=f"module:{module_qname}",
        name=module_qname.split(".")[-1],
        qualified_name=module_qname,
        file=file_rel,
        line_count=len(src_lines),
        docstring=mod_doc,
        docstring_source="present" if mod_doc else "missing",
        imports=imports.imports_raw,
        classes=[],
        module_level_functions=[],
        module_level_constants=[],
    )

    # First pass: classes + module-level functions + constants
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            cinfo = handle_class(node, module_qname, file_rel, src_lines, imports)
            module.classes.append(cinfo.id)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fn = handle_function(
                node,
                module_qname=module_qname,
                file_rel=file_rel,
                src_lines=src_lines,
                imports=imports,
                class_name=None,
            )
            module.module_level_functions.append(fn.id)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            module.module_level_constants.append(
                {
                    "name": node.target.id,
                    "annotation": ann_to_str(node.annotation),
                    "value_expr": ann_to_str(node.value) if node.value is not None else None,
                }
            )
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    module.module_level_constants.append(
                        {
                            "name": tgt.id,
                            "annotation": None,
                            "value_expr": ann_to_str(node.value),
                        }
                    )

    MODULES[module_qname] = module


def handle_class(
    node: ast.ClassDef,
    module_qname: str,
    file_rel: str,
    src_lines: List[str],
    imports: ImportIndex,
) -> ClassInfo:
    qname = f"{module_qname}.{node.name}"
    class_id = f"class:{qname}"

    bases: List[Dict[str, Optional[str]]] = []
    generics: List[str] = []
    for b in node.bases:
        b_str = ann_to_str(b) or ""
        bases.append({"name": b_str, "resolved_id": None})
        # collect TypeVar-like generic params from Generic[...]
        if b_str.startswith("Generic["):
            inside = b_str[len("Generic[") : -1]
            generics = [p.strip() for p in inside.split(",") if p.strip()]

    decs = extract_decorators(node.decorator_list)
    is_dc = any(decorator_is_dataclass(d) for d in node.decorator_list)

    # factory registrations from decorators
    factory_regs: List[Dict[str, str]] = []
    for d in node.decorator_list:
        res = decorator_is_factory_register(d, imports)
        if res is not None:
            factory_dotted, key = res
            factory_regs.append({"factory": factory_dotted, "key": key})
            FACTORY_REGISTRATIONS.append(
                {"class_id": class_id, "factory": factory_dotted, "key": key}
            )
            # keep factory registry up to date
            if factory_dotted in FACTORY_OBJECTS:
                f = FACTORY_OBJECTS[factory_dotted]
                f["registered_keys"].append(key)
                f["key_to_class"][key] = class_id

    # Check for abstract: any abstractmethod method OR ABC base
    has_abstract_method = any(
        isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef))
        and any(decorator_is_abstract(d) for d in m.decorator_list)
        for m in node.body
    )
    is_abstract = has_abstract_method or any(
        (ann_to_str(b) or "") in ("ABC", "abc.ABC") for b in node.bases
    )

    src = get_source_segment(src_lines, node.lineno, node.end_lineno or node.lineno)

    cinfo = ClassInfo(
        id=class_id,
        name=node.name,
        qualified_name=qname,
        module=module_qname,
        file=file_rel,
        line_start=node.lineno,
        line_end=node.end_lineno or node.lineno,
        is_abstract=is_abstract,
        is_dataclass=is_dc,
        decorators=decs,
        generic_parameters=generics,
        bases=bases,
        methods=[],
        attributes=[],
        factory_registrations=factory_regs,
        docstring=get_docstring(node),
        docstring_source="present" if get_docstring(node) else "missing",
        source=src,
    )
    CLASSES[qname] = cinfo

    # Collect dataclass / class-body annotated attributes
    for stmt in node.body:
        if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            cinfo.attributes.append(
                {
                    "name": stmt.target.id,
                    "annotation": ann_to_str(stmt.annotation),
                    "default": ann_to_str(stmt.value) if stmt.value is not None else None,
                    "from": "class_body",
                }
            )

    # Methods
    for stmt in node.body:
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fn = handle_function(
                stmt,
                module_qname=module_qname,
                file_rel=file_rel,
                src_lines=src_lines,
                imports=imports,
                class_name=node.name,
            )
            cinfo.methods.append(fn.id)

            # attributes from __init__ writes
            if stmt.name == "__init__":
                for w in fn.writes_attrs:
                    cinfo.attributes.append(
                        {
                            "name": w,
                            "annotation": None,
                            "default": None,
                            "from": "__init__",
                        }
                    )

    return cinfo


def handle_function(
    node,
    *,
    module_qname: str,
    file_rel: str,
    src_lines: List[str],
    imports: ImportIndex,
    class_name: Optional[str],
) -> FunctionInfo:
    decs_list = node.decorator_list
    decs = extract_decorators(decs_list)
    is_static = any(decorator_is_staticmethod(d) for d in decs_list)
    is_class = any(decorator_is_classmethod(d) for d in decs_list)
    is_abstract = any(decorator_is_abstract(d) for d in decs_list)

    if class_name is None:
        kind = "function"
        qname = f"{module_qname}.{node.name}"
    else:
        if is_static:
            kind = "staticmethod"
        elif is_class:
            kind = "classmethod"
        else:
            kind = "method"
        qname = f"{module_qname}.{class_name}.{node.name}"

    fn_id = f"func:{qname}"
    params = extract_params(node.args)
    returns = ann_to_str(node.returns)
    doc = get_docstring(node)
    src = get_source_segment(src_lines, node.lineno, node.end_lineno or node.lineno)

    # Analyze body (skip docstring-only expr)
    analyzer = BodyAnalyzer(imports, module_qname, class_name)
    body_to_scan = node.body
    if body_to_scan and isinstance(body_to_scan[0], ast.Expr) and isinstance(body_to_scan[0].value, ast.Constant) and isinstance(body_to_scan[0].value.value, str):
        body_to_scan = body_to_scan[1:]
    for stmt in body_to_scan:
        analyzer.visit(stmt)

    fn = FunctionInfo(
        id=fn_id,
        kind=kind,
        name=node.name,
        qualified_name=qname,
        module=module_qname,
        file=file_rel,
        line_start=node.lineno,
        line_end=node.end_lineno or node.lineno,
        class_name=class_name,
        visibility=visibility_of(node.name),
        is_abstract=is_abstract,
        is_generator=any(isinstance(n, (ast.Yield, ast.YieldFrom)) for n in ast.walk(node)),
        is_async=isinstance(node, ast.AsyncFunctionDef),
        decorators=decs,
        parameters=params,
        returns=returns,
        docstring=doc,
        docstring_source="present" if doc else "missing",
        source=src,
        callees=analyzer.callees,
        raises=analyzer.raises,
        reads_attrs=sorted(analyzer.reads_attrs - analyzer._attrs_as_call_target),
        writes_attrs=sorted(analyzer.writes_attrs),
    )
    # Attach analyzer fields used by triviality check
    fn._stmt_count = analyzer.stmt_count  # type: ignore[attr-defined]
    fn._has_cf = analyzer.has_control_flow  # type: ignore[attr-defined]

    trivial, reason = is_trivial(fn)
    if trivial:
        fn.trivial = True
        fn.trivial_reason = reason

    FUNCTIONS[fn_id] = fn
    return fn


# ---------------------------------------------------------------------------
# Post-processing: resolve ref: ids → func: or class: ids
# ---------------------------------------------------------------------------

def resolve_refs() -> None:
    """For every callee with target 'ref:X.Y', decide whether Y is a method on class X
    or a function in module X."""
    for fn in FUNCTIONS.values():
        for c in fn.callees:
            if c.target is None or not c.target.startswith("ref:"):
                continue
            dotted = c.target[len("ref:") :]
            # split off the last dot
            if "." not in dotted:
                c.target = f"func:{dotted}"
                continue
            head, tail = dotted.rsplit(".", 1)
            # try method on class
            if head in CLASSES:
                c.target = f"func:{head}.{tail}"
            else:
                c.target = f"func:{dotted}"


def fold_factory_registrations() -> None:
    """Walk FACTORY_REGISTRATIONS after all files are processed and populate
    FACTORY_OBJECTS[dotted]['registered_keys'] / key_to_class. Creates the
    factory object lazily if it wasn't declared with an explicit annotation."""
    for reg in FACTORY_REGISTRATIONS:
        factory_dotted = reg["factory"]
        key = reg["key"]
        class_id = reg["class_id"]
        f = FACTORY_OBJECTS.get(factory_dotted)
        if f is None:
            name = factory_dotted.rsplit(".", 1)[-1]
            mod = factory_dotted.rsplit(".", 1)[0] if "." in factory_dotted else ""
            f = {
                "id": f"factory:{factory_dotted}",
                "name": name,
                "module": mod,
                "class_type": None,
                "registered_keys": [],
                "key_to_class": {},
            }
            FACTORY_OBJECTS[factory_dotted] = f
        if key not in f["registered_keys"]:
            f["registered_keys"].append(key)
        f["key_to_class"][key] = class_id


# ---------------------------------------------------------------------------
# Markdown emitters
# ---------------------------------------------------------------------------

def yaml_escape_str(val: Optional[str]) -> str:
    if val is None:
        return "null"
    return json.dumps(val, ensure_ascii=False)


def write_frontmatter(lines: List[str], data: Dict[str, object]) -> None:
    lines.append("---")
    for k, v in data.items():
        if v is None:
            lines.append(f"{k}: null")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        elif isinstance(v, str):
            lines.append(f"{k}: {yaml_escape_str(v)}")
        elif isinstance(v, list):
            if not v:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for item in v:
                    if isinstance(item, dict):
                        first = True
                        for ik, iv in item.items():
                            prefix = "  - " if first else "    "
                            first = False
                            if iv is None:
                                lines.append(f"{prefix}{ik}: null")
                            elif isinstance(iv, bool):
                                lines.append(f"{prefix}{ik}: {'true' if iv else 'false'}")
                            elif isinstance(iv, (int, float)):
                                lines.append(f"{prefix}{ik}: {iv}")
                            elif isinstance(iv, list):
                                lines.append(f"{prefix}{ik}: {json.dumps(iv, ensure_ascii=False)}")
                            else:
                                lines.append(f"{prefix}{ik}: {yaml_escape_str(str(iv))}")
                    else:
                        lines.append(f"  - {yaml_escape_str(str(item))}")
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            for dk, dv in v.items():
                lines.append(f"  {dk}: {yaml_escape_str(str(dv)) if dv is not None else 'null'}")
        else:
            lines.append(f"{k}: {yaml_escape_str(str(v))}")
    lines.append("---")


def emit_function_md(fn: FunctionInfo, docs_root: Path) -> str:
    # folder: docs/functions/<module>/<Class>/ or docs/functions/<module>/
    parts = [docs_root, Path("functions"), Path(fn.module)]
    if fn.class_name:
        parts.append(Path(fn.class_name))
    folder = Path(*parts)
    folder.mkdir(parents=True, exist_ok=True)
    md_path = folder / f"{fn.name}.md"

    doc_rel_path = md_path.relative_to(docs_root).as_posix()

    frontmatter = {
        "id": fn.id,
        "kind": fn.kind,
        "name": fn.name,
        "qualified_name": fn.qualified_name,
        "module": fn.module,
        "file": fn.file,
        "line_start": fn.line_start,
        "line_end": fn.line_end,
        "class": fn.class_name,
        "visibility": fn.visibility,
        "is_abstract": fn.is_abstract,
        "is_generator": fn.is_generator,
        "is_async": fn.is_async,
        "decorators": fn.decorators,
        "parameters": [asdict(p) for p in fn.parameters],
        "returns": fn.returns,
        "docstring_source": fn.docstring_source,
        "callees": [
            {
                "target": c.target,
                "expr": c.expr,
                "call_sites": c.call_sites,
            }
            for c in fn.callees
        ],
        "raises": [
            {"exception": r.exception, "call_sites": r.call_sites} for r in fn.raises
        ],
        "reads_attrs": fn.reads_attrs,
        "writes_attrs": fn.writes_attrs,
    }

    lines: List[str] = []
    write_frontmatter(lines, frontmatter)
    lines.append("")
    lines.append(f"# `{fn.qualified_name}`")
    lines.append("")
    lines.append(f"**File:** [{fn.file}:{fn.line_start}](../../../../{fn.file}#L{fn.line_start})")
    if fn.class_name:
        lines.append(f"**Class:** `{fn.class_name}`")
    lines.append(f"**Visibility:** {fn.visibility}")
    lines.append(f"**Kind:** {fn.kind}")
    if fn.decorators:
        lines.append(f"**Decorators:** {', '.join(f'`{d}`' for d in fn.decorators)}")
    lines.append("")

    # Signature
    sig_params = []
    for p in fn.parameters:
        s = p.name
        if p.annotation:
            s += f": {p.annotation}"
        if p.default:
            s += f" = {p.default}"
        sig_params.append(s)
    ret = f" -> {fn.returns}" if fn.returns else ""
    lines.append("## Signature")
    lines.append("")
    lines.append("```python")
    lines.append(f"def {fn.name}({', '.join(sig_params)}){ret}")
    lines.append("```")
    lines.append("")

    # Docstring
    lines.append("## Docstring")
    lines.append("")
    if fn.docstring:
        lines.append(fn.docstring)
    else:
        lines.append("*(No docstring present — listed in `missing_docstrings.md`.)*")
    lines.append("")

    # Parameters
    lines.append("## Parameters")
    lines.append("")
    if fn.parameters:
        lines.append("| Name | Type | Default |")
        lines.append("|------|------|---------|")
        for p in fn.parameters:
            lines.append(
                f"| `{p.name}` | {'`' + p.annotation + '`' if p.annotation else '—'} | "
                f"{'`' + p.default + '`' if p.default else '—'} |"
            )
    else:
        lines.append("*(No parameters.)*")
    lines.append("")

    # Returns
    lines.append("## Returns")
    lines.append("")
    lines.append(f"`{fn.returns}`" if fn.returns else "*(Not annotated.)*")
    lines.append("")

    # Calls (resolved)
    lines.append("## Calls")
    lines.append("")
    resolved = [c for c in fn.callees if c.target]
    unresolved = [c for c in fn.callees if not c.target]
    if resolved:
        for c in resolved:
            sites = ", ".join(str(s) for s in c.call_sites)
            lines.append(f"- `{c.expr}` → `{c.target}` (lines: {sites})")
    else:
        lines.append("*(No resolved calls.)*")
    if unresolved:
        lines.append("")
        lines.append("### Unresolved")
        for c in unresolved:
            sites = ", ".join(str(s) for s in c.call_sites)
            lines.append(f"- `{c.expr}` (lines: {sites})")
    lines.append("")

    # Called by — placeholder; filled in second pass by graph builder
    lines.append("## Called by")
    lines.append("")
    lines.append("*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*")
    lines.append("")

    # Raises
    if fn.raises:
        lines.append("## Raises")
        lines.append("")
        for r in fn.raises:
            sites = ", ".join(str(s) for s in r.call_sites)
            lines.append(f"- `{r.exception}` (lines: {sites})")
        lines.append("")

    # Attr access
    if fn.reads_attrs or fn.writes_attrs:
        lines.append("## Attribute access")
        lines.append("")
        if fn.writes_attrs:
            lines.append("**Writes:**")
            for a in fn.writes_attrs:
                lines.append(f"- `{a}`")
            lines.append("")
        if fn.reads_attrs:
            lines.append("**Reads:**")
            for a in fn.reads_attrs:
                lines.append(f"- `{a}`")
            lines.append("")

    # Source
    lines.append("## Source")
    lines.append("")
    lines.append("```python")
    lines.append(fn.source)
    lines.append("```")
    lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return doc_rel_path


def emit_class_md(cls: ClassInfo, docs_root: Path) -> str:
    folder = docs_root / "classes" / cls.module
    folder.mkdir(parents=True, exist_ok=True)
    md_path = folder / f"{cls.name}.md"
    doc_rel_path = md_path.relative_to(docs_root).as_posix()

    frontmatter = {
        "id": cls.id,
        "kind": "class",
        "name": cls.name,
        "qualified_name": cls.qualified_name,
        "module": cls.module,
        "file": cls.file,
        "line_start": cls.line_start,
        "line_end": cls.line_end,
        "is_abstract": cls.is_abstract,
        "is_dataclass": cls.is_dataclass,
        "decorators": cls.decorators,
        "generic_parameters": cls.generic_parameters,
        "bases": cls.bases,
        "methods": cls.methods,
        "attributes": cls.attributes,
        "factory_registrations": cls.factory_registrations,
        "docstring_source": cls.docstring_source,
    }

    lines: List[str] = []
    write_frontmatter(lines, frontmatter)
    lines.append("")
    lines.append(f"# `{cls.qualified_name}`")
    lines.append("")
    lines.append(f"**File:** [{cls.file}:{cls.line_start}](../../../{cls.file}#L{cls.line_start})")
    lines.append(f"**Abstract:** {'yes' if cls.is_abstract else 'no'}")
    if cls.is_dataclass:
        lines.append(f"**Dataclass:** yes")
    if cls.generic_parameters:
        lines.append(f"**Generic parameters:** `{', '.join(cls.generic_parameters)}`")
    if cls.decorators:
        lines.append(f"**Decorators:** {', '.join(f'`{d}`' for d in cls.decorators)}")
    lines.append("")

    lines.append("## Docstring")
    lines.append("")
    lines.append(cls.docstring if cls.docstring else "*(No docstring present — listed in `missing_docstrings.md`.)*")
    lines.append("")

    # Bases
    lines.append("## Inheritance")
    lines.append("")
    lines.append("**Direct bases:**")
    for b in cls.bases:
        lines.append(f"- `{b['name']}`")
    lines.append("")
    lines.append("**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*")
    lines.append("")

    # Factory
    if cls.factory_registrations:
        lines.append("## Factory registration")
        lines.append("")
        for fr in cls.factory_registrations:
            lines.append(f"- Factory `{fr['factory']}` under key `{fr['key']}`")
        lines.append("")

    # Methods
    lines.append("## Methods")
    lines.append("")
    if cls.methods:
        for mid in cls.methods:
            fn = FUNCTIONS.get(mid)
            if fn is None:
                continue
            suffix = " *(trivial, skipped)*" if fn.trivial else ""
            ds = "" if fn.docstring else " — *(no docstring)*"
            lines.append(f"- `{fn.name}`{suffix}{ds}")
    else:
        lines.append("*(No methods.)*")
    lines.append("")

    # Attributes
    if cls.attributes:
        lines.append("## Attributes")
        lines.append("")
        lines.append("| Name | Type | Source |")
        lines.append("|------|------|--------|")
        for a in cls.attributes:
            lines.append(
                f"| `{a['name']}` | {'`'+a['annotation']+'`' if a['annotation'] else '—'} | {a.get('from','—')} |"
            )
        lines.append("")

    # Source
    lines.append("## Source")
    lines.append("")
    lines.append("```python")
    lines.append(cls.source)
    lines.append("```")
    lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return doc_rel_path


def emit_module_md(mod: ModuleInfo, docs_root: Path) -> str:
    folder = docs_root / "modules"
    folder.mkdir(parents=True, exist_ok=True)
    md_path = folder / f"{mod.qualified_name}.md"
    doc_rel_path = md_path.relative_to(docs_root).as_posix()

    frontmatter = {
        "id": mod.id,
        "kind": "module",
        "name": mod.name,
        "qualified_name": mod.qualified_name,
        "file": mod.file,
        "line_count": mod.line_count,
        "docstring_source": mod.docstring_source,
        "imports": mod.imports,
        "classes": mod.classes,
        "module_level_functions": mod.module_level_functions,
        "module_level_constants": mod.module_level_constants,
    }
    lines: List[str] = []
    write_frontmatter(lines, frontmatter)
    lines.append("")
    lines.append(f"# Module `{mod.qualified_name}`")
    lines.append("")
    lines.append(f"**File:** [{mod.file}](../../{mod.file})")
    lines.append(f"**Lines:** {mod.line_count}")
    lines.append("")
    lines.append("## Module docstring")
    lines.append("")
    lines.append(mod.docstring if mod.docstring else "*(No docstring — listed in `missing_docstrings.md`.)*")
    lines.append("")

    lines.append("## Contents")
    lines.append("")
    if mod.classes:
        lines.append("### Classes")
        for cid in mod.classes:
            cname = cid.split(".")[-1]
            lines.append(f"- `{cname}` — see `../classes/{mod.qualified_name}/{cname}.md`")
        lines.append("")
    if mod.module_level_functions:
        lines.append("### Module-level functions")
        for fid in mod.module_level_functions:
            fn = FUNCTIONS.get(fid)
            if fn is None:
                continue
            suffix = " *(trivial, skipped)*" if fn.trivial else ""
            lines.append(f"- `{fn.name}`{suffix}")
        lines.append("")
    if mod.module_level_constants:
        lines.append("### Module-level constants / TypeVars")
        for c in mod.module_level_constants:
            ann = f": `{c['annotation']}`" if c.get("annotation") else ""
            val = f" = `{c['value_expr']}`" if c.get("value_expr") else ""
            lines.append(f"- `{c['name']}`{ann}{val}")
        lines.append("")

    if mod.imports:
        lines.append("## Imports")
        lines.append("")
        for imp in mod.imports:
            if imp.get("kind") == "import":
                alias = f" as {imp['alias']}" if imp.get("alias") else ""
                lines.append(f"- `import {imp['module']}{alias}`")
            else:
                names = ", ".join(
                    (n["name"] + (f" as {n['alias']}" if n.get("alias") else "")) for n in imp.get("names", [])  # type: ignore[arg-type]
                )
                lines.append(f"- `from {imp['module']} import {names}`")
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return doc_rel_path


# ---------------------------------------------------------------------------
# Graph build
# ---------------------------------------------------------------------------

def build_graph(scope_rel: List[str]) -> Dict[str, object]:
    nodes: List[Dict[str, object]] = []
    edges: List[Dict[str, object]] = []
    unresolved: List[Dict[str, object]] = []
    skipped: List[Dict[str, object]] = []

    for m in MODULES.values():
        nodes.append(
            {
                "id": m.id,
                "kind": "module",
                "module": m.qualified_name,
                "file": m.file,
                "name": m.name,
                "doc_path": f"modules/{m.qualified_name}.md",
            }
        )

    for c in CLASSES.values():
        nodes.append(
            {
                "id": c.id,
                "kind": "class",
                "module": c.module,
                "file": c.file,
                "name": c.name,
                "is_abstract": c.is_abstract,
                "doc_path": f"classes/{c.module}/{c.name}.md",
            }
        )
        for b in c.bases:
            # resolve base name in graph — look for matching class qname ending with b['name']
            base_str = b["name"] or ""
            # strip generics
            base_bare = base_str.split("[")[0]
            # attempt exact match by qname
            matches = [cq for cq in CLASSES.keys() if cq.endswith("." + base_bare) or cq == base_bare]
            if len(matches) == 1:
                edges.append(
                    {
                        "kind": "inherits",
                        "from": c.id,
                        "to": f"class:{matches[0]}",
                        "base_expr": base_str,
                    }
                )
            else:
                edges.append(
                    {
                        "kind": "inherits",
                        "from": c.id,
                        "to": None,
                        "base_expr": base_str,
                        "note": "external or ambiguous base",
                    }
                )
        for fr in c.factory_registrations:
            edges.append(
                {
                    "kind": "registers",
                    "from": c.id,
                    "to": f"factory:{fr['factory']}",
                    "key": fr["key"],
                }
            )

    for fn in FUNCTIONS.values():
        if fn.trivial:
            skipped.append(
                {
                    "id": fn.id,
                    "file": fn.file,
                    "line_start": fn.line_start,
                    "name": fn.qualified_name,
                    "reason": fn.trivial_reason,
                }
            )
            continue
        doc_folder = f"functions/{fn.module}"
        if fn.class_name:
            doc_folder += f"/{fn.class_name}"
        nodes.append(
            {
                "id": fn.id,
                "kind": fn.kind,
                "module": fn.module,
                "class_id": f"class:{fn.module}.{fn.class_name}" if fn.class_name else None,
                "file": fn.file,
                "line_start": fn.line_start,
                "line_end": fn.line_end,
                "name": fn.name,
                "is_abstract": fn.is_abstract,
                "doc_path": f"{doc_folder}/{fn.name}.md",
            }
        )
        for c in fn.callees:
            if c.target:
                edges.append(
                    {
                        "kind": "calls",
                        "from": fn.id,
                        "to": c.target,
                        "expr": c.expr,
                        "call_sites": c.call_sites,
                    }
                )
            else:
                unresolved.append(
                    {
                        "from": fn.id,
                        "expr": c.expr,
                        "call_sites": c.call_sites,
                    }
                )
        for r in fn.raises:
            edges.append(
                {
                    "kind": "raises",
                    "from": fn.id,
                    "to": f"exception:{r.exception}",
                    "call_sites": r.call_sites,
                }
            )
        for a in fn.writes_attrs:
            edges.append({"kind": "writes_attr", "from": fn.id, "to": f"attr:{fn.module}.{fn.class_name}.{a}"})
        for a in fn.reads_attrs:
            edges.append({"kind": "reads_attr", "from": fn.id, "to": f"attr:{fn.module}.{fn.class_name}.{a}"})

    # factory nodes
    factories: List[Dict[str, object]] = []
    for dotted, f in FACTORY_OBJECTS.items():
        factories.append(
            {
                "id": f["id"],
                "kind": "factory",
                "module": f["module"],
                "name": f["name"],
                "class_type": f["class_type"],
                "registered_keys": f["registered_keys"],
                "key_to_class": f["key_to_class"],
            }
        )
        nodes.append(
            {
                "id": f["id"],
                "kind": "factory",
                "module": f["module"],
                "name": f["name"],
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": scope_rel,
        "nodes": nodes,
        "edges": edges,
        "factories": factories,
        "unresolved_calls": unresolved,
        "skipped_trivial": skipped,
    }


# ---------------------------------------------------------------------------
# Missing-docstrings + skipped reports
# ---------------------------------------------------------------------------

def write_missing_docstrings(docs_root: Path) -> Tuple[int, int, int]:
    by_module: Dict[str, List[str]] = {}
    total_funcs = 0
    missing_funcs = 0
    total_classes = len(CLASSES)
    missing_classes = 0

    for fn in FUNCTIONS.values():
        if fn.trivial:
            continue
        total_funcs += 1
        if fn.docstring is None:
            missing_funcs += 1
            by_module.setdefault(fn.module, []).append(
                f"- L{fn.line_start}: `{fn.qualified_name}` ({fn.kind})"
            )

    for c in CLASSES.values():
        if c.docstring is None:
            missing_classes += 1
            by_module.setdefault(c.module, []).insert(
                0, f"- L{c.line_start}: `{c.qualified_name}` (class)"
            )

    missing_modules = 0
    for m in MODULES.values():
        if m.docstring is None:
            missing_modules += 1
            by_module.setdefault(m.qualified_name, []).insert(
                0, f"- L1: `{m.qualified_name}` (module)"
            )

    out = docs_root / "missing_docstrings.md"
    lines = [
        "# Missing docstrings report",
        "",
        f"**Functions/methods missing docstrings:** {missing_funcs} / {total_funcs}  ",
        f"**Classes missing docstrings:** {missing_classes} / {total_classes}  ",
        f"**Modules missing docstrings:** {missing_modules} / {len(MODULES)}",
        "",
        "*Trivial functions are excluded from this count (see `skipped_trivial.md`).*",
        "",
    ]
    for mod in sorted(by_module.keys()):
        lines.append(f"## `{mod}`")
        lines.append("")
        lines.extend(by_module[mod])
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return missing_funcs, missing_classes, missing_modules


def write_skipped_report(docs_root: Path) -> int:
    skipped = [fn for fn in FUNCTIONS.values() if fn.trivial]
    by_module: Dict[str, List[str]] = {}
    for fn in skipped:
        by_module.setdefault(fn.module, []).append(
            f"- L{fn.line_start}: `{fn.qualified_name}` — {fn.trivial_reason}"
        )
    lines = [
        "# Skipped (trivial) functions",
        "",
        f"**Total skipped:** {len(skipped)}",
        "",
        "*Triviality rule: ≤3 statements AND no control flow AND no calls to project functions.*",
        "",
    ]
    for mod in sorted(by_module.keys()):
        lines.append(f"## `{mod}`")
        lines.append("")
        lines.extend(by_module[mod])
        lines.append("")
    (docs_root / "skipped_trivial.md").write_text("\n".join(lines), encoding="utf-8")
    return len(skipped)


# ---------------------------------------------------------------------------
# Mermaid sample
# ---------------------------------------------------------------------------

def _collect_ancestors(class_qname: str, out: Set[str]) -> None:
    """Walk `bases` of class_qname and add every in-scope ancestor to `out`."""
    cls = CLASSES.get(class_qname)
    if cls is None:
        return
    for b in cls.bases:
        base_bare = (b["name"] or "").split("[")[0]
        matches = [cq for cq in CLASSES.keys() if cq.endswith("." + base_bare)]
        if len(matches) == 1 and matches[0] not in out:
            out.add(matches[0])
            _collect_ancestors(matches[0], out)


def _emit_mermaid_for_class_set(class_qnames: Set[str], title: str, subtitle: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["```mermaid", "graph TD"]
    node_ids: Dict[str, str] = {}

    def short_id(qname: str) -> str:
        return "N" + str(abs(hash(qname)) % (10**8))

    for qname in sorted(class_qnames):
        c = CLASSES.get(qname)
        if c is None:
            continue
        sid = short_id(c.id)
        node_ids[c.id] = sid
        label = f"{c.name}"
        if c.is_abstract:
            label += " (abstract)"
        if c.factory_registrations:
            keys = ",".join(fr["key"] for fr in c.factory_registrations)
            label += f"<br/>[{keys}]"
        shape = f'{sid}["{label}"]' if not c.is_abstract else f'{sid}(("{label}"))'
        lines.append(f"    {shape}")

    for qname in sorted(class_qnames):
        c = CLASSES.get(qname)
        if c is None:
            continue
        for b in c.bases:
            base_bare = (b["name"] or "").split("[")[0]
            matches = [cq for cq in CLASSES.keys() if cq.endswith("." + base_bare)]
            if len(matches) == 1 and matches[0] in class_qnames:
                src = node_ids[c.id]
                dst_id = f"class:{matches[0]}"
                if dst_id in node_ids:
                    lines.append(f"    {node_ids[dst_id]} --> {src}")

    lines.append("```")
    header = [
        f"# {title}",
        "",
        subtitle,
        "",
        "Arrow: **base → subclass**. Abstract classes as circles. Square brackets: factory key.",
        "",
    ]
    out_path.write_text("\n".join(header + lines), encoding="utf-8")


def write_updater_mermaid(docs_root: Path) -> None:
    """One mermaid per factory: registered concrete classes + all their in-scope ancestors."""
    for dotted, f in FACTORY_OBJECTS.items():
        if not f["registered_keys"]:
            continue
        reg_class_ids = list(f["key_to_class"].values())
        reg_class_qnames = {cid[len("class:"):] for cid in reg_class_ids}
        full_set: Set[str] = set(reg_class_qnames)
        for q in reg_class_qnames:
            _collect_ancestors(q, full_set)
        safe_name = f["name"]
        out = docs_root / "samples" / f"factory_{safe_name}.mmd"
        _emit_mermaid_for_class_set(
            full_set,
            title=f"Factory `{f['name']}` — class hierarchy",
            subtitle=(
                f"Every concrete class registered with `{dotted}` plus all their "
                f"in-scope abstract ancestors. {len(reg_class_qnames)} registered "
                f"class(es), {len(full_set)} classes total in the diagram."
            ),
            out_path=out,
        )


# ---------------------------------------------------------------------------
# CLI flags JSON (POC-level: factory keys only)
# ---------------------------------------------------------------------------

def write_cli_flags_json(docs_root: Path) -> None:
    obj = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "poc_note": (
            "This POC output contains only factory keys extracted from "
            "@factory.register_class decorators. Full CLI flag extraction "
            "from _train_cli.py / _solve.py / _cli.py happens when those files "
            "are added to scope."
        ),
        "flags": [],
        "factories": list(FACTORY_OBJECTS.values()),
        "dispatch_rules": [
            {
                "target_factory": "deepxube.factories.updater_factory.updater_factory",
                "predicate_fn": "deepxube.factories.updater_factory.get_updater",
                "inputs": ["domain", "pathfind_arg", "her", "func_update"],
                "rule_summary": (
                    "Filters updater_factory registry by: (1) domain_type match via isinstance, "
                    "(2) pathfind_type match via issubclass, (3) UpdateHER subclass == her bool, "
                    "(4) functions_type equals pathfind's functions_type, (5) UpdateHeur or "
                    "UpdatePolicy subclass per func_update arg. Must resolve to exactly one class."
                ),
            }
        ],
    }
    (docs_root / "cli_flags.json").write_text(
        json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--scope",
        required=True,
        help="Path to a text file listing relative .py paths (one per line) to process",
    )
    ap.add_argument(
        "--repo-root",
        default=".",
        help="Path to deepxube-main/ (default: cwd)",
    )
    ap.add_argument(
        "--docs-root",
        default="docs",
        help="Output directory (default: docs/ under repo root)",
    )
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    docs_root = (repo_root / args.docs_root).resolve()
    docs_root.mkdir(parents=True, exist_ok=True)

    scope_file = Path(args.scope).resolve()
    scope_files = [
        line.strip()
        for line in scope_file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

    print(f"Scope: {len(scope_files)} file(s)")
    for rel in scope_files:
        py_path = repo_root / rel
        if not py_path.exists():
            print(f"  ! missing: {rel}")
            continue
        print(f"  - {rel}")
        process_file(py_path, repo_root)

    resolve_refs()
    fold_factory_registrations()

    # Emit markdown
    func_paths: List[str] = []
    for fn in FUNCTIONS.values():
        if fn.trivial:
            continue
        func_paths.append(emit_function_md(fn, docs_root))
    for c in CLASSES.values():
        emit_class_md(c, docs_root)
    for m in MODULES.values():
        emit_module_md(m, docs_root)

    graph = build_graph(scope_files)
    (docs_root / "graph.json").write_text(
        json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    write_cli_flags_json(docs_root)
    missing_fn, missing_cls, missing_mod = write_missing_docstrings(docs_root)
    n_skipped = write_skipped_report(docs_root)
    write_updater_mermaid(docs_root)

    total_functions = len([f for f in FUNCTIONS.values() if not f.trivial])
    print()
    print(f"=== POC extraction complete ===")
    print(f"  Modules:       {len(MODULES)}")
    print(f"  Classes:       {len(CLASSES)}")
    print(f"  Functions:     {total_functions} documented, {n_skipped} skipped (trivial)")
    print(f"  Docstrings missing — functions: {missing_fn}, classes: {missing_cls}, modules: {missing_mod}")
    print(f"  Nodes in graph: {len(graph['nodes'])}")
    print(f"  Edges in graph: {len(graph['edges'])}")
    print(f"  Unresolved calls: {len(graph['unresolved_calls'])}")
    print(f"  Output: {docs_root}")


if __name__ == "__main__":
    main()
