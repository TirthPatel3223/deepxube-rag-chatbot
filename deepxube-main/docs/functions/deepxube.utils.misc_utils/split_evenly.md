---
id: "func:deepxube.utils.misc_utils.split_evenly"
kind: "function"
name: "split_evenly"
qualified_name: "deepxube.utils.misc_utils.split_evenly"
module: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_start: 53
line_end: 66
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "num_total"
    annotation: "int"
    default: null
  - name: "num_splits"
    annotation: "int"
    default: null
returns: "List[int]"
docstring_source: "present"
callees:
  - target: "func:math.floor"
    expr: "math.floor"
    call_sites: [61]
  - target: null
    expr: "range"
    call_sites: [61, 63]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.misc_utils.split_evenly`

**File:** [deepxube/utils/misc_utils.py:53](../../../../deepxube/utils/misc_utils.py#L53)
**Visibility:** public
**Kind:** function

## Signature

```python
def split_evenly(num_total: int, num_splits: int) -> List[int]
```

## Docstring

Partition ``num_total`` into ``num_splits`` integers that differ by
at most 1, distributing the remainder across the leading buckets.

:param num_total: Total to split.
:param num_splits: Number of buckets.
:return: List of length ``num_splits`` summing to ``num_total``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `num_total` | `int` | — |
| `num_splits` | `int` | — |

## Returns

`List[int]`

## Calls

- `math.floor` → `func:math.floor` (lines: 61)

### Unresolved
- `range` (lines: 61, 63)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def split_evenly(num_total: int, num_splits: int) -> List[int]:
    """ Partition ``num_total`` into ``num_splits`` integers that differ by
    at most 1, distributing the remainder across the leading buckets.

    :param num_total: Total to split.
    :param num_splits: Number of buckets.
    :return: List of length ``num_splits`` summing to ``num_total``.
    """
    num_per: List[int] = [math.floor(num_total / num_splits) for _ in range(num_splits)]
    left_over: int = num_total % num_splits
    for idx in range(left_over):
        num_per[idx] += 1

    return num_per
```
