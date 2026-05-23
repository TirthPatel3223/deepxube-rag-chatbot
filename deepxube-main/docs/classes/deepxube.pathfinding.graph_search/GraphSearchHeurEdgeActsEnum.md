---
id: "class:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum"
kind: "class"
name: "GraphSearchHeurEdgeActsEnum"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 243
line_end: 254
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('graph_q')"
generic_parameters: []
bases:
  - name: "GraphSearchHeurEdge[ActsEnum, FNsHeurQ]"
    resolved_id: null
  - name: "PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeGraph]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum.domain_type"
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "graph_q"
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum`

**File:** [deepxube/pathfinding/graph_search.py:243](../../../deepxube/pathfinding/graph_search.py#L243)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('graph_q')`

## Docstring

Concrete edge-graph search (Q heuristic) for ActsEnum domains; registered as ``graph_q``. 

## Inheritance

**Direct bases:**
- `GraphSearchHeurEdge[ActsEnum, FNsHeurQ]`
- `PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeGraph]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `graph_q`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class GraphSearchHeurEdgeActsEnum(GraphSearchHeurEdge[ActsEnum, FNsHeurQ], PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeGraph]):
    """ Concrete edge-graph search (Q heuristic) for ActsEnum domains; registered as ``graph_q``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurQ]:
        """ :return: ``FNsHeurQ``. """
        return FNsHeurQ
```
