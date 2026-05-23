---
id: "class:deepxube.pathfinding.graph_search.GraphSearchEdgeHasPolicyParser"
kind: "class"
name: "GraphSearchEdgeHasPolicyParser"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchEdgeHasPolicyParser"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 344
line_end: 348
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('graph_q_p')"
generic_parameters: []
bases:
  - name: "GraphSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchEdgeHasPolicyParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchEdgeHasPolicyParser`

**File:** [deepxube/pathfinding/graph_search.py:344](../../../deepxube/pathfinding/graph_search.py#L344)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('graph_q_p')`

## Docstring

CLI parser for the ``graph_q_p`` (Q heuristic + policy) graph-search variant. 

## Inheritance

**Direct bases:**
- `GraphSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class GraphSearchEdgeHasPolicyParser(GraphSearchParser):
    """ CLI parser for the ``graph_q_p`` (Q heuristic + policy) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_q_p"
```
