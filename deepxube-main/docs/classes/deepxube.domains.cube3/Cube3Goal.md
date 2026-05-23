---
id: "class:deepxube.domains.cube3.Cube3Goal"
kind: "class"
name: "Cube3Goal"
qualified_name: "deepxube.domains.cube3.Cube3Goal"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 36
line_end: 40
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Goal"
    resolved_id: null
methods:
  - "func:deepxube.domains.cube3.Cube3Goal.__init__"
attributes:
  - name: "self.colors"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.cube3.Cube3Goal`

**File:** [deepxube/domains/cube3.py:36](../../../deepxube/domains/cube3.py#L36)
**Abstract:** no

## Docstring

Goal: target flat colour array that the cube must match to be solved. 

## Inheritance

**Direct bases:**
- `Goal`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.colors` | — | __init__ |

## Source

```python
class Cube3Goal(Goal):
    """ Goal: target flat colour array that the cube must match to be solved. """

    def __init__(self, colors: NDArray[np.uint8]):
        self.colors: NDArray[np.uint8] = colors
```
