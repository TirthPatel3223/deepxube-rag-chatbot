---
id: "class:deepxube.base.nnet_input.StateGoalActIn"
kind: "class"
name: "StateGoalActIn"
qualified_name: "deepxube.base.nnet_input.StateGoalActIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 88
line_end: 94
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
  - "func:deepxube.base.nnet_input.StateGoalActIn.to_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.StateGoalActIn`

**File:** [deepxube/base/nnet_input.py:88](../../../deepxube/base/nnet_input.py#L88)
**Abstract:** yes
**Generic parameters:** `D, S, G, A`

## Docstring

Marker mixin: input is built from (states, goals, one action per row). 

## Inheritance

**Direct bases:**
- `NNetInput[D]`
- `Generic[D, S, G, A]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `to_np` *(trivial, skipped)*

## Source

```python
class StateGoalActIn(NNetInput[D], Generic[D, S, G, A]):
    """ Marker mixin: input is built from (states, goals, one action per row). """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G], actions: List[A]) -> List[NDArray]:
        """ Convert (state, goal, action) triples to numpy inputs. """
        pass
```
