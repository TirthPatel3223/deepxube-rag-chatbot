---
id: "class:deepxube.base.nnet_input.StateGoalActFixIn"
kind: "class"
name: "StateGoalActFixIn"
qualified_name: "deepxube.base.nnet_input.StateGoalActFixIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 79
line_end: 85
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
  - "func:deepxube.base.nnet_input.StateGoalActFixIn.to_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.StateGoalActFixIn`

**File:** [deepxube/base/nnet_input.py:79](../../../deepxube/base/nnet_input.py#L79)
**Abstract:** yes
**Generic parameters:** `D, S, G, A`

## Docstring

Marker mixin: input is built from (states, goals, fixed-length action lists). 

## Inheritance

**Direct bases:**
- `NNetInput[D]`
- `Generic[D, S, G, A]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `to_np` *(trivial, skipped)*

## Source

```python
class StateGoalActFixIn(NNetInput[D], Generic[D, S, G, A]):
    """ Marker mixin: input is built from (states, goals, fixed-length action lists). """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G], actions_l: List[List[A]]) -> List[NDArray]:
        """ Convert (state, goal, action-list) triples to numpy inputs. """
        pass
```
