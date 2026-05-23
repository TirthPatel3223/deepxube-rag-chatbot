---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_rb"
kind: "method"
name: "_get_instance_data_rb"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_rb"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 142
line_end: 156
class: "UpdatePolicyRLKeepGoalABC"
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
  - target: null
    expr: "edges_popped.extend"
    call_sites: [147]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [147]
  - target: "func:deepxube.updaters.updater_policy_rl._get_edge_popped_data"
    expr: "_get_edge_popped_data"
    call_sites: [148]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._rb_add"
    expr: "self._rb_add"
    call_sites: [151]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._sample_rb"
    expr: "self._sample_rb"
    call_sites: [154]
  - target: null
    expr: "len"
    call_sites: [154]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [156]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_rb`

**File:** [deepxube/updaters/updater_policy_rl.py:142](../../../../deepxube/updaters/updater_policy_rl.py#L142)
**Class:** `UpdatePolicyRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_rb(self, instances: List[Instance], times: Times) -> List[NDArray]
```

## Docstring

Replay-buffer path: push popped edges, then sample a training batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[Instance]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `_get_edge_popped_data` → `func:deepxube.updaters.updater_policy_rl._get_edge_popped_data` (lines: 148)
- `self._rb_add` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._rb_add` (lines: 151)
- `self._sample_rb` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._sample_rb` (lines: 154)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._inputs_ctgs_to_np` (lines: 156)

### Unresolved
- `edges_popped.extend` (lines: 147)
- `instance.get_edges_popped` (lines: 147)
- `len` (lines: 154)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_rb(self, instances: List[Instance], times: Times) -> List[NDArray]:
        """ Replay-buffer path: push popped edges, then sample a training batch. """
        # get popped edge data
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())
        states_p, goals_p, actions_p = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_p, goals_p, actions_p, times)

        # rb q-learning update
        states, goals, actions = self._sample_rb(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, times)
```
