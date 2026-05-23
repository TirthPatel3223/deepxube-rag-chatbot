---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._step_sync_main"
kind: "method"
name: "_step_sync_main"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._step_sync_main"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 132
line_end: 146
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
  - name: "pathfind"
    annotation: "PathFindSetHeurV"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.updater_v_rl._pathfind_v_step"
    expr: "_pathfind_v_step"
    call_sites: [135]
  - target: "func:deepxube.updaters.updater_v_rl._get_nodes_popped_data"
    expr: "_get_nodes_popped_data"
    call_sites: [138]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._rb_add"
    expr: "self._rb_add"
    call_sites: [141]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._sample_rb_vi_target"
    expr: "self._sample_rb_vi_target"
    call_sites: [144]
  - target: null
    expr: "len"
    call_sites: [144]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [146]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._step_sync_main`

**File:** [deepxube/updaters/updater_v_rl.py:132](../../../../deepxube/updaters/updater_v_rl.py#L132)
**Class:** `UpdateHeurVRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step_sync_main(self, pathfind: PathFindSetHeurV, times: Times) -> List[NDArray]
```

## Docstring

Take a step, push popped nodes to the buffer, and return a VI-targeted sample batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `PathFindSetHeurV` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `_pathfind_v_step` → `func:deepxube.updaters.updater_v_rl._pathfind_v_step` (lines: 135)
- `_get_nodes_popped_data` → `func:deepxube.updaters.updater_v_rl._get_nodes_popped_data` (lines: 138)
- `self._rb_add` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._rb_add` (lines: 141)
- `self._sample_rb_vi_target` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._sample_rb_vi_target` (lines: 144)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._inputs_ctgs_to_np` (lines: 146)

### Unresolved
- `len` (lines: 144)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _step_sync_main(self, pathfind: PathFindSetHeurV, times: Times) -> List[NDArray]:
        """ Take a step, push popped nodes to the buffer, and return a VI-targeted sample batch. """
        # take a step
        nodes_popped: List[Node] = _pathfind_v_step(pathfind)

        # get sync states/goals/is_solved
        states_sync, goals_sync, is_solved_l_sync = _get_nodes_popped_data(nodes_popped, times)

        # add to replay buffer
        self._rb_add(states_sync, goals_sync, is_solved_l_sync, times)

        # rb value iteration update
        states, goals, ctgs_backup = self._sample_rb_vi_target(len(nodes_popped), times)

        return self._inputs_ctgs_to_np(states, goals, ctgs_backup, times)
```
