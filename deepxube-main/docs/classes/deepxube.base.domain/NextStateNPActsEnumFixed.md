---
id: "class:deepxube.base.domain.NextStateNPActsEnumFixed"
kind: "class"
name: "NextStateNPActsEnumFixed"
qualified_name: "deepxube.base.domain.NextStateNPActsEnumFixed"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 597
line_end: 608
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "NextStateNPActsEnum[S, A, G]"
    resolved_id: null
  - name: "ActsEnumFixed[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.NextStateNPActsEnumFixed._get_state_np_actions"
  - "func:deepxube.base.domain.NextStateNPActsEnumFixed._sample_state_np_action"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.NextStateNPActsEnumFixed`

**File:** [deepxube/base/domain.py:597](../../../deepxube/base/domain.py#L597)
**Abstract:** yes

## Docstring

``NextStateNP`` + ``ActsEnumFixed``: each row's action list is the fixed set. 

## Inheritance

**Direct bases:**
- `NextStateNPActsEnum[S, A, G]`
- `ActsEnumFixed[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_get_state_np_actions`
- `_sample_state_np_action`

## Source

```python
class NextStateNPActsEnumFixed(NextStateNPActsEnum[S, A, G], ActsEnumFixed[S, A, G], ABC):
    """ ``NextStateNP`` + ``ActsEnumFixed``: each row's action list is the fixed set. """

    def _get_state_np_actions(self, states_np: List[NDArray]) -> List[List[A]]:
        """ :return: A copy of the fixed action list per row in ``states_np[0]``. """
        state_actions: List[A] = self.get_actions_fixed()
        return [state_actions.copy() for _ in range(states_np[0].shape[0])]

    def _sample_state_np_action(self, states_np: List[NDArray]) -> List[A]:
        """ Uniformly sample one action per row from the fixed action list. """
        state_actions_l: List[List[A]] = self._get_state_np_actions(states_np)
        return [random.choice(state_actions) for state_actions in state_actions_l]
```
