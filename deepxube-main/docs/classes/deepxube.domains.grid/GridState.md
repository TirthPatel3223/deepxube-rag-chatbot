---
id: "class:deepxube.domains.grid.GridState"
kind: "class"
name: "GridState"
qualified_name: "deepxube.domains.grid.GridState"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 26
line_end: 39
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "State"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.GridState.__init__"
  - "func:deepxube.domains.grid.GridState.__hash__"
  - "func:deepxube.domains.grid.GridState.__eq__"
attributes:
  - name: "self.robot_x"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.robot_y"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.grid.GridState`

**File:** [deepxube/domains/grid.py:26](../../../deepxube/domains/grid.py#L26)
**Abstract:** no

## Docstring

State: robot position ``(robot_x, robot_y)`` on the grid. 

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
| `self.robot_x` | — | __init__ |
| `self.robot_y` | — | __init__ |

## Source

```python
class GridState(State):
    """ State: robot position ``(robot_x, robot_y)`` on the grid. """

    def __init__(self, robot_x: int, robot_y: int):
        self.robot_x: int = robot_x
        self.robot_y: int = robot_y

    def __hash__(self) -> int:
        return hash(self.robot_x + self.robot_y)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, GridState):
            return (self.robot_x == other.robot_x) and (self.robot_y == other.robot_y)
        return NotImplemented
```
