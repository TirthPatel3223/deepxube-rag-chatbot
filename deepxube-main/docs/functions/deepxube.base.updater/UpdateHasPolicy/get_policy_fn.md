---
id: "func:deepxube.base.updater.UpdateHasPolicy.get_policy_fn"
kind: "method"
name: "get_policy_fn"
qualified_name: "deepxube.base.updater.UpdateHasPolicy.get_policy_fn"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 638
line_end: 640
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
returns: "PolicyFn"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.UpdateHasPolicy._get_policy_fn_from_dict"
    expr: "self._get_policy_fn_from_dict"
    call_sites: [640]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasPolicy.get_policy_fn`

**File:** [deepxube/base/updater.py:638](../../../../deepxube/base/updater.py#L638)
**Class:** `UpdateHasPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_policy_fn(self) -> PolicyFn
```

## Docstring

:return: Current policy-function callable. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`PolicyFn`

## Calls

- `self._get_policy_fn_from_dict` → `func:deepxube.base.updater.UpdateHasPolicy._get_policy_fn_from_dict` (lines: 640)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_policy_fn(self) -> PolicyFn:
        """ :return: Current policy-function callable. """
        return self._get_policy_fn_from_dict()
```
