---
id: "class:deepxube.base.domain.NextStateNPActsEnum"
kind: "class"
name: "NextStateNPActsEnum"
qualified_name: "deepxube.base.domain.NextStateNPActsEnum"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 550
line_end: 586
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "NextStateNP[S, A, G]"
    resolved_id: null
  - name: "ActsEnum[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.NextStateNPActsEnum.expand"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.NextStateNPActsEnum`

**File:** [deepxube/base/domain.py:550](../../../deepxube/base/domain.py#L550)
**Abstract:** yes

## Docstring

Combines ``NextStateNP`` with ``ActsEnum`` so ``expand`` runs vectorised in numpy space. 

## Inheritance

**Direct bases:**
- `NextStateNP[S, A, G]`
- `ActsEnum[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `expand`

## Source

```python
class NextStateNPActsEnum(NextStateNP[S, A, G], ActsEnum[S, A, G], ABC):
    """ Combines ``NextStateNP`` with ``ActsEnum`` so ``expand`` runs vectorised in numpy space. """

    def expand(self, states: List[S]) -> Tuple[List[List[S]], List[List[A]], List[List[float]]]:
        """ Vectorised version of ``ActsEnum.expand`` working in numpy space. """
        # initialize
        states_np: List[NDArray] = self._states_to_np(states)
        states_exp_l: List[List[S]] = [[] for _ in range(len(states))]
        actions_exp_l: List[List[A]] = [[] for _ in range(len(states))]
        tcs_l: List[List[float]] = [[] for _ in range(len(states))]
        state_actions: List[List[A]] = self.get_state_actions(states)

        num_actions_tot: NDArray[np.int_] = np.array([len(x) for x in state_actions])
        num_actions_taken: NDArray[np.int_] = np.zeros(len(states), dtype=int)
        actions_lt: NDArray[np.bool_] = num_actions_taken < num_actions_tot

        # for each move, get next states, transition costs, and if solved
        while np.any(actions_lt):
            idxs: NDArray[np.int_] = np.where(actions_lt)[0]
            states_np_idxs: List[NDArray] = [states_np_i[idxs] for states_np_i in states_np]
            actions_idxs: List[A] = [state_actions[idx].pop(0) for idx in idxs]

            # next state
            states_next_np, tcs_move = self._next_state_np(states_np_idxs, actions_idxs)
            states_next: List[S] = self._np_to_states(states_next_np)

            # append
            idx: int
            for exp_idx, idx in enumerate(idxs):
                states_exp_l[idx].append(states_next[exp_idx])
                actions_exp_l[idx].append(actions_idxs[exp_idx])
                tcs_l[idx].append(tcs_move[exp_idx])

            num_actions_taken[idxs] = num_actions_taken[idxs] + 1
            actions_lt[idxs] = num_actions_taken[idxs] < num_actions_tot[idxs]

        return states_exp_l, actions_exp_l, tcs_l
```
