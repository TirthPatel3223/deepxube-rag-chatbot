---
id: "func:deepxube.pathfinding.graph_search.InstanceNodeGraph.push_pop_nodes"
kind: "method"
name: "push_pop_nodes"
qualified_name: "deepxube.pathfinding.graph_search.InstanceNodeGraph.push_pop_nodes"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 158
line_end: 161
class: "InstanceNodeGraph"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nodes"
    annotation: "List[Node]"
    default: null
  - name: "costs"
    annotation: "List[float]"
    default: null
returns: "List[Node]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.graph_search.InstanceNodeGraph._push_to_open"
    expr: "self._push_to_open"
    call_sites: [160]
  - target: "func:deepxube.pathfinding.graph_search.InstanceNodeGraph._pop_from_open"
    expr: "self._pop_from_open"
    call_sites: [161]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.InstanceNodeGraph.push_pop_nodes`

**File:** [deepxube/pathfinding/graph_search.py:158](../../../../deepxube/pathfinding/graph_search.py#L158)
**Class:** `InstanceNodeGraph`
**Visibility:** public
**Kind:** method

## Signature

```python
def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]
```

## Docstring

Push nodes onto the open heap, then pop the next best batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |
| `costs` | `List[float]` | — |

## Returns

`List[Node]`

## Calls

- `self._push_to_open` → `func:deepxube.pathfinding.graph_search.InstanceNodeGraph._push_to_open` (lines: 160)
- `self._pop_from_open` → `func:deepxube.pathfinding.graph_search.InstanceNodeGraph._pop_from_open` (lines: 161)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Push nodes onto the open heap, then pop the next best batch. """
        self._push_to_open(nodes, costs)
        return self._pop_from_open()
```
