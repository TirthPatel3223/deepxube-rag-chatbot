---
id: "func:deepxube.base.updater.UpdateHasPolicy.get_policy_nnet_par"
kind: "method"
name: "get_policy_nnet_par"
qualified_name: "deepxube.base.updater.UpdateHasPolicy.get_policy_nnet_par"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 634
line_end: 636
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
returns: "PolicyNNetPar"
docstring_source: "present"
callees:
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [636]
  - target: "func:deepxube.base.updater.UpdateHasPolicy.policy_name"
    expr: "self.policy_name"
    call_sites: [636]
raises: []
reads_attrs:
  - "self.nnet_par_dict"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasPolicy.get_policy_nnet_par`

**File:** [deepxube/base/updater.py:634](../../../../deepxube/base/updater.py#L634)
**Class:** `UpdateHasPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_policy_nnet_par(self) -> PolicyNNetPar
```

## Docstring

:return: Registered policy NNet parameter object. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`PolicyNNetPar`

## Calls

- `cast` → `func:typing.cast` (lines: 636)
- `self.policy_name` → `func:deepxube.base.updater.UpdateHasPolicy.policy_name` (lines: 636)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_par_dict`

## Source

```python
    def get_policy_nnet_par(self) -> PolicyNNetPar:
        """ :return: Registered policy NNet parameter object. """
        return cast(PolicyNNetPar, self.nnet_par_dict[self.policy_name()])
```
