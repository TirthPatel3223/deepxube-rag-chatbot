---
id: "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_output"
kind: "staticmethod"
name: "_get_output"
qualified_name: "deepxube.base.heuristic.HeurNNetParQFixOut._get_output"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 357
line_end: 365
class: "HeurNNetParQFixOut"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@staticmethod"
parameters:
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "q_vals_np"
    annotation: "NDArray[np.float64]"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "List[List[float]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [359, 364]
  - target: "func:numpy.maximum"
    expr: "np.maximum"
    call_sites: [360]
  - target: null
    expr: "q_vals_np[state_idx].astype(np.float64).tolist"
    call_sites: [363]
  - target: null
    expr: "q_vals_np[state_idx].astype"
    call_sites: [363]
  - target: null
    expr: "range"
    call_sites: [364]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQFixOut._get_output`

**File:** [deepxube/base/heuristic.py:357](../../../../deepxube/base/heuristic.py#L357)
**Class:** `HeurNNetParQFixOut`
**Visibility:** private
**Kind:** staticmethod
**Decorators:** `@staticmethod`

## Signature

```python
def _get_output(states: List[State], q_vals_np: NDArray[np.float64], update_num: Optional[int]) -> List[List[float]]
```

## Docstring

Clamp Q-values non-negative; zero on ``update_num == 0``; split into per-state lists. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `states` | `List[State]` | — |
| `q_vals_np` | `NDArray[np.float64]` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`List[List[float]]`

## Calls

- `np.maximum` → `func:numpy.maximum` (lines: 360)

### Unresolved
- `len` (lines: 359, 364)
- `q_vals_np[state_idx].astype(np.float64).tolist` (lines: 363)
- `q_vals_np[state_idx].astype` (lines: 363)
- `range` (lines: 364)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_output(states: List[State], q_vals_np: NDArray[np.float64], update_num: Optional[int]) -> List[List[float]]:
        """ Clamp Q-values non-negative; zero on ``update_num == 0``; split into per-state lists. """
        assert q_vals_np.shape[0] == len(states)
        q_vals_np = np.maximum(q_vals_np, 0)
        if (update_num is not None) and (update_num == 0):
            q_vals_np = q_vals_np * 0
        q_vals_l: List[List[float]] = [q_vals_np[state_idx].astype(np.float64).tolist() for state_idx in
                                       range(len(states))]
        return q_vals_l
```
