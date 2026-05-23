---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy._get_pathfind_functions"
kind: "method"
name: "_get_pathfind_functions"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy._get_pathfind_functions"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 299
line_end: 301
class: "UpdateHeurQRLHERPolicy"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "FNsHeurQPolicy"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.FNsHeurQPolicy"
    expr: "FNsHeurQPolicy"
    call_sites: [301]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy.get_heur_fn"
    expr: "self.get_heur_fn"
    call_sites: [301]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy.get_policy_fn"
    expr: "self.get_policy_fn"
    call_sites: [301]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy._get_pathfind_functions`

**File:** [deepxube/updaters/updater_q_rl.py:299](../../../../deepxube/updaters/updater_q_rl.py#L299)
**Class:** `UpdateHeurQRLHERPolicy`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_pathfind_functions(self) -> FNsHeurQPolicy
```

## Docstring

Build the ``FNsHeurQPolicy`` bundle from this updater's Q + policy fns. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`FNsHeurQPolicy`

## Calls

- `FNsHeurQPolicy` → `func:deepxube.base.pathfinding.FNsHeurQPolicy` (lines: 301)
- `self.get_heur_fn` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy.get_heur_fn` (lines: 301)
- `self.get_policy_fn` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy.get_policy_fn` (lines: 301)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_pathfind_functions(self) -> FNsHeurQPolicy:
        """ Build the ``FNsHeurQPolicy`` bundle from this updater's Q + policy fns. """
        return FNsHeurQPolicy(self.get_heur_fn(), self.get_policy_fn())
```
