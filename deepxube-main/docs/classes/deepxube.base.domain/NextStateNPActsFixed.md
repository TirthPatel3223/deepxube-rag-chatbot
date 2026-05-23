---
id: "class:deepxube.base.domain.NextStateNPActsFixed"
kind: "class"
name: "NextStateNPActsFixed"
qualified_name: "deepxube.base.domain.NextStateNPActsFixed"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 589
line_end: 594
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "NextStateNP[S, A, G]"
    resolved_id: null
  - name: "ActsFixed[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.NextStateNPActsFixed._sample_state_np_action"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.NextStateNPActsFixed`

**File:** [deepxube/base/domain.py:589](../../../deepxube/base/domain.py#L589)
**Abstract:** yes

## Docstring

``NextStateNP`` + ``ActsFixed``: action set fixed, state representation numpy. 

## Inheritance

**Direct bases:**
- `NextStateNP[S, A, G]`
- `ActsFixed[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_sample_state_np_action`

## Source

```python
class NextStateNPActsFixed(NextStateNP[S, A, G], ActsFixed[S, A, G], ABC):
    """ ``NextStateNP`` + ``ActsFixed``: action set fixed, state representation numpy. """

    def _sample_state_np_action(self, states_np: List[NDArray]) -> List[A]:
        """ Sample one action per row from the fixed action set. """
        return self.sample_action(states_np[0].shape[0])
```
