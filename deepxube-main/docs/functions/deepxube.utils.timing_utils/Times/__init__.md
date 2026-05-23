---
id: "func:deepxube.utils.timing_utils.Times.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.utils.timing_utils.Times.__init__"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 73
line_end: 86
class: "Times"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "time_names"
    annotation: "Optional[List[str]]"
    default: "None"
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.timing_utils.init_times"
    expr: "init_times"
    call_sites: [82]
  - target: "func:deepxube.utils.timing_utils.init_counts"
    expr: "init_counts"
    call_sites: [83]
  - target: null
    expr: "dict"
    call_sites: [85, 86]
raises: []
reads_attrs:
  - "self.counts"
  - "self.sub_counts"
  - "self.sub_times"
  - "self.times"
writes_attrs:
  - "self.counts"
  - "self.sub_counts"
  - "self.sub_times"
  - "self.times"
---

# `deepxube.utils.timing_utils.Times.__init__`

**File:** [deepxube/utils/timing_utils.py:73](../../../../deepxube/utils/timing_utils.py#L73)
**Class:** `Times`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, time_names: Optional[List[str]] = None) -> None
```

## Docstring

Create a new ``Times`` with optional pre-declared bucket names.

:param time_names: Names of buckets to start with at zero. If
    ``None``, buckets are created lazily on first ``record_time``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `time_names` | `Optional[List[str]]` | `None` |

## Returns

`None`

## Calls

- `init_times` → `func:deepxube.utils.timing_utils.init_times` (lines: 82)
- `init_counts` → `func:deepxube.utils.timing_utils.init_counts` (lines: 83)

### Unresolved
- `dict` (lines: 85, 86)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.counts`
- `self.sub_counts`
- `self.sub_times`
- `self.times`

**Reads:**
- `self.counts`
- `self.sub_counts`
- `self.sub_times`
- `self.times`

## Source

```python
    def __init__(self, time_names: Optional[List[str]] = None) -> None:
        """ Create a new ``Times`` with optional pre-declared bucket names.

        :param time_names: Names of buckets to start with at zero. If
            ``None``, buckets are created lazily on first ``record_time``.
        """
        if time_names is None:
            time_names = []

        self.times: OrderedDict[str, float] = init_times(time_names)
        self.counts: OrderedDict[str, int] = init_counts(time_names)

        self.sub_times: Dict[str, Times] = dict()
        self.sub_counts: Dict[str, int] = dict()
```
