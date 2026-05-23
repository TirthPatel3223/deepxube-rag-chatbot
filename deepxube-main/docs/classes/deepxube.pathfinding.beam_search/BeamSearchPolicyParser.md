---
id: "class:deepxube.pathfinding.beam_search.BeamSearchPolicyParser"
kind: "class"
name: "BeamSearchPolicyParser"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchPolicyParser"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 333
line_end: 337
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('beam_p')"
generic_parameters: []
bases:
  - name: "BeamSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearchPolicyParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchPolicyParser`

**File:** [deepxube/pathfinding/beam_search.py:333](../../../deepxube/pathfinding/beam_search.py#L333)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('beam_p')`

## Docstring

CLI parser for the ``beam_p`` (policy-only) beam-search variant. 

## Inheritance

**Direct bases:**
- `BeamSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class BeamSearchPolicyParser(BeamSearchParser):
    """ CLI parser for the ``beam_p`` (policy-only) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_p"
```
