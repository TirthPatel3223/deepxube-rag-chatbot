---
id: "class:deepxube.pathfinding.graph_search.InstanceNodeGraph"
kind: "class"
name: "InstanceNodeGraph"
qualified_name: "deepxube.pathfinding.graph_search.InstanceNodeGraph"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 147
line_end: 161
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "InstanceNode"
    resolved_id: null
  - name: "InstanceGraph[Node]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.InstanceNodeGraph.__init__"
  - "func:deepxube.pathfinding.graph_search.InstanceNodeGraph.filter_expanded_nodes"
  - "func:deepxube.pathfinding.graph_search.InstanceNodeGraph.push_pop_nodes"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.InstanceNodeGraph`

**File:** [deepxube/pathfinding/graph_search.py:147](../../../deepxube/pathfinding/graph_search.py#L147)
**Abstract:** no

## Docstring

Node-driven graph-search instance; pre-inserts the root into the closed dict at cost 0. 

## Inheritance

**Direct bases:**
- `InstanceNode`
- `InstanceGraph[Node]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `filter_expanded_nodes`
- `push_pop_nodes`

## Source

```python
class InstanceNodeGraph(InstanceNode, InstanceGraph[Node]):
    """ Node-driven graph-search instance; pre-inserts the root into the closed dict at cost 0. """

    def __init__(self, root_node: Node, inst_info: Any):
        super().__init__(root_node, inst_info)
        self.closed_dict[self.root_node.state] = 0.0

    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Filter expanded children through the closed dict; discard nodes that do not improve it. """
        return self._check_closed(nodes)

    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Push nodes onto the open heap, then pop the next best batch. """
        self._push_to_open(nodes, costs)
        return self._pop_from_open()
```
