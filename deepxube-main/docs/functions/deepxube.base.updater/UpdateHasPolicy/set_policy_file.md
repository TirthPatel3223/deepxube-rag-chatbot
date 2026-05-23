---
id: "func:deepxube.base.updater.UpdateHasPolicy.set_policy_file"
kind: "method"
name: "set_policy_file"
qualified_name: "deepxube.base.updater.UpdateHasPolicy.set_policy_file"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 630
line_end: 632
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
  - name: "policy_file"
    annotation: "str"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.UpdateHasPolicy.set_nnet_file"
    expr: "self.set_nnet_file"
    call_sites: [632]
  - target: "func:deepxube.base.updater.UpdateHasPolicy.policy_name"
    expr: "self.policy_name"
    call_sites: [632]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasPolicy.set_policy_file`

**File:** [deepxube/base/updater.py:630](../../../../deepxube/base/updater.py#L630)
**Class:** `UpdateHasPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_policy_file(self, policy_file: str) -> None
```

## Docstring

Record the policy network's checkpoint path. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `policy_file` | `str` | — |

## Returns

`None`

## Calls

- `self.set_nnet_file` → `func:deepxube.base.updater.UpdateHasPolicy.set_nnet_file` (lines: 632)
- `self.policy_name` → `func:deepxube.base.updater.UpdateHasPolicy.policy_name` (lines: 632)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def set_policy_file(self, policy_file: str) -> None:
        """ Record the policy network's checkpoint path. """
        self.set_nnet_file(self.policy_name(), policy_file)
```
