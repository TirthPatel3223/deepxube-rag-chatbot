---
id: "class:deepxube.pathfinding.beam_search.BeamSearchNodeHasPolicyParser"
kind: "class"
name: "BeamSearchNodeHasPolicyParser"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchNodeHasPolicyParser"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 357
line_end: 361
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('beam_v_p')"
generic_parameters: []
bases:
  - name: "BeamSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchNodeHasPolicyParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchNodeHasPolicyParser`

**File:** [deepxube/pathfinding/beam_search.py:357](../../../deepxube/pathfinding/beam_search.py#L357)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('beam_v_p')`

## Docstring

CLI parser for the ``beam_v_p`` (V heuristic + policy) beam-search variant. 

## Inheritance

**Direct bases:**
- `BeamSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class BeamSearchNodeHasPolicyParser(BeamSearchParser):
    """ CLI parser for the ``beam_v_p`` (V heuristic + policy) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_v_p"
```
