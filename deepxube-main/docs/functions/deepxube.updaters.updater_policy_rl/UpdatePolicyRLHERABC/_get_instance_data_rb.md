---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._get_instance_data_rb"
kind: "method"
name: "_get_instance_data_rb"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._get_instance_data_rb"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 167
line_end: 193
class: "UpdatePolicyRLHERABC"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instances"
    annotation: "List[Instance]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._get_her_goals"
    expr: "self._get_her_goals"
    call_sites: [170]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [173, 184]
  - target: null
    expr: "zip"
    call_sites: [177]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [178, 182]
  - target: null
    expr: "states_her.extend"
    call_sites: [180]
  - target: null
    expr: "goals_her.extend"
    call_sites: [181]
  - target: null
    expr: "len"
    call_sites: [181, 190]
  - target: null
    expr: "actions_her.extend"
    call_sites: [182]
  - target: null
    expr: "times.record_time"
    call_sites: [184]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._rb_add"
    expr: "self._rb_add"
    call_sites: [187]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._sample_rb"
    expr: "self._sample_rb"
    call_sites: [190]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [193]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._get_instance_data_rb`

**File:** [deepxube/updaters/updater_policy_rl.py:167](../../../../deepxube/updaters/updater_policy_rl.py#L167)
**Class:** `UpdatePolicyRLHERABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_rb(self, instances: List[Instance], times: Times) -> List[NDArray]
```

## Docstring

Relabel goals via HER, push the relabeled batch, then sample for training. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[Instance]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `self._get_her_goals` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._get_her_goals` (lines: 170)
- `time.time` → `func:time.time` (lines: 173, 184)
- `self._rb_add` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._rb_add` (lines: 187)
- `self._sample_rb` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._sample_rb` (lines: 190)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._inputs_ctgs_to_np` (lines: 193)

### Unresolved
- `zip` (lines: 177)
- `instance.get_edges_popped` (lines: 178, 182)
- `states_her.extend` (lines: 180)
- `goals_her.extend` (lines: 181)
- `len` (lines: 181, 190)
- `actions_her.extend` (lines: 182)
- `times.record_time` (lines: 184)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_rb(self, instances: List[Instance], times: Times) -> List[NDArray]:
        """ Relabel goals via HER, push the relabeled batch, then sample for training. """
        # get goals according to HER
        instances, goals_inst_her = self._get_her_goals(instances, times)

        # get states and goals
        start_time = time.time()
        states_her: List[State] = []
        goals_her: List[Goal] = []
        actions_her: List[Action] = []
        for instance, goal_her in zip(instances, goals_inst_her, strict=True):
            nodes: List[Node] = [edge.node for edge in instance.get_edges_popped()]
            states_inst: List[State] = [node.state for node in nodes]
            states_her.extend(states_inst)
            goals_her.extend([goal_her] * len(states_inst))
            actions_her.extend([edge.action for edge in instance.get_edges_popped()])

        times.record_time("data_her", time.time() - start_time)

        # add to replay buffer
        self._rb_add(states_her, goals_her, actions_her, times)

        # rb q-learning update
        states, goals, actions = self._sample_rb(len(states_her), times)

        # to_np
        return self._inputs_ctgs_to_np(states, goals, actions, times)
```
