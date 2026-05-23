---
id: "class:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy"
kind: "class"
name: "BeamSearchHeurEdgeActsPolicy"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 286
line_end: 297
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('beam_q_p')"
generic_parameters: []
bases:
  - name: "BeamSearchHeurEdge[Domain, FNsHeurQPolicy]"
    resolved_id: null
  - name: "PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeBeam]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy.domain_type"
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "beam_q_p"
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy`

**File:** [deepxube/pathfinding/beam_search.py:286](../../../deepxube/pathfinding/beam_search.py#L286)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('beam_q_p')`

## Docstring

Concrete edge-beam (Q heuristic + policy) for any Domain; registered as ``beam_q_p``. 

## Inheritance

**Direct bases:**
- `BeamSearchHeurEdge[Domain, FNsHeurQPolicy]`
- `PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeBeam]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `beam_q_p`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class BeamSearchHeurEdgeActsPolicy(BeamSearchHeurEdge[Domain, FNsHeurQPolicy], PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeBeam]):
    """ Concrete edge-beam (Q heuristic + policy) for any Domain; registered as ``beam_q_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurQPolicy]:
        """ :return: ``FNsHeurQPolicy``. """
        return FNsHeurQPolicy
```
