---
id: "func:deepxube.utils.timing_utils.add_times"
kind: "function"
name: "add_times"
qualified_name: "deepxube.utils.timing_utils.add_times"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 14
line_end: 24
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "times"
    annotation: "OrderedDict[str, float]"
    default: null
  - name: "times_to_add"
    annotation: "OrderedDict[str, float]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "times_to_add.items"
    call_sites: [21]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.timing_utils.add_times`

**File:** [deepxube/utils/timing_utils.py:14](../../../../deepxube/utils/timing_utils.py#L14)
**Visibility:** public
**Kind:** function

## Signature

```python
def add_times(times: OrderedDict[str, float], times_to_add: OrderedDict[str, float]) -> None
```

## Docstring

Add ``times_to_add`` into ``times`` bucket by bucket, creating missing
buckets at 0.0.

:param times: Destination accumulator; modified in place.
:param times_to_add: Increment values keyed by bucket name.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `times` | `OrderedDict[str, float]` | — |
| `times_to_add` | `OrderedDict[str, float]` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `times_to_add.items` (lines: 21)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def add_times(times: OrderedDict[str, float], times_to_add: OrderedDict[str, float]) -> None:
    """ Add ``times_to_add`` into ``times`` bucket by bucket, creating missing
    buckets at 0.0.

    :param times: Destination accumulator; modified in place.
    :param times_to_add: Increment values keyed by bucket name.
    """
    for key, value in times_to_add.items():
        if key not in times:
            times[key] = 0.0
        times[key] += value
```
