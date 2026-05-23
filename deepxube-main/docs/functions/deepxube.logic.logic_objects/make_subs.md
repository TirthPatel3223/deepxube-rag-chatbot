---
id: "func:deepxube.logic.logic_objects.make_subs"
kind: "function"
name: "make_subs"
qualified_name: "deepxube.logic.logic_objects.make_subs"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 406
line_end: 411
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
  - name: "subs"
    annotation: "Dict[str, str]"
    default: null
returns: "Clause"
docstring_source: "present"
callees:
  - target: "func:deepxube.logic.logic_objects.make_subs_lit"
    expr: "make_subs_lit"
    call_sites: [408, 409]
  - target: null
    expr: "tuple"
    call_sites: [409]
  - target: "func:deepxube.logic.logic_objects.Clause"
    expr: "Clause"
    call_sites: [410]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_objects.make_subs`

**File:** [deepxube/logic/logic_objects.py:406](../../../../deepxube/logic/logic_objects.py#L406)
**Visibility:** public
**Kind:** function

## Signature

```python
def make_subs(clause: Clause, subs: Dict[str, str]) -> Clause
```

## Docstring

:return: A new Clause with all variables in head and body replaced according to ``subs``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `clause` | `Clause` | — |
| `subs` | `Dict[str, str]` | — |

## Returns

`Clause`

## Calls

- `make_subs_lit` → `func:deepxube.logic.logic_objects.make_subs_lit` (lines: 408, 409)
- `Clause` → `func:deepxube.logic.logic_objects.Clause` (lines: 410)

### Unresolved
- `tuple` (lines: 409)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def make_subs(clause: Clause, subs: Dict[str, str]) -> Clause:
    """ :return: A new Clause with all variables in head and body replaced according to ``subs``. """
    head_sub: Literal = make_subs_lit(clause.head, subs)
    body_sub: Tuple[Literal, ...] = tuple(make_subs_lit(x, subs) for x in clause.body)
    clause_sub: Clause = Clause(head_sub, body_sub)
    return clause_sub
```
