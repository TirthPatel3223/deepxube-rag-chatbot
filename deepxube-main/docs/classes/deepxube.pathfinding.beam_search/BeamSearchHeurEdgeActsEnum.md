---
id: "class:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum"
kind: "class"
name: "BeamSearchHeurEdgeActsEnum"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 256
line_end: 267
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('beam_q')"
generic_parameters: []
bases:
  - name: "BeamSearchHeurEdge[ActsEnum, FNsHeurQ]"
    resolved_id: null
  - name: "PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeBeam]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum.domain_type"
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "beam_q"
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum`

**File:** [deepxube/pathfinding/beam_search.py:256](../../../deepxube/pathfinding/beam_search.py#L256)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('beam_q')`

## Docstring

Concrete edge-beam (Q heuristic) for ActsEnum domains; registered as ``beam_q``. 

## Inheritance

**Direct bases:**
- `BeamSearchHeurEdge[ActsEnum, FNsHeurQ]`
- `PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeBeam]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `beam_q`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class BeamSearchHeurEdgeActsEnum(BeamSearchHeurEdge[ActsEnum, FNsHeurQ], PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeBeam]):
    """ Concrete edge-beam (Q heuristic) for ActsEnum domains; registered as ``beam_q``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurQ]:
        """ :return: ``FNsHeurQ``. """
        return FNsHeurQ
```
