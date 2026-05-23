---
id: "func:deepxube.domains.npuzzle.NPuzzle._move_np"
kind: "method"
name: "_move_np"
qualified_name: "deepxube.domains.npuzzle.NPuzzle._move_np"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 335
line_end: 351
class: "NPuzzle"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_np"
    annotation: "NDArray[int_t]"
    default: null
  - name: "z_idxs"
    annotation: "NDArray[np.int_]"
    default: null
  - name: "action"
    annotation: "int"
    default: null
returns: "Tuple[NDArray[int_t], NDArray[int_t], List[float]]"
docstring_source: "present"
callees:
  - target: null
    expr: "states_np.copy"
    call_sites: [338]
  - target: null
    expr: "np.arange(0, states_next_np.shape[0]).astype"
    call_sites: [341]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [341]
  - target: null
    expr: "range"
    call_sites: [349]
raises: []
reads_attrs:
  - "self.swap_zero_idxs"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle._move_np`

**File:** [deepxube/domains/npuzzle.py:335](../../../../deepxube/domains/npuzzle.py#L335)
**Class:** `NPuzzle`
**Visibility:** private
**Kind:** method

## Signature

```python
def _move_np(self, states_np: NDArray[int_t], z_idxs: NDArray[np.int_], action: int) -> Tuple[NDArray[int_t], NDArray[int_t], List[float]]
```

## Docstring

:return: ``(next states, new zero indices, transition costs)`` after one slide move. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `NDArray[int_t]` | — |
| `z_idxs` | `NDArray[np.int_]` | — |
| `action` | `int` | — |

## Returns

`Tuple[NDArray[int_t], NDArray[int_t], List[float]]`

## Calls

- `np.arange` → `func:numpy.arange` (lines: 341)

### Unresolved
- `states_np.copy` (lines: 338)
- `np.arange(0, states_next_np.shape[0]).astype` (lines: 341)
- `range` (lines: 349)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.swap_zero_idxs`

## Source

```python
    def _move_np(self, states_np: NDArray[int_t], z_idxs: NDArray[np.int_],
                 action: int) -> Tuple[NDArray[int_t], NDArray[int_t], List[float]]:
        """ :return: ``(next states, new zero indices, transition costs)`` after one slide move. """
        states_next_np: NDArray[int_t] = states_np.copy()

        # get index to swap with zero
        state_idxs: NDArray[np.int_] = np.arange(0, states_next_np.shape[0]).astype(int)
        swap_z_idxs: NDArray[int_t] = self.swap_zero_idxs[z_idxs, action]

        # swap zero with adjacent tile
        states_next_np[state_idxs, z_idxs] = states_np[state_idxs, swap_z_idxs]
        states_next_np[state_idxs, swap_z_idxs] = 0

        # transition costs
        transition_costs: List[float] = [1.0 for _ in range(states_np.shape[0])]

        return states_next_np, swap_z_idxs, transition_costs
```
