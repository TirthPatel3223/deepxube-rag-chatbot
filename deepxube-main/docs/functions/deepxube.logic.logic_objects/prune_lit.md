---
id: "func:deepxube.logic.logic_objects.prune_lit"
kind: "function"
name: "prune_lit"
qualified_name: "deepxube.logic.logic_objects.prune_lit"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 293
line_end: 301
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
  - name: "lit_to_prune"
    annotation: "Literal"
    default: null
  - name: "idxs_vars_req"
    annotation: "List[Tuple[int, str]]"
    default: null
returns: "bool"
docstring_source: "present"
callees: []
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_objects.prune_lit`

**File:** [deepxube/logic/logic_objects.py:293](../../../../deepxube/logic/logic_objects.py#L293)
**Visibility:** public
**Kind:** function

## Signature

```python
def prune_lit(lit: Literal, lit_to_prune: Literal, idxs_vars_req: List[Tuple[int, str]]) -> bool
```

## Docstring

:return: True if ``lit_to_prune`` can be ruled out as a match for ``lit`` given the required variable bindings. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `lit` | `Literal` | — |
| `lit_to_prune` | `Literal` | — |
| `idxs_vars_req` | `List[Tuple[int, str]]` | — |

## Returns

`bool`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def prune_lit(lit: Literal, lit_to_prune: Literal, idxs_vars_req: List[Tuple[int, str]]) -> bool:
    """ :return: True if ``lit_to_prune`` can be ruled out as a match for ``lit`` given the required variable bindings. """
    if lit.positive != lit_to_prune.positive:
        return True
    else:
        for idx, var_req in idxs_vars_req:
            if lit_to_prune.arguments[idx] != var_req:
                return True
    return False
```
