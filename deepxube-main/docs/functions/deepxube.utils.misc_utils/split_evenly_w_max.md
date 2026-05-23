---
id: "func:deepxube.utils.misc_utils.split_evenly_w_max"
kind: "function"
name: "split_evenly_w_max"
qualified_name: "deepxube.utils.misc_utils.split_evenly_w_max"
module: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_start: 69
line_end: 90
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
  - name: "max_per"
    annotation: "int"
    default: null
returns: "List[int]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.misc_utils.split_evenly"
    expr: "split_evenly"
    call_sites: [84]
  - target: null
    expr: "min"
    call_sites: [86]
  - target: null
    expr: "num_per.append"
    call_sites: [87]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.misc_utils.split_evenly_w_max`

**File:** [deepxube/utils/misc_utils.py:69](../../../../deepxube/utils/misc_utils.py#L69)
**Visibility:** public
**Kind:** function

## Signature

```python
def split_evenly_w_max(num_total: int, num_splits: int, max_per: int) -> List[int]
```

## Docstring

Partition ``num_total`` into chunks, each no larger than ``max_per``,
balanced across ``num_splits`` per round. The returned list may be
longer than ``num_splits`` if ``num_total > num_splits * max_per``.

:param num_total: Total to split.
:param num_splits: Target number of buckets per round.
:param max_per: Maximum value of any single bucket.
:return: List of positive integers summing to ``num_total``, each
    at most ``max_per``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `num_total` | `int` | — |
| `num_splits` | `int` | — |
| `max_per` | `int` | — |

## Returns

`List[int]`

## Calls

- `split_evenly` → `func:deepxube.utils.misc_utils.split_evenly` (lines: 84)

### Unresolved
- `min` (lines: 86)
- `num_per.append` (lines: 87)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def split_evenly_w_max(num_total: int, num_splits: int, max_per: int) -> List[int]:
    """ Partition ``num_total`` into chunks, each no larger than ``max_per``,
    balanced across ``num_splits`` per round. The returned list may be
    longer than ``num_splits`` if ``num_total > num_splits * max_per``.

    :param num_total: Total to split.
    :param num_splits: Target number of buckets per round.
    :param max_per: Maximum value of any single bucket.
    :return: List of positive integers summing to ``num_total``, each
        at most ``max_per``.
    """
    num_done: int = 0
    num_per: List[int] = []
    while num_done < num_total:
        num_left = num_total - num_done
        num_per_no_max: List[int] = split_evenly(num_left, num_splits)
        for num_per_i in num_per_no_max:
            num_per_i = min(num_per_i, max_per)
            num_per.append(num_per_i)
            num_done += num_per_i
    assert num_done == num_total
    return num_per
```
