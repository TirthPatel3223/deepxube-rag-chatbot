# Documentation Schema (v1)

This file is the authoritative spec for every `.md` and `.json` artifact the
extractor produces. **Freeze this before scaling from POC to full codebase.**

---

## 1. Directory layout

```
deepxube-main/docs/
  functions/                 # one .md per non-trivial function / method
    <dotted.module.path>/
      <ClassName>/           # only if the function is a method
        <func_name>.md
      <func_name>.md         # module-level functions live directly here
  classes/
    <dotted.module.path>/
      <ClassName>.md
  modules/
    <dotted.module.path>.md
  graph.json                 # merged knowledge graph (nodes + edges)
  cli_flags.json             # CLI flag catalog + factory-key dispatch table
  missing_docstrings.md      # human-readable gap report
  skipped_trivial.md         # functions skipped under the triviality rule
  samples/
    updaters_flow.mmd        # sample mermaid diagram (POC only)
  extractor/
    extract.py               # the extraction script
    SCHEMA.md                # this file
    README.md                # how to run
    poc_scope.txt            # files processed in the POC
```

---

## 2. Common identifier scheme

Every node in the graph has a stable `id`:

| Node kind | `id` format                                                  |
|-----------|--------------------------------------------------------------|
| module    | `module:<dotted.module.path>`                                |
| class     | `class:<dotted.module.path>.<ClassName>`                     |
| function  | `func:<dotted.module.path>.<func_name>`                      |
| method    | `func:<dotted.module.path>.<ClassName>.<method_name>`        |
| factory   | `factory:<dotted.factory.path>`                              |
| cli_flag  | `flag:<flag_name>` (e.g. `flag:--heur_type`)                 |

`<dotted.module.path>` is the Python import path (`deepxube.base.updater`).

---

## 3. Function / method `.md` schema

Every non-trivial function gets its own file. YAML frontmatter + Markdown body.

### 3.1 YAML frontmatter

```yaml
---
id: func:deepxube.base.updater.Update.__init__
kind: method                     # function | method | staticmethod | classmethod
name: __init__
qualified_name: deepxube.base.updater.Update.__init__
module: deepxube.base.updater
file: deepxube/base/updater.py   # path relative to deepxube-main/
line_start: 116
line_end: 143
class: Update                    # null for module-level functions
visibility: public               # public | private | dunder
is_abstract: false
is_generator: false
is_async: false
decorators: []                   # list of decorator strings, e.g. ["@abstractmethod"]
parameters:
  - name: domain
    annotation: "D"
    default: null
  - name: pathfind_arg
    annotation: "str"
    default: null
returns: "None"                  # string annotation, or "None"
docstring_source: missing        # present | missing
callees:                         # best-effort static resolution
  - target: func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs
    call_sites: [119]
  - target: func:deepxube.base.updater.Update.add_nnet_par
    call_sites: [127]
unresolved_callees:              # calls we could not statically resolve
  - expr: "copy.deepcopy"
    call_sites: [183]
callers: []                      # populated in second pass (inverse of callees)
raises:                          # bare `raise X(...)` statements
  - exception: ValueError
    call_sites: [147]
reads_attrs:                     # self.* attribute reads (methods only)
  - self.from_q
writes_attrs:                    # self.* attribute assignments (methods only)
  - self.domain
  - self.pathfind_arg
activation:                      # which CLI-flag configurations reach this code
  via_factory_key: null          # if the enclosing class registers under a factory key, else null
  flag_conditions: []            # explicit `args.foo == X` guards found up the call stack
---
```

### 3.2 Markdown body

```markdown
# `<qualified_name>`

**File:** [<path>:<line_start>](<relative-link>)
**Class:** `<ClassName>` (if method)
**Visibility:** public | private | dunder
**Decorators:** `@abstractmethod`, `@staticmethod`, ...

## Signature

```python
def <name>(<params>) -> <return>
```

## Docstring

<verbatim docstring, or "*(No docstring present — see missing_docstrings.md)*">

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| ... | ... | ... | *(from docstring :param: if available)* |

## Returns

`<return-type>` *(description from docstring if available)*

## Calls

- `<qualified_name>` (lines: N, M) — [link to callee doc]
- ...

### Unresolved

- `expr.method(...)` at line N — *could not resolve statically*

## Called by

- `<qualified_name>` — [link]
- ...

## Activation conditions

- Registered under factory key: `update_v_rl` (via class `UpdateHeurVRLKeepGoal`)
- Reached when: `--heur_type V` AND `--pathfind graph_v.*` AND `--her` is false

## Source

```python
<full source of the function, verbatim>
```
```

---

## 4. Class `.md` schema

### 4.1 YAML frontmatter

```yaml
---
id: class:deepxube.base.updater.Update
kind: class
name: Update
qualified_name: deepxube.base.updater.Update
module: deepxube.base.updater
file: deepxube/base/updater.py
line_start: 92
line_end: 460
is_abstract: true                # has at least one @abstractmethod
is_dataclass: false
decorators: []
generic_parameters: ["D", "FNs", "P", "Inst"]
bases:                           # direct base classes
  - name: "Generic[D, FNs, P, Inst]"
    resolved_id: null            # null if external (e.g. typing.Generic)
  - name: "ABC"
    resolved_id: null
mro_sketch:                      # best-effort, local to codebase
  - class:deepxube.base.updater.Update
mixins: []                       # classes identified as mixins by naming/usage
methods:                         # id references — full docs are separate files
  - id: func:deepxube.base.updater.Update.__init__
  - id: func:deepxube.base.updater.Update.set_nnet_par_info_l_dict
  ...
attributes:                      # class-level and self.* attributes (from __init__)
  - name: domain
    annotation: "D"
    assigned_in: [func:deepxube.base.updater.Update.__init__]
factory_registrations: []        # list of {factory_name, key} — for concrete classes
subclasses: []                   # reverse edge, populated in second pass
docstring_source: present        # present | missing
---
```

### 4.2 Markdown body

```markdown
# `<ClassName>`

**File:** [<path>:<line_start>](<link>)
**Abstract:** yes/no
**Generic parameters:** `D, FNs, P, Inst`

## Docstring

<verbatim or "missing">

## Inheritance

**Bases:** `Generic[D, FNs, P, Inst]`, `ABC`

**Subclasses:** `UpdateHER`, `UpdateHasHeur`, `UpdateHasPolicy`, ... (links)

## Factory registration

This class registers with `updater_factory` under keys:
- `update_v_rl` → `UpdateHeurVRLKeepGoal`

## Methods

- [`__init__`](...) — (no docstring)
- [`set_nnet_par_info_l_dict`](...) — sets per-process NNet info ...
- ... (links)

## Attributes (from `__init__` and class body)

| Name | Type | Notes |
|------|------|-------|

## Activation conditions

<if concrete and factory-registered: which CLI combos reach this class>
```

---

## 5. Module `.md` schema

### 5.1 YAML frontmatter

```yaml
---
id: module:deepxube.base.updater
kind: module
name: updater
qualified_name: deepxube.base.updater
file: deepxube/base/updater.py
line_count: 666
docstring_source: missing
imports:
  - from: deepxube.nnet.nnet_utils
    names: [NNetParInfo, NNetCallable, NNetPar, ...]
  - from: numpy
    alias: np
classes: [class:deepxube.base.updater.Update, ...]
module_level_functions: [func:deepxube.base.updater._put_from_q]
module_level_constants:          # name + annotation + inferred type
  - name: FNsH
    annotation: null
    inferred: TypeVar
---
```

### 5.2 Markdown body

```markdown
# Module `<qualified_name>`

**File:** [<path>](<link>)
**Lines:** <count>

## Module docstring

<verbatim or "missing">

## Summary

*(LLM-generated later — for now, blank with a stub)*

## Contents

### Classes
- [`Update`](...) — abstract base for all updaters (inherited doc from class)
- [`UpdateHER`](...)
- ...

### Module-level functions
- [`_put_from_q`](...)

### Constants / TypeVars
- `FNsH` — `TypeVar('FNsH', bound=FNsHeur)`

## Imports

From `deepxube.nnet.nnet_utils`: `NNetParInfo`, `NNetCallable`, ...
```

---

## 6. `graph.json` schema

Single merged file covering the whole codebase (for the POC: just the scope).

```json
{
  "schema_version": "1.0",
  "generated_at": "2026-04-24T...",
  "scope": ["deepxube/base/updater.py", "deepxube/updaters/updater_sup.py", ...],
  "nodes": [
    {
      "id": "class:deepxube.base.updater.Update",
      "kind": "class",
      "module": "deepxube.base.updater",
      "file": "deepxube/base/updater.py",
      "name": "Update",
      "is_abstract": true,
      "doc_path": "classes/deepxube.base.updater/Update.md"
    },
    {
      "id": "func:deepxube.base.updater.Update.__init__",
      "kind": "method",
      "class_id": "class:deepxube.base.updater.Update",
      "module": "deepxube.base.updater",
      "file": "deepxube/base/updater.py",
      "name": "__init__",
      "line_start": 116,
      "line_end": 143,
      "doc_path": "functions/deepxube.base.updater/Update/__init__.md"
    }
  ],
  "edges": [
    {
      "kind": "calls",
      "from": "func:deepxube.base.updater.Update.__init__",
      "to": "func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs",
      "call_sites": [119]
    },
    {
      "kind": "inherits",
      "from": "class:deepxube.base.updater.UpdateHeurVRL",
      "to": "class:deepxube.base.updater.UpdateHeurV"
    },
    {
      "kind": "registers",
      "from": "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal",
      "to": "factory:deepxube.factories.updater_factory.updater_factory",
      "key": "update_v_rl"
    },
    {
      "kind": "raises",
      "from": "func:deepxube.base.updater.UpdateHeurVRLKeepGoalABC._get_instance_data_norb",
      "to": "exception:ValueError",
      "call_sites": [147]
    }
  ],
  "factories": [
    {
      "id": "factory:deepxube.factories.updater_factory.updater_factory",
      "class_type": "Update",
      "registered_keys": ["update_p_rl", "update_p_rl_her", "update_v_rl", ...],
      "key_to_class": {
        "update_v_rl": "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal"
      }
    }
  ],
  "unresolved_calls": [
    {
      "from": "func:deepxube.base.updater.Update.start_procs",
      "expr": "copy.deepcopy",
      "call_sites": [183]
    }
  ],
  "skipped_trivial": [
    {
      "id": "func:deepxube.base.updater.Update.__repr__",
      "reason": "≤3 lines + no control flow + no non-self calls"
    }
  ]
}
```

### Edge kinds

| `kind`        | From                  | To                              | Notes                                          |
|---------------|-----------------------|---------------------------------|------------------------------------------------|
| `calls`       | function/method       | function/method                 | Static best-effort; `call_sites` = line list   |
| `inherits`    | class                 | class                           | Direct base only (full MRO is derived)         |
| `implements`  | class                 | function (abstract)             | Concrete class overrides abstract method       |
| `registers`   | class                 | factory                         | `@factory.register_class("key")` decorator    |
| `raises`      | function              | exception (as `exception:<Name>`) | From `raise X(...)` statements              |
| `reads_attr`  | method                | attribute                       | `self.foo` read                                |
| `writes_attr` | method                | attribute                       | `self.foo = ...` write                         |
| `activated_by`| class (concrete)      | cli_flag_combo                  | Derived — `get_updater()` predicate evaluation |

---

## 7. `cli_flags.json` schema

```json
{
  "schema_version": "1.0",
  "flags": [
    {
      "name": "--heur_type",
      "entry_points": ["deepxube train", "deepxube solve", "deepxube time"],
      "type": "str",
      "choices": ["V", "Q", "QFix"],
      "default": null,
      "help": "...",
      "mutually_exclusive_with": []
    }
  ],
  "dispatch_rules": [
    {
      "target_factory": "updater_factory",
      "predicate": "get_updater()",
      "inputs": ["domain", "pathfind_arg", "her", "func_update"],
      "rule_source_file": "deepxube/factories/updater_factory.py",
      "rule_source_line": 14,
      "resolution": "filters updater_factory._class_registry by domain_type, pathfind_type, UpdateHER subclass match, functions_type match, then UpdateHeur|UpdatePolicy subclass match"
    }
  ]
}
```

**POC note:** The POC emits only the factory-registration portion of `cli_flags.json`
(i.e. the list of factory keys and their registered classes). Full CLI flag extraction
(argparse scraping from `_train_cli.py` / `_solve.py` / `_cli.py`) happens when those
modules are processed.

---

## 8. Triviality rule

A function is skipped (no `.md` file, entry in `skipped_trivial.md` instead) iff
**all three** of:

1. Body is ≤3 statements (after removing docstring and `pass`)
2. No control flow: no `if`, `for`, `while`, `try`, `with`, `match`
3. No calls to any other project function (calls to builtins like `len`, `print`,
   `str`, `int`, `list`, and to `self.<attr>` attribute access are OK)

Skipped functions still appear in `graph.json` under `skipped_trivial` with their
id, file, line, and reason. `__init__.py` re-export-only files are skipped entirely.

---

## 9. Docstring handling

- If present, docstring is preserved **verbatim** (indentation normalized).
- If absent, entry added to `missing_docstrings.md` with file, line, and
  qualified name, grouped by module.
- `docstring_source` field in frontmatter: `present` or `missing` (not
  `auto_generated` — the user explicitly chose human-only prose).
- No LLM pass on descriptions (per the 2026-04-24 decision).

---

## 10. File-naming edge cases

- Python function name `__init__` → file `__init__.md` (inside the class folder)
- Dotted module path `deepxube.updaters.utils.replay_buffer_utils` → folder
  `docs/functions/deepxube.updaters.utils.replay_buffer_utils/` (single flat
  folder name with dots, NOT nested folders — matches the "choose one" decision)
- Overloaded functions: impossible in Python at module scope — the last
  definition wins, which is what we document

---

## 11. Schema stability policy

This is v1.0. Any breaking change bumps the major version and requires a full
re-extraction. Additive changes (new optional fields) bump the minor version
and leave existing artifacts valid.
