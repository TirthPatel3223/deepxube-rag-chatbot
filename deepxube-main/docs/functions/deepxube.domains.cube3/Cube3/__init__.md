---
id: "func:deepxube.domains.cube3.Cube3.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.cube3.Cube3.__init__"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 519
line_end: 538
class: "Cube3"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [521]
  - target: null
    expr: "super"
    call_sites: [521]
  - target: null
    expr: "len"
    call_sites: [524]
  - target: null
    expr: "(np.arange(0, self.num_stickers, 1, dtype=np.uint8) // self.cube_len ** 2).astype"
    call_sites: [528]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [528]
  - target: "func:deepxube.domains.cube3._get_adj"
    expr: "_get_adj"
    call_sites: [535]
  - target: "func:deepxube.domains.cube3.Cube3._compute_rotation_idxs"
    expr: "self._compute_rotation_idxs"
    call_sites: [537]
  - target: "func:deepxube.domains.cube3.Cube3Action"
    expr: "Cube3Action"
    call_sites: [538]
  - target: null
    expr: "range"
    call_sites: [538]
raises: []
reads_attrs:
  - "self.actions"
  - "self.adj_faces"
  - "self.atomic_actions"
  - "self.cube_len"
  - "self.goal_colors"
  - "self.num_actions"
  - "self.num_colors"
  - "self.num_stickers"
  - "self.rotate_idxs_new"
  - "self.rotate_idxs_old"
writes_attrs:
  - "self.actions"
  - "self.adj_faces"
  - "self.cube_len"
  - "self.goal_colors"
  - "self.num_actions"
  - "self.num_colors"
  - "self.num_stickers"
  - "self.rotate_idxs_new"
  - "self.rotate_idxs_old"
---

# `deepxube.domains.cube3.Cube3.__init__`

**File:** [deepxube/domains/cube3.py:519](../../../../deepxube/domains/cube3.py#L519)
**Class:** `Cube3`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self) -> None
```

## Docstring

Precompute the solved colour array and per-move sticker-index permutation tables. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

- `np.arange` → `func:numpy.arange` (lines: 528)
- `_get_adj` → `func:deepxube.domains.cube3._get_adj` (lines: 535)
- `self._compute_rotation_idxs` → `func:deepxube.domains.cube3.Cube3._compute_rotation_idxs` (lines: 537)
- `Cube3Action` → `func:deepxube.domains.cube3.Cube3Action` (lines: 538)

### Unresolved
- `super().__init__` (lines: 521)
- `super` (lines: 521)
- `len` (lines: 524)
- `(np.arange(0, self.num_stickers, 1, dtype=np.uint8) // self.cube_len ** 2).astype` (lines: 528)
- `range` (lines: 538)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.actions`
- `self.adj_faces`
- `self.cube_len`
- `self.goal_colors`
- `self.num_actions`
- `self.num_colors`
- `self.num_stickers`
- `self.rotate_idxs_new`
- `self.rotate_idxs_old`

**Reads:**
- `self.actions`
- `self.adj_faces`
- `self.atomic_actions`
- `self.cube_len`
- `self.goal_colors`
- `self.num_actions`
- `self.num_colors`
- `self.num_stickers`
- `self.rotate_idxs_new`
- `self.rotate_idxs_old`

## Source

```python
    def __init__(self) -> None:
        """ Precompute the solved colour array and per-move sticker-index permutation tables. """
        super().__init__()
        self.cube_len: int = 3
        self.num_colors: int = 6
        self.num_actions = len(self.atomic_actions)
        self.num_stickers: int = self.num_colors * (self.cube_len ** 2)

        # solved state
        self.goal_colors: NDArray[np.uint8] = (np.arange(0, self.num_stickers, 1,
                                                         dtype=np.uint8) // (self.cube_len ** 2)).astype(np.uint8)

        # get idxs changed for moves
        self.rotate_idxs_new: Dict[str, NDArray[np.int_]]
        self.rotate_idxs_old: Dict[str, NDArray[np.int_]]

        self.adj_faces: Dict[int, NDArray[np.int_]] = _get_adj()

        self.rotate_idxs_new, self.rotate_idxs_old = self._compute_rotation_idxs(self.cube_len, self.atomic_actions)
        self.actions: List[Cube3Action] = [Cube3Action(x) for x in range(self.num_actions)]
```
