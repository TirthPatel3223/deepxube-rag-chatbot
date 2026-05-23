---
id: "class:deepxube.base.domain.GoalStateSampGoalSamp"
kind: "class"
name: "GoalStateSampGoalSamp"
qualified_name: "deepxube.base.domain.GoalStateSampGoalSamp"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 384
line_end: 390
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GoalStateGoalPairSampleable[S, A, G]"
    resolved_id: null
  - name: "GoalStateSampleable[S, A, G]"
    resolved_id: null
  - name: "GoalSampleableFromState[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalStateSampGoalSamp.sample_goalstate_goal_pairs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalStateSampGoalSamp`

**File:** [deepxube/base/domain.py:384](../../../deepxube/base/domain.py#L384)
**Abstract:** yes

## Docstring

Sample goal state and then sample goals from goal states 

## Inheritance

**Direct bases:**
- `GoalStateGoalPairSampleable[S, A, G]`
- `GoalStateSampleable[S, A, G]`
- `GoalSampleableFromState[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_goalstate_goal_pairs`

## Source

```python
class GoalStateSampGoalSamp(GoalStateGoalPairSampleable[S, A, G], GoalStateSampleable[S, A, G], GoalSampleableFromState[S, A, G], ABC):
    """ Sample goal state and then sample goals from goal states """
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[S], List[G]]:
        """ Sample goal states first, then derive goals from each. """
        states_goal: List[S] = self.sample_goal_states(num)
        goals: List[G] = self.sample_goal_from_state(None, states_goal)
        return states_goal, goals
```
