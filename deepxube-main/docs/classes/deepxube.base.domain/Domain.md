---
id: "class:deepxube.base.domain.Domain"
kind: "class"
name: "Domain"
qualified_name: "deepxube.base.domain.Domain"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 81
line_end: 175
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "S"
  - "A"
  - "G"
bases:
  - name: "ABC"
    resolved_id: null
  - name: "Generic[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.Domain.__init__"
  - "func:deepxube.base.domain.Domain.sample_problem_instances"
  - "func:deepxube.base.domain.Domain.sample_state_action"
  - "func:deepxube.base.domain.Domain.next_state"
  - "func:deepxube.base.domain.Domain.is_solved"
  - "func:deepxube.base.domain.Domain.sample_next_state"
  - "func:deepxube.base.domain.Domain.random_walk"
  - "func:deepxube.base.domain.Domain.get_nnet_pars"
  - "func:deepxube.base.domain.Domain.set_nnet_fns"
attributes:
  - name: "self.nnet_pars"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.Domain`

**File:** [deepxube/base/domain.py:81](../../../deepxube/base/domain.py#L81)
**Abstract:** yes
**Generic parameters:** `S, A, G`

## Docstring

Abstract base for all domains. Holds the registered NNet parameter
objects; concrete subclasses add transition / action / goal logic via
the mixins defined below. 

## Inheritance

**Direct bases:**
- `ABC`
- `Generic[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `sample_problem_instances` *(trivial, skipped)*
- `sample_state_action` *(trivial, skipped)*
- `next_state` *(trivial, skipped)*
- `is_solved` *(trivial, skipped)*
- `sample_next_state`
- `random_walk`
- `get_nnet_pars` *(trivial, skipped)*
- `set_nnet_fns` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.nnet_pars` | — | __init__ |

## Source

```python
class Domain(ABC, Generic[S, A, G]):
    """ Abstract base for all domains. Holds the registered NNet parameter
    objects; concrete subclasses add transition / action / goal logic via
    the mixins defined below. """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """ Initialise an empty list of registered NNet parameter objects. """
        self.nnet_pars: List[Tuple[str, str, NNetPar]] = []

    @abstractmethod
    def sample_problem_instances(self, num_steps_l: List[int], times: Optional[Times] = None) -> Tuple[List[S], List[G]]:
        """ Return start goal pairs with num_steps_l between start and goal

        :param num_steps_l: Number of steps to take between start and goal. Does not have to directly correspond to number of steps and can also be ignored.
        :param times: Times that can be used to profile code
        :return: List of start states and list of goals
        """
        pass

    @abstractmethod
    def sample_state_action(self, states: List[S]) -> List[A]:
        """ Get a random action that is applicable to the current state

        :param states: List of states
        :return: List of random actions applicable to given states
        """
        pass

    @abstractmethod
    def next_state(self, states: List[S], actions: List[A]) -> Tuple[List[S], List[float]]:
        """ Get the next state and transition cost given the current state and action

        :param states: List of states
        :param actions: List of actions to take
        :return: Next states, transition costs
        """
        pass

    @abstractmethod
    def is_solved(self, states: List[S], goals: List[G]) -> List[bool]:
        """ Returns true if the state is a member of the set of goal states represented by the goal

        :param states: List of states
        :param goals: List of goals
        :return: List of booleans where the element at index i corresponds to whether or not the state at index i is a member of the set of goal states
        represented by the goal at index i
        """
        pass

    def sample_next_state(self, states: List[S]) -> Tuple[List[S], List[float]]:
        """ Get random next state and transition cost given the current state

        :param states: List of states
        :return: Next states, transition costs
        """
        actions_rand: List[A] = self.sample_state_action(states)
        return self.next_state(states, actions_rand)

    def random_walk(self, states: List[S], num_steps_l: List[int]) -> Tuple[List[S], List[float]]:
        """ Perform a random walk on the given states for the given number of steps

        :param states: List of states
        :param num_steps_l: number of steps to take for each state
        :return: The resulting state and the path cost for each random walk
        """
        states_walk: List[S] = [state for state in states]
        path_costs: List[float] = [0.0 for _ in states]

        num_steps: NDArray[np.int_] = np.array(num_steps_l)
        num_steps_curr: NDArray[np.int_] = np.zeros(len(states), dtype=int)
        steps_lt: NDArray[np.bool_] = num_steps_curr < num_steps
        while np.any(steps_lt):
            idxs: NDArray[np.int_] = np.where(steps_lt)[0]
            states_to_move = [states_walk[idx] for idx in idxs]

            states_moved, tcs = self.sample_next_state(states_to_move)

            idx: int
            for move_idx, idx in enumerate(idxs):
                states_walk[idx] = states_moved[move_idx]
                path_costs[idx] += tcs[move_idx]

            num_steps_curr[idxs] = num_steps_curr[idxs] + 1

            steps_lt[idxs] = num_steps_curr[idxs] < num_steps[idxs]

        return states_walk, path_costs

    def get_nnet_pars(self) -> List[Tuple[str, str, NNetPar]]:
        """ :return: List of ``(name, file, NNetPar)`` registered with this domain. """
        return self.nnet_pars

    def set_nnet_fns(self, nnet_fn_dict: Dict[str, NNetCallable]) -> None:
        """ Hook for domains that want to receive freshly-built NNet callables (default no-op). """
        pass
```
