---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal._get_pathfind_functions"
kind: "method"
name: "_get_pathfind_functions"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal._get_pathfind_functions"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 246
line_end: 248
class: "UpdateHeurVRLKeepGoal"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "FNsHeurV"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.FNsHeurV"
    expr: "FNsHeurV"
    call_sites: [248]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal.get_heur_fn"
    expr: "self.get_heur_fn"
    call_sites: [248]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal._get_pathfind_functions`

**File:** [deepxube/updaters/updater_v_rl.py:246](../../../../deepxube/updaters/updater_v_rl.py#L246)
**Class:** `UpdateHeurVRLKeepGoal`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_pathfind_functions(self) -> FNsHeurV
```

## Docstring

Build the ``FNsHeurV`` bundle using this updater's heuristic fn. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`FNsHeurV`

## Calls

- `FNsHeurV` → `func:deepxube.base.pathfinding.FNsHeurV` (lines: 248)
- `self.get_heur_fn` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal.get_heur_fn` (lines: 248)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_pathfind_functions(self) -> FNsHeurV:
        """ Build the ``FNsHeurV`` bundle using this updater's heuristic fn. """
        return FNsHeurV(self.get_heur_fn())
```
