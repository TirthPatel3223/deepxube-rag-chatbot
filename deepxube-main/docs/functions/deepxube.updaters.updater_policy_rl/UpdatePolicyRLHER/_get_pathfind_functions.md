---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER._get_pathfind_functions"
kind: "method"
name: "_get_pathfind_functions"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER._get_pathfind_functions"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 219
line_end: 221
class: "UpdatePolicyRLHER"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "FNsPolicy"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.FNsPolicy"
    expr: "FNsPolicy"
    call_sites: [221]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER.get_policy_fn"
    expr: "self.get_policy_fn"
    call_sites: [221]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER._get_pathfind_functions`

**File:** [deepxube/updaters/updater_policy_rl.py:219](../../../../deepxube/updaters/updater_policy_rl.py#L219)
**Class:** `UpdatePolicyRLHER`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_pathfind_functions(self) -> FNsPolicy
```

## Docstring

Build the ``FNsPolicy`` bundle using this updater's policy fn. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`FNsPolicy`

## Calls

- `FNsPolicy` → `func:deepxube.base.pathfinding.FNsPolicy` (lines: 221)
- `self.get_policy_fn` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER.get_policy_fn` (lines: 221)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_pathfind_functions(self) -> FNsPolicy:
        """ Build the ``FNsPolicy`` bundle using this updater's policy fn. """
        return FNsPolicy(self.get_policy_fn())
```
