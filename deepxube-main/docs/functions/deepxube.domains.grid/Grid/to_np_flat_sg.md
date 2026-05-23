---
id: "func:deepxube.domains.grid.Grid.to_np_flat_sg"
kind: "method"
name: "to_np_flat_sg"
qualified_name: "deepxube.domains.grid.Grid.to_np_flat_sg"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 114
line_end: 117
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
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [116, 117]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.grid.Grid.to_np_flat_sg`

**File:** [deepxube/domains/grid.py:114](../../../../deepxube/domains/grid.py#L114)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_flat_sg(self, states: List[GridState], goals: List[GridGoal]) -> List[NDArray]
```

## Docstring

:return: Stacked ``[sx, sy, gx, gy]`` arrays for each state/goal pair. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[GridState]` | — |
| `goals` | `List[GridGoal]` | — |

## Returns

`List[NDArray]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 116, 117)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_flat_sg(self, states: List[GridState], goals: List[GridGoal]) -> List[NDArray]:
        """ :return: Stacked ``[sx, sy, gx, gy]`` arrays for each state/goal pair. """
        return [np.stack([np.stack([state.robot_x for state in states]), np.stack([state.robot_y for state in states]),
                          np.stack([goal.robot_x for goal in goals]), np.stack([goal.robot_y for goal in goals])], axis=1)]
```
