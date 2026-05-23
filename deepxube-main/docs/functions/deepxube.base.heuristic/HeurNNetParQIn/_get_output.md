---
id: "func:deepxube.base.heuristic.HeurNNetParQIn._get_output"
kind: "staticmethod"
name: "_get_output"
qualified_name: "deepxube.base.heuristic.HeurNNetParQIn._get_output"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 422
line_end: 431
class: "HeurNNetParQIn"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@staticmethod"
parameters:
  - name: "states_rep"
    annotation: "List[State]"
    default: null
  - name: "q_vals_np"
    annotation: "NDArray[np.float64]"
    default: null
  - name: "split_idxs"
    annotation: "List[int]"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "List[List[float]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [424]
  - target: "func:numpy.maximum"
    expr: "np.maximum"
    call_sites: [425]
  - target: null
    expr: "q_vals_np.astype(np.float64).tolist"
    call_sites: [429]
  - target: null
    expr: "q_vals_np.astype"
    call_sites: [429]
  - target: "func:deepxube.utils.misc_utils.unflatten"
    expr: "misc_utils.unflatten"
    call_sites: [430]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQIn._get_output`

**File:** [deepxube/base/heuristic.py:422](../../../../deepxube/base/heuristic.py#L422)
**Class:** `HeurNNetParQIn`
**Visibility:** private
**Kind:** staticmethod
**Decorators:** `@staticmethod`

## Signature

```python
def _get_output(states_rep: List[State], q_vals_np: NDArray[np.float64], split_idxs: List[int], update_num: Optional[int]) -> List[List[float]]
```

## Docstring

Clamp non-negative, zero on warmup, then unflatten back into per-state Q-value lists. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `states_rep` | `List[State]` | — |
| `q_vals_np` | `NDArray[np.float64]` | — |
| `split_idxs` | `List[int]` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`List[List[float]]`

## Calls

- `np.maximum` → `func:numpy.maximum` (lines: 425)
- `misc_utils.unflatten` → `func:deepxube.utils.misc_utils.unflatten` (lines: 430)

### Unresolved
- `len` (lines: 424)
- `q_vals_np.astype(np.float64).tolist` (lines: 429)
- `q_vals_np.astype` (lines: 429)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_output(states_rep: List[State], q_vals_np: NDArray[np.float64], split_idxs: List[int], update_num: Optional[int]) -> List[List[float]]:
        """ Clamp non-negative, zero on warmup, then unflatten back into per-state Q-value lists. """
        assert q_vals_np.shape[0] == len(states_rep)
        q_vals_np = np.maximum(q_vals_np[:, 0], 0)
        if (update_num is not None) and (update_num == 0):
            q_vals_np = q_vals_np * 0

        q_vals_flat: List[float] = q_vals_np.astype(np.float64).tolist()
        q_vals_l: List[List[float]] = misc_utils.unflatten(q_vals_flat, split_idxs)
        return q_vals_l
```
