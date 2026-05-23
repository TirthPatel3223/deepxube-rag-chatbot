---
id: "func:deepxube.domains.npuzzle.NPuzzle.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.__init__"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 68
line_end: 88
class: "NPuzzle"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "dim"
    annotation: "int"
    default: "4"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [70]
  - target: null
    expr: "super"
    call_sites: [70]
  - target: null
    expr: "np.concatenate((np.arange(1, self.dim * self.dim), [0])).astype"
    call_sites: [82]
  - target: "func:numpy.concatenate"
    expr: "np.concatenate"
    call_sites: [82]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [82]
  - target: "func:deepxube.domains.npuzzle.NPuzzle._get_swap_zero_idxs"
    expr: "self._get_swap_zero_idxs"
    call_sites: [85]
  - target: "func:deepxube.domains.npuzzle.NPAction"
    expr: "NPAction"
    call_sites: [88]
  - target: null
    expr: "range"
    call_sites: [88]
raises: []
reads_attrs:
  - "self.actions"
  - "self.dim"
  - "self.dtype"
  - "self.goal_tiles"
  - "self.num_actions"
  - "self.num_tiles"
  - "self.swap_zero_idxs"
writes_attrs:
  - "self.actions"
  - "self.dim"
  - "self.dtype"
  - "self.goal_tiles"
  - "self.num_actions"
  - "self.num_tiles"
  - "self.swap_zero_idxs"
---

# `deepxube.domains.npuzzle.NPuzzle.__init__`

**File:** [deepxube/domains/npuzzle.py:68](../../../../deepxube/domains/npuzzle.py#L68)
**Class:** `NPuzzle`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, dim: int = 4)
```

## Docstring

Build the solved goal tiles, precompute the swap-zero index table, and initialise 4 fixed actions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `dim` | `int` | `4` |

## Returns

*(Not annotated.)*

## Calls

- `np.concatenate` → `func:numpy.concatenate` (lines: 82)
- `np.arange` → `func:numpy.arange` (lines: 82)
- `self._get_swap_zero_idxs` → `func:deepxube.domains.npuzzle.NPuzzle._get_swap_zero_idxs` (lines: 85)
- `NPAction` → `func:deepxube.domains.npuzzle.NPAction` (lines: 88)

### Unresolved
- `super().__init__` (lines: 70)
- `super` (lines: 70)
- `np.concatenate((np.arange(1, self.dim * self.dim), [0])).astype` (lines: 82)
- `range` (lines: 88)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.actions`
- `self.dim`
- `self.dtype`
- `self.goal_tiles`
- `self.num_actions`
- `self.num_tiles`
- `self.swap_zero_idxs`

**Reads:**
- `self.actions`
- `self.dim`
- `self.dtype`
- `self.goal_tiles`
- `self.num_actions`
- `self.num_tiles`
- `self.swap_zero_idxs`

## Source

```python
    def __init__(self, dim: int = 4):
        """ Build the solved goal tiles, precompute the swap-zero index table, and initialise 4 fixed actions. """
        super().__init__()

        self.dim: int = dim
        self.dtype: type
        if self.dim <= 15:
            self.dtype = np.uint8
        else:
            self.dtype = np.int_

        self.num_tiles: int = dim ** 2

        # Solved state
        self.goal_tiles: NDArray[int_t] = np.concatenate((np.arange(1, self.dim * self.dim), [0])).astype(self.dtype)

        # Next state ops
        self.swap_zero_idxs: NDArray[int_t] = self._get_swap_zero_idxs(self.dim)

        self.num_actions: int = 4
        self.actions: List[NPAction] = [NPAction(x) for x in range(self.num_actions)]
```
