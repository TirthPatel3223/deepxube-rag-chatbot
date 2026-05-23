---
id: "class:deepxube.domains.sokoban.SkAction"
kind: "class"
name: "SkAction"
qualified_name: "deepxube.domains.sokoban.SkAction"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 63
line_end: 74
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Action"
    resolved_id: null
methods:
  - "func:deepxube.domains.sokoban.SkAction.__init__"
  - "func:deepxube.domains.sokoban.SkAction.__hash__"
  - "func:deepxube.domains.sokoban.SkAction.__eq__"
attributes:
  - name: "self.action"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.sokoban.SkAction`

**File:** [deepxube/domains/sokoban.py:63](../../../deepxube/domains/sokoban.py#L63)
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

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.action` | — | __init__ |

## Source

```python
class SkAction(Action):
    """ Action: integer index (0=up, 1=down, 2=left, 3=right). """
    def __init__(self, action: int):
        self.action = action

    def __hash__(self) -> int:
        return self.action

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SkAction):
            return self.action == other.action
        return NotImplemented
```
