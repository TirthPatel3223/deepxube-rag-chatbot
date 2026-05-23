---
id: "class:deepxube.base.domain.StateSampleableFromGoal"
kind: "class"
name: "StateSampleableFromGoal"
qualified_name: "deepxube.base.domain.StateSampleableFromGoal"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 349
line_end: 358
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.StateSampleableFromGoal.sample_state_from_goal"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.StateSampleableFromGoal`

**File:** [deepxube/base/domain.py:349](../../../deepxube/base/domain.py#L349)
**Abstract:** yes

## Docstring

Can sample states from goals 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_state_from_goal` *(trivial, skipped)*

## Source

```python
class StateSampleableFromGoal(Domain[S, A, G]):
    """ Can sample states from goals """
    @abstractmethod
    def sample_state_from_goal(self, goals: List[G]) -> List[S]:
        """ Given a goal, sample a state that is a member of the set of states represneted by that goal.

        :param goals: List of goals
        :return: List of list of states, where each state is a member of the set of goal states represented by the corresponding goal
        """
        pass
```
