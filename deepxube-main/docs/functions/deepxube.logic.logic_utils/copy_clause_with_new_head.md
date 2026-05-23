---
id: "func:deepxube.logic.logic_utils.copy_clause_with_new_head"
kind: "function"
name: "copy_clause_with_new_head"
qualified_name: "deepxube.logic.logic_utils.copy_clause_with_new_head"
module: "deepxube.logic.logic_utils"
file: "deepxube/logic/logic_utils.py"
line_start: 99
line_end: 105
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "clause"
    annotation: "Clause"
    default: null
  - name: "head_name_new"
    annotation: "str"
    default: null
returns: "Clause"
docstring_source: "present"
callees:
  - target: "func:deepxube.logic.logic_objects.Clause"
    expr: "Clause"
    call_sites: [102]
  - target: "func:deepxube.logic.logic_objects.Literal"
    expr: "Literal"
    call_sites: [102]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_utils.copy_clause_with_new_head`

**File:** [deepxube/logic/logic_utils.py:99](../../../../deepxube/logic/logic_utils.py#L99)
**Visibility:** public
**Kind:** function

## Signature

```python
def copy_clause_with_new_head(clause: Clause, head_name_new: str) -> Clause
```

## Docstring

:return: A copy of ``clause`` with the head predicate name replaced by ``head_name_new``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `clause` | `Clause` | — |
| `head_name_new` | `str` | — |

## Returns

`Clause`

## Calls

- `Clause` → `func:deepxube.logic.logic_objects.Clause` (lines: 102)
- `Literal` → `func:deepxube.logic.logic_objects.Literal` (lines: 102)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def copy_clause_with_new_head(clause: Clause, head_name_new: str) -> Clause:
    """ :return: A copy of ``clause`` with the head predicate name replaced by ``head_name_new``. """
    assert clause.head.positive, "Head should be positive"
    clause_new = Clause(Literal(head_name_new, clause.head.arguments, clause.head.directions,
                                positive=clause.head.positive), clause.body)

    return clause_new
```
