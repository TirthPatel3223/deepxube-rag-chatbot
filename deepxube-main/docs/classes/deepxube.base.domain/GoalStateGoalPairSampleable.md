---
id: "class:deepxube.base.domain.GoalStateGoalPairSampleable"
kind: "class"
name: "GoalStateGoalPairSampleable"
qualified_name: "deepxube.base.domain.GoalStateGoalPairSampleable"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 376
line_end: 381
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalStateGoalPairSampleable.sample_goalstate_goal_pairs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalStateGoalPairSampleable`

**File:** [deepxube/base/domain.py:376](../../../deepxube/base/domain.py#L376)
**Abstract:** yes

## Docstring

Can sample pairs of states and corresponding goals of which the sampled state is a member 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_goalstate_goal_pairs` *(trivial, skipped)*

## Source

```python
class GoalStateGoalPairSampleable(Domain[S, A, G]):
    """ Can sample pairs of states and corresponding goals of which the sampled state is a member """
    @abstractmethod
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[S], List[G]]:
        """ :return: ``num`` (goal-state, goal) pairs where the state satisfies the goal. """
        pass
```
