---
id: "class:deepxube.pathfinding.beam_search.BeamSearchNodeParser"
kind: "class"
name: "BeamSearchNodeParser"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchNodeParser"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 341
line_end: 345
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('beam_v')"
generic_parameters: []
bases:
  - name: "BeamSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchNodeParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchNodeParser`

**File:** [deepxube/pathfinding/beam_search.py:341](../../../deepxube/pathfinding/beam_search.py#L341)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('beam_v')`

## Docstring

CLI parser for the ``beam_v`` (V heuristic) beam-search variant. 

## Inheritance

**Direct bases:**
- `BeamSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class BeamSearchNodeParser(BeamSearchParser):
    """ CLI parser for the ``beam_v`` (V heuristic) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_v"
```
