---
id: "class:deepxube.domains.sokoban.SkState"
kind: "class"
name: "SkState"
qualified_name: "deepxube.domains.sokoban.SkState"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 23
line_end: 52
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "State"
    resolved_id: null
methods:
  - "func:deepxube.domains.sokoban.SkState.__init__"
  - "func:deepxube.domains.sokoban.SkState.__hash__"
  - "func:deepxube.domains.sokoban.SkState.__eq__"
attributes:
  - name: "self.agent"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.boxes"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.hash"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.walls"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.sokoban.SkState`

**File:** [deepxube/domains/sokoban.py:23](../../../deepxube/domains/sokoban.py#L23)
**Abstract:** no

## Docstring

State: agent position, binary box map, and binary wall map for a Sokoban board. 

## Inheritance

**Direct bases:**
- `State`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` — *(no docstring)*
- `__hash__`
- `__eq__` — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.agent` | — | __init__ |
| `self.boxes` | — | __init__ |
| `self.hash` | — | __init__ |
| `self.walls` | — | __init__ |

## Source

```python
class SkState(State):
    """ State: agent position, binary box map, and binary wall map for a Sokoban board. """
    __slots__ = ['agent', 'boxes', 'walls', 'hash']

    def __init__(self, agent: NDArray[np.int_], boxes: NDArray[np.uint8], walls: NDArray[np.uint8]):
        self.agent: NDArray[np.int_] = agent
        self.boxes: NDArray[np.uint8] = boxes
        self.walls: NDArray[np.uint8] = walls

        self.hash: Optional[int] = None

    def __hash__(self) -> int:
        """ :return: Hash of the concatenated agent + boxes + walls byte representation. """
        if self.hash is None:
            boxes_flat = self.boxes.flatten()
            walls_flat = self.walls.flatten()
            state: NDArray[np.int_] = np.concatenate((self.agent, boxes_flat.astype(int), walls_flat.astype(int)), axis=0)

            self.hash = hash(state.tobytes())

        return self.hash

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SkState):
            agents_eq: bool = np.array_equal(self.agent, other.agent)
            boxes_eq: bool = np.array_equal(self.boxes, other.boxes)
            walls_eq: bool = np.array_equal(self.walls, other.walls)

            return agents_eq and boxes_eq and walls_eq
        return NotImplemented
```
