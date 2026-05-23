---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_rb"
kind: "method"
name: "_get_instance_data_rb"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_rb"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 182
line_end: 196
class: "UpdateHeurVRLKeepGoalABC"
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
    annotation: "List[InstanceNode]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "nodes_popped.extend"
    call_sites: [187]
  - target: null
    expr: "instance.get_nodes_popped"
    call_sites: [187]
  - target: "func:deepxube.updaters.updater_v_rl._get_nodes_popped_data"
    expr: "_get_nodes_popped_data"
    call_sites: [188]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._rb_add"
    expr: "self._rb_add"
    call_sites: [191]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._sample_rb_vi_target"
    expr: "self._sample_rb_vi_target"
    call_sites: [194]
  - target: null
    expr: "len"
    call_sites: [194]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [196]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_rb`

**File:** [deepxube/updaters/updater_v_rl.py:182](../../../../deepxube/updaters/updater_v_rl.py#L182)
**Class:** `UpdateHeurVRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_rb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]
```

## Docstring

Replay-buffer path: push popped nodes, then sample and VI-target. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceNode]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `_get_nodes_popped_data` → `func:deepxube.updaters.updater_v_rl._get_nodes_popped_data` (lines: 188)
- `self._rb_add` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._rb_add` (lines: 191)
- `self._sample_rb_vi_target` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._sample_rb_vi_target` (lines: 194)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._inputs_ctgs_to_np` (lines: 196)

### Unresolved
- `nodes_popped.extend` (lines: 187)
- `instance.get_nodes_popped` (lines: 187)
- `len` (lines: 194)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_rb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]:
        """ Replay-buffer path: push popped nodes, then sample and VI-target. """
        # get popped node data
        nodes_popped: List[Node] = []
        for instance in instances:
            nodes_popped.extend(instance.get_nodes_popped())
        states_popped, goals_popped, is_solved_l = _get_nodes_popped_data(nodes_popped, times)

        # add to replay buffer
        self._rb_add(states_popped, goals_popped, is_solved_l, times)

        # rb value iteration update
        states, goals, ctgs_backup = self._sample_rb_vi_target(len(nodes_popped), times)

        return self._inputs_ctgs_to_np(states, goals, ctgs_backup, times)
```
