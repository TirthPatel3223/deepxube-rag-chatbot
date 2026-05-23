---
id: "class:deepxube.base.domain.GoalStateSampleable"
kind: "class"
name: "GoalStateSampleable"
qualified_name: "deepxube.base.domain.GoalStateSampleable"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 326
line_end: 333
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalStateSampleable.sample_goal_states"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalStateSampleable`

**File:** [deepxube/base/domain.py:326](../../../deepxube/base/domain.py#L326)
**Abstract:** yes

## Docstring

Can sample goal states 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_goal_states` *(trivial, skipped)*

## Source

```python
class GoalStateSampleable(Domain[S, A, G]):
    """ Can sample goal states """
    @abstractmethod
    def sample_goal_states(self, num: int) -> List[S]:
        """ Sample goal states
        :return: Goal states
        """
        pass
```
