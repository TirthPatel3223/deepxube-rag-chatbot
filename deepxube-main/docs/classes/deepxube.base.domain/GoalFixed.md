---
id: "class:deepxube.base.domain.GoalFixed"
kind: "class"
name: "GoalFixed"
qualified_name: "deepxube.base.domain.GoalFixed"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 361
line_end: 373
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GoalSampleable[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalFixed.get_goal"
  - "func:deepxube.base.domain.GoalFixed.sample_goals"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalFixed`

**File:** [deepxube/base/domain.py:361](../../../deepxube/base/domain.py#L361)
**Abstract:** yes

## Docstring

Goal is the same for all problem instances 

## Inheritance

**Direct bases:**
- `GoalSampleable[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_goal` *(trivial, skipped)*
- `sample_goals`

## Source

```python
class GoalFixed(GoalSampleable[S, A, G]):
    """ Goal is the same for all problem instances """

    @abstractmethod
    def get_goal(self) -> G:
        """
        :return: Fixed goal
        """
        pass

    def sample_goals(self, num: int) -> List[G]:
        """ :return: ``num`` copies of the fixed goal. """
        return [self.get_goal()] * num
```
