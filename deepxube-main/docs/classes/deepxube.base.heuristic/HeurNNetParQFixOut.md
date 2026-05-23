---
id: "class:deepxube.base.heuristic.HeurNNetParQFixOut"
kind: "class"
name: "HeurNNetParQFixOut"
qualified_name: "deepxube.base.heuristic.HeurNNetParQFixOut"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 317
line_end: 370
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HeurNNetParQ"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_fn"
  - "func:deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_par_fn"
  - "func:deepxube.base.heuristic.HeurNNetParQFixOut.to_np"
  - "func:deepxube.base.heuristic.HeurNNetParQFixOut._to_np_fixed_acts"
  - "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_input"
  - "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_output"
  - "func:deepxube.base.heuristic.HeurNNetParQFixOut._check_same_num_acts"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurNNetParQFixOut`

**File:** [deepxube/base/heuristic.py:317](../../../deepxube/base/heuristic.py#L317)
**Abstract:** yes

## Docstring

DQN with a fixed output shape

    

## Inheritance

**Direct bases:**
- `HeurNNetParQ`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_nnet_fn`
- `get_nnet_par_fn`
- `to_np`
- `_to_np_fixed_acts` *(trivial, skipped)*
- `_get_input`
- `_get_output`
- `_check_same_num_acts` *(trivial, skipped)*

## Source

```python
class HeurNNetParQFixOut(HeurNNetParQ, ABC):
    """ DQN with a fixed output shape

    """
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnQ:
        """ In-process callable that runs the fixed-output Q network and slices per-state outputs. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet: List[NDArray] = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray[np.float64] = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]
            return self._get_output(states, q_vals_np, update_num)

        return heuristic_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet: List[NDArray] = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray[np.float64] = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]
            return self._get_output(states, q_vals_np, update_num)

        return heuristic_fn

    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Validate equal action counts then delegate to ``_to_np_fixed_acts``. """
        self._check_same_num_acts(actions_l)
        return self._to_np_fixed_acts(states, goals, actions_l)

    @abstractmethod
    def _to_np_fixed_acts(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Subclass hook: build numpy inputs given equal-length per-state action lists. """
        pass

    def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
        """ Prepare numpy inputs for the network (delegates to ``to_np``). """
        inputs_nnet: List[NDArray] = self.to_np(states, goals, actions_l)
        return inputs_nnet

    @staticmethod
    def _get_output(states: List[State], q_vals_np: NDArray[np.float64], update_num: Optional[int]) -> List[List[float]]:
        """ Clamp Q-values non-negative; zero on ``update_num == 0``; split into per-state lists. """
        assert q_vals_np.shape[0] == len(states)
        q_vals_np = np.maximum(q_vals_np, 0)
        if (update_num is not None) and (update_num == 0):
            q_vals_np = q_vals_np * 0
        q_vals_l: List[List[float]] = [q_vals_np[state_idx].astype(np.float64).tolist() for state_idx in
                                       range(len(states))]
        return q_vals_l

    @staticmethod
    def _check_same_num_acts(actions_l: List[List[Action]]) -> None:
        """ Assert every per-state action list has the same length. """
        assert len(set(len(actions) for actions in actions_l)) == 1, "num actions should be the same for all instances"
```
