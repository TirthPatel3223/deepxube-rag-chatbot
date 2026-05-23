---
id: "func:deepxube.utils.data_utils.np_to_shnd"
kind: "function"
name: "np_to_shnd"
qualified_name: "deepxube.utils.data_utils.np_to_shnd"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 244
line_end: 253
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "arr"
    annotation: "NDArray"
    default: null
returns: "SharedNDArray"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.data_utils.SharedNDArray"
    expr: "SharedNDArray"
    call_sites: [250]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.data_utils.np_to_shnd`

**File:** [deepxube/utils/data_utils.py:244](../../../../deepxube/utils/data_utils.py#L244)
**Visibility:** public
**Kind:** function

## Signature

```python
def np_to_shnd(arr: NDArray) -> SharedNDArray
```

## Docstring

Copy an in-process numpy array into a fresh shared-memory block.

:param arr: Source numpy array. Its shape and dtype are preserved.
:return: A new ``SharedNDArray`` whose contents equal ``arr``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `arr` | `NDArray` | — |

## Returns

`SharedNDArray`

## Calls

- `SharedNDArray` → `func:deepxube.utils.data_utils.SharedNDArray` (lines: 250)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def np_to_shnd(arr: NDArray) -> SharedNDArray:
    """ Copy an in-process numpy array into a fresh shared-memory block.

    :param arr: Source numpy array. Its shape and dtype are preserved.
    :return: A new ``SharedNDArray`` whose contents equal ``arr``.
    """
    arr_shm: SharedNDArray = SharedNDArray(arr.shape, arr.dtype, None, True)
    arr_shm.array[:] = arr

    return arr_shm
```
