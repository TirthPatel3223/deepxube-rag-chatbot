---
id: "func:deepxube.base.updater.UpdateSup._step_sync_main"
kind: "method"
name: "_step_sync_main"
qualified_name: "deepxube.base.updater.UpdateSup._step_sync_main"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 586
line_end: 587
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
  - name: "pathfind"
    annotation: "PS"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "missing"
callees:
  - target: "func:deepxube.base.updater.NotImplementedError"
    expr: "NotImplementedError"
    call_sites: [587]
raises:
  - exception: "NotImplementedError"
    call_sites: [587]
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateSup._step_sync_main`

**File:** [deepxube/base/updater.py:586](../../../../deepxube/base/updater.py#L586)
**Class:** `UpdateSup`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step_sync_main(self, pathfind: PS, times: Times) -> List[NDArray]
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `PS` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `NotImplementedError` → `func:deepxube.base.updater.NotImplementedError` (lines: 587)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `NotImplementedError` (lines: 587)

## Source

```python
    def _step_sync_main(self, pathfind: PS, times: Times) -> List[NDArray]:
        raise NotImplementedError("No sync_main option for supervised update")
```
