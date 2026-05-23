---
id: "class:deepxube.base.domain.ActsFixed"
kind: "class"
name: "ActsFixed"
qualified_name: "deepxube.base.domain.ActsFixed"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 210
line_end: 220
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.ActsFixed.sample_action"
  - "func:deepxube.base.domain.ActsFixed.sample_state_action"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.ActsFixed`

**File:** [deepxube/base/domain.py:210](../../../deepxube/base/domain.py#L210)
**Abstract:** yes

## Docstring

Action mixin: action set is the same in every state. 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_action` *(trivial, skipped)*
- `sample_state_action`

## Source

```python
class ActsFixed(Domain[S, A, G]):
    """ Action mixin: action set is the same in every state. """

    @abstractmethod
    def sample_action(self, num: int) -> List[A]:
        """ :return: ``num`` random actions from the fixed action set. """
        pass

    def sample_state_action(self, states: List[S]) -> List[A]:
        """ Sample one random action per state, ignoring per-state availability. """
        return self.sample_action(len(states))
```
