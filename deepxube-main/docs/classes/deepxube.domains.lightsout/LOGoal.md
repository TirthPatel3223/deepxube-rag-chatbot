---
id: "class:deepxube.domains.lightsout.LOGoal"
kind: "class"
name: "LOGoal"
qualified_name: "deepxube.domains.lightsout.LOGoal"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 35
line_end: 39
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Goal"
    resolved_id: null
methods:
  - "func:deepxube.domains.lightsout.LOGoal.__init__"
attributes:
  - name: "self.tiles"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.lightsout.LOGoal`

**File:** [deepxube/domains/lightsout.py:35](../../../deepxube/domains/lightsout.py#L35)
**Abstract:** no

## Docstring

Goal: target tile configuration (typically all-zeros = all off). 

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
class LOGoal(Goal):
    """ Goal: target tile configuration (typically all-zeros = all off). """

    def __init__(self, tiles: NDArray[np.uint8]):
        self.tiles: NDArray[np.uint8] = tiles
```
