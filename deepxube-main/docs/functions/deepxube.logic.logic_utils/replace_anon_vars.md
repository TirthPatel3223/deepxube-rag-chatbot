---
id: "func:deepxube.logic.logic_utils.replace_anon_vars"
kind: "function"
name: "replace_anon_vars"
qualified_name: "deepxube.logic.logic_utils.replace_anon_vars"
module: "deepxube.logic.logic_utils"
file: "deepxube/logic/logic_utils.py"
line_start: 39
line_end: 61
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "lit"
    annotation: "Literal"
    default: null
  - name: "all_lits"
    annotation: "List[Literal]"
    default: null
returns: "Literal"
docstring_source: "present"
callees:
  - target: null
    expr: "set"
    call_sites: [42]
  - target: null
    expr: "all_args.update"
    call_sites: [44]
  - target: null
    expr: "all_args.add"
    call_sites: [54]
  - target: null
    expr: "args_new.append"
    call_sites: [56, 58]
  - target: "func:deepxube.logic.logic_objects.Literal"
    expr: "Literal"
    call_sites: [60]
  - target: null
    expr: "tuple"
    call_sites: [60]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_utils.replace_anon_vars`

**File:** [deepxube/logic/logic_utils.py:39](../../../../deepxube/logic/logic_utils.py#L39)
**Visibility:** public
**Kind:** function

## Signature

```python
def replace_anon_vars(lit: Literal, all_lits: List[Literal]) -> Literal
```

## Docstring

Replace each anonymous ``'_'`` argument in ``lit`` with a fresh variable name not used in ``all_lits``;
:return: the updated Literal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `lit` | `Literal` | — |
| `all_lits` | `List[Literal]` | — |

## Returns

`Literal`

## Calls

- `Literal` → `func:deepxube.logic.logic_objects.Literal` (lines: 60)

### Unresolved
- `set` (lines: 42)
- `all_args.update` (lines: 44)
- `all_args.add` (lines: 54)
- `args_new.append` (lines: 56, 58)
- `tuple` (lines: 60)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def replace_anon_vars(lit: Literal, all_lits: List[Literal]) -> Literal:
    """ Replace each anonymous ``'_'`` argument in ``lit`` with a fresh variable name not used in ``all_lits``;
    :return: the updated Literal. """
    all_args: Set[str] = set()
    for lit2 in [lit] + all_lits:
        all_args.update(lit2.arguments)

    args_new: List[str] = []
    for arg in lit.arguments:
        if arg == "_":
            arg_new: str = "V0"
            arg_new_idx: int = 0
            while arg_new in all_args:
                arg_new_idx += 1
                arg_new = f"V{arg_new_idx}"
            all_args.add(arg_new)

            args_new.append(arg_new)
        else:
            args_new.append(arg)

    lit_ret: Literal = Literal(lit.predicate, tuple(args_new), lit.directions, positive=lit.positive)
    return lit_ret
```
