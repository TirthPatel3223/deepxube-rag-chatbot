---
id: "class:deepxube.pathfinding.graph_search.GraphSearchHeurNode"
kind: "class"
name: "GraphSearchHeurNode"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurNode"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 177
line_end: 199
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GraphSearch[D, FNsHV, InstanceNodeGraph]"
    resolved_id: null
  - name: "PathFindNode[D, FNsHV, InstanceNodeGraph]"
    resolved_id: null
  - name: "PathFindSetHeurV[D, FNsHV, InstanceNodeGraph]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurNode.make_instances"
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurNode._compute_costs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurNode`

**File:** [deepxube/pathfinding/graph_search.py:177](../../../deepxube/pathfinding/graph_search.py#L177)
**Abstract:** yes

## Docstring

Abstract node-driven graph search using a V heuristic; cost = weight * path_cost + heuristic. 

## Inheritance

**Direct bases:**
- `GraphSearch[D, FNsHV, InstanceNodeGraph]`
- `PathFindNode[D, FNsHV, InstanceNodeGraph]`
- `PathFindSetHeurV[D, FNsHV, InstanceNodeGraph]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `make_instances`
- `_compute_costs`

## Source

```python
class GraphSearchHeurNode(GraphSearch[D, FNsHV, InstanceNodeGraph], PathFindNode[D, FNsHV, InstanceNodeGraph],
                          PathFindSetHeurV[D, FNsHV, InstanceNodeGraph], ABC):
    """ Abstract node-driven graph search using a V heuristic; cost = weight * path_cost + heuristic. """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeGraph]:
        """ Build node-graph instances, optionally computing root heuristic values. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, compute_root_vals)
        return self._construct_instances(InstanceNodeGraph, nodes_root, inst_infos, beam_size, weight, eps)

    def _compute_costs(self, instances: List[InstanceNodeGraph], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ :return: Per-instance costs = weight * path_cost + heuristic (lower = higher priority). """
        start_time = time.time()
        nodes_c_flat: List[Node] = misc_utils.flatten(nodes_by_inst)[0]
        weights, split_idxs = misc_utils.flatten([[instance.weight] * len(nodes_c) for instance, nodes_c in zip(instances, nodes_by_inst, strict=True)])
        path_costs: List[float] = [node.path_cost for node in nodes_c_flat]
        heuristics: List[float] = [node.heuristic for node in nodes_c_flat]
        costs_flat: List[float] = ((np.array(weights) * np.array(path_costs)) + np.array(heuristics)).tolist()
        costs_by_inst: List[List[float]] = misc_utils.unflatten(costs_flat, split_idxs)

        self.times.record_time("cost", time.time() - start_time)

        return costs_by_inst
```
