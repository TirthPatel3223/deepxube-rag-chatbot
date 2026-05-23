---
id: "func:deepxube.domains.grid.Grid.sample_start_states"
kind: "method"
name: "sample_start_states"
qualified_name: "deepxube.domains.grid.Grid.sample_start_states"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 84
line_end: 86
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
  - name: "num_states"
    annotation: "int"
    default: null
returns: "List[GridState]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.grid.GridState"
    expr: "GridState"
    call_sites: [86]
  - target: null
    expr: "np.random.randint"
    call_sites: [86]
  - target: null
    expr: "range"
    call_sites: [86]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.grid.Grid.sample_start_states`

**File:** [deepxube/domains/grid.py:84](../../../../deepxube/domains/grid.py#L84)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_start_states(self, num_states: int) -> List[GridState]
```

## Docstring

:return: ``num_states`` random positions on the grid. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_states` | `int` | — |

## Returns

`List[GridState]`

## Calls

- `GridState` → `func:deepxube.domains.grid.GridState` (lines: 86)

### Unresolved
- `np.random.randint` (lines: 86)
- `range` (lines: 86)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def sample_start_states(self, num_states: int) -> List[GridState]:
        """ :return: ``num_states`` random positions on the grid. """
        return [GridState(np.random.randint(self.dim), np.random.randint(self.dim)) for _ in range(num_states)]
```
