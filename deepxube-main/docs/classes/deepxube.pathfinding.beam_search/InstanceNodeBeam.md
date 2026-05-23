---
id: "class:deepxube.pathfinding.beam_search.InstanceNodeBeam"
kind: "class"
name: "InstanceNodeBeam"
qualified_name: "deepxube.pathfinding.beam_search.InstanceNodeBeam"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 125
line_end: 135
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "InstanceNode"
    resolved_id: null
  - name: "InstanceBeam"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.InstanceNodeBeam.filter_expanded_nodes"
  - "func:deepxube.pathfinding.beam_search.InstanceNodeBeam.push_pop_nodes"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.InstanceNodeBeam`

**File:** [deepxube/pathfinding/beam_search.py:125](../../../deepxube/pathfinding/beam_search.py#L125)
**Abstract:** no

## Docstring

Node-driven beam instance: keeps the top ``beam_size`` expanded children. 

## Inheritance

**Direct bases:**
- `InstanceNode`
- `InstanceBeam`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `filter_expanded_nodes` *(trivial, skipped)*
- `push_pop_nodes`

## Source

```python
class InstanceNodeBeam(InstanceNode, InstanceBeam):
    """ Node-driven beam instance: keeps the top ``beam_size`` expanded children. """

    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ No filtering — keep all expanded children. """
        return nodes

    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Pick the beam from the expanded nodes by their costs (logits). """
        next_idxs: List[int] = self.select_idxs_from_logits(costs)
        return [nodes[idx] for idx in next_idxs]
```
