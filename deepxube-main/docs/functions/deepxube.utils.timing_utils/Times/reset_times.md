---
id: "func:deepxube.utils.timing_utils.Times.reset_times"
kind: "method"
name: "reset_times"
qualified_name: "deepxube.utils.timing_utils.Times.reset_times"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 141
line_end: 150
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
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "self.times.keys"
    call_sites: [145]
  - target: null
    expr: "self.sub_times.values"
    call_sites: [149]
  - target: null
    expr: "sub_time.reset_times"
    call_sites: [150]
raises: []
reads_attrs:
  - "self.counts"
  - "self.sub_times"
  - "self.times"
writes_attrs: []
---

# `deepxube.utils.timing_utils.Times.reset_times`

**File:** [deepxube/utils/timing_utils.py:141](../../../../deepxube/utils/timing_utils.py#L141)
**Class:** `Times`
**Visibility:** public
**Kind:** method

## Signature

```python
def reset_times(self) -> None
```

## Docstring

Zero every bucket and count, recursively across all sub-timers.
Existing bucket names are retained.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.times.keys` (lines: 145)
- `self.sub_times.values` (lines: 149)
- `sub_time.reset_times` (lines: 150)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.counts`
- `self.sub_times`
- `self.times`

## Source

```python
    def reset_times(self) -> None:
        """ Zero every bucket and count, recursively across all sub-timers.
        Existing bucket names are retained.
        """
        for key in self.times.keys():
            self.times[key] = 0.0
            self.counts[key] = 0

        for sub_time in self.sub_times.values():
            sub_time.reset_times()
```
