---
id: "class:deepxube.pathfinding.graph_search.GraphSearchHeurEdge"
kind: "class"
name: "GraphSearchHeurEdge"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurEdge"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 202
line_end: 224
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GraphSearch[D, FNsHQ, InstanceEdgeGraph]"
    resolved_id: null
  - name: "PathFindEdge[D, FNsHQ, InstanceEdgeGraph]"
    resolved_id: null
  - name: "PathFindSetHeurQ[D, FNsHQ, InstanceEdgeGraph]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge.make_instances"
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge._compute_costs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurEdge`

**File:** [deepxube/pathfinding/graph_search.py:202](../../../deepxube/pathfinding/graph_search.py#L202)
**Abstract:** yes

## Docstring

Abstract edge-driven graph search using Q-values; cost = weight * node.path_cost + q_val. 

## Inheritance

**Direct bases:**
- `GraphSearch[D, FNsHQ, InstanceEdgeGraph]`
- `PathFindEdge[D, FNsHQ, InstanceEdgeGraph]`
- `PathFindSetHeurQ[D, FNsHQ, InstanceEdgeGraph]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `make_instances`
- `_compute_costs`

## Source

```python
class GraphSearchHeurEdge(GraphSearch[D, FNsHQ, InstanceEdgeGraph], PathFindEdge[D, FNsHQ, InstanceEdgeGraph],
                          PathFindSetHeurQ[D, FNsHQ, InstanceEdgeGraph], ABC):
    """ Abstract edge-driven graph search using Q-values; cost = weight * node.path_cost + q_val. """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       batch_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeGraph]:
        """ Build edge-graph instances from (state, goal) pairs. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, True)
        return self._construct_instances(InstanceEdgeGraph, nodes_root, inst_infos, batch_size, weight, eps)

    def _compute_costs(self, instances: List[InstanceEdgeGraph], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ :return: Per-instance costs = weight * node.path_cost + q_val (lower = higher priority). """
        start_time = time.time()
        edges_flat: List[EdgeQ] = misc_utils.flatten(edges_by_inst)[0]
        weights_flat, split_idxs = misc_utils.flatten([[instance.weight] * len(edges) for instance, edges in zip(instances, edges_by_inst, strict=True)])
        path_costs_flat: List[float] = [edge.node.path_cost for edge in edges_flat]
        qvals_flat: List[float] = [edge.q_val for edge in edges_flat]
        costs_flat: List[float] = ((np.array(weights_flat) * np.array(path_costs_flat)) + np.array(qvals_flat)).tolist()
        costs_by_inst: List[List[float]] = misc_utils.unflatten(costs_flat, split_idxs)

        self.times.record_time("cost", time.time() - start_time)

        return costs_by_inst
```
