---
id: "func:deepxube.pathfinding.graph_search.InstanceEdgeGraph.push_pop_edges"
kind: "method"
name: "push_pop_edges"
qualified_name: "deepxube.pathfinding.graph_search.InstanceEdgeGraph.push_pop_edges"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 171
line_end: 174
class: "InstanceEdgeGraph"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "edges"
    annotation: "List[EdgeQ]"
    default: null
  - name: "costs"
    annotation: "List[float]"
    default: null
returns: "List[EdgeQ]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.graph_search.InstanceEdgeGraph._push_to_open"
    expr: "self._push_to_open"
    call_sites: [173]
  - target: "func:deepxube.pathfinding.graph_search.InstanceEdgeGraph._pop_from_open"
    expr: "self._pop_from_open"
    call_sites: [174]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.InstanceEdgeGraph.push_pop_edges`

**File:** [deepxube/pathfinding/graph_search.py:171](../../../../deepxube/pathfinding/graph_search.py#L171)
**Class:** `InstanceEdgeGraph`
**Visibility:** public
**Kind:** method

## Signature

```python
def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]
```

## Docstring

Push edges onto the open heap, then pop the next best batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `edges` | `List[EdgeQ]` | — |
| `costs` | `List[float]` | — |

## Returns

`List[EdgeQ]`

## Calls

- `self._push_to_open` → `func:deepxube.pathfinding.graph_search.InstanceEdgeGraph._push_to_open` (lines: 173)
- `self._pop_from_open` → `func:deepxube.pathfinding.graph_search.InstanceEdgeGraph._pop_from_open` (lines: 174)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Push edges onto the open heap, then pop the next best batch. """
        self._push_to_open(edges, costs)
        return self._pop_from_open()
```
