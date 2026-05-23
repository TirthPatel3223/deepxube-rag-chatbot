---
id: "class:deepxube.domains.npuzzle.NPAction"
kind: "class"
name: "NPAction"
qualified_name: "deepxube.domains.npuzzle.NPAction"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 46
line_end: 58
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Action"
    resolved_id: null
methods:
  - "func:deepxube.domains.npuzzle.NPAction.__init__"
  - "func:deepxube.domains.npuzzle.NPAction.__hash__"
  - "func:deepxube.domains.npuzzle.NPAction.__eq__"
attributes:
  - name: "self.action"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.npuzzle.NPAction`

**File:** [deepxube/domains/npuzzle.py:46](../../../deepxube/domains/npuzzle.py#L46)
**Abstract:** no

## Docstring

Action: slide direction index (0=U, 1=D, 2=L, 3=R — moves the blank tile). 

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
class NPAction(Action):
    """ Action: slide direction index (0=U, 1=D, 2=L, 3=R — moves the blank tile). """

    def __init__(self, action: int):
        self.action = action

    def __hash__(self) -> int:
        return self.action

    def __eq__(self, other: object) -> bool:
        if isinstance(other, NPAction):
            return self.action == other.action
        return NotImplemented
```
