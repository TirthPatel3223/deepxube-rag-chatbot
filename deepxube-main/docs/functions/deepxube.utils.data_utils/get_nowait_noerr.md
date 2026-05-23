---
id: "func:deepxube.utils.data_utils.get_nowait_noerr"
kind: "function"
name: "get_nowait_noerr"
qualified_name: "deepxube.utils.data_utils.get_nowait_noerr"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 61
line_end: 72
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
returns: "Any"
docstring_source: "present"
callees:
  - target: null
    expr: "q.get_nowait"
    call_sites: [69]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.data_utils.get_nowait_noerr`

**File:** [deepxube/utils/data_utils.py:61](../../../../deepxube/utils/data_utils.py#L61)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_nowait_noerr(q: Queue) -> Any
```

## Docstring

Non-blocking ``queue.get_nowait`` that swallows the ``Empty``
exception and returns ``None`` instead.

:param q: The multiprocessing queue.
:return: The dequeued value, or ``None`` if the queue was empty.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `q` | `Queue` | — |

## Returns

`Any`

## Calls

*(No resolved calls.)*

### Unresolved
- `q.get_nowait` (lines: 69)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_nowait_noerr(q: Queue) -> Any:
    """ Non-blocking ``queue.get_nowait`` that swallows the ``Empty``
    exception and returns ``None`` instead.

    :param q: The multiprocessing queue.
    :return: The dequeued value, or ``None`` if the queue was empty.
    """
    try:
        q_ret: Any = q.get_nowait()
        return q_ret
    except queue.Empty:
        return None
```
