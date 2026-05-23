---
id: "class:deepxube.base.domain.StateGoalVizable"
kind: "class"
name: "StateGoalVizable"
qualified_name: "deepxube.base.domain.StateGoalVizable"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 179
line_end: 186
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.StateGoalVizable.visualize_state_goal"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.StateGoalVizable`

**File:** [deepxube/base/domain.py:179](../../../deepxube/base/domain.py#L179)
**Abstract:** yes

## Docstring

Can visualize problem instances

    

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `visualize_state_goal` *(trivial, skipped)*

## Source

```python
class StateGoalVizable(Domain[S, A, G]):
    """ Can visualize problem instances

    """
    @abstractmethod
    def visualize_state_goal(self, state: S, goal: G, fig: Figure) -> None:
        """ Render a single (state, goal) pair onto the matplotlib ``fig``. """
        pass
```
