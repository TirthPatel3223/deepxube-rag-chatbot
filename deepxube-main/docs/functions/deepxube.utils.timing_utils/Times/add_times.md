---
id: "func:deepxube.utils.timing_utils.Times.add_times"
kind: "method"
name: "add_times"
qualified_name: "deepxube.utils.timing_utils.Times.add_times"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 115
line_end: 139
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
  - name: "time"
    annotation: "'Times'"
    default: null
  - name: "path"
    annotation: "Optional[List[str]]"
    default: "None"
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [123]
  - target: null
    expr: "path.pop"
    call_sites: [124]
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [126, 135]
  - target: null
    expr: "self.sub_times[path_0].add_times"
    call_sites: [128]
  - target: null
    expr: "sum"
    call_sites: [129, 139]
  - target: null
    expr: "time.counts.values"
    call_sites: [129]
  - target: "func:deepxube.utils.timing_utils.add_times"
    expr: "add_times"
    call_sites: [131]
  - target: "func:deepxube.utils.timing_utils.add_counts"
    expr: "add_counts"
    call_sites: [132]
  - target: null
    expr: "time.sub_times.keys"
    call_sites: [133]
  - target: null
    expr: "self.sub_times.keys"
    call_sites: [134]
  - target: null
    expr: "self.sub_times[sub_time_name].add_times"
    call_sites: [138]
  - target: null
    expr: "time.sub_times[sub_time_name].counts.values"
    call_sites: [139]
raises: []
reads_attrs:
  - "self.counts"
  - "self.sub_counts"
  - "self.sub_times"
  - "self.times"
writes_attrs: []
---

# `deepxube.utils.timing_utils.Times.add_times`

**File:** [deepxube/utils/timing_utils.py:115](../../../../deepxube/utils/timing_utils.py#L115)
**Class:** `Times`
**Visibility:** public
**Kind:** method

## Signature

```python
def add_times(self, time: 'Times', path: Optional[List[str]] = None) -> None
```

## Docstring

Merge another ``Times`` into this one, bucket-wise (and
recursively across sub-timers).

:param time: Source timer whose counts and times will be added in.
:param path: Optional path under which to nest ``time``. Missing
    path segments are created. ``path`` is consumed.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `time` | `'Times'` | — |
| `path` | `Optional[List[str]]` | `None` |

## Returns

`None`

## Calls

- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 126, 135)
- `add_times` → `func:deepxube.utils.timing_utils.add_times` (lines: 131)
- `add_counts` → `func:deepxube.utils.timing_utils.add_counts` (lines: 132)

### Unresolved
- `len` (lines: 123)
- `path.pop` (lines: 124)
- `self.sub_times[path_0].add_times` (lines: 128)
- `sum` (lines: 129, 139)
- `time.counts.values` (lines: 129)
- `time.sub_times.keys` (lines: 133)
- `self.sub_times.keys` (lines: 134)
- `self.sub_times[sub_time_name].add_times` (lines: 138)
- `time.sub_times[sub_time_name].counts.values` (lines: 139)

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
    def add_times(self, time: 'Times', path: Optional[List[str]] = None) -> None:
        """ Merge another ``Times`` into this one, bucket-wise (and
        recursively across sub-timers).

        :param time: Source timer whose counts and times will be added in.
        :param path: Optional path under which to nest ``time``. Missing
            path segments are created. ``path`` is consumed.
        """
        if (path is not None) and (len(path) > 0):
            path_0: str = path.pop(0)
            if path_0 not in self.sub_times:
                self.sub_times[path_0] = Times()
                self.sub_counts[path_0] = 0
            self.sub_times[path_0].add_times(time, path=path)
            self.sub_counts[path_0] += sum(time.counts.values())
        else:
            add_times(self.times, time.times)
            add_counts(self.counts, time.counts)
            for sub_time_name in time.sub_times.keys():
                if sub_time_name not in self.sub_times.keys():
                    self.sub_times[sub_time_name] = Times()
                    self.sub_counts[sub_time_name] = 0

                self.sub_times[sub_time_name].add_times(time.sub_times[sub_time_name])
                self.sub_counts[sub_time_name] += sum(time.sub_times[sub_time_name].counts.values())
```
