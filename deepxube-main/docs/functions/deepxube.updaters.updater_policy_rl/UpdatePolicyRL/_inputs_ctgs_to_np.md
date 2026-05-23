---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._inputs_ctgs_to_np"
kind: "method"
name: "_inputs_ctgs_to_np"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRL._inputs_ctgs_to_np"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 61
line_end: 78
class: "UpdatePolicyRL"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "actions"
    annotation: "List[Action]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [64, 71, 74, 76]
  - target: null
    expr: "np.flatnonzero(np.random.random(len(states)) < self.up_args.policy_rand_prob).tolist"
    call_sites: [65]
  - target: "func:numpy.flatnonzero"
    expr: "np.flatnonzero"
    call_sites: [65]
  - target: null
    expr: "np.random.random"
    call_sites: [65]
  - target: null
    expr: "len"
    call_sites: [65, 66]
  - target: null
    expr: "self.domain.sample_state_action"
    call_sites: [68]
  - target: null
    expr: "zip"
    call_sites: [69]
  - target: null
    expr: "times.record_time"
    call_sites: [71, 76]
  - target: null
    expr: "self.get_policy_nnet_par().to_np_train"
    call_sites: [75]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL.get_policy_nnet_par"
    expr: "self.get_policy_nnet_par"
    call_sites: [75]
raises: []
reads_attrs:
  - "self.domain"
  - "self.up_args"
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRL._inputs_ctgs_to_np`

**File:** [deepxube/updaters/updater_policy_rl.py:61](../../../../deepxube/updaters/updater_policy_rl.py#L61)
**Class:** `UpdatePolicyRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _inputs_ctgs_to_np(self, states: List[State], goals: List[Goal], actions: List[Action], times: Times) -> List[NDArray]
```

## Docstring

Mix in random actions per ``policy_rand_prob``, then package inputs for policy training. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `time.time` → `func:time.time` (lines: 64, 71, 74, 76)
- `np.flatnonzero` → `func:numpy.flatnonzero` (lines: 65)
- `self.get_policy_nnet_par` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL.get_policy_nnet_par` (lines: 75)

### Unresolved
- `np.flatnonzero(np.random.random(len(states)) < self.up_args.policy_rand_prob).tolist` (lines: 65)
- `np.random.random` (lines: 65)
- `len` (lines: 65, 66)
- `self.domain.sample_state_action` (lines: 68)
- `zip` (lines: 69)
- `times.record_time` (lines: 71, 76)
- `self.get_policy_nnet_par().to_np_train` (lines: 75)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.up_args`

## Source

```python
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
```
