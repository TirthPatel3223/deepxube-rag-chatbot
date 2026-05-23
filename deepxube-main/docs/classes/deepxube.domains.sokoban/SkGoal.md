---
id: "class:deepxube.domains.sokoban.SkGoal"
kind: "class"
name: "SkGoal"
qualified_name: "deepxube.domains.sokoban.SkGoal"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 55
line_end: 60
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Goal"
    resolved_id: null
methods:
  - "func:deepxube.domains.sokoban.SkGoal.__init__"
attributes:
  - name: "self.boxes"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.sokoban.SkGoal`

**File:** [deepxube/domains/sokoban.py:55](../../../deepxube/domains/sokoban.py#L55)
**Abstract:** no

## Docstring

Goal: target binary box map that boxes must match to solve the puzzle. 

## Inheritance

**Direct bases:**
- `Goal`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.boxes` | — | __init__ |

## Source

```python
class SkGoal(Goal):
    """ Goal: target binary box map that boxes must match to solve the puzzle. """
    __slots__ = ['boxes']

    def __init__(self, boxes: NDArray[np.uint8]):
        self.boxes: NDArray[np.uint8] = boxes
```
