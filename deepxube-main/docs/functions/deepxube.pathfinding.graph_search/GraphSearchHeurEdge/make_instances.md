---
id: "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge.make_instances"
kind: "method"
name: "make_instances"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurEdge.make_instances"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 206
line_end: 210
class: "GraphSearchHeurEdge"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "inst_infos"
    annotation: "Optional[List[Any]]"
    default: "None"
  - name: "compute_root_vals"
    annotation: "bool"
    default: "True"
  - name: "batch_size"
    annotation: "Optional[int]"
    default: "None"
  - name: "weight"
    annotation: "Optional[float]"
    default: "None"
  - name: "eps"
    annotation: "Optional[float]"
    default: "None"
returns: "List[InstanceEdgeGraph]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge._create_root_nodes"
    expr: "self._create_root_nodes"
    call_sites: [209]
  - target: "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge._construct_instances"
    expr: "self._construct_instances"
    call_sites: [210]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurEdge.make_instances`

**File:** [deepxube/pathfinding/graph_search.py:206](../../../../deepxube/pathfinding/graph_search.py#L206)
**Class:** `GraphSearchHeurEdge`
**Visibility:** public
**Kind:** method

## Signature

```python
def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True, batch_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeGraph]
```

## Docstring

Build edge-graph instances from (state, goal) pairs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `inst_infos` | `Optional[List[Any]]` | `None` |
| `compute_root_vals` | `bool` | `True` |
| `batch_size` | `Optional[int]` | `None` |
| `weight` | `Optional[float]` | `None` |
| `eps` | `Optional[float]` | `None` |

## Returns

`List[InstanceEdgeGraph]`

## Calls

- `self._create_root_nodes` → `func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge._create_root_nodes` (lines: 209)
- `self._construct_instances` → `func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge._construct_instances` (lines: 210)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       batch_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeGraph]:
        """ Build edge-graph instances from (state, goal) pairs. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, True)
        return self._construct_instances(InstanceEdgeGraph, nodes_root, inst_infos, batch_size, weight, eps)
```
