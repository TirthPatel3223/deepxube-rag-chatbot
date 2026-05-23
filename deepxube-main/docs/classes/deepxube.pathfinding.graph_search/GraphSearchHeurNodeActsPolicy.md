---
id: "class:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy"
kind: "class"
name: "GraphSearchHeurNodeActsPolicy"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 258
line_end: 269
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('graph_v_p')"
generic_parameters: []
bases:
  - name: "GraphSearchHeurNode[Domain, FNsHeurVPolicy]"
    resolved_id: null
  - name: "PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeGraph]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy.domain_type"
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "graph_v_p"
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy`

**File:** [deepxube/pathfinding/graph_search.py:258](../../../deepxube/pathfinding/graph_search.py#L258)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('graph_v_p')`

## Docstring

Concrete node-graph search (V heuristic + policy) for any Domain; registered as ``graph_v_p``. 

## Inheritance

**Direct bases:**
- `GraphSearchHeurNode[Domain, FNsHeurVPolicy]`
- `PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeGraph]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `graph_v_p`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class GraphSearchHeurNodeActsPolicy(GraphSearchHeurNode[Domain, FNsHeurVPolicy], PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeGraph]):
    """ Concrete node-graph search (V heuristic + policy) for any Domain; registered as ``graph_v_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy``. """
        return FNsHeurVPolicy
```
