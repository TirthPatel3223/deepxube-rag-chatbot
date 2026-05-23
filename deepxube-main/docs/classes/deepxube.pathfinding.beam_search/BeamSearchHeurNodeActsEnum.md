---
id: "class:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum"
kind: "class"
name: "BeamSearchHeurNodeActsEnum"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 241
line_end: 252
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('beam_v')"
generic_parameters: []
bases:
  - name: "BeamSearchHeurNode[ActsEnum, FNsHeurV]"
    resolved_id: null
  - name: "PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeBeam]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum.domain_type"
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "beam_v"
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum`

**File:** [deepxube/pathfinding/beam_search.py:241](../../../deepxube/pathfinding/beam_search.py#L241)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('beam_v')`

## Docstring

Concrete node-beam (V heuristic) for ActsEnum domains; registered as ``beam_v``. 

## Inheritance

**Direct bases:**
- `BeamSearchHeurNode[ActsEnum, FNsHeurV]`
- `PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeBeam]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `beam_v`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class BeamSearchHeurNodeActsEnum(BeamSearchHeurNode[ActsEnum, FNsHeurV], PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeBeam]):
    """ Concrete node-beam (V heuristic) for ActsEnum domains; registered as ``beam_v``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurV]:
        """ :return: ``FNsHeurV``. """
        return FNsHeurV
```
