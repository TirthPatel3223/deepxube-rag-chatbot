---
id: "class:deepxube.base.domain.GoalSampleableFromState"
kind: "class"
name: "GoalSampleableFromState"
qualified_name: "deepxube.base.domain.GoalSampleableFromState"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 336
line_end: 346
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalSampleableFromState.sample_goal_from_state"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalSampleableFromState`

**File:** [deepxube/base/domain.py:336](../../../deepxube/base/domain.py#L336)
**Abstract:** yes

## Docstring

Can sample goals from states such that the state is a member of the sampled goal 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_goal_from_state` *(trivial, skipped)*

## Source

```python
class GoalSampleableFromState(Domain[S, A, G]):
    """ Can sample goals from states such that the state is a member of the sampled goal """
    @abstractmethod
    def sample_goal_from_state(self, states_start: Optional[List[S]], states_goal: List[S]) -> List[G]:
        """ Given a state, sample a goal that represents a set of goal states of which the given state is a member.

        :param states_start: Optional list of start states. Can be used to sample goals that are difficult to achieve from the given start state.
        :param states_goal: List of states from which goals will be sampled.
        :return: Goals
        """
        pass
```
