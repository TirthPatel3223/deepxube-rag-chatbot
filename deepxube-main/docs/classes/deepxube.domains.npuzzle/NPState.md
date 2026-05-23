---
id: "class:deepxube.domains.npuzzle.NPState"
kind: "class"
name: "NPState"
qualified_name: "deepxube.domains.npuzzle.NPState"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 20
line_end: 36
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "State"
    resolved_id: null
methods:
  - "func:deepxube.domains.npuzzle.NPState.__init__"
  - "func:deepxube.domains.npuzzle.NPState.__hash__"
  - "func:deepxube.domains.npuzzle.NPState.__eq__"
attributes:
  - name: "self.hash"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.tiles"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.npuzzle.NPState`

**File:** [deepxube/domains/npuzzle.py:20](../../../deepxube/domains/npuzzle.py#L20)
**Abstract:** no

## Docstring

State: tile configuration as a flat integer array (0 = blank tile). 

## Inheritance

**Direct bases:**
- `State`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `__hash__` *(trivial, skipped)* — *(no docstring)*
- `__eq__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.hash` | — | __init__ |
| `self.tiles` | — | __init__ |

## Source

```python
class NPState(State):
    """ State: tile configuration as a flat integer array (0 = blank tile). """
    __slots__ = ['tiles', 'hash']

    def __init__(self, tiles: NDArray[int_t]):
        self.tiles: NDArray[int_t] = tiles
        self.hash: Optional[int] = None

    def __hash__(self) -> int:
        if self.hash is None:
            self.hash = hash(self.tiles.tobytes())
        return self.hash

    def __eq__(self, other: object) -> bool:
        if isinstance(other, NPState):
            return np.array_equal(self.tiles, other.tiles)
        return NotImplemented
```
