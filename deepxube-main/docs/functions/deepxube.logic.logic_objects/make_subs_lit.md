---
id: "func:deepxube.logic.logic_objects.make_subs_lit"
kind: "function"
name: "make_subs_lit"
qualified_name: "deepxube.logic.logic_objects.make_subs_lit"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 399
line_end: 403
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
  - name: "subs"
    annotation: "Dict[str, str]"
    default: null
returns: "Literal"
docstring_source: "present"
callees:
  - target: null
    expr: "tuple"
    call_sites: [401]
  - target: "func:deepxube.logic.logic_objects.Literal"
    expr: "Literal"
    call_sites: [402]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_objects.make_subs_lit`

**File:** [deepxube/logic/logic_objects.py:399](../../../../deepxube/logic/logic_objects.py#L399)
**Visibility:** public
**Kind:** function

## Signature

```python
def make_subs_lit(lit: Literal, subs: Dict[str, str]) -> Literal
```

## Docstring

:return: A new Literal with all variables replaced according to ``subs``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `lit` | `Literal` | — |
| `subs` | `Dict[str, str]` | — |

## Returns

`Literal`

## Calls

- `Literal` → `func:deepxube.logic.logic_objects.Literal` (lines: 402)

### Unresolved
- `tuple` (lines: 401)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def make_subs_lit(lit: Literal, subs: Dict[str, str]) -> Literal:
    """ :return: A new Literal with all variables replaced according to ``subs``. """
    args_sub: Tuple[str, ...] = tuple(subs[x] for x in lit.arguments)
    lit_sub: Literal = Literal(lit.predicate, args_sub, lit.directions, positive=lit.positive)
    return lit_sub
```
