---
id: "class:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy"
kind: "class"
name: "BeamSearchHeurNodeActsPolicy"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 271
line_end: 282
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('beam_v_p')"
generic_parameters: []
bases:
  - name: "BeamSearchHeurNode[Domain, FNsHeurVPolicy]"
    resolved_id: null
  - name: "PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeBeam]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy.domain_type"
  - "func:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "beam_v_p"
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy`

**File:** [deepxube/pathfinding/beam_search.py:271](../../../deepxube/pathfinding/beam_search.py#L271)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('beam_v_p')`

## Docstring

Concrete node-beam (V heuristic + policy) for any Domain; registered as ``beam_v_p``. 

## Inheritance

**Direct bases:**
- `BeamSearchHeurNode[Domain, FNsHeurVPolicy]`
- `PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeBeam]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `beam_v_p`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class BeamSearchHeurNodeActsPolicy(BeamSearchHeurNode[Domain, FNsHeurVPolicy], PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeBeam]):
    """ Concrete node-beam (V heuristic + policy) for any Domain; registered as ``beam_v_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy``. """
        return FNsHeurVPolicy
```
