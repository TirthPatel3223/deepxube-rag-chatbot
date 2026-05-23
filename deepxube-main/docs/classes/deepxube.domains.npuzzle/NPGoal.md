---
id: "class:deepxube.domains.npuzzle.NPGoal"
kind: "class"
name: "NPGoal"
qualified_name: "deepxube.domains.npuzzle.NPGoal"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 39
line_end: 43
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Goal"
    resolved_id: null
methods:
  - "func:deepxube.domains.npuzzle.NPGoal.__init__"
attributes:
  - name: "self.tiles"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.npuzzle.NPGoal`

**File:** [deepxube/domains/npuzzle.py:39](../../../deepxube/domains/npuzzle.py#L39)
**Abstract:** no

## Docstring

Goal: target tile configuration (value ``num_tiles`` acts as a wildcard). 

## Inheritance

**Direct bases:**
- `Goal`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.tiles` | — | __init__ |

## Source

```python
class NPGoal(Goal):
    """ Goal: target tile configuration (value ``num_tiles`` acts as a wildcard). """

    def __init__(self, tiles: NDArray[int_t]):
        self.tiles: NDArray[int_t] = tiles
```
