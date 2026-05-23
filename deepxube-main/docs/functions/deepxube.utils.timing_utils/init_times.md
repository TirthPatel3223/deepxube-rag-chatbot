---
id: "func:deepxube.utils.timing_utils.init_times"
kind: "function"
name: "init_times"
qualified_name: "deepxube.utils.timing_utils.init_times"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 40
line_end: 49
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "time_names"
    annotation: "List[str]"
    default: null
returns: "OrderedDict[str, float]"
docstring_source: "present"
callees:
  - target: "func:collections.OrderedDict"
    expr: "OrderedDict"
    call_sites: [46]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.timing_utils.init_times`

**File:** [deepxube/utils/timing_utils.py:40](../../../../deepxube/utils/timing_utils.py#L40)
**Visibility:** public
**Kind:** function

## Signature

```python
def init_times(time_names: List[str]) -> OrderedDict[str, float]
```

## Docstring

Build a zero-initialised ordered mapping from bucket name to 0.0.

:param time_names: Ordered list of bucket names.
:return: ``OrderedDict`` with the same order, all values ``0.0``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `time_names` | `List[str]` | — |

## Returns

`OrderedDict[str, float]`

## Calls

- `OrderedDict` → `func:collections.OrderedDict` (lines: 46)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def init_times(time_names: List[str]) -> OrderedDict[str, float]:
    """ Build a zero-initialised ordered mapping from bucket name to 0.0.

    :param time_names: Ordered list of bucket names.
    :return: ``OrderedDict`` with the same order, all values ``0.0``.
    """
    times: OrderedDict[str, float] = OrderedDict()
    for time_name in time_names:
        times[time_name] = 0.0
    return times
```
