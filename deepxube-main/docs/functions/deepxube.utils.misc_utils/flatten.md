---
id: "func:deepxube.utils.misc_utils.flatten"
kind: "function"
name: "flatten"
qualified_name: "deepxube.utils.misc_utils.flatten"
module: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_start: 15
line_end: 29
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "data"
    annotation: "List[List[Any]]"
    default: null
returns: "Tuple[List[Any], List[int]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [24]
  - target: null
    expr: "np.cumsum(num_each)[:-1].tolist"
    call_sites: [25]
  - target: "func:numpy.cumsum"
    expr: "np.cumsum"
    call_sites: [25]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.misc_utils.flatten`

**File:** [deepxube/utils/misc_utils.py:15](../../../../deepxube/utils/misc_utils.py#L15)
**Visibility:** public
**Kind:** function

## Signature

```python
def flatten(data: List[List[Any]]) -> Tuple[List[Any], List[int]]
```

## Docstring

Flatten a list of lists into one list plus the split points that
recover the original grouping.

:param data: List of sublists to concatenate.
:return: Tuple of (flat list, split_idxs) where ``split_idxs`` are the
    cumulative lengths of all but the last sublist. Pass them to
    ``unflatten`` (or ``np.split``) to rebuild the grouping.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `data` | `List[List[Any]]` | — |

## Returns

`Tuple[List[Any], List[int]]`

## Calls

- `np.cumsum` → `func:numpy.cumsum` (lines: 25)

### Unresolved
- `len` (lines: 24)
- `np.cumsum(num_each)[:-1].tolist` (lines: 25)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def flatten(data: List[List[Any]]) -> Tuple[List[Any], List[int]]:
    """ Flatten a list of lists into one list plus the split points that
    recover the original grouping.

    :param data: List of sublists to concatenate.
    :return: Tuple of (flat list, split_idxs) where ``split_idxs`` are the
        cumulative lengths of all but the last sublist. Pass them to
        ``unflatten`` (or ``np.split``) to rebuild the grouping.
    """
    num_each = [len(x) for x in data]
    split_idxs: List[int] = np.cumsum(num_each)[:-1].tolist()

    data_flat = [item for sublist in data for item in sublist]

    return data_flat, split_idxs
```
