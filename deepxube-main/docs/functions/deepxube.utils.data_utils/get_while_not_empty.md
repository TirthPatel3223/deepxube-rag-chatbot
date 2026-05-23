---
id: "func:deepxube.utils.data_utils.get_while_not_empty"
kind: "function"
name: "get_while_not_empty"
qualified_name: "deepxube.utils.data_utils.get_while_not_empty"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 75
line_end: 91
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
returns: "List[Any]"
docstring_source: "present"
callees:
  - target: null
    expr: "q.empty"
    call_sites: [84]
  - target: null
    expr: "q.get_nowait"
    call_sites: [86]
  - target: null
    expr: "q_rets.append"
    call_sites: [87]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.data_utils.get_while_not_empty`

**File:** [deepxube/utils/data_utils.py:75](../../../../deepxube/utils/data_utils.py#L75)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_while_not_empty(q: Queue) -> List[Any]
```

## Docstring

Drain all currently-available items from ``q`` without blocking.

:param q: The multiprocessing queue.
:return: List of items drained. Empty if the queue was empty at the
    start of the call.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `q` | `Queue` | — |

## Returns

`List[Any]`

## Calls

*(No resolved calls.)*

### Unresolved
- `q.empty` (lines: 84)
- `q.get_nowait` (lines: 86)
- `q_rets.append` (lines: 87)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_while_not_empty(q: Queue) -> List[Any]:
    """ Drain all currently-available items from ``q`` without blocking.

    :param q: The multiprocessing queue.
    :return: List of items drained. Empty if the queue was empty at the
        start of the call.
    """
    q_rets: List[Any] = []

    while not q.empty():
        try:
            q_ret: Any = q.get_nowait()
            q_rets.append(q_ret)
        except queue.Empty:
            break

    return q_rets
```
