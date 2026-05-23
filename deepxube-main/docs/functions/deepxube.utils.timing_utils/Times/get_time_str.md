---
id: "func:deepxube.utils.timing_utils.Times.get_time_str"
kind: "method"
name: "get_time_str"
qualified_name: "deepxube.utils.timing_utils.Times.get_time_str"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 166
line_end: 185
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
  - name: "prefix"
    annotation: "str"
    default: "''"
  - name: "decplace"
    annotation: "int"
    default: "2"
returns: "str"
docstring_source: "present"
callees:
  - target: null
    expr: "self.times.items"
    call_sites: [175]
  - target: null
    expr: "sub_time.get_total_time"
    call_sites: [176]
  - target: null
    expr: "self.sub_times.items"
    call_sites: [177, 182]
  - target: null
    expr: "', '.join"
    call_sites: [179]
  - target: "func:deepxube.utils.timing_utils.Times.get_total_time"
    expr: "self.get_total_time"
    call_sites: [179]
  - target: null
    expr: "sub_time.get_time_str"
    call_sites: [183]
raises: []
reads_attrs:
  - "self.sub_times"
  - "self.times"
writes_attrs: []
---

# `deepxube.utils.timing_utils.Times.get_time_str`

**File:** [deepxube/utils/timing_utils.py:166](../../../../deepxube/utils/timing_utils.py#L166)
**Class:** `Times`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_time_str(self, prefix: str = '', decplace: int = 2) -> str
```

## Docstring

Format every bucket and sub-timer into a single human-readable
multi-line string.

:param prefix: String prepended to each nested line (used internally
    for recursive indentation).
:param decplace: Number of decimal places to render.
:return: A multi-line string listing per-bucket times and a total.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `prefix` | `str` | `''` |
| `decplace` | `int` | `2` |

## Returns

`str`

## Calls

- `self.get_total_time` → `func:deepxube.utils.timing_utils.Times.get_total_time` (lines: 179)

### Unresolved
- `self.times.items` (lines: 175)
- `sub_time.get_total_time` (lines: 176)
- `self.sub_times.items` (lines: 177, 182)
- `', '.join` (lines: 179)
- `sub_time.get_time_str` (lines: 183)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.sub_times`
- `self.times`

## Source

```python
    def get_time_str(self, prefix: str = "", decplace: int = 2) -> str:
        """ Format every bucket and sub-timer into a single human-readable
        multi-line string.

        :param prefix: String prepended to each nested line (used internally
            for recursive indentation).
        :param decplace: Number of decimal places to render.
        :return: A multi-line string listing per-bucket times and a total.
        """
        time_str_l: List[str] = [f"{key}: {val:.{decplace}f}" for key, val in self.times.items()]
        sub_time_str_l: List[str] = [f"->{key}: {sub_time.get_total_time():.{decplace}f}"
                                     for key, sub_time in self.sub_times.items()]

        time_str: str = ", ".join(time_str_l + sub_time_str_l + [f"Tot: {self.get_total_time():.{decplace}f}"])

        prefix_new: str = f"\t{prefix}"
        for key, sub_time in self.sub_times.items():
            time_str = f"{time_str}\n{prefix_new}({key}): {sub_time.get_time_str(prefix=prefix_new)}"

        return time_str
```
