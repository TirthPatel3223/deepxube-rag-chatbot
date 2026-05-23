---
id: "func:deepxube.base.domain.GoalSampGoalStateSamp.sample_goalstate_goal_pairs"
kind: "method"
name: "sample_goalstate_goal_pairs"
qualified_name: "deepxube.base.domain.GoalSampGoalStateSamp.sample_goalstate_goal_pairs"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 395
line_end: 399
class: "GoalSampGoalStateSamp"
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
  - target: "func:deepxube.base.domain.GoalSampGoalStateSamp.sample_goals"
    expr: "self.sample_goals"
    call_sites: [397]
  - target: "func:deepxube.base.domain.GoalSampGoalStateSamp.sample_state_from_goal"
    expr: "self.sample_state_from_goal"
    call_sites: [398]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.GoalSampGoalStateSamp.sample_goalstate_goal_pairs`

**File:** [deepxube/base/domain.py:395](../../../../deepxube/base/domain.py#L395)
**Class:** `GoalSampGoalStateSamp`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[S], List[G]]
```

## Docstring

Sample goals first, then sample one matching state per goal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`Tuple[List[S], List[G]]`

## Calls

- `self.sample_goals` → `func:deepxube.base.domain.GoalSampGoalStateSamp.sample_goals` (lines: 397)
- `self.sample_state_from_goal` → `func:deepxube.base.domain.GoalSampGoalStateSamp.sample_state_from_goal` (lines: 398)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[S], List[G]]:
        """ Sample goals first, then sample one matching state per goal. """
        goals: List[G] = self.sample_goals(num)
        states_goal: List[S] = self.sample_state_from_goal(goals)
        return states_goal, goals
```
