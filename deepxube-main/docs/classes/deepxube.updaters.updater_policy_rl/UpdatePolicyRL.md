---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRL"
kind: "class"
name: "UpdatePolicyRL"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRL"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 43
line_end: 97
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdatePolicy[D, FNsP, PathFindActsPolicy, Instance]"
    resolved_id: null
  - name: "UpdateRL[D, FNsP, PathFindActsPolicy, Instance]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL.pathfind_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL.__init__"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._step"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._inputs_ctgs_to_np"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._init_replay_buffer"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._rb_add"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._sample_rb"
attributes:
  - name: "self.rb"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRL`

**File:** [deepxube/updaters/updater_policy_rl.py:43](../../../deepxube/updaters/updater_policy_rl.py#L43)
**Abstract:** yes

## Docstring

Abstract base for policy RL updaters: owns the policy replay buffer
and the random-action mixin used for exploration. 

## Inheritance

**Direct bases:**
- `UpdatePolicy[D, FNsP, PathFindActsPolicy, Instance]`
- `UpdateRL[D, FNsP, PathFindActsPolicy, Instance]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `pathfind_type` *(trivial, skipped)*
- `__init__`
- `_step`
- `_inputs_ctgs_to_np`
- `_init_replay_buffer`
- `_rb_add`
- `_sample_rb`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.rb` | — | __init__ |

## Source

```python
class UpdatePolicyRL(UpdatePolicy[D, FNsP, PathFindActsPolicy, Instance], UpdateRL[D, FNsP, PathFindActsPolicy, Instance], ABC):
    """ Abstract base for policy RL updaters: owns the policy replay buffer
    and the random-action mixin used for exploration. """

    @staticmethod
    def pathfind_type() -> Type[PathFindActsPolicy]:
        """ :return: ``PathFindActsPolicy`` — policy-driven action pathfinder. """
        return PathFindActsPolicy

    def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs):
        """ Initialise the base updater and create an empty policy replay buffer. """
        super().__init__(domain, pathfind_arg, up_args)
        self.rb: ReplayBufferP = ReplayBufferP(0)

    def _step(self, pathfind: PathFindActsPolicy, times: Times) -> None:
        """ Advance the pathfinder by one step (side effect only). """
        _pathfind_step(pathfind)

    def _inputs_ctgs_to_np(self, states: List[State], goals: List[Goal], actions: List[Action], times: Times) -> List[NDArray]:
        """ Mix in random actions per ``policy_rand_prob``, then package inputs for policy training. """
        # sample random actions
        start_time = time.time()
        rand_idxs: List[int] = np.flatnonzero(np.random.random(len(states)) < self.up_args.policy_rand_prob).tolist()
        if len(rand_idxs) > 0:
            states_rand_acts: List[State] = [states[rand_idx] for rand_idx in rand_idxs]
            actions_rand: List[Action] = self.domain.sample_state_action(states_rand_acts)
            for rand_idx, action_rand in zip(rand_idxs, actions_rand):
                actions[rand_idx] = action_rand
        times.record_time("rand_acts", time.time() - start_time)

        # to_np
        start_time = time.time()
        inputs_np: List[NDArray] = self.get_policy_nnet_par().to_np_train(states, goals, actions)
        times.record_time("to_np", time.time() - start_time)

        return inputs_np

    def _init_replay_buffer(self, max_size: int) -> None:
        """ Replace the replay buffer with a fresh one of the given capacity. """
        self.rb = ReplayBufferP(max_size)

    def _rb_add(self, states: List[State], goals: List[Goal], actions: List[Action], times: Times) -> None:
        """ Push a batch of (state, goal, action) triples to the buffer. """
        start_time = time.time()
        self.rb.add(list(zip(states, goals, actions, strict=True)))
        times.record_time("rb_add", time.time() - start_time)

    def _sample_rb(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[Action]]:
        """ Uniformly sample ``num`` (state, goal, action) triples from the buffer. """
        # sample from replay buffer
        start_time = time.time()
        states, goals, actions = self.rb.sample(num)
        times.record_time("rb_samp", time.time() - start_time)

        return states, goals, actions
```
