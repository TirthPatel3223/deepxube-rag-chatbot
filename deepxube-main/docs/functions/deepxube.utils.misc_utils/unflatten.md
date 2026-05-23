---
id: "func:deepxube.utils.misc_utils.unflatten"
kind: "function"
name: "unflatten"
qualified_name: "deepxube.utils.misc_utils.unflatten"
module: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_start: 32
line_end: 50
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "data"
    annotation: "Union[List[Any], NDArray[Any]]"
    default: null
  - name: "split_idxs"
    annotation: "List[int]"
    default: null
returns: "List[List[Any]]"
docstring_source: "present"
callees:
  - target: null
    expr: "data_split.append"
    call_sites: [45, 48]
  - target: null
    expr: "list"
    call_sites: [45, 48]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.misc_utils.unflatten`

**File:** [deepxube/utils/misc_utils.py:32](../../../../deepxube/utils/misc_utils.py#L32)
**Visibility:** public
**Kind:** function

## Signature

```python
def unflatten(data: Union[List[Any], NDArray[Any]], split_idxs: List[int]) -> List[List[Any]]
```

## Docstring

Inverse of ``flatten``: split a flat sequence back into sublists at
the given cumulative boundaries.

:param data: Flat sequence (list or ndarray).
:param split_idxs: Cumulative split points, as produced by ``flatten``.
:return: List of sublists reproducing the original grouping.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `data` | `Union[List[Any], NDArray[Any]]` | — |
| `split_idxs` | `List[int]` | — |

## Returns

`List[List[Any]]`

## Calls

*(No resolved calls.)*

### Unresolved
- `data_split.append` (lines: 45, 48)
- `list` (lines: 45, 48)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def unflatten(data: Union[List[Any], NDArray[Any]], split_idxs: List[int]) -> List[List[Any]]:
    """ Inverse of ``flatten``: split a flat sequence back into sublists at
    the given cumulative boundaries.

    :param data: Flat sequence (list or ndarray).
    :param split_idxs: Cumulative split points, as produced by ``flatten``.
    :return: List of sublists reproducing the original grouping.
    """
    data_split: List[List[Any]] = []

    start_idx: int = 0
    end_idx: int
    for end_idx in split_idxs:
        data_split.append(list(data[start_idx:end_idx]))
        start_idx = end_idx

    data_split.append(list(data[start_idx:]))

    return data_split
```
