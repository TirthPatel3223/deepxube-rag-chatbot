---
id: "func:deepxube.utils.timing_utils.add_counts"
kind: "function"
name: "add_counts"
qualified_name: "deepxube.utils.timing_utils.add_counts"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 27
line_end: 37
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "counts"
    annotation: "OrderedDict[str, int]"
    default: null
  - name: "counts_to_add"
    annotation: "OrderedDict[str, int]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "counts_to_add.items"
    call_sites: [34]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.timing_utils.add_counts`

**File:** [deepxube/utils/timing_utils.py:27](../../../../deepxube/utils/timing_utils.py#L27)
**Visibility:** public
**Kind:** function

## Signature

```python
def add_counts(counts: OrderedDict[str, int], counts_to_add: OrderedDict[str, int]) -> None
```

## Docstring

Add ``counts_to_add`` into ``counts`` bucket by bucket, creating
missing buckets at 0.

:param counts: Destination accumulator; modified in place.
:param counts_to_add: Increment values keyed by bucket name.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `counts` | `OrderedDict[str, int]` | — |
| `counts_to_add` | `OrderedDict[str, int]` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `counts_to_add.items` (lines: 34)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def add_counts(counts: OrderedDict[str, int], counts_to_add: OrderedDict[str, int]) -> None:
    """ Add ``counts_to_add`` into ``counts`` bucket by bucket, creating
    missing buckets at 0.

    :param counts: Destination accumulator; modified in place.
    :param counts_to_add: Increment values keyed by bucket name.
    """
    for key, value in counts_to_add.items():
        if key not in counts:
            counts[key] = 0
        counts[key] += value
```
