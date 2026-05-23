---
id: "func:deepxube.tests.time_tests.data_runner"
kind: "function"
name: "data_runner"
qualified_name: "deepxube.tests.time_tests.data_runner"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 23
line_end: 29
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "queue1"
    annotation: "Queue"
    default: null
  - name: "queue2"
    annotation: "Queue"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "queue1.get"
    call_sites: [26]
  - target: null
    expr: "queue2.put"
    call_sites: [29]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.data_runner`

**File:** [deepxube/tests/time_tests.py:23](../../../../deepxube/tests/time_tests.py#L23)
**Visibility:** public
**Kind:** function

## Signature

```python
def data_runner(queue1: Queue, queue2: Queue) -> None
```

## Docstring

Worker that echoes items from ``queue1`` to ``queue2`` until it receives ``None``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `queue1` | `Queue` | — |
| `queue2` | `Queue` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `queue1.get` (lines: 26)
- `queue2.put` (lines: 29)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def data_runner(queue1: Queue, queue2: Queue) -> None:
    """ Worker that echoes items from ``queue1`` to ``queue2`` until it receives ``None``. """
    while True:
        the = queue1.get()
        if the is None:
            break
        queue2.put(the)
```
