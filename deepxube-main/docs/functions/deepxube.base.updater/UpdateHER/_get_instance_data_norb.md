---
id: "func:deepxube.base.updater.UpdateHER._get_instance_data_norb"
kind: "method"
name: "_get_instance_data_norb"
qualified_name: "deepxube.base.updater.UpdateHER._get_instance_data_norb"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 468
line_end: 469
class: "UpdateHER"
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
    call_sites: [469]
raises:
  - exception: "NotImplementedError"
    call_sites: [469]
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHER._get_instance_data_norb`

**File:** [deepxube/base/updater.py:468](../../../../deepxube/base/updater.py#L468)
**Class:** `UpdateHER`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_norb(self, instances: List[Inst], times: Times) -> List[NDArray]
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

- `NotImplementedError` → `func:deepxube.base.updater.NotImplementedError` (lines: 469)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `NotImplementedError` (lines: 469)

## Source

```python
    def _get_instance_data_norb(self, instances: List[Inst], times: Times) -> List[NDArray]:
        raise NotImplementedError("Must use replay buffer if doing HER.")
```
