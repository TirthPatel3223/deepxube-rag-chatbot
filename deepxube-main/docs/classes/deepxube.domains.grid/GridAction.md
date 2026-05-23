---
id: "class:deepxube.domains.grid.GridAction"
kind: "class"
name: "GridAction"
qualified_name: "deepxube.domains.grid.GridAction"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 50
line_end: 65
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Action"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.GridAction.__init__"
  - "func:deepxube.domains.grid.GridAction.__hash__"
  - "func:deepxube.domains.grid.GridAction.__eq__"
  - "func:deepxube.domains.grid.GridAction.__repr__"
attributes:
  - name: "self.action"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.grid.GridAction`

**File:** [deepxube/domains/grid.py:50](../../../deepxube/domains/grid.py#L50)
**Abstract:** no

## Docstring

Action: integer index (0=up, 1=down, 2=left, 3=right). 

## Inheritance

**Direct bases:**
- `Action`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `__hash__` *(trivial, skipped)* — *(no docstring)*
- `__eq__` *(trivial, skipped)* — *(no docstring)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.action` | — | __init__ |

## Source

```python
class GridAction(Action):
    """ Action: integer index (0=up, 1=down, 2=left, 3=right). """

    def __init__(self, action: int):
        self.action = action

    def __hash__(self) -> int:
        return self.action

    def __eq__(self, other: object) -> bool:
        if isinstance(other, GridAction):
            return self.action == other.action
        return NotImplemented

    def __repr__(self) -> str:
        return f"{self.action}"
```
