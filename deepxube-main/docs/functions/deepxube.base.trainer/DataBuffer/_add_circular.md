---
id: "func:deepxube.base.trainer.DataBuffer._add_circular"
kind: "method"
name: "_add_circular"
qualified_name: "deepxube.base.trainer.DataBuffer._add_circular"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 113
line_end: 129
class: "DataBuffer"
visibility: "private"
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
    expr: "len"
    call_sites: [117, 123]
  - target: null
    expr: "min"
    call_sites: [119]
  - target: null
    expr: "range"
    call_sites: [123]
raises: []
reads_attrs:
  - "self.add_idx"
  - "self.arrays"
  - "self.max_size"
writes_attrs:
  - "self.add_idx"
---

# `deepxube.base.trainer.DataBuffer._add_circular`

**File:** [deepxube/base/trainer.py:113](../../../../deepxube/base/trainer.py#L113)
**Class:** `DataBuffer`
**Visibility:** private
**Kind:** method

## Signature

```python
def _add_circular(self, arrays_add: List[NDArray]) -> None
```

## Docstring

Wrap-around append into the pre-allocated arrays. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `arrays_add` | `List[NDArray]` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 117, 123)
- `min` (lines: 119)
- `range` (lines: 123)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.add_idx`

**Reads:**
- `self.add_idx`
- `self.arrays`
- `self.max_size`

## Source

```python
    def _add_circular(self, arrays_add: List[NDArray]) -> None:
        """ Wrap-around append into the pre-allocated arrays. """
        start_idx: int = 0
        num_add: int = arrays_add[0].shape[0]
        assert len(self.arrays) == len(arrays_add), "should have same number of arrays"
        while start_idx < num_add:
            num_add_i: int = min(num_add - start_idx, self.max_size - self.add_idx)
            end_idx: int = start_idx + num_add_i
            add_idx_end: int = self.add_idx + num_add_i

            for input_idx in range(len(self.arrays)):
                self.arrays[input_idx][self.add_idx:add_idx_end] = arrays_add[input_idx][start_idx:end_idx]

            start_idx = end_idx
            self.add_idx = add_idx_end
            if self.add_idx == self.max_size:
                self.add_idx = 0
```
