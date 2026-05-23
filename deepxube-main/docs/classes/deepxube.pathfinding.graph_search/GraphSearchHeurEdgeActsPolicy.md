---
id: "class:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy"
kind: "class"
name: "GraphSearchHeurEdgeActsPolicy"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 273
line_end: 284
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('graph_q_p')"
generic_parameters: []
bases:
  - name: "GraphSearchHeurEdge[Domain, FNsHeurQPolicy]"
    resolved_id: null
  - name: "PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeGraph]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy.domain_type"
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "graph_q_p"
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy`

**File:** [deepxube/pathfinding/graph_search.py:273](../../../deepxube/pathfinding/graph_search.py#L273)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('graph_q_p')`

## Docstring

Concrete edge-graph search (Q heuristic + policy) for any Domain; registered as ``graph_q_p``. 

## Inheritance

**Direct bases:**
- `GraphSearchHeurEdge[Domain, FNsHeurQPolicy]`
- `PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeGraph]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `graph_q_p`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class GraphSearchHeurEdgeActsPolicy(GraphSearchHeurEdge[Domain, FNsHeurQPolicy], PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeGraph]):
    """ Concrete edge-graph search (Q heuristic + policy) for any Domain; registered as ``graph_q_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurQPolicy]:
        """ :return: ``FNsHeurQPolicy``. """
        return FNsHeurQPolicy
```
