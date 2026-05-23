---
id: "class:deepxube.pathfinding.beam_search.BeamSearchEdgeHasPolicyParser"
kind: "class"
name: "BeamSearchEdgeHasPolicyParser"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchEdgeHasPolicyParser"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 365
line_end: 369
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('beam_q_p')"
generic_parameters: []
bases:
  - name: "BeamSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchEdgeHasPolicyParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchEdgeHasPolicyParser`

**File:** [deepxube/pathfinding/beam_search.py:365](../../../deepxube/pathfinding/beam_search.py#L365)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('beam_q_p')`

## Docstring

CLI parser for the ``beam_q_p`` (Q heuristic + policy) beam-search variant. 

## Inheritance

**Direct bases:**
- `BeamSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class BeamSearchEdgeHasPolicyParser(BeamSearchParser):
    """ CLI parser for the ``beam_q_p`` (Q heuristic + policy) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_q_p"
```
