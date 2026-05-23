---
id: "class:deepxube.pathfinding.graph_search.GraphSearchNodeParser"
kind: "class"
name: "GraphSearchNodeParser"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchNodeParser"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 320
line_end: 324
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_parser('graph_v')"
generic_parameters: []
bases:
  - name: "GraphSearchParser"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchNodeParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchNodeParser`

**File:** [deepxube/pathfinding/graph_search.py:320](../../../deepxube/pathfinding/graph_search.py#L320)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_parser('graph_v')`

## Docstring

CLI parser for the ``graph_v`` (V heuristic) graph-search variant. 

## Inheritance

**Direct bases:**
- `GraphSearchParser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_alg_name` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class GraphSearchNodeParser(GraphSearchParser):
    """ CLI parser for the ``graph_v`` (V heuristic) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_v"
```
