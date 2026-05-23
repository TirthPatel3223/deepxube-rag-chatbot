---
id: "func:deepxube.base.updater.UpdatePolicy.get_policy_fn"
kind: "method"
name: "get_policy_fn"
qualified_name: "deepxube.base.updater.UpdatePolicy.get_policy_fn"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 733
line_end: 738
class: "UpdatePolicy"
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
  - target: null
    expr: "super().get_policy_fn"
    call_sites: [736]
  - target: null
    expr: "super"
    call_sites: [736]
  - target: null
    expr: "NotImplementedError"
    call_sites: [738]
raises:
  - exception: "NotImplementedError"
    call_sites: [738]
reads_attrs:
  - "self.up_args"
writes_attrs: []
---

# `deepxube.base.updater.UpdatePolicy.get_policy_fn`

**File:** [deepxube/base/updater.py:733](../../../../deepxube/base/updater.py#L733)
**Class:** `UpdatePolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_policy_fn(self) -> PolicyFn
```

## Docstring

:return: Policy function. ``sync_main`` is not yet supported. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`PolicyFn`

## Calls

*(No resolved calls.)*

### Unresolved
- `super().get_policy_fn` (lines: 736)
- `super` (lines: 736)
- `NotImplementedError` (lines: 738)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `NotImplementedError` (lines: 738)

## Attribute access

**Reads:**
- `self.up_args`

## Source

```python
    def get_policy_fn(self) -> PolicyFn:
        """ :return: Policy function. ``sync_main`` is not yet supported. """
        if not self.up_args.sync_main:
            return super().get_policy_fn()
        else:
            raise NotImplementedError("sync_main not yet implemented for policy_fn")
```
