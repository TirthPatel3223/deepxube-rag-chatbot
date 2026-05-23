---
id: "func:deepxube.base.trainer.Status.update_step_probs"
kind: "method"
name: "update_step_probs"
qualified_name: "deepxube.base.trainer.Status.update_step_probs"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 156
line_end: 164
class: "Status"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "step_to_search_perf"
    annotation: "Dict[int, PathFindPerf]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "float"
    call_sites: [158]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [158]
  - target: null
    expr: "step_to_search_perf[step].per_solved"
    call_sites: [158]
  - target: null
    expr: "step_to_search_perf.keys"
    call_sites: [159]
  - target: null
    expr: "min"
    call_sites: [161]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [163]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [164]
raises: []
reads_attrs:
  - "self.step_max"
  - "self.step_max_curr"
  - "self.step_probs"
writes_attrs:
  - "self.step_max_curr"
  - "self.step_probs"
---

# `deepxube.base.trainer.Status.update_step_probs`

**File:** [deepxube/base/trainer.py:156](../../../../deepxube/base/trainer.py#L156)
**Class:** `Status`
**Visibility:** public
**Kind:** method

## Signature

```python
def update_step_probs(self, step_to_search_perf: Dict[int, PathFindPerf]) -> None
```

## Docstring

Adapt the step-count sampling distribution based on the latest solve rate. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `step_to_search_perf` | `Dict[int, PathFindPerf]` | — |

## Returns

`None`

## Calls

- `np.mean` → `func:numpy.mean` (lines: 158)
- `np.zeros` → `func:numpy.zeros` (lines: 163)
- `np.arange` → `func:numpy.arange` (lines: 164)

### Unresolved
- `float` (lines: 158)
- `step_to_search_perf[step].per_solved` (lines: 158)
- `step_to_search_perf.keys` (lines: 159)
- `min` (lines: 161)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.step_max_curr`
- `self.step_probs`

**Reads:**
- `self.step_max`
- `self.step_max_curr`
- `self.step_probs`

## Source

```python
    def update_step_probs(self, step_to_search_perf: Dict[int, PathFindPerf]) -> None:
        """ Adapt the step-count sampling distribution based on the latest solve rate. """
        ave_solve: float = float(np.mean([step_to_search_perf[step].per_solved()
                                          for step in step_to_search_perf.keys()]))
        if ave_solve >= 50.0:
            self.step_max_curr = min(self.step_max_curr * 2, self.step_max)

        self.step_probs = np.zeros(self.step_max + 1)
        self.step_probs[np.arange(0, self.step_max_curr + 1)] = 1 / (self.step_max_curr + 1)
```
