---
id: "func:deepxube.base.updater.UpdateHasPolicy.set_policy_nnet"
kind: "method"
name: "set_policy_nnet"
qualified_name: "deepxube.base.updater.UpdateHasPolicy.set_policy_nnet"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 626
line_end: 628
class: "UpdateHasPolicy"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "policy_nnet"
    annotation: "PolicyNNetPar"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.UpdateHasPolicy.add_nnet_par"
    expr: "self.add_nnet_par"
    call_sites: [628]
  - target: "func:deepxube.base.updater.UpdateHasPolicy.policy_name"
    expr: "self.policy_name"
    call_sites: [628]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasPolicy.set_policy_nnet`

**File:** [deepxube/base/updater.py:626](../../../../deepxube/base/updater.py#L626)
**Class:** `UpdateHasPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_policy_nnet(self, policy_nnet: PolicyNNetPar) -> None
```

## Docstring

Register the policy NNet parameter object. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `policy_nnet` | `PolicyNNetPar` | — |

## Returns

`None`

## Calls

- `self.add_nnet_par` → `func:deepxube.base.updater.UpdateHasPolicy.add_nnet_par` (lines: 628)
- `self.policy_name` → `func:deepxube.base.updater.UpdateHasPolicy.policy_name` (lines: 628)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def set_policy_nnet(self, policy_nnet: PolicyNNetPar) -> None:
        """ Register the policy NNet parameter object. """
        self.add_nnet_par(self.policy_name(), policy_nnet)
```
