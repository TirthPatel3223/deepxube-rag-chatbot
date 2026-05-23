---
id: "class:deepxube.base.domain.NextStateNP"
kind: "class"
name: "NextStateNP"
qualified_name: "deepxube.base.domain.NextStateNP"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 481
line_end: 547
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.NextStateNP.next_state"
  - "func:deepxube.base.domain.NextStateNP.random_walk"
  - "func:deepxube.base.domain.NextStateNP._states_to_np"
  - "func:deepxube.base.domain.NextStateNP._np_to_states"
  - "func:deepxube.base.domain.NextStateNP._sample_state_np_action"
  - "func:deepxube.base.domain.NextStateNP._next_state_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.NextStateNP`

**File:** [deepxube/base/domain.py:481](../../../deepxube/base/domain.py#L481)
**Abstract:** yes

## Docstring

Convenience mixin for domains whose state has an obvious numpy
representation. ``next_state`` and ``random_walk`` route through ``_next_state_np``
so the heavy lifting stays vectorised. 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `next_state`
- `random_walk`
- `_states_to_np` *(trivial, skipped)*
- `_np_to_states` *(trivial, skipped)*
- `_sample_state_np_action` *(trivial, skipped)*
- `_next_state_np` *(trivial, skipped)*

## Source

```python
class NextStateNP(Domain[S, A, G]):
    """ Convenience mixin for domains whose state has an obvious numpy
    representation. ``next_state`` and ``random_walk`` route through ``_next_state_np``
    so the heavy lifting stays vectorised. """

    def next_state(self, states: List[S], actions: List[A]) -> Tuple[List[S], List[float]]:
        """ ``next_state`` via numpy: convert states, run ``_next_state_np``, convert back. """
        states_np: List[NDArray] = self._states_to_np(states)
        states_next_np, tcs = self._next_state_np(states_np, actions)
        states_next: List[S] = self._np_to_states(states_next_np)

        return states_next, tcs

    def random_walk(self, states: List[S], num_steps_l: List[int]) -> Tuple[List[S], List[float]]:
        """ Vectorised numpy random walk; semantics match ``Domain.random_walk``. """
        states_np = self._states_to_np(states)
        path_costs: List[float] = [0.0 for _ in states]

        num_steps: NDArray[np.int_] = np.array(num_steps_l)
        num_steps_curr: NDArray[np.int_] = np.zeros(len(states), dtype=int)
        steps_lt: NDArray[np.bool_] = num_steps_curr < num_steps
        while np.any(steps_lt):
            idxs: NDArray[np.int_] = np.where(steps_lt)[0]
            states_np_tomove: List[NDArray] = [states_np_i[idxs] for states_np_i in states_np]
            actions_rand: List[A] = self._sample_state_np_action(states_np_tomove)

            states_moved, tcs = self._next_state_np(states_np_tomove, actions_rand)

            for l_idx in range(len(states_np)):
                states_np[l_idx][idxs] = states_moved[l_idx]
            idx: int
            for act_idx, idx in enumerate(idxs):
                path_costs[idx] += tcs[act_idx]

            num_steps_curr[idxs] = num_steps_curr[idxs] + 1

            steps_lt[idxs] = num_steps_curr[idxs] < num_steps[idxs]

        return self._np_to_states(states_np), path_costs

    @abstractmethod
    def _states_to_np(self, states: List[S]) -> List[NDArray]:
        """ Convert states to a list of numpy arrays (one element per tensor slot). """
        pass

    @abstractmethod
    def _np_to_states(self, states_np_l: List[NDArray]) -> List[S]:
        """ Inverse of ``_states_to_np``: rebuild ``S`` objects from numpy slots. """
        pass

    @abstractmethod
    def _sample_state_np_action(self, states_np: List[NDArray]) -> List[A]:
        """ Sample a random applicable action per state given the numpy representation. """
        pass

    @abstractmethod
    def _next_state_np(self, states_np: List[NDArray], actions: List[A]) -> Tuple[List[NDArray], List[float]]:
        """ Get the next state and transition cost given the current numpy representations of the state and action


        @param states_np: numpy representation of states. Each row in each element of states_np list represents
        information for a different state. There can be one or more multiple elements in the list for each state.
        This object should not be mutated.
        @param actions: actions
        @return: Numpy representation of next states, transition costs
        """
        pass
```
