---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ._get_pathfind_functions"
kind: "method"
name: "_get_pathfind_functions"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ._get_pathfind_functions"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 277
line_end: 279
class: "UpdatePolicyRLHERHeurQ"
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
    call_sites: [279]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ.get_heur_fn"
    expr: "self.get_heur_fn"
    call_sites: [279]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ.get_policy_fn"
    expr: "self.get_policy_fn"
    call_sites: [279]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ._get_pathfind_functions`

**File:** [deepxube/updaters/updater_policy_rl.py:277](../../../../deepxube/updaters/updater_policy_rl.py#L277)
**Class:** `UpdatePolicyRLHERHeurQ`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_pathfind_functions(self) -> FNsHeurQPolicy
```

## Docstring

Build the ``FNsHeurQPolicy`` bundle from Q + policy fns. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`FNsHeurQPolicy`

## Calls

- `FNsHeurQPolicy` → `func:deepxube.base.pathfinding.FNsHeurQPolicy` (lines: 279)
- `self.get_heur_fn` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ.get_heur_fn` (lines: 279)
- `self.get_policy_fn` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ.get_policy_fn` (lines: 279)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_pathfind_functions(self) -> FNsHeurQPolicy:
        """ Build the ``FNsHeurQPolicy`` bundle from Q + policy fns. """
        return FNsHeurQPolicy(self.get_heur_fn(), self.get_policy_fn())
```
