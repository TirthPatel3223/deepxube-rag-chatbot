---
id: "class:deepxube.domains.lightsout.LOAction"
kind: "class"
name: "LOAction"
qualified_name: "deepxube.domains.lightsout.LOAction"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 42
line_end: 54
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Action"
    resolved_id: null
methods:
  - "func:deepxube.domains.lightsout.LOAction.__init__"
  - "func:deepxube.domains.lightsout.LOAction.__hash__"
  - "func:deepxube.domains.lightsout.LOAction.__eq__"
attributes:
  - name: "self.action"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.lightsout.LOAction`

**File:** [deepxube/domains/lightsout.py:42](../../../deepxube/domains/lightsout.py#L42)
**Abstract:** no

## Docstring

Action: index of the tile to toggle (toggles that tile and its cardinal neighbours). 

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
class LOAction(Action):
    """ Action: index of the tile to toggle (toggles that tile and its cardinal neighbours). """

    def __init__(self, action: int):
        self.action = action

    def __hash__(self) -> int:
        return self.action

    def __eq__(self, other: object) -> bool:
        if isinstance(other, LOAction):
            return self.action == other.action
        return NotImplemented
```
