---
id: "func:deepxube.utils.timing_utils.init_counts"
kind: "function"
name: "init_counts"
qualified_name: "deepxube.utils.timing_utils.init_counts"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 52
line_end: 61
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
returns: "OrderedDict[str, int]"
docstring_source: "present"
callees:
  - target: "func:collections.OrderedDict"
    expr: "OrderedDict"
    call_sites: [58]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.timing_utils.init_counts`

**File:** [deepxube/utils/timing_utils.py:52](../../../../deepxube/utils/timing_utils.py#L52)
**Visibility:** public
**Kind:** function

## Signature

```python
def init_counts(time_names: List[str]) -> OrderedDict[str, int]
```

## Docstring

Build a zero-initialised ordered mapping from bucket name to 0.

:param time_names: Ordered list of bucket names.
:return: ``OrderedDict`` with the same order, all values ``0``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `time_names` | `List[str]` | — |

## Returns

`OrderedDict[str, int]`

## Calls

- `OrderedDict` → `func:collections.OrderedDict` (lines: 58)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def init_counts(time_names: List[str]) -> OrderedDict[str, int]:
    """ Build a zero-initialised ordered mapping from bucket name to 0.

    :param time_names: Ordered list of bucket names.
    :return: ``OrderedDict`` with the same order, all values ``0``.
    """
    counts: OrderedDict[str, int] = OrderedDict()
    for time_name in time_names:
        counts[time_name] = 0
    return counts
```
