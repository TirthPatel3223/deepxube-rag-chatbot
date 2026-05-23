---
id: "func:deepxube.base.trainer.DataBuffer.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.trainer.DataBuffer.__init__"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 67
line_end: 88
class: "DataBuffer"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "max_size"
    annotation: "int"
    default: null
  - name: "shapes"
    annotation: "List[Tuple[int, ...]]"
    default: null
  - name: "dtypes"
    annotation: "List[np.dtype]"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [80, 88]
  - target: null
    expr: "print"
    call_sites: [81, 82, 84, 88]
  - target: null
    expr: "format"
    call_sites: [81]
  - target: null
    expr: "enumerate"
    call_sites: [83]
  - target: null
    expr: "zip"
    call_sites: [83]
  - target: "func:numpy.empty"
    expr: "np.empty"
    call_sites: [85]
  - target: null
    expr: "self.arrays.append"
    call_sites: [86]
raises: []
reads_attrs:
  - "self.add_idx"
  - "self.arrays"
  - "self.curr_size"
  - "self.max_size"
writes_attrs:
  - "self.add_idx"
  - "self.arrays"
  - "self.curr_size"
  - "self.max_size"
---

# `deepxube.base.trainer.DataBuffer.__init__`

**File:** [deepxube/base/trainer.py:67](../../../../deepxube/base/trainer.py#L67)
**Class:** `DataBuffer`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, max_size: int, shapes: List[Tuple[int, ...]], dtypes: List[np.dtype])
```

## Docstring

Pre-allocate one numpy array per (shape, dtype) at full ``max_size``.

:param max_size: Capacity in rows.
:param shapes: Shape (excluding leading row dim) for each parallel array.
:param dtypes: Dtype for each parallel array.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `max_size` | `int` | — |
| `shapes` | `List[Tuple[int, ...]]` | — |
| `dtypes` | `List[np.dtype]` | — |

## Returns

*(Not annotated.)*

## Calls

- `time.time` → `func:time.time` (lines: 80, 88)
- `np.empty` → `func:numpy.empty` (lines: 85)

### Unresolved
- `print` (lines: 81, 82, 84, 88)
- `format` (lines: 81)
- `enumerate` (lines: 83)
- `zip` (lines: 83)
- `self.arrays.append` (lines: 86)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.add_idx`
- `self.arrays`
- `self.curr_size`
- `self.max_size`

**Reads:**
- `self.add_idx`
- `self.arrays`
- `self.curr_size`
- `self.max_size`

## Source

```python
    def __init__(self, max_size: int, shapes: List[Tuple[int, ...]], dtypes: List[np.dtype]):
        """ Pre-allocate one numpy array per (shape, dtype) at full ``max_size``.

        :param max_size: Capacity in rows.
        :param shapes: Shape (excluding leading row dim) for each parallel array.
        :param dtypes: Dtype for each parallel array.
        """
        self.arrays: List[NDArray] = []
        self.max_size: int = max_size
        self.curr_size: int = 0
        self.add_idx: int = 0

        # first add
        start_time = time.time()
        print(f"Initializing data buffer with max size {format(self.max_size, ',')}")
        print("Input array sizes:")
        for array_idx, (shape, dtype) in enumerate(zip(shapes, dtypes)):
            print(f"index: {array_idx}, dtype: {dtype}, shape:", shape)
            array: NDArray = np.empty((self.max_size,) + shape, dtype=dtype)
            self.arrays.append(array)

        print(f"Data buffer initialized. Time: {time.time() - start_time}")
```
