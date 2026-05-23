---
id: "class:deepxube.pathfinding.beam_search.BeamSearchPolicy"
kind: "class"
name: "BeamSearchPolicy"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchPolicy"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 157
line_end: 187
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('beam_p')"
generic_parameters: []
bases:
  - name: "BeamSearch[Domain, FNsPolicy, InstanceEdgeBeam]"
    resolved_id: null
  - name: "PathFindEdge[Domain, FNsPolicy, InstanceEdgeBeam]"
    resolved_id: null
  - name: "PathFindActsPolicy[Domain, FNsPolicy, InstanceEdgeBeam]"
    resolved_id: null
  - name: "PathFindSetPolicy[Domain, FNsPolicy, InstanceEdgeBeam]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchPolicy.domain_type"
  - "func:deepxube.pathfinding.beam_search.BeamSearchPolicy.functions_type"
  - "func:deepxube.pathfinding.beam_search.BeamSearchPolicy.make_instances"
  - "func:deepxube.pathfinding.beam_search.BeamSearchPolicy._compute_costs"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "beam_p"
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchPolicy`

**File:** [deepxube/pathfinding/beam_search.py:157](../../../deepxube/pathfinding/beam_search.py#L157)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('beam_p')`

## Docstring

Policy-driven beam search: edges chosen by the policy network's action probabilities. 

## Inheritance

**Direct bases:**
- `BeamSearch[Domain, FNsPolicy, InstanceEdgeBeam]`
- `PathFindEdge[Domain, FNsPolicy, InstanceEdgeBeam]`
- `PathFindActsPolicy[Domain, FNsPolicy, InstanceEdgeBeam]`
- `PathFindSetPolicy[Domain, FNsPolicy, InstanceEdgeBeam]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `beam_p`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*
- `make_instances`
- `_compute_costs`

## Source

```python
class BeamSearchPolicy(BeamSearch[Domain, FNsPolicy, InstanceEdgeBeam], PathFindEdge[Domain, FNsPolicy, InstanceEdgeBeam],
                       PathFindActsPolicy[Domain, FNsPolicy, InstanceEdgeBeam], PathFindSetPolicy[Domain, FNsPolicy, InstanceEdgeBeam]):
    """ Policy-driven beam search: edges chosen by the policy network's action probabilities. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsPolicy]:
        """ :return: ``FNsPolicy``. """
        return FNsPolicy

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeBeam]:
        """ Build edge-beam instances from (state, goal) pairs with optional per-call beam parameter overrides. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, True)
        return self._construct_instances(InstanceEdgeBeam, nodes_root, inst_infos, beam_size, temp, eps)

    def _compute_costs(self, instances: List[InstanceEdgeBeam], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ Logits = the policy's per-edge log-probabilities (already in ``edge.q_val``). """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for edges in edges_by_inst:
            logits: List[float] = [edge.q_val for edge in edges]  # corresponds to prob densities
            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst
```
