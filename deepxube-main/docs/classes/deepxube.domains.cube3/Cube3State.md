---
id: "class:deepxube.domains.cube3.Cube3State"
kind: "class"
name: "Cube3State"
qualified_name: "deepxube.domains.cube3.Cube3State"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 16
line_end: 33
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "State"
    resolved_id: null
methods:
  - "func:deepxube.domains.cube3.Cube3State.__init__"
  - "func:deepxube.domains.cube3.Cube3State.__hash__"
  - "func:deepxube.domains.cube3.Cube3State.__eq__"
attributes:
  - name: "self.colors"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.hash"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.cube3.Cube3State`

**File:** [deepxube/domains/cube3.py:16](../../../deepxube/domains/cube3.py#L16)
**Abstract:** no

## Docstring

State: flat uint8 array of 54 sticker colour indices (6 faces × 9 stickers). 

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
| `self.colors` | — | __init__ |
| `self.hash` | — | __init__ |

## Source

```python
class Cube3State(State):
    """ State: flat uint8 array of 54 sticker colour indices (6 faces × 9 stickers). """
    __slots__ = ['colors', 'hash']

    def __init__(self, colors: NDArray[np.uint8]) -> None:
        self.colors: NDArray[np.uint8] = colors
        self.hash: Optional[int] = None

    def __hash__(self) -> int:
        """ :return: Hash of the colour byte representation. """
        if self.hash is None:
            self.hash = hash(self.colors.tobytes())
        return self.hash

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Cube3State):
            return np.array_equal(self.colors, other.colors)
        return NotImplemented
```
