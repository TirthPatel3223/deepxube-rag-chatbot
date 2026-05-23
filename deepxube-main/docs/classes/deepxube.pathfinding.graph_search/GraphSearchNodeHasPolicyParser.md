---
id: "class:deepxube.pathfinding.graph_search.GraphSearchNodeHasPolicyParser"
kind: "class"
name: "GraphSearchNodeHasPolicyParser"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchNodeHasPolicyParser"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 336
line_end: 340
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('graph_v_p')"
generic_parameters: []
bases:
  - name: "GraphSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchNodeHasPolicyParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchNodeHasPolicyParser`

**File:** [deepxube/pathfinding/graph_search.py:336](../../../deepxube/pathfinding/graph_search.py#L336)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('graph_v_p')`

## Docstring

CLI parser for the ``graph_v_p`` (V heuristic + policy) graph-search variant. 

## Inheritance

**Direct bases:**
- `GraphSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class GraphSearchNodeHasPolicyParser(GraphSearchParser):
    """ CLI parser for the ``graph_v_p`` (V heuristic + policy) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_v_p"
```
