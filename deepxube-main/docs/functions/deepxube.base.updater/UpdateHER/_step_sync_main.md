---
id: "func:deepxube.base.updater.UpdateHER._step_sync_main"
kind: "method"
name: "_step_sync_main"
qualified_name: "deepxube.base.updater.UpdateHER._step_sync_main"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 464
line_end: 466
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
  - name: "pathfind"
    annotation: "P"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "missing"
callees:
  - target: "func:deepxube.base.updater.NotImplementedError"
    expr: "NotImplementedError"
    call_sites: [465]
raises:
  - exception: "NotImplementedError"
    call_sites: [465]
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHER._step_sync_main`

**File:** [deepxube/base/updater.py:464](../../../../deepxube/base/updater.py#L464)
**Class:** `UpdateHER`
**Visibility:** private
**Kind:** method

## Signature

```python
def _step_sync_main(self, pathfind: P, times: Times) -> List[NDArray]
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `P` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `NotImplementedError` → `func:deepxube.base.updater.NotImplementedError` (lines: 465)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `NotImplementedError` (lines: 465)

## Source

```python
    def _step_sync_main(self, pathfind: P, times: Times) -> List[NDArray]:
        raise NotImplementedError("Cannot train with sync_main if also doing hindsight experience replay (HER) since goal relabeling is done after search is "
                                  "complete.")
```
