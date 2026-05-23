---
id: "func:deepxube.base.updater.UpdateHasPolicy._get_policy_fn_from_dict"
kind: "method"
name: "_get_policy_fn_from_dict"
qualified_name: "deepxube.base.updater.UpdateHasPolicy._get_policy_fn_from_dict"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 642
line_end: 644
class: "UpdateHasPolicy"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "PolicyFn"
docstring_source: "present"
callees:
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [644]
  - target: "func:deepxube.base.updater.UpdateHasPolicy.policy_name"
    expr: "self.policy_name"
    call_sites: [644]
raises: []
reads_attrs:
  - "self.nnet_fn_dict"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasPolicy._get_policy_fn_from_dict`

**File:** [deepxube/base/updater.py:642](../../../../deepxube/base/updater.py#L642)
**Class:** `UpdateHasPolicy`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_policy_fn_from_dict(self) -> PolicyFn
```

## Docstring

Fetch the policy callable from the NNet-function dict. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`PolicyFn`

## Calls

- `cast` → `func:typing.cast` (lines: 644)
- `self.policy_name` → `func:deepxube.base.updater.UpdateHasPolicy.policy_name` (lines: 644)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_fn_dict`

## Source

```python
    def _get_policy_fn_from_dict(self) -> PolicyFn:
        """ Fetch the policy callable from the NNet-function dict. """
        return cast(PolicyFn, self.nnet_fn_dict[self.policy_name()])
```
