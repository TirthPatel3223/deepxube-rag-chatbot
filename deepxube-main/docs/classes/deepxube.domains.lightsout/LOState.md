---
id: "class:deepxube.domains.lightsout.LOState"
kind: "class"
name: "LOState"
qualified_name: "deepxube.domains.lightsout.LOState"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 14
line_end: 32
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "State"
    resolved_id: null
methods:
  - "func:deepxube.domains.lightsout.LOState.__init__"
  - "func:deepxube.domains.lightsout.LOState.__hash__"
  - "func:deepxube.domains.lightsout.LOState.__eq__"
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

# `deepxube.domains.lightsout.LOState`

**File:** [deepxube/domains/lightsout.py:14](../../../deepxube/domains/lightsout.py#L14)
**Abstract:** no

## Docstring

State: binary tile configuration as a flat uint8 array (0=off, 1=on). 

## Inheritance

**Direct bases:**
- `State`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `__hash__`
- `__eq__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.hash` | — | __init__ |
| `self.tiles` | — | __init__ |

## Source

```python
class LOState(State):
    """ State: binary tile configuration as a flat uint8 array (0=off, 1=on). """
    __slots__ = ['tiles', 'hash']

    def __init__(self, tiles: NDArray[np.uint8]):
        self.tiles: NDArray[np.uint8] = tiles
        self.hash: Optional[int] = None

    def __hash__(self) -> int:
        """ :return: Hash of the tile bytes. """
        if self.hash is None:
            self.hash = hash(self.tiles.tobytes())

        return self.hash

    def __eq__(self, other: object) -> bool:
        if isinstance(other, LOState):
            return np.array_equal(self.tiles, other.tiles)
        return NotImplemented
```
