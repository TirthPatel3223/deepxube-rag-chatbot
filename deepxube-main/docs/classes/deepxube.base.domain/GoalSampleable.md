---
id: "class:deepxube.base.domain.GoalSampleable"
kind: "class"
name: "GoalSampleable"
qualified_name: "deepxube.base.domain.GoalSampleable"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 316
line_end: 323
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalSampleable.sample_goals"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalSampleable`

**File:** [deepxube/base/domain.py:316](../../../deepxube/base/domain.py#L316)
**Abstract:** yes

## Docstring

Can sample goals 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_goals` *(trivial, skipped)*

## Source

```python
class GoalSampleable(Domain[S, A, G]):
    """ Can sample goals """
    @abstractmethod
    def sample_goals(self, num: int) -> List[G]:
        """ Sample goals
        :return: Goals
        """
        pass
```
