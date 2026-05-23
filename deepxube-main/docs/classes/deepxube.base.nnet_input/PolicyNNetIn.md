---
id: "class:deepxube.base.nnet_input.PolicyNNetIn"
kind: "class"
name: "PolicyNNetIn"
qualified_name: "deepxube.base.nnet_input.PolicyNNetIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 97
line_end: 118
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "D"
  - "S"
  - "G"
  - "A"
bases:
  - name: "NNetInput[D]"
    resolved_id: null
  - name: "Generic[D, S, G, A]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.PolicyNNetIn.to_np"
  - "func:deepxube.base.nnet_input.PolicyNNetIn.to_np_fn"
  - "func:deepxube.base.nnet_input.PolicyNNetIn.nnet_out_to_actions"
  - "func:deepxube.base.nnet_input.PolicyNNetIn.states_goals_actions_split_idx"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.PolicyNNetIn`

**File:** [deepxube/base/nnet_input.py:97](../../../deepxube/base/nnet_input.py#L97)
**Abstract:** yes
**Generic parameters:** `D, S, G, A`

## Docstring

Marker mixin: input feeds a policy network — needs both training (with actions) and inference (without) conversions. 

## Inheritance

**Direct bases:**
- `NNetInput[D]`
- `Generic[D, S, G, A]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `to_np` *(trivial, skipped)*
- `to_np_fn` *(trivial, skipped)*
- `nnet_out_to_actions` *(trivial, skipped)*
- `states_goals_actions_split_idx` *(trivial, skipped)*

## Source

```python
class PolicyNNetIn(NNetInput[D], Generic[D, S, G, A]):
    """ Marker mixin: input feeds a policy network — needs both training (with actions) and inference (without) conversions. """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G], actions: List[A]) -> List[NDArray]:
        """ Training-side conversion (target actions included). """
        pass

    @abstractmethod
    def to_np_fn(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """ Inference-side conversion (no actions). """
        pass

    @abstractmethod
    def nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[A]:
        """ Decode network output arrays into ``A`` objects. """
        pass

    @abstractmethod
    def states_goals_actions_split_idx(self) -> int:
        """ :return: Index in the ``to_np`` list at which actions begin (states/goals on the left). """
        pass
```
