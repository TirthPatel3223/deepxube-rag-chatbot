---
id: "func:deepxube.domains.npuzzle.NPuzzle._get_num_inversions"
kind: "method"
name: "_get_num_inversions"
qualified_name: "deepxube.domains.npuzzle.NPuzzle._get_num_inversions"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 251
line_end: 260
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
returns: "NDArray[np.int_]"
docstring_source: "present"
callees:
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [253]
  - target: null
    expr: "range"
    call_sites: [254, 255]
  - target: "func:numpy.logical_and"
    expr: "np.logical_and"
    call_sites: [256, 258]
raises: []
reads_attrs:
  - "self.num_tiles"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle._get_num_inversions`

**File:** [deepxube/domains/npuzzle.py:251](../../../../deepxube/domains/npuzzle.py#L251)
**Class:** `NPuzzle`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_num_inversions(self, states_np: NDArray[int_t]) -> NDArray[np.int_]
```

## Docstring

:return: Number of tile inversions in each state (pairs i<j where tile[i] > tile[j] and neither is 0). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `NDArray[int_t]` | — |

## Returns

`NDArray[np.int_]`

## Calls

- `np.zeros` → `func:numpy.zeros` (lines: 253)
- `np.logical_and` → `func:numpy.logical_and` (lines: 256, 258)

### Unresolved
- `range` (lines: 254, 255)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_tiles`

## Source

```python
    def _get_num_inversions(self, states_np: NDArray[int_t]) -> NDArray[np.int_]:
        """ :return: Number of tile inversions in each state (pairs i<j where tile[i] > tile[j] and neither is 0). """
        num_inversions: NDArray[np.int_] = np.zeros(states_np.shape[0], dtype=int)
        for idx_1 in range(self.num_tiles):
            for idx_2 in range(idx_1 + 1, self.num_tiles):
                no_zeros: NDArray[np.bool_] = np.logical_and(states_np[:, idx_1] != 0, states_np[:, idx_2] != 0)
                has_inversion: NDArray[np.bool_] = states_np[:, idx_1] > states_np[:, idx_2]
                num_inversions = num_inversions + np.logical_and(no_zeros, has_inversion)

        return num_inversions
```
