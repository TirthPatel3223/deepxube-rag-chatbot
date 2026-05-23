---
id: "func:deepxube.utils.timing_utils.Times.get_total_time"
kind: "method"
name: "get_total_time"
qualified_name: "deepxube.utils.timing_utils.Times.get_total_time"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 152
line_end: 164
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
returns: "float"
docstring_source: "present"
callees:
  - target: null
    expr: "self.times.values"
    call_sites: [158]
  - target: null
    expr: "self.sub_times.values"
    call_sites: [161]
  - target: null
    expr: "sub_time.get_total_time"
    call_sites: [162]
raises: []
reads_attrs:
  - "self.sub_times"
  - "self.times"
writes_attrs: []
---

# `deepxube.utils.timing_utils.Times.get_total_time`

**File:** [deepxube/utils/timing_utils.py:152](../../../../deepxube/utils/timing_utils.py#L152)
**Class:** `Times`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_total_time(self) -> float
```

## Docstring

Return the sum of every bucket in this timer and all sub-timers.

:return: Total accumulated seconds.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`float`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.times.values` (lines: 158)
- `self.sub_times.values` (lines: 161)
- `sub_time.get_total_time` (lines: 162)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.sub_times`
- `self.times`

## Source

```python
    def get_total_time(self) -> float:
        """ Return the sum of every bucket in this timer and all sub-timers.

        :return: Total accumulated seconds.
        """
        time_tot: float = 0.0
        for time_elapsed in self.times.values():
            time_tot += time_elapsed

        for sub_time in self.sub_times.values():
            time_tot += sub_time.get_total_time()

        return time_tot
```
