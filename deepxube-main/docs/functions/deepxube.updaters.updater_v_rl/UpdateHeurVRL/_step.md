---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._step"
kind: "method"
name: "_step"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRL._step"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 61
line_end: 63
class: "UpdateHeurVRL"
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
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.updater_v_rl._pathfind_v_step"
    expr: "_pathfind_v_step"
    call_sites: [63]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRL._step`

**File:** [deepxube/updaters/updater_v_rl.py:61](../../../../deepxube/updaters/updater_v_rl.py#L61)
**Class:** `UpdateHeurVRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step(self, pathfind: PathFindSetHeurV, times: Times) -> None
```

## Docstring

Advance the pathfinder by one step (side effect only). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `PathFindSetHeurV` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `_pathfind_v_step` → `func:deepxube.updaters.updater_v_rl._pathfind_v_step` (lines: 63)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _step(self, pathfind: PathFindSetHeurV, times: Times) -> None:
        """ Advance the pathfinder by one step (side effect only). """
        _pathfind_v_step(pathfind)
```
