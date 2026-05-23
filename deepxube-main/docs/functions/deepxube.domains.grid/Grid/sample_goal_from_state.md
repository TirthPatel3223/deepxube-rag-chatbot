---
id: "func:deepxube.domains.grid.Grid.sample_goal_from_state"
kind: "method"
name: "sample_goal_from_state"
qualified_name: "deepxube.domains.grid.Grid.sample_goal_from_state"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 103
line_end: 105
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
  - name: "states_start"
    annotation: "Optional[List[GridState]]"
    default: null
  - name: "states_goal"
    annotation: "List[GridState]"
    default: null
returns: "List[GridGoal]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.grid.GridGoal"
    expr: "GridGoal"
    call_sites: [105]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.grid.Grid.sample_goal_from_state`

**File:** [deepxube/domains/grid.py:103](../../../../deepxube/domains/grid.py#L103)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goal_from_state(self, states_start: Optional[List[GridState]], states_goal: List[GridState]) -> List[GridGoal]
```

## Docstring

:return: Goals matching the ``(x, y)`` position of each state in ``states_goal``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_start` | `Optional[List[GridState]]` | — |
| `states_goal` | `List[GridState]` | — |

## Returns

`List[GridGoal]`

## Calls

- `GridGoal` → `func:deepxube.domains.grid.GridGoal` (lines: 105)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_goal_from_state(self, states_start: Optional[List[GridState]], states_goal: List[GridState]) -> List[GridGoal]:
        """ :return: Goals matching the ``(x, y)`` position of each state in ``states_goal``. """
        return [GridGoal(state_goal.robot_x, state_goal.robot_y) for state_goal in states_goal]
```
