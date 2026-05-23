---
id: "class:deepxube.base.nnet_input.StateGoalIn"
kind: "class"
name: "StateGoalIn"
qualified_name: "deepxube.base.nnet_input.StateGoalIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 70
line_end: 76
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "D"
  - "S"
  - "G"
bases:
  - name: "NNetInput[D]"
    resolved_id: null
  - name: "Generic[D, S, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.StateGoalIn.to_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.StateGoalIn`

**File:** [deepxube/base/nnet_input.py:70](../../../deepxube/base/nnet_input.py#L70)
**Abstract:** yes
**Generic parameters:** `D, S, G`

## Docstring

Marker mixin: input is built from (states, goals). 

## Inheritance

**Direct bases:**
- `NNetInput[D]`
- `Generic[D, S, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `to_np` *(trivial, skipped)*

## Source

```python
class StateGoalIn(NNetInput[D], Generic[D, S, G]):
    """ Marker mixin: input is built from (states, goals). """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """ Convert (state, goal) pairs to numpy network inputs. """
        pass
```
