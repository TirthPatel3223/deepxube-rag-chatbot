---
id: "func:deepxube.domains.grid.Grid.string_to_action"
kind: "method"
name: "string_to_action"
qualified_name: "deepxube.domains.grid.Grid.string_to_action"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 135
line_end: 140
class: "Grid"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "act_str"
    annotation: "str"
    default: null
returns: "Optional[GridAction]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.grid.GridAction"
    expr: "GridAction"
    call_sites: [138]
  - target: null
    expr: "int"
    call_sites: [138]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.grid.Grid.string_to_action`

**File:** [deepxube/domains/grid.py:135](../../../../deepxube/domains/grid.py#L135)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def string_to_action(self, act_str: str) -> Optional[GridAction]
```

## Docstring

:return: ``GridAction`` for ``'0'``–``'3'``, or ``None`` if unrecognised. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `act_str` | `str` | — |

## Returns

`Optional[GridAction]`

## Calls

- `GridAction` → `func:deepxube.domains.grid.GridAction` (lines: 138)

### Unresolved
- `int` (lines: 138)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def string_to_action(self, act_str: str) -> Optional[GridAction]:
        """ :return: ``GridAction`` for ``'0'``–``'3'``, or ``None`` if unrecognised. """
        if act_str in {"0", "1", "2", "3"}:
            return GridAction(int(act_str))
        else:
            return None
```
