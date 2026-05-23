---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy._get_pathfind_functions"
kind: "method"
name: "_get_pathfind_functions"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy._get_pathfind_functions"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 288
line_end: 290
class: "UpdateHeurVRLHERPolicy"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "FNsHeurVPolicy"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.FNsHeurVPolicy"
    expr: "FNsHeurVPolicy"
    call_sites: [290]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy.get_heur_fn"
    expr: "self.get_heur_fn"
    call_sites: [290]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy.get_policy_fn"
    expr: "self.get_policy_fn"
    call_sites: [290]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy._get_pathfind_functions`

**File:** [deepxube/updaters/updater_v_rl.py:288](../../../../deepxube/updaters/updater_v_rl.py#L288)
**Class:** `UpdateHeurVRLHERPolicy`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_pathfind_functions(self) -> FNsHeurVPolicy
```

## Docstring

Build the ``FNsHeurVPolicy`` bundle from this updater's V + policy fns. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`FNsHeurVPolicy`

## Calls

- `FNsHeurVPolicy` → `func:deepxube.base.pathfinding.FNsHeurVPolicy` (lines: 290)
- `self.get_heur_fn` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy.get_heur_fn` (lines: 290)
- `self.get_policy_fn` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy.get_policy_fn` (lines: 290)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_pathfind_functions(self) -> FNsHeurVPolicy:
        """ Build the ``FNsHeurVPolicy`` bundle from this updater's V + policy fns. """
        return FNsHeurVPolicy(self.get_heur_fn(), self.get_policy_fn())
```
