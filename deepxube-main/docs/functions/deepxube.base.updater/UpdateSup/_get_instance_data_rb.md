---
id: "func:deepxube.base.updater.UpdateSup._get_instance_data_rb"
kind: "method"
name: "_get_instance_data_rb"
qualified_name: "deepxube.base.updater.UpdateSup._get_instance_data_rb"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 589
line_end: 590
class: "UpdateSup"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instances"
    annotation: "List[Inst]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "missing"
callees:
  - target: "func:deepxube.base.updater.NotImplementedError"
    expr: "NotImplementedError"
    call_sites: [590]
raises:
  - exception: "NotImplementedError"
    call_sites: [590]
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateSup._get_instance_data_rb`

**File:** [deepxube/base/updater.py:589](../../../../deepxube/base/updater.py#L589)
**Class:** `UpdateSup`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_rb(self, instances: List[Inst], times: Times) -> List[NDArray]
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[Inst]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `NotImplementedError` → `func:deepxube.base.updater.NotImplementedError` (lines: 590)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `NotImplementedError` (lines: 590)

## Source

```python
    def _get_instance_data_rb(self, instances: List[Inst], times: Times) -> List[NDArray]:
        raise NotImplementedError("No replay buffer used with supervised update")
```
