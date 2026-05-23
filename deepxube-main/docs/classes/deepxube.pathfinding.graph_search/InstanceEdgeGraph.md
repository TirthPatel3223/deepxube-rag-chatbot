---
id: "class:deepxube.pathfinding.graph_search.InstanceEdgeGraph"
kind: "class"
name: "InstanceEdgeGraph"
qualified_name: "deepxube.pathfinding.graph_search.InstanceEdgeGraph"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 164
line_end: 174
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "InstanceEdge"
    resolved_id: null
  - name: "InstanceGraph[EdgeQ]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.InstanceEdgeGraph.filter_popped_nodes"
  - "func:deepxube.pathfinding.graph_search.InstanceEdgeGraph.push_pop_edges"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.InstanceEdgeGraph`

**File:** [deepxube/pathfinding/graph_search.py:164](../../../deepxube/pathfinding/graph_search.py#L164)
**Abstract:** no

## Docstring

Edge-driven graph-search instance; closed-dict check is applied to nodes after they are popped. 

## Inheritance

**Direct bases:**
- `InstanceEdge`
- `InstanceGraph[EdgeQ]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `filter_popped_nodes`
- `push_pop_edges`

## Source

```python
class InstanceEdgeGraph(InstanceEdge, InstanceGraph[EdgeQ]):
    """ Edge-driven graph-search instance; closed-dict check is applied to nodes after they are popped. """

    def filter_popped_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Filter popped nodes through the closed dict. """
        return self._check_closed(nodes)

    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Push edges onto the open heap, then pop the next best batch. """
        self._push_to_open(edges, costs)
        return self._pop_from_open()
```
