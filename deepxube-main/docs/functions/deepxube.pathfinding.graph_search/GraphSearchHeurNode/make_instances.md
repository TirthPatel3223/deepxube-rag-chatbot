---
id: "func:deepxube.pathfinding.graph_search.GraphSearchHeurNode.make_instances"
kind: "method"
name: "make_instances"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurNode.make_instances"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 181
line_end: 185
class: "GraphSearchHeurNode"
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
  - name: "beam_size"
    annotation: "Optional[int]"
    default: "None"
  - name: "weight"
    annotation: "Optional[float]"
    default: "None"
  - name: "eps"
    annotation: "Optional[float]"
    default: "None"
returns: "List[InstanceNodeGraph]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.graph_search.GraphSearchHeurNode._create_root_nodes"
    expr: "self._create_root_nodes"
    call_sites: [184]
  - target: "func:deepxube.pathfinding.graph_search.GraphSearchHeurNode._construct_instances"
    expr: "self._construct_instances"
    call_sites: [185]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurNode.make_instances`

**File:** [deepxube/pathfinding/graph_search.py:181](../../../../deepxube/pathfinding/graph_search.py#L181)
**Class:** `GraphSearchHeurNode`
**Visibility:** public
**Kind:** method

## Signature

```python
def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True, beam_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeGraph]
```

## Docstring

Build node-graph instances, optionally computing root heuristic values. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `inst_infos` | `Optional[List[Any]]` | `None` |
| `compute_root_vals` | `bool` | `True` |
| `beam_size` | `Optional[int]` | `None` |
| `weight` | `Optional[float]` | `None` |
| `eps` | `Optional[float]` | `None` |

## Returns

`List[InstanceNodeGraph]`

## Calls

- `self._create_root_nodes` → `func:deepxube.pathfinding.graph_search.GraphSearchHeurNode._create_root_nodes` (lines: 184)
- `self._construct_instances` → `func:deepxube.pathfinding.graph_search.GraphSearchHeurNode._construct_instances` (lines: 185)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeGraph]:
        """ Build node-graph instances, optionally computing root heuristic values. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, compute_root_vals)
        return self._construct_instances(InstanceNodeGraph, nodes_root, inst_infos, beam_size, weight, eps)
```
