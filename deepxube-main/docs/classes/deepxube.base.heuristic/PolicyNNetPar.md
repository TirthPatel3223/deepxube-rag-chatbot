---
id: "class:deepxube.base.heuristic.PolicyNNetPar"
kind: "class"
name: "PolicyNNetPar"
qualified_name: "deepxube.base.heuristic.PolicyNNetPar"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 472
line_end: 566
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "NNetPar[PolicyFn]"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.PolicyNNetPar.__init__"
  - "func:deepxube.base.heuristic.PolicyNNetPar.get_nnet_fn"
  - "func:deepxube.base.heuristic.PolicyNNetPar.get_nnet_par_fn"
  - "func:deepxube.base.heuristic.PolicyNNetPar.get_nnet"
  - "func:deepxube.base.heuristic.PolicyNNetPar.to_np_fn"
  - "func:deepxube.base.heuristic.PolicyNNetPar.to_np_train"
  - "func:deepxube.base.heuristic.PolicyNNetPar._nnet_out_to_actions"
  - "func:deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep"
  - "func:deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs"
  - "func:deepxube.base.heuristic.PolicyNNetPar.__repr__"
attributes:
  - name: "self.num_rand"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_samp"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.PolicyNNetPar`

**File:** [deepxube/base/heuristic.py:472](../../../deepxube/base/heuristic.py#L472)
**Abstract:** yes

## Docstring

Parallelisable wrapper for a policy network: builds a callable that samples
``num_samp`` actions from the network plus ``num_rand`` random actions per state. 

## Inheritance

**Direct bases:**
- `NNetPar[PolicyFn]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `get_nnet_fn`
- `get_nnet_par_fn`
- `get_nnet` *(trivial, skipped)*
- `to_np_fn` *(trivial, skipped)*
- `to_np_train` *(trivial, skipped)*
- `_nnet_out_to_actions` *(trivial, skipped)*
- `_get_nnet_inputs_rep`
- `_np_to_acts_and_pdfs`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.num_rand` | — | __init__ |
| `self.num_samp` | — | __init__ |

## Source

```python
class PolicyNNetPar(NNetPar[PolicyFn]):
    """ Parallelisable wrapper for a policy network: builds a callable that samples
    ``num_samp`` actions from the network plus ``num_rand`` random actions per state. """

    def __init__(self, num_samp: int, num_rand: int):
        """ Store the sample counts.

        :param num_samp: Number of network-sampled actions per state.
        :param num_rand: Number of random (mode-collapse guard) actions per state.
        """
        self.num_samp: int = num_samp
        self.num_rand: int = num_rand

    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> PolicyFn:
        """ Build an in-process policy callable. On warmup (``update_num == 0``) returns purely random actions. """
        nnet.eval()
        if (update_num is not None) and (update_num == 0):
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                assert len(states) == len(goals)  # to stop PyCharm from complaining
                return policy_fn_rand(domain, states, self.num_samp + self.num_rand)
        else:
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                inputs_nnet_rep: List[NDArray] = self._get_nnet_inputs_rep(states, goals, self.num_samp)
                nnet_out_np: List[NDArray[np.float64]] = nnet_batched(nnet, inputs_nnet_rep, batch_size, device)

                actions_l, pdfs_l = self._np_to_acts_and_pdfs(nnet_out_np[0:-1], nnet_out_np[-1], len(states), self.num_samp)
                return _combine_nnet_with_rand(domain, actions_l, pdfs_l, states, self.num_rand)

        return policy_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> PolicyFn:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        if (update_num is not None) and (update_num == 0):
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                assert len(states) == len(goals)  # to stop PyCharm from complaining
                return policy_fn_rand(domain, states, self.num_samp + self.num_rand)
        else:
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                inputs_nnet_rep: List[NDArray] = self._get_nnet_inputs_rep(states, goals, self.num_samp)
                nnet_out_np: List[NDArray[np.float64]] = get_nnet_par_out(inputs_nnet_rep, nnet_par_info)

                actions_l, pdfs_l = self._np_to_acts_and_pdfs(nnet_out_np[0:-1], nnet_out_np[-1], len(states), self.num_samp)
                return _combine_nnet_with_rand(domain, actions_l, pdfs_l, states, self.num_rand)

        return policy_fn

    @abstractmethod
    def get_nnet(self) -> PolicyNNet:
        """ :return: A freshly-constructed policy network. """
        pass

    @abstractmethod
    def to_np_fn(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]:
        """ Inference-side numpy conversion (no actions). """
        pass

    @abstractmethod
    def to_np_train(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]:
        """ Training-side numpy conversion (target actions included). """
        pass

    @abstractmethod
    def _nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[Action]:
        """ Decode raw network outputs into ``Action`` objects. """
        pass

    def _get_nnet_inputs_rep(self, states: List[State], goals: List[Goal], num_samp: int) -> List[NDArray]:
        """ Repeat each (state, goal) input row ``num_samp`` times so the network samples multiple actions per state in one batch. """
        inputs_nnet: List[NDArray] = self.to_np_fn(states, goals)
        inputs_nnet_rep_interleave: List[NDArray] = []
        for inputs_nnet_i in inputs_nnet:
            inputs_nnet_rep_interleave.append(np.repeat(inputs_nnet_i, num_samp, axis=0))
        return inputs_nnet_rep_interleave

    def _np_to_acts_and_pdfs(self, actions_np: List[NDArray[np.float64]], pdfs_np: NDArray[np.float64], num_states: int,
                             num_samp: int) -> Tuple[List[List[Action]], List[List[float]]]:
        """ Slice the interleaved (state, sample) outputs back into per-state lists of actions and pdfs. """
        assert len(pdfs_np.shape) == 2
        assert pdfs_np.shape[1] == 1

        actions_l: List[List[Action]] = []
        pdfs_l: List[List[float]] = []
        for state_idx in range(num_states):
            start_idx: int = state_idx * num_samp
            end_idx: int = start_idx + num_samp
            actions_np_state: List[NDArray[np.float64]] = [actions_np_i[start_idx:end_idx] for actions_np_i in actions_np]
            pdfs_state: List[float] = pdfs_np[start_idx:end_idx, 0].tolist()

            actions_l.append(self._nnet_out_to_actions(actions_np_state))
            pdfs_l.append(pdfs_state)

        return actions_l, pdfs_l

    def __repr__(self) -> str:
        return f"{self.get_nnet()}\n#Samp: {self.num_samp}, #Rand Samp: {self.num_rand}"
```
