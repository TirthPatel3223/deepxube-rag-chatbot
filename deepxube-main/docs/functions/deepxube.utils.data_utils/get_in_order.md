---
id: "func:deepxube.utils.data_utils.get_in_order"
kind: "function"
name: "get_in_order"
qualified_name: "deepxube.utils.data_utils.get_in_order"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 94
line_end: 110
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "q"
    annotation: "Queue"
    default: null
  - name: "num"
    annotation: "int"
    default: null
returns: "List[Any]"
docstring_source: "present"
callees:
  - target: null
    expr: "range"
    call_sites: [106, 107]
  - target: null
    expr: "q.get"
    call_sites: [108]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.data_utils.get_in_order`

**File:** [deepxube/utils/data_utils.py:94](../../../../deepxube/utils/data_utils.py#L94)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_in_order(q: Queue, num: int) -> List[Any]
```

## Docstring

Pull ``num`` ``(idx, val)`` pairs from ``q`` and return them as a
list positioned by ``idx``.

Workers put ``(idx, payload)`` tuples onto the queue; this reorders the
arrivals so the caller gets deterministic indexing regardless of which
worker completed first.

:param q: Queue from which workers publish ``(idx, val)`` tuples.
:param num: Number of items to read.
:return: List of length ``num`` with ``ret_vals[idx] = val``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `q` | `Queue` | — |
| `num` | `int` | — |

## Returns

`List[Any]`

## Calls

*(No resolved calls.)*

### Unresolved
- `range` (lines: 106, 107)
- `q.get` (lines: 108)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_in_order(q: Queue, num: int) -> List[Any]:
    """ Pull ``num`` ``(idx, val)`` pairs from ``q`` and return them as a
    list positioned by ``idx``.

    Workers put ``(idx, payload)`` tuples onto the queue; this reorders the
    arrivals so the caller gets deterministic indexing regardless of which
    worker completed first.

    :param q: Queue from which workers publish ``(idx, val)`` tuples.
    :param num: Number of items to read.
    :return: List of length ``num`` with ``ret_vals[idx] = val``.
    """
    ret_vals: List[Any] = [None for _ in range(num)]
    for _ in range(num):
        idx, val = q.get()
        ret_vals[idx] = val
    return ret_vals
```
