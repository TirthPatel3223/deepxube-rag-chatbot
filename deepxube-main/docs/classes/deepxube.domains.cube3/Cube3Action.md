---
id: "class:deepxube.domains.cube3.Cube3Action"
kind: "class"
name: "Cube3Action"
qualified_name: "deepxube.domains.cube3.Cube3Action"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 43
line_end: 55
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Action"
    resolved_id: null
methods:
  - "func:deepxube.domains.cube3.Cube3Action.__init__"
  - "func:deepxube.domains.cube3.Cube3Action.__hash__"
  - "func:deepxube.domains.cube3.Cube3Action.__eq__"
attributes:
  - name: "self.action"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.cube3.Cube3Action`

**File:** [deepxube/domains/cube3.py:43](../../../deepxube/domains/cube3.py#L43)
**Abstract:** no

## Docstring

Action: integer index into ``atomic_actions`` (0–11 for U/D/L/R/B/F × ±1). 

## Inheritance

**Direct bases:**
- `Action`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `__hash__` *(trivial, skipped)* — *(no docstring)*
- `__eq__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.action` | — | __init__ |

## Source

```python
class Cube3Action(Action):
    """ Action: integer index into ``atomic_actions`` (0–11 for U/D/L/R/B/F × ±1). """

    def __init__(self, action: int) -> None:
        self.action = action

    def __hash__(self) -> int:
        return self.action

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Cube3Action):
            return self.action == other.action
        return NotImplemented
```
