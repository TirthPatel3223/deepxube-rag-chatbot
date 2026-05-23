---
id: "class:deepxube.base.pathfinding.InstanceNode"
kind: "class"
name: "InstanceNode"
qualified_name: "deepxube.base.pathfinding.InstanceNode"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 402
line_end: 413
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Instance"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.InstanceNode.filter_expanded_nodes"
  - "func:deepxube.base.pathfinding.InstanceNode.push_pop_nodes"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.InstanceNode`

**File:** [deepxube/base/pathfinding.py:402](../../../deepxube/base/pathfinding.py#L402)
**Abstract:** yes

## Docstring

Instance variant where the open set holds nodes (used by node-driven pathfinders). 

## Inheritance

**Direct bases:**
- `Instance`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `filter_expanded_nodes` *(trivial, skipped)*
- `push_pop_nodes` *(trivial, skipped)*

## Source

```python
class InstanceNode(Instance, ABC):
    """ Instance variant where the open set holds nodes (used by node-driven pathfinders). """

    @abstractmethod
    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Subclass hook: filter freshly-expanded nodes (e.g. CLOSED-list duplicate suppression). """
        pass

    @abstractmethod
    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Push children with their costs, pop the next frontier; return the popped nodes. """
        pass
```
