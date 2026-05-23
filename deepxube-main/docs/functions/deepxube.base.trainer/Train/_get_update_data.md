---
id: "func:deepxube.base.trainer.Train._get_update_data"
kind: "method"
name: "_get_update_data"
qualified_name: "deepxube.base.trainer.Train._get_update_data"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 322
line_end: 329
class: "Train"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num_gen"
    annotation: "int"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [324, 329]
  - target: null
    expr: "self.db.size"
    call_sites: [325]
  - target: null
    expr: "self.updater.get_update_data"
    call_sites: [326]
  - target: null
    expr: "self.db.add"
    call_sites: [328]
  - target: null
    expr: "times.record_time"
    call_sites: [329]
raises: []
reads_attrs:
  - "self.db"
  - "self.updater"
writes_attrs: []
---

# `deepxube.base.trainer.Train._get_update_data`

**File:** [deepxube/base/trainer.py:322](../../../../deepxube/base/trainer.py#L322)
**Class:** `Train`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_update_data(self, num_gen: int, times: Times) -> None
```

## Docstring

Drain the updater's output queue into the data buffer until we have ``num_gen`` rows. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_gen` | `int` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 324, 329)

### Unresolved
- `self.db.size` (lines: 325)
- `self.updater.get_update_data` (lines: 326)
- `self.db.add` (lines: 328)
- `times.record_time` (lines: 329)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.db`
- `self.updater`

## Source

```python
    def _get_update_data(self, num_gen: int, times: Times) -> None:
        """ Drain the updater's output queue into the data buffer until we have ``num_gen`` rows. """
        start_time = time.time()
        while self.db.size() < num_gen:
            data_l: List[List[NDArray]] = self.updater.get_update_data()
            for data in data_l:
                self.db.add(data)
        times.record_time("up_data", time.time() - start_time)
```
