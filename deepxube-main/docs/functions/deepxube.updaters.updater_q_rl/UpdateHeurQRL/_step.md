---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._step"
kind: "method"
name: "_step"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRL._step"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 67
line_end: 69
class: "UpdateHeurQRL"
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
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.updater_q_rl._pathfind_q_step"
    expr: "_pathfind_q_step"
    call_sites: [69]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRL._step`

**File:** [deepxube/updaters/updater_q_rl.py:67](../../../../deepxube/updaters/updater_q_rl.py#L67)
**Class:** `UpdateHeurQRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step(self, pathfind: PathFindSetHeurQ, times: Times) -> None
```

## Docstring

Advance the pathfinder by one step (side effect only). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `PathFindSetHeurQ` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `_pathfind_q_step` → `func:deepxube.updaters.updater_q_rl._pathfind_q_step` (lines: 69)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _step(self, pathfind: PathFindSetHeurQ, times: Times) -> None:
        """ Advance the pathfinder by one step (side effect only). """
        _pathfind_q_step(pathfind)
```
