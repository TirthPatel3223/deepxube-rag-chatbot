---
id: "func:deepxube.base.domain.GoalStateSampGoalSamp.sample_goalstate_goal_pairs"
kind: "method"
name: "sample_goalstate_goal_pairs"
qualified_name: "deepxube.base.domain.GoalStateSampGoalSamp.sample_goalstate_goal_pairs"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 386
line_end: 390
class: "GoalStateSampGoalSamp"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num"
    annotation: "int"
    default: null
returns: "Tuple[List[S], List[G]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.GoalStateSampGoalSamp.sample_goal_states"
    expr: "self.sample_goal_states"
    call_sites: [388]
  - target: "func:deepxube.base.domain.GoalStateSampGoalSamp.sample_goal_from_state"
    expr: "self.sample_goal_from_state"
    call_sites: [389]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.GoalStateSampGoalSamp.sample_goalstate_goal_pairs`

**File:** [deepxube/base/domain.py:386](../../../../deepxube/base/domain.py#L386)
**Class:** `GoalStateSampGoalSamp`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[S], List[G]]
```

## Docstring

Sample goal states first, then derive goals from each. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`Tuple[List[S], List[G]]`

## Calls

- `self.sample_goal_states` → `func:deepxube.base.domain.GoalStateSampGoalSamp.sample_goal_states` (lines: 388)
- `self.sample_goal_from_state` → `func:deepxube.base.domain.GoalStateSampGoalSamp.sample_goal_from_state` (lines: 389)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[S], List[G]]:
        """ Sample goal states first, then derive goals from each. """
        states_goal: List[S] = self.sample_goal_states(num)
        goals: List[G] = self.sample_goal_from_state(None, states_goal)
        return states_goal, goals
```
