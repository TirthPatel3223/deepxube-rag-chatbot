---
id: "class:deepxube.base.domain.ActsEnum"
kind: "class"
name: "ActsEnum"
qualified_name: "deepxube.base.domain.ActsEnum"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 238
line_end: 290
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.ActsEnum.get_state_actions"
  - "func:deepxube.base.domain.ActsEnum.sample_state_action"
  - "func:deepxube.base.domain.ActsEnum.expand"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.ActsEnum`

**File:** [deepxube/base/domain.py:238](../../../deepxube/base/domain.py#L238)
**Abstract:** yes

## Docstring

Action mixin: applicable actions can be enumerated for any state. 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_state_actions` *(trivial, skipped)*
- `sample_state_action`
- `expand`

## Source

```python
class ActsEnum(Domain[S, A, G]):
    """ Action mixin: applicable actions can be enumerated for any state. """

    @abstractmethod
    def get_state_actions(self, states: List[S]) -> List[List[A]]:
        """ Get actions applicable to each states

        :param states: List of states
        :return: Applicable actions
        """
        pass

    def sample_state_action(self, states: List[S]) -> List[A]:
        """ Sample one applicable action per state uniformly from ``get_state_actions``. """
        state_actions_l: List[List[A]] = self.get_state_actions(states)
        return [random.choice(state_actions) for state_actions in state_actions_l]

    def expand(self, states: List[S]) -> Tuple[List[List[S]], List[List[A]], List[List[float]]]:
        """ Generate all children for the state, assumes there is at least one child state
        :param states: List of states
        :return: Children of each state, actions, transition costs for each state
        """
        # TODO further validate
        # initialize
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
            states_idxs: List[S] = [states[idx] for idx in idxs]
            actions_idxs: List[A] = [state_actions[idx].pop(0) for idx in idxs]

            # next state
            states_next, tcs_move = self.next_state(states_idxs, actions_idxs)

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
