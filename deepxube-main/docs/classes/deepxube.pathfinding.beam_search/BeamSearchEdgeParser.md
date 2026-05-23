---
id: "class:deepxube.pathfinding.beam_search.BeamSearchEdgeParser"
kind: "class"
name: "BeamSearchEdgeParser"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchEdgeParser"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 349
line_end: 353
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('beam_q')"
generic_parameters: []
bases:
  - name: "BeamSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchEdgeParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchEdgeParser`

**File:** [deepxube/pathfinding/beam_search.py:349](../../../deepxube/pathfinding/beam_search.py#L349)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('beam_q')`

## Docstring

CLI parser for the ``beam_q`` (Q heuristic) beam-search variant. 

## Inheritance

**Direct bases:**
- `BeamSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class BeamSearchEdgeParser(BeamSearchParser):
    """ CLI parser for the ``beam_q`` (Q heuristic) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_q"
```
