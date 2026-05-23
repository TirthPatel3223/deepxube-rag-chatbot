---
id: "func:deepxube.utils.timing_utils.Times.record_time"
kind: "method"
name: "record_time"
qualified_name: "deepxube.utils.timing_utils.Times.record_time"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 88
line_end: 113
class: "Times"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "time_name"
    annotation: "str"
    default: null
  - name: "time_elapsed"
    annotation: "float"
    default: null
  - name: "path"
    annotation: "Optional[List[str]]"
    default: "None"
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [99]
  - target: null
    expr: "path.pop"
    call_sites: [100]
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [102]
  - target: null
    expr: "self.sub_times[path_0].record_time"
    call_sites: [105]
  - target: null
    expr: "self.times.keys"
    call_sites: [108]
raises: []
reads_attrs:
  - "self.counts"
  - "self.sub_counts"
  - "self.sub_times"
  - "self.times"
writes_attrs: []
---

# `deepxube.utils.timing_utils.Times.record_time`

**File:** [deepxube/utils/timing_utils.py:88](../../../../deepxube/utils/timing_utils.py#L88)
**Class:** `Times`
**Visibility:** public
**Kind:** method

## Signature

```python
def record_time(self, time_name: str, time_elapsed: float, path: Optional[List[str]] = None) -> None
```

## Docstring

Accumulate ``time_elapsed`` seconds into bucket ``time_name``.

If ``path`` is given, the entry is recorded inside a nested
``Times`` at that path. Missing path segments are created. The
``path`` list is consumed (first element popped).

:param time_name: Bucket name within the innermost ``Times``.
:param time_elapsed: Seconds to add.
:param path: Optional list of sub-timer names for nesting.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `time_name` | `str` | — |
| `time_elapsed` | `float` | — |
| `path` | `Optional[List[str]]` | `None` |

## Returns

`None`

## Calls

- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 102)

### Unresolved
- `len` (lines: 99)
- `path.pop` (lines: 100)
- `self.sub_times[path_0].record_time` (lines: 105)
- `self.times.keys` (lines: 108)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.counts`
- `self.sub_counts`
- `self.sub_times`
- `self.times`

## Source

```python
    def record_time(self, time_name: str, time_elapsed: float, path: Optional[List[str]] = None) -> None:
        """ Accumulate ``time_elapsed`` seconds into bucket ``time_name``.

        If ``path`` is given, the entry is recorded inside a nested
        ``Times`` at that path. Missing path segments are created. The
        ``path`` list is consumed (first element popped).

        :param time_name: Bucket name within the innermost ``Times``.
        :param time_elapsed: Seconds to add.
        :param path: Optional list of sub-timer names for nesting.
        """
        if (path is not None) and (len(path) > 0):
            path_0: str = path.pop(0)
            if path_0 not in self.sub_times:
                self.sub_times[path_0] = Times()
                self.sub_counts[path_0] = 0

            self.sub_times[path_0].record_time(time_name, time_elapsed, path=path)
            self.sub_counts[path_0] += 1
        else:
            if time_name not in self.times.keys():
                self.times[time_name] = 0
                self.counts[time_name] = 0

            self.times[time_name] += time_elapsed
            self.counts[time_name] += 1
```
