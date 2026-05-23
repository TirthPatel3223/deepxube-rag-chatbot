---
id: "class:deepxube.base.heuristic.HeurNNetParQIn"
kind: "class"
name: "HeurNNetParQIn"
qualified_name: "deepxube.base.heuristic.HeurNNetParQIn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 373
line_end: 431
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
  - "func:deepxube.base.heuristic.HeurNNetParQIn.get_nnet_fn"
  - "func:deepxube.base.heuristic.HeurNNetParQIn.get_nnet_par_fn"
  - "func:deepxube.base.heuristic.HeurNNetParQIn.to_np"
  - "func:deepxube.base.heuristic.HeurNNetParQIn._to_np_one_act"
  - "func:deepxube.base.heuristic.HeurNNetParQIn._get_input"
  - "func:deepxube.base.heuristic.HeurNNetParQIn._get_output"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurNNetParQIn`

**File:** [deepxube/base/heuristic.py:373](../../../deepxube/base/heuristic.py#L373)
**Abstract:** yes

## Docstring

DQN that takes a single action as input

    

## Inheritance

**Direct bases:**
- `HeurNNetParQ`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_nnet_fn`
- `get_nnet_par_fn`
- `to_np`
- `_to_np_one_act` *(trivial, skipped)*
- `_get_input`
- `_get_output`

## Source

```python
class HeurNNetParQIn(HeurNNetParQ, ABC):
    """ DQN that takes a single action as input

    """
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device,
                    update_num: Optional[int]) -> HeurFnQ:
        """ In-process callable that flattens per-state actions, runs the action-input Q network, and unflattens the result. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet, states_rep, split_idxs = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]
            return self._get_output(states_rep, q_vals_np, split_idxs, update_num)

        return heuristic_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet, states_rep, split_idxs = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]
            return self._get_output(states_rep, q_vals_np, split_idxs, update_num)

        return heuristic_fn

    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Assert one action per state, then delegate to ``_to_np_one_act``. """
        assert all((len(actions) == 1) for actions in actions_l), "there should only be one action per state/goal pair"
        actions_one: List[Action] = [actions[0] for actions in actions_l]
        return self._to_np_one_act(states, goals, actions_one)

    @abstractmethod
    def _to_np_one_act(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]:
        """ Subclass hook: build numpy inputs for one action per (state, goal). """
        pass

    def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> Tuple[List[NDArray], List[State], List[int]]:
        """ Flatten per-state actions, replicate states/goals to match, and produce numpy inputs + split indices. """
        actions_flat, split_idxs = misc_utils.flatten(actions_l)
        states_rep: List[State] = []
        goals_rep: List[Goal] = []
        for state, goal, actions in zip(states, goals, actions_l, strict=True):
            states_rep.extend([state] * len(actions))
            goals_rep.extend([goal] * len(actions))
        inputs_nnet: List[NDArray] = self._to_np_one_act(states_rep, goals_rep, actions_flat)

        return inputs_nnet, states_rep, split_idxs

    @staticmethod
    def _get_output(states_rep: List[State], q_vals_np: NDArray[np.float64], split_idxs: List[int], update_num: Optional[int]) -> List[List[float]]:
        """ Clamp non-negative, zero on warmup, then unflatten back into per-state Q-value lists. """
        assert q_vals_np.shape[0] == len(states_rep)
        q_vals_np = np.maximum(q_vals_np[:, 0], 0)
        if (update_num is not None) and (update_num == 0):
            q_vals_np = q_vals_np * 0

        q_vals_flat: List[float] = q_vals_np.astype(np.float64).tolist()
        q_vals_l: List[List[float]] = misc_utils.unflatten(q_vals_flat, split_idxs)
        return q_vals_l
```
