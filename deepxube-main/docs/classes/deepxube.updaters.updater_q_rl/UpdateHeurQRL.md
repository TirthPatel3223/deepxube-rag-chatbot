---
id: "class:deepxube.updaters.updater_q_rl.UpdateHeurQRL"
kind: "class"
name: "UpdateHeurQRL"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRL"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 53
line_end: 116
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeurQ[D, FNsHQ, PathFindSetHeurQ]"
    resolved_id: null
  - name: "UpdateRL[D, FNsHQ, PathFindSetHeurQ, InstanceEdge]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL.pathfind_type"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL.__init__"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._step"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._q_learning_target"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._inputs_ctgs_to_np"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._init_replay_buffer"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._rb_add"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._sample_rb_qlearn_target"
attributes:
  - name: "self.rb"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRL`

**File:** [deepxube/updaters/updater_q_rl.py:53](../../../deepxube/updaters/updater_q_rl.py#L53)
**Abstract:** yes

## Docstring

Abstract base for Q-heuristic RL updaters: owns the Q replay buffer and
the Q-learning target computation. 

## Inheritance

**Direct bases:**
- `UpdateHeurQ[D, FNsHQ, PathFindSetHeurQ]`
- `UpdateRL[D, FNsHQ, PathFindSetHeurQ, InstanceEdge]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `pathfind_type` *(trivial, skipped)*
- `__init__`
- `_step`
- `_q_learning_target`
- `_inputs_ctgs_to_np`
- `_init_replay_buffer`
- `_rb_add`
- `_sample_rb_qlearn_target`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.rb` | — | __init__ |

## Source

```python
class UpdateHeurQRL(UpdateHeurQ[D, FNsHQ, PathFindSetHeurQ], UpdateRL[D, FNsHQ, PathFindSetHeurQ, InstanceEdge], ABC):
    """ Abstract base for Q-heuristic RL updaters: owns the Q replay buffer and
    the Q-learning target computation. """

    @staticmethod
    def pathfind_type() -> Type[PathFindSetHeurQ]:
        """ :return: ``PathFindSetHeurQ`` — Q-heuristic batch pathfinder. """
        return PathFindSetHeurQ

    def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs):
        """ Initialise the base updater and create an empty Q replay buffer. """
        super().__init__(domain, pathfind_arg, up_args)
        self.rb: ReplayBufferQ = ReplayBufferQ(0)

    def _step(self, pathfind: PathFindSetHeurQ, times: Times) -> None:
        """ Advance the pathfinder by one step (side effect only). """
        _pathfind_q_step(pathfind)

    def _q_learning_target(self, goals: List[Goal], is_solved_l: List[bool], tcs: List[float], states_next: List[State], times: Times) -> List[float]:
        """ Compute Q-learning targets: ``tc + min_a' Q(s', a')`` zeroed for solved states. """
        start_time = time.time()
        # min cost-to-go for next state
        actions_next: List[List[Action]] = self.get_pathfind().get_state_actions(states_next, goals)
        qvals_next_l: List[List[float]] = self._get_targ_heur_fn()(states_next, goals, actions_next)
        qvals_next_min: List[float] = [min(qvals_next) for qvals_next in qvals_next_l]

        # backup cost-to-go
        ctg_backups: NDArray = np.array(tcs) + np.array(qvals_next_min)
        ctg_backups = ctg_backups * np.logical_not(np.array(is_solved_l))

        times.record_time("qlearn_targ", time.time() - start_time)

        return cast(List[float], ctg_backups.tolist())

    def _inputs_ctgs_to_np(self, states: List[State], goals: List[Goal], actions: List[Action], ctgs_backup: List[float], times: Times) -> List[NDArray]:
        """ Package state/goal/action into numpy inputs and append the ctg target array. """
        start_time = time.time()
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])
        times.record_time("to_np", time.time() - start_time)

        return inputs_np + [np.array(ctgs_backup)]

    def _init_replay_buffer(self, max_size: int) -> None:
        """ Replace the replay buffer with a fresh one of the given capacity. """
        self.rb = ReplayBufferQ(max_size)

    def _rb_add(self, states: List[State], goals: List[Goal], is_solved_l: List[bool], actions: List[Action], tcs: List[float], states_next: List[State],
                times: Times) -> None:
        """ Push a batch of six-tuples (state, goal, is_solved, action, tc, next) to the buffer. """
        start_time = time.time()
        self.rb.add(list(zip(states, goals, is_solved_l, actions, tcs, states_next, strict=True)))
        times.record_time("rb_add", time.time() - start_time)

    def _sample_rb_qlearn_target(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[Action], List[float]]:
        """ Sample ``num`` items from the buffer and compute Q-learning targets for them. """
        # sample from replay buffer
        start_time = time.time()
        states, goals, is_solved_l, actions, tcs, states_next = self.rb.sample(num)
        times.record_time("rb_samp", time.time() - start_time)

        # value iteration update
        ctgs_backup: List[float] = self._q_learning_target(goals, is_solved_l, tcs, states_next, times)

        return states, goals, actions, ctgs_backup
```
