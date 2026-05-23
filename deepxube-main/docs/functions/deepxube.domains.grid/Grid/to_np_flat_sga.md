---
id: "func:deepxube.domains.grid.Grid.to_np_flat_sga"
kind: "method"
name: "to_np_flat_sga"
qualified_name: "deepxube.domains.grid.Grid.to_np_flat_sga"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 119
line_end: 121
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
  - name: "states"
    annotation: "List[GridState]"
    default: null
  - name: "goals"
    annotation: "List[GridGoal]"
    default: null
  - name: "actions"
    annotation: "List[GridAction]"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.grid.Grid.to_np_flat_sg"
    expr: "self.to_np_flat_sg"
    call_sites: [121]
  - target: "func:numpy.expand_dims"
    expr: "np.expand_dims"
    call_sites: [121]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [121]
  - target: "func:deepxube.domains.grid.Grid.actions_to_indices"
    expr: "self.actions_to_indices"
    call_sites: [121]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.grid.Grid.to_np_flat_sga`

**File:** [deepxube/domains/grid.py:119](../../../../deepxube/domains/grid.py#L119)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_flat_sga(self, states: List[GridState], goals: List[GridGoal], actions: List[GridAction]) -> List[NDArray]
```

## Docstring

:return: Flat state+goal arrays extended with action indices. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[GridState]` | — |
| `goals` | `List[GridGoal]` | — |
| `actions` | `List[GridAction]` | — |

## Returns

`List[NDArray]`

## Calls

- `self.to_np_flat_sg` → `func:deepxube.domains.grid.Grid.to_np_flat_sg` (lines: 121)
- `np.expand_dims` → `func:numpy.expand_dims` (lines: 121)
- `np.array` → `func:numpy.array` (lines: 121)
- `self.actions_to_indices` → `func:deepxube.domains.grid.Grid.actions_to_indices` (lines: 121)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_flat_sga(self, states: List[GridState], goals: List[GridGoal], actions: List[GridAction]) -> List[NDArray]:
        """ :return: Flat state+goal arrays extended with action indices. """
        return self.to_np_flat_sg(states, goals) + [np.expand_dims(np.array(self.actions_to_indices(actions)), 1)]
```
