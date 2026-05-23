---
id: "func:deepxube.base.domain.ActsEnumFixed.get_num_acts"
kind: "method"
name: "get_num_acts"
qualified_name: "deepxube.base.domain.ActsEnumFixed.get_num_acts"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 310
line_end: 312
class: "ActsEnumFixed"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "int"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [312]
  - target: "func:deepxube.base.domain.ActsEnumFixed.get_actions_fixed"
    expr: "self.get_actions_fixed"
    call_sites: [312]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.ActsEnumFixed.get_num_acts`

**File:** [deepxube/base/domain.py:310](../../../../deepxube/base/domain.py#L310)
**Class:** `ActsEnumFixed`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_num_acts(self) -> int
```

## Docstring

:return: Number of fixed actions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`int`

## Calls

- `self.get_actions_fixed` → `func:deepxube.base.domain.ActsEnumFixed.get_actions_fixed` (lines: 312)

### Unresolved
- `len` (lines: 312)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_num_acts(self) -> int:
        """ :return: Number of fixed actions. """
        return len(self.get_actions_fixed())
```
