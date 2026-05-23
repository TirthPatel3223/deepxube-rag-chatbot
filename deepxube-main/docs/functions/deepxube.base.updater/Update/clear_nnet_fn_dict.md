---
id: "func:deepxube.base.updater.Update.clear_nnet_fn_dict"
kind: "method"
name: "clear_nnet_fn_dict"
qualified_name: "deepxube.base.updater.Update.clear_nnet_fn_dict"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 163
line_end: 164
class: "Update"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "missing"
callees:
  - target: "func:deepxube.base.updater.dict"
    expr: "dict"
    call_sites: [164]
raises: []
reads_attrs:
  - "self.nnet_fn_dict"
writes_attrs:
  - "self.nnet_fn_dict"
---

# `deepxube.base.updater.Update.clear_nnet_fn_dict`

**File:** [deepxube/base/updater.py:163](../../../../deepxube/base/updater.py#L163)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def clear_nnet_fn_dict(self) -> None
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

- `dict` → `func:deepxube.base.updater.dict` (lines: 164)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.nnet_fn_dict`

**Reads:**
- `self.nnet_fn_dict`

## Source

```python
    def clear_nnet_fn_dict(self) -> None:
        self.nnet_fn_dict = dict()
```
