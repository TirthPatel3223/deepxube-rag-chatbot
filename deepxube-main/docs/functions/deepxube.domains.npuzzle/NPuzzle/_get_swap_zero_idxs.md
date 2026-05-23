---
id: "func:deepxube.domains.npuzzle.NPuzzle._get_swap_zero_idxs"
kind: "method"
name: "_get_swap_zero_idxs"
qualified_name: "deepxube.domains.npuzzle.NPuzzle._get_swap_zero_idxs"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 292
line_end: 333
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
  - name: "n"
    annotation: "int"
    default: null
returns: "NDArray[int_t]"
docstring_source: "present"
callees:
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [294]
  - target: null
    expr: "len"
    call_sites: [294]
  - target: null
    expr: "enumerate"
    call_sites: [295]
  - target: null
    expr: "range"
    call_sites: [296, 297]
  - target: "func:numpy.ravel_multi_index"
    expr: "np.ravel_multi_index"
    call_sites: [298, 329]
  - target: "func:numpy.ones"
    expr: "np.ones"
    call_sites: [300]
raises: []
reads_attrs:
  - "self.dtype"
  - "self.moves"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle._get_swap_zero_idxs`

**File:** [deepxube/domains/npuzzle.py:292](../../../../deepxube/domains/npuzzle.py#L292)
**Class:** `NPuzzle`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_swap_zero_idxs(self, n: int) -> NDArray[int_t]
```

## Docstring

:return: Table of shape ``(n², 4)`` mapping ``(zero_index, action)`` → flat index to swap with. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `n` | `int` | — |

## Returns

`NDArray[int_t]`

## Calls

- `np.zeros` → `func:numpy.zeros` (lines: 294)
- `np.ravel_multi_index` → `func:numpy.ravel_multi_index` (lines: 298, 329)
- `np.ones` → `func:numpy.ones` (lines: 300)

### Unresolved
- `len` (lines: 294)
- `enumerate` (lines: 295)
- `range` (lines: 296, 297)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dtype`
- `self.moves`

## Source

```python
    def _get_swap_zero_idxs(self, n: int) -> NDArray[int_t]:
        """ :return: Table of shape ``(n², 4)`` mapping ``(zero_index, action)`` → flat index to swap with. """
        swap_zero_idxs: NDArray[int_t] = np.zeros((n ** 2, len(self.moves)), dtype=self.dtype)
        for moveIdx, move in enumerate(self.moves):
            for i in range(n):
                for j in range(n):
                    z_idx = np.ravel_multi_index((i, j), (n, n))

                    state: NDArray = np.ones((n, n), dtype=int)
                    state[i, j] = 0

                    is_eligible: bool = False
                    if move == 'U':
                        is_eligible = i < (n - 1)
                    elif move == 'D':
                        is_eligible = i > 0
                    elif move == 'L':
                        is_eligible = j < (n - 1)
                    elif move == 'R':
                        is_eligible = j > 0

                    if is_eligible:
                        swap_i: int = -1
                        swap_j: int = -1
                        if move == 'U':
                            swap_i = i + 1
                            swap_j = j
                        elif move == 'D':
                            swap_i = i - 1
                            swap_j = j
                        elif move == 'L':
                            swap_i = i
                            swap_j = j + 1
                        elif move == 'R':
                            swap_i = i
                            swap_j = j - 1

                        swap_zero_idxs[z_idx, moveIdx] = np.ravel_multi_index((swap_i, swap_j), (n, n))
                    else:
                        swap_zero_idxs[z_idx, moveIdx] = z_idx

        return swap_zero_idxs
```
