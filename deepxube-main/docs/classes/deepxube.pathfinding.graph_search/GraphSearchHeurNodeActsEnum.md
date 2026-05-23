---
id: "class:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum"
kind: "class"
name: "GraphSearchHeurNodeActsEnum"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 228
line_end: 239
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('graph_v')"
generic_parameters: []
bases:
  - name: "GraphSearchHeurNode[ActsEnum, FNsHeurV]"
    resolved_id: null
  - name: "PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeGraph]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum.domain_type"
  - "func:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum.functions_type"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "graph_v"
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum`

**File:** [deepxube/pathfinding/graph_search.py:228](../../../deepxube/pathfinding/graph_search.py#L228)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('graph_v')`

## Docstring

Concrete node-graph search (V heuristic) for ActsEnum domains; registered as ``graph_v``. 

## Inheritance

**Direct bases:**
- `GraphSearchHeurNode[ActsEnum, FNsHeurV]`
- `PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeGraph]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `graph_v`

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*

## Source

```python
class GraphSearchHeurNodeActsEnum(GraphSearchHeurNode[ActsEnum, FNsHeurV], PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeGraph]):
    """ Concrete node-graph search (V heuristic) for ActsEnum domains; registered as ``graph_v``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurV]:
        """ :return: ``FNsHeurV``. """
        return FNsHeurV
```
