---
id: "func:deepxube.utils.data_utils.SharedNDArray.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.utils.data_utils.SharedNDArray.__init__"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 178
line_end: 203
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
  - name: "shape"
    annotation: "Tuple[int, ...]"
    default: null
  - name: "dtype"
    annotation: "np.dtype"
    default: null
  - name: "name"
    annotation: "Optional[str]"
    default: null
  - name: "create"
    annotation: "bool"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "tuple"
    call_sites: [189]
  - target: "func:numpy.dtype"
    expr: "np.dtype"
    call_sites: [190]
  - target: null
    expr: "int"
    call_sites: [196]
  - target: "func:numpy.prod"
    expr: "np.prod"
    call_sites: [196]
  - target: "func:multiprocessing.shared_memory.SharedMemory"
    expr: "shared_memory.SharedMemory"
    call_sites: [197, 200]
  - target: "func:numpy.ndarray"
    expr: "np.ndarray"
    call_sites: [203]
raises: []
reads_attrs:
  - "self.array"
  - "self.dtype"
  - "self.shape"
  - "self.shm"
writes_attrs:
  - "self.array"
  - "self.dtype"
  - "self.shape"
  - "self.shm"
---

# `deepxube.utils.data_utils.SharedNDArray.__init__`

**File:** [deepxube/utils/data_utils.py:178](../../../../deepxube/utils/data_utils.py#L178)
**Class:** `SharedNDArray`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, shape: Tuple[int, ...], dtype: np.dtype, name: Optional[str], create: bool)
```

## Docstring

Create a new shared-memory block or attach to an existing one.

:param shape: Array shape.
:param dtype: Array dtype.
:param name: Shared-memory block name. Must be ``None`` if
    ``create=True`` (the OS assigns one); must be a valid existing
    block name if ``create=False``.
:param create: ``True`` to allocate a new block, ``False`` to
    attach to an existing block by ``name``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `shape` | `Tuple[int, ...]` | — |
| `dtype` | `np.dtype` | — |
| `name` | `Optional[str]` | — |
| `create` | `bool` | — |

## Returns

*(Not annotated.)*

## Calls

- `np.dtype` → `func:numpy.dtype` (lines: 190)
- `np.prod` → `func:numpy.prod` (lines: 196)
- `shared_memory.SharedMemory` → `func:multiprocessing.shared_memory.SharedMemory` (lines: 197, 200)
- `np.ndarray` → `func:numpy.ndarray` (lines: 203)

### Unresolved
- `tuple` (lines: 189)
- `int` (lines: 196)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.array`
- `self.dtype`
- `self.shape`
- `self.shm`

**Reads:**
- `self.array`
- `self.dtype`
- `self.shape`
- `self.shm`

## Source

```python
    def __init__(self, shape: Tuple[int, ...], dtype: np.dtype, name: Optional[str], create: bool):
        """ Create a new shared-memory block or attach to an existing one.

        :param shape: Array shape.
        :param dtype: Array dtype.
        :param name: Shared-memory block name. Must be ``None`` if
            ``create=True`` (the OS assigns one); must be a valid existing
            block name if ``create=False``.
        :param create: ``True`` to allocate a new block, ``False`` to
            attach to an existing block by ``name``.
        """
        self.shape = tuple(shape)
        self.dtype = np.dtype(dtype)

        self.shm: SharedMemory
        if create:
            # create new shared block
            assert name is None, "Let SharedMemory do name creation"
            nbytes: int = int(np.prod(self.shape)) * self.dtype.itemsize
            self.shm = shared_memory.SharedMemory(create=True, size=nbytes, name=name)
        else:
            # attach to existing shared block
            self.shm = shared_memory.SharedMemory(name=name)

        # numpy view backed by shared memory
        self.array: NDArray = np.ndarray(self.shape, dtype=self.dtype, buffer=self.shm.buf)
```
