---
id: "class:deepxube.domains.grid.GridGoal"
kind: "class"
name: "GridGoal"
qualified_name: "deepxube.domains.grid.GridGoal"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 42
line_end: 47
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Goal"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.GridGoal.__init__"
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

# `deepxube.domains.grid.GridGoal`

**File:** [deepxube/domains/grid.py:42](../../../deepxube/domains/grid.py#L42)
**Abstract:** no

## Docstring

Goal: target position ``(robot_x, robot_y)`` on the grid. 

## Inheritance

**Direct bases:**
- `Goal`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.robot_x` | — | __init__ |
| `self.robot_y` | — | __init__ |

## Source

```python
class GridGoal(Goal):
    """ Goal: target position ``(robot_x, robot_y)`` on the grid. """

    def __init__(self, robot_x: int, robot_y: int):
        self.robot_x: int = robot_x
        self.robot_y: int = robot_y
```
