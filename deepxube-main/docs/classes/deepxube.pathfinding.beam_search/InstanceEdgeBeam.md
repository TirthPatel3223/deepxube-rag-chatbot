---
id: "class:deepxube.pathfinding.beam_search.InstanceEdgeBeam"
kind: "class"
name: "InstanceEdgeBeam"
qualified_name: "deepxube.pathfinding.beam_search.InstanceEdgeBeam"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 138
line_end: 153
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "InstanceEdge"
    resolved_id: null
  - name: "InstanceBeam"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.InstanceEdgeBeam.__init__"
  - "func:deepxube.pathfinding.beam_search.InstanceEdgeBeam.filter_popped_nodes"
  - "func:deepxube.pathfinding.beam_search.InstanceEdgeBeam.push_pop_edges"
attributes:
  - name: "self.beam_edges"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.InstanceEdgeBeam`

**File:** [deepxube/pathfinding/beam_search.py:138](../../../deepxube/pathfinding/beam_search.py#L138)
**Abstract:** no

## Docstring

Edge-driven beam instance: beam selects from edges (action probabilities or Q-values). 

## Inheritance

**Direct bases:**
- `InstanceEdge`
- `InstanceBeam`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `filter_popped_nodes` *(trivial, skipped)*
- `push_pop_edges`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.beam_edges` | — | __init__ |

## Source

```python
class InstanceEdgeBeam(InstanceEdge, InstanceBeam):
    """ Edge-driven beam instance: beam selects from edges (action probabilities or Q-values). """

    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise plus an empty list to hold currently-selected edges. """
        super().__init__(root_node, inst_info)
        self.beam_edges: List[EdgeQ] = []

    def filter_popped_nodes(self, nodes: List[Node]) -> List[Node]:
        """ No filtering — keep all popped nodes. """
        return nodes

    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Pick the beam from candidate edges by their logits. """
        next_idxs: List[int] = self.select_idxs_from_logits(costs)
        return [edges[idx] for idx in next_idxs]
```
