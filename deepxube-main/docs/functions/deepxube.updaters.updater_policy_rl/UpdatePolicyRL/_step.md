---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._step"
kind: "method"
name: "_step"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRL._step"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 57
line_end: 59
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
  - name: "pathfind"
    annotation: "PathFindActsPolicy"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.updater_policy_rl._pathfind_step"
    expr: "_pathfind_step"
    call_sites: [59]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRL._step`

**File:** [deepxube/updaters/updater_policy_rl.py:57](../../../../deepxube/updaters/updater_policy_rl.py#L57)
**Class:** `UpdatePolicyRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step(self, pathfind: PathFindActsPolicy, times: Times) -> None
```

## Docstring

Advance the pathfinder by one step (side effect only). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `PathFindActsPolicy` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `_pathfind_step` → `func:deepxube.updaters.updater_policy_rl._pathfind_step` (lines: 59)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _step(self, pathfind: PathFindActsPolicy, times: Times) -> None:
        """ Advance the pathfinder by one step (side effect only). """
        _pathfind_step(pathfind)
```
