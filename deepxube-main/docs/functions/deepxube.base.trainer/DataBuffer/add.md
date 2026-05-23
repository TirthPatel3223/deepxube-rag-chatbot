---
id: "func:deepxube.base.trainer.DataBuffer.add"
kind: "method"
name: "add"
qualified_name: "deepxube.base.trainer.DataBuffer.add"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 90
line_end: 94
class: "DataBuffer"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "arrays_add"
    annotation: "List[NDArray]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "min"
    call_sites: [92]
  - target: null
    expr: "len"
    call_sites: [93]
  - target: "func:deepxube.base.trainer.DataBuffer._add_circular"
    expr: "self._add_circular"
    call_sites: [94]
raises: []
reads_attrs:
  - "self.arrays"
  - "self.curr_size"
  - "self.max_size"
writes_attrs:
  - "self.curr_size"
---

# `deepxube.base.trainer.DataBuffer.add`

**File:** [deepxube/base/trainer.py:90](../../../../deepxube/base/trainer.py#L90)
**Class:** `DataBuffer`
**Visibility:** public
**Kind:** method

## Signature

```python
def add(self, arrays_add: List[NDArray]) -> None
```

## Docstring

Append the rows of ``arrays_add`` (parallel across all stored arrays) circularly. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `arrays_add` | `List[NDArray]` | — |

## Returns

`None`

## Calls

- `self._add_circular` → `func:deepxube.base.trainer.DataBuffer._add_circular` (lines: 94)

### Unresolved
- `min` (lines: 92)
- `len` (lines: 93)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.curr_size`

**Reads:**
- `self.arrays`
- `self.curr_size`
- `self.max_size`

## Source

```python
    def add(self, arrays_add: List[NDArray]) -> None:
        """ Append the rows of ``arrays_add`` (parallel across all stored arrays) circularly. """
        self.curr_size = min(self.curr_size + arrays_add[0].shape[0], self.max_size)
        assert len(self.arrays) > 0, "Data buffer should have at least one array."
        self._add_circular(arrays_add)
```
