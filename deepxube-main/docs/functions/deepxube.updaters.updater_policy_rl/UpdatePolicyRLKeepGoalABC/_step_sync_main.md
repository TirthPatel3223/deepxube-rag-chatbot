---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._step_sync_main"
kind: "method"
name: "_step_sync_main"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._step_sync_main"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 108
line_end: 122
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
  - name: "pathfind"
    annotation: "PathFindActsPolicy"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.updater_policy_rl._pathfind_step"
    expr: "_pathfind_step"
    call_sites: [111]
  - target: "func:deepxube.updaters.updater_policy_rl._get_edge_popped_data"
    expr: "_get_edge_popped_data"
    call_sites: [114]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._rb_add"
    expr: "self._rb_add"
    call_sites: [117]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._sample_rb"
    expr: "self._sample_rb"
    call_sites: [120]
  - target: null
    expr: "len"
    call_sites: [120]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [122]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._step_sync_main`

**File:** [deepxube/updaters/updater_policy_rl.py:108](../../../../deepxube/updaters/updater_policy_rl.py#L108)
**Class:** `UpdatePolicyRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step_sync_main(self, pathfind: PathFindActsPolicy, times: Times) -> List[NDArray]
```

## Docstring

Take a step, push popped edges, and return a sampled training batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `PathFindActsPolicy` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `_pathfind_step` → `func:deepxube.updaters.updater_policy_rl._pathfind_step` (lines: 111)
- `_get_edge_popped_data` → `func:deepxube.updaters.updater_policy_rl._get_edge_popped_data` (lines: 114)
- `self._rb_add` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._rb_add` (lines: 117)
- `self._sample_rb` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._sample_rb` (lines: 120)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._inputs_ctgs_to_np` (lines: 122)

### Unresolved
- `len` (lines: 120)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _step_sync_main(self, pathfind: PathFindActsPolicy, times: Times) -> List[NDArray]:
        """ Take a step, push popped edges, and return a sampled training batch. """
        # take a step
        edges_popped: List[EdgeQ] = _pathfind_step(pathfind)

        # get sync states/goals/is_solved
        states_sync, goals_sync, actions_sync = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_sync, goals_sync, actions_sync, times)

        # rb q-learning update
        states, goals, actions = self._sample_rb(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, times)
```
