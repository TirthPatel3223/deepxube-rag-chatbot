---
id: "func:deepxube.utils.data_utils.sel_l"
kind: "function"
name: "sel_l"
qualified_name: "deepxube.utils.data_utils.sel_l"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 128
line_end: 139
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "data_l"
    annotation: "List[NDArray]"
    default: null
  - name: "idxs"
    annotation: "NDArray"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "range"
    call_sites: [136]
  - target: null
    expr: "len"
    call_sites: [136]
  - target: null
    expr: "data_l_sel.append"
    call_sites: [137]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.data_utils.sel_l`

**File:** [deepxube/utils/data_utils.py:128](../../../../deepxube/utils/data_utils.py#L128)
**Visibility:** public
**Kind:** function

## Signature

```python
def sel_l(data_l: List[NDArray], idxs: NDArray) -> List[NDArray]
```

## Docstring

Index every array in a list with the same row indices.

:param data_l: List of numpy arrays sharing axis-0 length.
:param idxs: Row indices to select from each array.
:return: A parallel list where each element is ``arr[idxs]``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `data_l` | `List[NDArray]` | — |
| `idxs` | `NDArray` | — |

## Returns

`List[NDArray]`

## Calls

*(No resolved calls.)*

### Unresolved
- `range` (lines: 136)
- `len` (lines: 136)
- `data_l_sel.append` (lines: 137)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def sel_l(data_l: List[NDArray], idxs: NDArray) -> List[NDArray]:
    """ Index every array in a list with the same row indices.

    :param data_l: List of numpy arrays sharing axis-0 length.
    :param idxs: Row indices to select from each array.
    :return: A parallel list where each element is ``arr[idxs]``.
    """
    data_l_sel: List[NDArray] = []
    for np_idx in range(len(data_l)):
        data_l_sel.append(data_l[np_idx][idxs])

    return data_l_sel
```
