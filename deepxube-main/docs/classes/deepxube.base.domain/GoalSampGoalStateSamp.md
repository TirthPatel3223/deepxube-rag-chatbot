---
id: "class:deepxube.base.domain.GoalSampGoalStateSamp"
kind: "class"
name: "GoalSampGoalStateSamp"
qualified_name: "deepxube.base.domain.GoalSampGoalStateSamp"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 393
line_end: 399
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GoalStateGoalPairSampleable[S, A, G]"
    resolved_id: null
  - name: "GoalSampleable[S, A, G]"
    resolved_id: null
  - name: "StateSampleableFromGoal[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalSampGoalStateSamp.sample_goalstate_goal_pairs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalSampGoalStateSamp`

**File:** [deepxube/base/domain.py:393](../../../deepxube/base/domain.py#L393)
**Abstract:** yes

## Docstring

Sample goals and then sample goal states from goals 

## Inheritance

**Direct bases:**
- `GoalStateGoalPairSampleable[S, A, G]`
- `GoalSampleable[S, A, G]`
- `StateSampleableFromGoal[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_goalstate_goal_pairs`

## Source

```python
class GoalSampGoalStateSamp(GoalStateGoalPairSampleable[S, A, G], GoalSampleable[S, A, G], StateSampleableFromGoal[S, A, G], ABC):
    """ Sample goals and then sample goal states from goals """
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[S], List[G]]:
        """ Sample goals first, then sample one matching state per goal. """
        goals: List[G] = self.sample_goals(num)
        states_goal: List[S] = self.sample_state_from_goal(goals)
        return states_goal, goals
```
