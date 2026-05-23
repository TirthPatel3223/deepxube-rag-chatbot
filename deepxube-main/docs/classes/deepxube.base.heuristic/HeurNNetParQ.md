---
id: "class:deepxube.base.heuristic.HeurNNetParQ"
kind: "class"
name: "HeurNNetParQ"
qualified_name: "deepxube.base.heuristic.HeurNNetParQ"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 298
line_end: 314
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HeurNNetPar[HeurFnQ]"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.HeurNNetParQ.get_nnet_fn"
  - "func:deepxube.base.heuristic.HeurNNetParQ.get_nnet_par_fn"
  - "func:deepxube.base.heuristic.HeurNNetParQ.to_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurNNetParQ`

**File:** [deepxube/base/heuristic.py:298](../../../deepxube/base/heuristic.py#L298)
**Abstract:** yes

## Docstring

Q-type heuristic ``Par`` base; concrete subclasses are the fixed-output and action-input variants. 

## Inheritance

**Direct bases:**
- `HeurNNetPar[HeurFnQ]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_nnet_fn` *(trivial, skipped)*
- `get_nnet_par_fn` *(trivial, skipped)*
- `to_np` *(trivial, skipped)*

## Source

```python
class HeurNNetParQ(HeurNNetPar[HeurFnQ]):
    """ Q-type heuristic ``Par`` base; concrete subclasses are the fixed-output and action-input variants. """

    @abstractmethod
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnQ:
        """ :return: In-process Q-heuristic callable. """
        pass

    @abstractmethod
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ:
        """ :return: Worker-routed Q-heuristic callable. """
        pass

    @abstractmethod
    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Convert (state, goal, per-state action list) into numpy inputs. """
        pass
```
