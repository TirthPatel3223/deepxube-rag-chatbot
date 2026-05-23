---
id: "class:deepxube.logic.logic_objects.VarNode"
kind: "class"
name: "VarNode"
qualified_name: "deepxube.logic.logic_objects.VarNode"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 53
line_end: 61
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.logic.logic_objects.VarNode.__init__"
  - "func:deepxube.logic.logic_objects.VarNode.add_neighbor"
attributes:
  - name: "self.neighbors"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.rep"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.logic.logic_objects.VarNode`

**File:** [deepxube/logic/logic_objects.py:53](../../../deepxube/logic/logic_objects.py#L53)
**Abstract:** no

## Docstring

Node in the clause variable graph used by ``Clause.__hash__``; holds a hash rep and a neighbour list. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `add_neighbor` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.neighbors` | — | __init__ |
| `self.rep` | — | __init__ |

## Source

```python
class VarNode:
    """ Node in the clause variable graph used by ``Clause.__hash__``; holds a hash rep and a neighbour list. """

    def __init__(self) -> None:
        self.rep: int = 0
        self.neighbors: List[VarNode] = []

    def add_neighbor(self, neighbor: 'VarNode') -> None:
        self.neighbors.append(neighbor)
```
