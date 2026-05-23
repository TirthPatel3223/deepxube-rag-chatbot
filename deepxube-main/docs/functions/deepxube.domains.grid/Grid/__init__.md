---
id: "func:deepxube.domains.grid.Grid.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.grid.Grid.__init__"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 75
line_end: 79
class: "Grid"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "dim"
    annotation: "int"
    default: "7"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [77]
  - target: null
    expr: "super"
    call_sites: [77]
  - target: "func:deepxube.domains.grid.GridAction"
    expr: "GridAction"
    call_sites: [79]
raises: []
reads_attrs:
  - "self.actions_fixed"
  - "self.dim"
writes_attrs:
  - "self.actions_fixed"
  - "self.dim"
---

# `deepxube.domains.grid.Grid.__init__`

**File:** [deepxube/domains/grid.py:75](../../../../deepxube/domains/grid.py#L75)
**Class:** `Grid`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, dim: int = 7)
```

## Docstring

Set grid dimension and precompute the 4 fixed actions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `dim` | `int` | `7` |

## Returns

*(Not annotated.)*

## Calls

- `GridAction` → `func:deepxube.domains.grid.GridAction` (lines: 79)

### Unresolved
- `super().__init__` (lines: 77)
- `super` (lines: 77)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.actions_fixed`
- `self.dim`

**Reads:**
- `self.actions_fixed`
- `self.dim`

## Source

```python
    def __init__(self, dim: int = 7):
        """ Set grid dimension and precompute the 4 fixed actions. """
        super().__init__()
        self.dim: int = dim
        self.actions_fixed: List[GridAction] = [GridAction(x) for x in [0, 1, 2, 3]]
```
