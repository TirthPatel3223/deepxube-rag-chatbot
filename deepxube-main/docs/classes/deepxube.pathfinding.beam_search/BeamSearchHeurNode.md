---
id: "class:deepxube.pathfinding.beam_search.BeamSearchHeurNode"
kind: "class"
name: "BeamSearchHeurNode"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurNode"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 190
line_end: 214
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "BeamSearch[D, FNsHV, InstanceNodeBeam]"
    resolved_id: null
  - name: "PathFindNode[D, FNsHV, InstanceNodeBeam]"
    resolved_id: null
  - name: "PathFindSetHeurV[D, FNsHV, InstanceNodeBeam]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurNode.make_instances"
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurNode._compute_costs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurNode`

**File:** [deepxube/pathfinding/beam_search.py:190](../../../deepxube/pathfinding/beam_search.py#L190)
**Abstract:** yes

## Docstring

Abstract node-driven beam search guided by a value heuristic (V). Logits = -(transition_cost + heuristic). 

## Inheritance

**Direct bases:**
- `BeamSearch[D, FNsHV, InstanceNodeBeam]`
- `PathFindNode[D, FNsHV, InstanceNodeBeam]`
- `PathFindSetHeurV[D, FNsHV, InstanceNodeBeam]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `make_instances`
- `_compute_costs`

## Source

```python
class BeamSearchHeurNode(BeamSearch[D, FNsHV, InstanceNodeBeam], PathFindNode[D, FNsHV, InstanceNodeBeam],
                         PathFindSetHeurV[D, FNsHV, InstanceNodeBeam], ABC):
    """ Abstract node-driven beam search guided by a value heuristic (V). Logits = -(transition_cost + heuristic). """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeBeam]:
        """ Build node-beam instances, optionally computing root heuristic values. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, compute_root_vals)
        return self._construct_instances(InstanceNodeBeam, nodes_root, inst_infos, beam_size, temp, eps)

    def _compute_costs(self, instances: List[InstanceNodeBeam], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ :return: Per-instance logits = -(transition_cost + heuristic); higher is better. """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for nodes in nodes_by_inst:
            logits: List[float] = []
            for node in nodes:
                assert node.parent_t_cost is not None
                logits.append(-(node.parent_t_cost + node.heuristic))

            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst
```
