---
id: "func:deepxube.base.updater.Update._get_instance_data"
kind: "method"
name: "_get_instance_data"
qualified_name: "deepxube.base.updater.Update._get_instance_data"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 489
line_end: 494
class: "Update"
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
  - name: "rb_size"
    annotation: "int"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.Update._get_instance_data_norb"
    expr: "self._get_instance_data_norb"
    call_sites: [492]
  - target: "func:deepxube.base.updater.Update._get_instance_data_rb"
    expr: "self._get_instance_data_rb"
    call_sites: [494]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.Update._get_instance_data`

**File:** [deepxube/base/updater.py:489](../../../../deepxube/base/updater.py#L489)
**Class:** `Update`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data(self, instances: List[Inst], rb_size: int, times: Times) -> List[NDArray]
```

## Docstring

Dispatch to ``_get_instance_data_norb`` or ``_get_instance_data_rb`` based on ``rb_size``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[Inst]` | — |
| `rb_size` | `int` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `self._get_instance_data_norb` → `func:deepxube.base.updater.Update._get_instance_data_norb` (lines: 492)
- `self._get_instance_data_rb` → `func:deepxube.base.updater.Update._get_instance_data_rb` (lines: 494)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data(self, instances: List[Inst], rb_size: int, times: Times) -> List[NDArray]:
        """ Dispatch to ``_get_instance_data_norb`` or ``_get_instance_data_rb`` based on ``rb_size``. """
        if rb_size == 0:
            return self._get_instance_data_norb(instances, times)
        else:
            return self._get_instance_data_rb(instances, times)
```
