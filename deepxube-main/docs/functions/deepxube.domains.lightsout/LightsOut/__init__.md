---
id: "func:deepxube.domains.lightsout.LightsOut.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.lightsout.LightsOut.__init__"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 63
line_end: 82
class: "LightsOut"
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
    default: "7"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [65]
  - target: null
    expr: "super"
    call_sites: [65]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [69, 82]
  - target: null
    expr: "range"
    call_sites: [70, 81]
  - target: null
    expr: "int"
    call_sites: [71]
  - target: "func:numpy.floor"
    expr: "np.floor"
    call_sites: [71]
  - target: "func:deepxube.domains.lightsout.LOAction"
    expr: "LOAction"
    call_sites: [81]
raises: []
reads_attrs:
  - "self.actions_fixed"
  - "self.dim"
  - "self.goal_np"
  - "self.move_matrix"
  - "self.num_tiles"
writes_attrs:
  - "self.actions_fixed"
  - "self.dim"
  - "self.goal_np"
  - "self.move_matrix"
  - "self.num_tiles"
---

# `deepxube.domains.lightsout.LightsOut.__init__`

**File:** [deepxube/domains/lightsout.py:63](../../../../deepxube/domains/lightsout.py#L63)
**Class:** `LightsOut`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, dim: int = 7)
```

## Docstring

Build the move matrix mapping each tile to the 5 indices it affects (itself + up to 4 neighbours). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `dim` | `int` | `7` |

## Returns

*(Not annotated.)*

## Calls

- `np.zeros` → `func:numpy.zeros` (lines: 69, 82)
- `np.floor` → `func:numpy.floor` (lines: 71)
- `LOAction` → `func:deepxube.domains.lightsout.LOAction` (lines: 81)

### Unresolved
- `super().__init__` (lines: 65)
- `super` (lines: 65)
- `range` (lines: 70, 81)
- `int` (lines: 71)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.actions_fixed`
- `self.dim`
- `self.goal_np`
- `self.move_matrix`
- `self.num_tiles`

**Reads:**
- `self.actions_fixed`
- `self.dim`
- `self.goal_np`
- `self.move_matrix`
- `self.num_tiles`

## Source

```python
    def __init__(self, dim: int = 7):
        """ Build the move matrix mapping each tile to the 5 indices it affects (itself + up to 4 neighbours). """
        super().__init__()
        self.dim: int = dim
        self.num_tiles: int = self.dim ** 2

        self.move_matrix: NDArray = np.zeros((self.num_tiles, 5), dtype=np.int64)
        for move in range(self.num_tiles):
            x_pos = int(np.floor(move / self.dim))
            y_pos = move % self.dim

            right = move + self.dim if x_pos < (self.dim-1) else move
            left = move - self.dim if x_pos > 0 else move
            up = move + 1 if y_pos < (self.dim - 1) else move
            down = move - 1 if y_pos > 0 else move

            self.move_matrix[move] = [move, right, left, up, down]

        self.actions_fixed: List[LOAction] = [LOAction(x) for x in range(self.num_tiles)]
        self.goal_np: NDArray = np.zeros(self.num_tiles, dtype=np.uint8)
```
