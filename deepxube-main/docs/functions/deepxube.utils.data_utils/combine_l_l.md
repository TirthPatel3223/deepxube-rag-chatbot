---
id: "func:deepxube.utils.data_utils.combine_l_l"
kind: "function"
name: "combine_l_l"
qualified_name: "deepxube.utils.data_utils.combine_l_l"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 142
line_end: 169
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "l_l"
    annotation: "List[List[NDArray]]"
    default: null
  - name: "comb"
    annotation: "str"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "range"
    call_sites: [156]
  - target: null
    expr: "len"
    call_sites: [156]
  - target: "func:numpy.concatenate"
    expr: "np.concatenate"
    call_sites: [161]
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [163]
  - target: null
    expr: "ValueError"
    call_sites: [165]
  - target: null
    expr: "l_l_comb.append"
    call_sites: [167]
raises:
  - exception: "ValueError"
    call_sites: [165]
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.data_utils.combine_l_l`

**File:** [deepxube/utils/data_utils.py:142](../../../../deepxube/utils/data_utils.py#L142)
**Visibility:** public
**Kind:** function

## Signature

```python
def combine_l_l(l_l: List[List[NDArray]], comb: str) -> List[NDArray]
```

## Docstring

Combine a list of per-item ndarray lists into a single per-position
ndarray list by either concatenating or stacking.

Given ``[[a1, b1], [a2, b2], ...]`` returns ``[comb(a1,a2,...), comb(b1,b2,...)]``.

:param l_l: Outer list: one entry per item; inner list: one ndarray per
    position. Inner lists must all have the same length.
:param comb: ``"concat"`` for ``np.concatenate`` along axis 0;
    ``"stack"`` for ``np.stack`` along axis 0.
:return: List of combined ndarrays, same length as ``l_l[0]``.
:raises ValueError: If ``comb`` is neither ``"concat"`` nor ``"stack"``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `l_l` | `List[List[NDArray]]` | — |
| `comb` | `str` | — |

## Returns

`List[NDArray]`

## Calls

- `np.concatenate` → `func:numpy.concatenate` (lines: 161)
- `np.stack` → `func:numpy.stack` (lines: 163)

### Unresolved
- `range` (lines: 156)
- `len` (lines: 156)
- `ValueError` (lines: 165)
- `l_l_comb.append` (lines: 167)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 165)

## Source

```python
def combine_l_l(l_l: List[List[NDArray]], comb: str) -> List[NDArray]:
    """ Combine a list of per-item ndarray lists into a single per-position
    ndarray list by either concatenating or stacking.

    Given ``[[a1, b1], [a2, b2], ...]`` returns ``[comb(a1,a2,...), comb(b1,b2,...)]``.

    :param l_l: Outer list: one entry per item; inner list: one ndarray per
        position. Inner lists must all have the same length.
    :param comb: ``"concat"`` for ``np.concatenate`` along axis 0;
        ``"stack"`` for ``np.stack`` along axis 0.
    :return: List of combined ndarrays, same length as ``l_l[0]``.
    :raises ValueError: If ``comb`` is neither ``"concat"`` nor ``"stack"``.
    """
    l_l_comb: List[NDArray] = []
    for np_idx in range(len(l_l[0])):
        l_l_idx: List[NDArray] = [x[np_idx] for x in l_l]

        l_l_idx_comb: NDArray
        if comb == "concat":
            l_l_idx_comb = np.concatenate(l_l_idx, axis=0)
        elif comb == "stack":
            l_l_idx_comb = np.stack(l_l_idx, axis=0)
        else:
            raise ValueError(f"Unknown comb method {comb}")

        l_l_comb.append(l_l_idx_comb)

    return l_l_comb
```
