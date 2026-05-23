---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_rb"
kind: "method"
name: "_get_instance_data_rb"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_rb"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 182
line_end: 196
class: "UpdateHeurQRLKeepGoalABC"
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
    annotation: "List[InstanceEdge]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "edges_popped.extend"
    call_sites: [187]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [187]
  - target: "func:deepxube.updaters.updater_q_rl._get_edge_popped_data"
    expr: "_get_edge_popped_data"
    call_sites: [188]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._rb_add"
    expr: "self._rb_add"
    call_sites: [191]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._sample_rb_qlearn_target"
    expr: "self._sample_rb_qlearn_target"
    call_sites: [194]
  - target: null
    expr: "len"
    call_sites: [194]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [196]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_rb`

**File:** [deepxube/updaters/updater_q_rl.py:182](../../../../deepxube/updaters/updater_q_rl.py#L182)
**Class:** `UpdateHeurQRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_rb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]
```

## Docstring

Replay-buffer path: push popped edges, then sample and Q-target. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceEdge]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `_get_edge_popped_data` → `func:deepxube.updaters.updater_q_rl._get_edge_popped_data` (lines: 188)
- `self._rb_add` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._rb_add` (lines: 191)
- `self._sample_rb_qlearn_target` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._sample_rb_qlearn_target` (lines: 194)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._inputs_ctgs_to_np` (lines: 196)

### Unresolved
- `edges_popped.extend` (lines: 187)
- `instance.get_edges_popped` (lines: 187)
- `len` (lines: 194)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_rb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Replay-buffer path: push popped edges, then sample and Q-target. """
        # get popped edge data
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())
        states_p, goals_p, is_solved_l_p, actions_p, tcs_p, states_next_p = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_p, goals_p, is_solved_l_p, actions_p, tcs_p, states_next_p, times)

        # rb q-learning update
        states, goals, actions, ctgs_backup = self._sample_rb_qlearn_target(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, ctgs_backup, times)
```
