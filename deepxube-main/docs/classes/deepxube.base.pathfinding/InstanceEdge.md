---
id: "class:deepxube.base.pathfinding.InstanceEdge"
kind: "class"
name: "InstanceEdge"
qualified_name: "deepxube.base.pathfinding.InstanceEdge"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 419
line_end: 430
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
  - "func:deepxube.base.pathfinding.InstanceEdge.filter_popped_nodes"
  - "func:deepxube.base.pathfinding.InstanceEdge.push_pop_edges"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.InstanceEdge`

**File:** [deepxube/base/pathfinding.py:419](../../../deepxube/base/pathfinding.py#L419)
**Abstract:** yes

## Docstring

Instance variant where the open set holds edges (used by edge-driven pathfinders, e.g. Q*). 

## Inheritance

**Direct bases:**
- `Instance`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `filter_popped_nodes` *(trivial, skipped)*
- `push_pop_edges` *(trivial, skipped)*

## Source

```python
class InstanceEdge(Instance, ABC):
    """ Instance variant where the open set holds edges (used by edge-driven pathfinders, e.g. Q*). """

    @abstractmethod
    def filter_popped_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Subclass hook: filter popped nodes before edge expansion. """
        pass

    @abstractmethod
    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Push edges with their costs, pop the next frontier edges. """
        pass
```
