---
id: "class:deepxube.base.pathfinding.EdgeQ"
kind: "class"
name: "EdgeQ"
qualified_name: "deepxube.base.pathfinding.EdgeQ"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 138
line_end: 147
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.base.pathfinding.EdgeQ.__init__"
attributes:
  - name: "self.action"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.node"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.q_val"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.EdgeQ`

**File:** [deepxube/base/pathfinding.py:138](../../../deepxube/base/pathfinding.py#L138)
**Abstract:** no

## Docstring

Lightweight (parent-node, action, q_val) triple used by edge-based pathfinders. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.action` | — | __init__ |
| `self.node` | — | __init__ |
| `self.q_val` | — | __init__ |

## Source

```python
class EdgeQ:
    """ Lightweight (parent-node, action, q_val) triple used by edge-based pathfinders. """

    __slots__ = ['node', 'action', 'q_val']

    def __init__(self, node: Node, action: Action, q_val: float):
        """ Store the source node, the action, and its Q-value. """
        self.node: Node = node
        self.action: Action = action
        self.q_val: float = q_val
```
