---
id: "func:deepxube.domains.npuzzle.NPuzzle._is_solvable"
kind: "method"
name: "_is_solvable"
qualified_name: "deepxube.domains.npuzzle.NPuzzle._is_solvable"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 235
line_end: 249
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
returns: "NDArray[np.bool_]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.npuzzle.NPuzzle._get_num_inversions"
    expr: "self._get_num_inversions"
    call_sites: [237]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [238, 243]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [241]
  - target: "func:numpy.floor"
    expr: "np.floor"
    call_sites: [242]
  - target: "func:numpy.logical_and"
    expr: "np.logical_and"
    call_sites: [244, 245]
  - target: "func:numpy.logical_not"
    expr: "np.logical_not"
    call_sites: [244, 245]
  - target: "func:numpy.logical_or"
    expr: "np.logical_or"
    call_sites: [246]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle._is_solvable`

**File:** [deepxube/domains/npuzzle.py:235](../../../../deepxube/domains/npuzzle.py#L235)
**Class:** `NPuzzle`
**Visibility:** private
**Kind:** method

## Signature

```python
def _is_solvable(self, states_np: NDArray[int_t]) -> NDArray[np.bool_]
```

## Docstring

:return: Boolean array indicating which states are solvable (inversion parity check). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `NDArray[int_t]` | — |

## Returns

`NDArray[np.bool_]`

## Calls

- `self._get_num_inversions` → `func:deepxube.domains.npuzzle.NPuzzle._get_num_inversions` (lines: 237)
- `np.array` → `func:numpy.array` (lines: 238, 243)
- `np.where` → `func:numpy.where` (lines: 241)
- `np.floor` → `func:numpy.floor` (lines: 242)
- `np.logical_and` → `func:numpy.logical_and` (lines: 244, 245)
- `np.logical_not` → `func:numpy.logical_not` (lines: 244, 245)
- `np.logical_or` → `func:numpy.logical_or` (lines: 246)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def _is_solvable(self, states_np: NDArray[int_t]) -> NDArray[np.bool_]:
        """ :return: Boolean array indicating which states are solvable (inversion parity check). """
        num_inversions: NDArray[np.int_] = self._get_num_inversions(states_np)
        num_inversions_is_even: NDArray[np.bool_] = np.array(num_inversions % 2 == 0)
        if self.dim % 2 == 0:
            # even
            _, z_idxs = np.where(states_np == 0)
            z_row_from_bottom_1 = self.dim - np.floor(z_idxs / self.dim)
            z_from_bottom_1_is_even: NDArray[np.bool_] = np.array(z_row_from_bottom_1 % 2 == 0)
            case_1: NDArray[np.bool_] = np.logical_and(z_from_bottom_1_is_even, np.logical_not(num_inversions_is_even))
            case_2: NDArray[np.bool_] = np.logical_and(np.logical_not(z_from_bottom_1_is_even), num_inversions_is_even)
            return np.logical_or(case_1, case_2)
        else:
            # odd
            return num_inversions_is_even
```
