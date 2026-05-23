---
id: "class:deepxube.pathfinding.beam_search.BeamSearchHeurEdge"
kind: "class"
name: "BeamSearchHeurEdge"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurEdge"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 217
line_end: 237
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "BeamSearch[D, FNsHQ, InstanceEdgeBeam]"
    resolved_id: null
  - name: "PathFindEdge[D, FNsHQ, InstanceEdgeBeam]"
    resolved_id: null
  - name: "PathFindSetHeurQ[D, FNsHQ, InstanceEdgeBeam]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurEdge.make_instances"
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurEdge._compute_costs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurEdge`

**File:** [deepxube/pathfinding/beam_search.py:217](../../../deepxube/pathfinding/beam_search.py#L217)
**Abstract:** yes

## Docstring

Abstract edge-driven beam search guided by a Q heuristic. Logits = -q_val (lower Q = worse beam candidate). 

## Inheritance

**Direct bases:**
- `BeamSearch[D, FNsHQ, InstanceEdgeBeam]`
- `PathFindEdge[D, FNsHQ, InstanceEdgeBeam]`
- `PathFindSetHeurQ[D, FNsHQ, InstanceEdgeBeam]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `make_instances`
- `_compute_costs`

## Source

```python
class BeamSearchHeurEdge(BeamSearch[D, FNsHQ, InstanceEdgeBeam], PathFindEdge[D, FNsHQ, InstanceEdgeBeam],
                         PathFindSetHeurQ[D, FNsHQ, InstanceEdgeBeam], ABC):
    """ Abstract edge-driven beam search guided by a Q heuristic. Logits = -q_val (lower Q = worse beam candidate). """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeBeam]:
        """ Build edge-beam instances from (state, goal) pairs. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, True)
        return self._construct_instances(InstanceEdgeBeam, nodes_root, inst_infos, beam_size, temp, eps)

    def _compute_costs(self, instances: List[InstanceEdgeBeam], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ :return: Per-instance logits = -q_val; higher is better. """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for edges in edges_by_inst:
            logits: List[float] = [-edge.q_val for edge in edges]
            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst
```
