---
id: "func:deepxube.utils.data_utils.SharedNDArray.__getitem__"
kind: "method"
name: "__getitem__"
qualified_name: "deepxube.utils.data_utils.SharedNDArray.__getitem__"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 231
line_end: 232
class: "SharedNDArray"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "key"
    annotation: "Any"
    default: null
returns: "NDArray"
docstring_source: "missing"
callees:
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [232]
raises: []
reads_attrs:
  - "self.array"
writes_attrs: []
---

# `deepxube.utils.data_utils.SharedNDArray.__getitem__`

**File:** [deepxube/utils/data_utils.py:231](../../../../deepxube/utils/data_utils.py#L231)
**Class:** `SharedNDArray`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __getitem__(self, key: Any) -> NDArray
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `key` | `Any` | — |

## Returns

`NDArray`

## Calls

- `cast` → `func:typing.cast` (lines: 232)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.array`

## Source

```python
    def __getitem__(self, key: Any) -> NDArray:
        return cast(NDArray, self.array[key])
```
