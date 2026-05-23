---
id: "class:deepxube.updaters.updater_v_rl.UpdateHeurVRL"
kind: "class"
name: "UpdateHeurVRL"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRL"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 47
line_end: 121
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeurV[D, FNsHV, PathFindSetHeurV]"
    resolved_id: null
  - name: "UpdateRL[D, FNsHV, PathFindSetHeurV, InstanceNode]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL.pathfind_type"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL.__init__"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._step"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._value_iteration_target"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._inputs_ctgs_to_np"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._init_replay_buffer"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._rb_add"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._sample_rb_vi_target"
attributes:
  - name: "self.rb"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRL`

**File:** [deepxube/updaters/updater_v_rl.py:47](../../../deepxube/updaters/updater_v_rl.py#L47)
**Abstract:** yes

## Docstring

Abstract base for V-heuristic RL updaters: owns the replay buffer and
the value-iteration target computation. 

## Inheritance

**Direct bases:**
- `UpdateHeurV[D, FNsHV, PathFindSetHeurV]`
- `UpdateRL[D, FNsHV, PathFindSetHeurV, InstanceNode]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `pathfind_type` *(trivial, skipped)*
- `__init__`
- `_step`
- `_value_iteration_target`
- `_inputs_ctgs_to_np`
- `_init_replay_buffer`
- `_rb_add`
- `_sample_rb_vi_target`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.rb` | — | __init__ |

## Source

```python
class UpdateHeurVRL(UpdateHeurV[D, FNsHV, PathFindSetHeurV], UpdateRL[D, FNsHV, PathFindSetHeurV, InstanceNode], ABC):
    """ Abstract base for V-heuristic RL updaters: owns the replay buffer and
    the value-iteration target computation. """

    @staticmethod
    def pathfind_type() -> Type[PathFindSetHeurV]:
        """ :return: ``PathFindSetHeurV`` — V-heuristic batch pathfinder. """
        return PathFindSetHeurV

    def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs):
        """ Initialise the base updater and create an empty V replay buffer. """
        super().__init__(domain, pathfind_arg, up_args)
        self.rb: ReplayBufferV = ReplayBufferV(0)

    def _step(self, pathfind: PathFindSetHeurV, times: Times) -> None:
        """ Advance the pathfinder by one step (side effect only). """
        _pathfind_v_step(pathfind)

    def _value_iteration_target(self, goals: List[Goal], is_solved_l: List[bool], tcs_l: List[List[float]], states_exp: List[List[State]],
                                times: Times) -> List[float]:
        """ Compute one-step value-iteration targets: ``min_a (tc + V(s'))`` zeroed for solved states. """
        start_time = time.time()
        # get cost-to-go of expanded states
        states_exp_flat, split_idxs = misc_utils.flatten(states_exp)
        goals_flat: List[Goal] = []
        for goal, state_exp in zip(goals, states_exp, strict=True):
            goals_flat.extend([goal] * len(state_exp))
        ctg_next: List[float] = self._get_targ_heur_fn()(states_exp_flat, goals_flat)

        # backup cost-to-go
        ctg_next_p_tc = np.concatenate(tcs_l, axis=0) + np.array(ctg_next)
        ctg_next_p_tc_l = np.split(ctg_next_p_tc, split_idxs)

        ctgs_backup = np.array([np.min(x) for x in ctg_next_p_tc_l]) * np.logical_not(is_solved_l)
        ctgs_backup_l: List[float] = cast(List[float], ctgs_backup.tolist())

        times.record_time("vi_targ", time.time() - start_time)

        return ctgs_backup_l

    def _inputs_ctgs_to_np(self, states: List[State], goals: List[Goal], ctgs_backup: List[float], times: Times) -> List[NDArray]:
        """ Package state/goal into numpy inputs and append the ctg target array. """
        start_time = time.time()
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals)
        data_np: List[NDArray] = inputs_np + [np.array(ctgs_backup)]
        times.record_time("to_np", time.time() - start_time)

        return data_np

    def _init_replay_buffer(self, max_size: int) -> None:
        """ Replace the replay buffer with a fresh one of the given capacity. """
        self.rb = ReplayBufferV(max_size)

    def _rb_add(self, states: List[State], goals: List[Goal], is_solved_l: List[bool], times: Times) -> None:
        """ Push a batch of (state, goal, is_solved) triples to the buffer. """
        start_time = time.time()
        self.rb.add(list(zip(states, goals, is_solved_l, strict=True)))
        times.record_time("rb_add", time.time() - start_time)

    def _sample_rb_vi_target(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[float]]:
        """ Sample ``num`` items, expand their next states, and return VI-targeted ctgs. """
        # sample from replay buffer
        start_time = time.time()
        states, goals, is_solved_l = self.rb.sample(num)
        times.record_time("rb_samp", time.time() - start_time)

        # expand states
        start_time = time.time()
        states_exp, _, tcs_l = self.get_pathfind().expand_states(states, goals)
        times.record_time("vi_expand", time.time() - start_time)

        # value iteration update
        ctgs_backup: List[float] = self._value_iteration_target(goals, is_solved_l, tcs_l, states_exp, times)

        return states, goals, ctgs_backup
```
