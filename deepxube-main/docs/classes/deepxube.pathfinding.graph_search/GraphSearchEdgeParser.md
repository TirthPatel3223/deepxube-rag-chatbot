---
id: "class:deepxube.pathfinding.graph_search.GraphSearchEdgeParser"
kind: "class"
name: "GraphSearchEdgeParser"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchEdgeParser"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 328
line_end: 332
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('graph_q')"
generic_parameters: []
bases:
  - name: "GraphSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchEdgeParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchEdgeParser`

**File:** [deepxube/pathfinding/graph_search.py:328](../../../deepxube/pathfinding/graph_search.py#L328)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('graph_q')`

## Docstring

CLI parser for the ``graph_q`` (Q heuristic) graph-search variant. 

## Inheritance

**Direct bases:**
- `GraphSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class GraphSearchEdgeParser(GraphSearchParser):
    """ CLI parser for the ``graph_q`` (Q heuristic) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_q"
```
