---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._step_sync_main"
kind: "method"
name: "_step_sync_main"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._step_sync_main"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 127
line_end: 141
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
  - name: "pathfind"
    annotation: "PathFindSetHeurQ"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.updater_q_rl._pathfind_q_step"
    expr: "_pathfind_q_step"
    call_sites: [130]
  - target: "func:deepxube.updaters.updater_q_rl._get_edge_popped_data"
    expr: "_get_edge_popped_data"
    call_sites: [133]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._rb_add"
    expr: "self._rb_add"
    call_sites: [136]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._sample_rb_qlearn_target"
    expr: "self._sample_rb_qlearn_target"
    call_sites: [139]
  - target: null
    expr: "len"
    call_sites: [139]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [141]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._step_sync_main`

**File:** [deepxube/updaters/updater_q_rl.py:127](../../../../deepxube/updaters/updater_q_rl.py#L127)
**Class:** `UpdateHeurQRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step_sync_main(self, pathfind: PathFindSetHeurQ, times: Times) -> List[NDArray]
```

## Docstring

Take a step, push popped edges, and return a Q-targeted sample batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `PathFindSetHeurQ` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `_pathfind_q_step` → `func:deepxube.updaters.updater_q_rl._pathfind_q_step` (lines: 130)
- `_get_edge_popped_data` → `func:deepxube.updaters.updater_q_rl._get_edge_popped_data` (lines: 133)
- `self._rb_add` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._rb_add` (lines: 136)
- `self._sample_rb_qlearn_target` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._sample_rb_qlearn_target` (lines: 139)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._inputs_ctgs_to_np` (lines: 141)

### Unresolved
- `len` (lines: 139)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _step_sync_main(self, pathfind: PathFindSetHeurQ, times: Times) -> List[NDArray]:
        """ Take a step, push popped edges, and return a Q-targeted sample batch. """
        # take a step
        edges_popped: List[EdgeQ] = _pathfind_q_step(pathfind)

        # get sync states/goals/is_solved
        states_sync, goals_sync, is_solved_l_sync, actions_sync, tcs_sync, states_next_sync = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_sync, goals_sync, is_solved_l_sync, actions_sync, tcs_sync, states_next_sync, times)

        # rb q-learning update
        states, goals, actions, ctgs_backup = self._sample_rb_qlearn_target(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, ctgs_backup, times)
```
