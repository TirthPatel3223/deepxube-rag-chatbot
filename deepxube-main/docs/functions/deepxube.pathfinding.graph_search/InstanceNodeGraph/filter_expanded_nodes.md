---
id: "func:deepxube.pathfinding.graph_search.InstanceNodeGraph.filter_expanded_nodes"
kind: "method"
name: "filter_expanded_nodes"
qualified_name: "deepxube.pathfinding.graph_search.InstanceNodeGraph.filter_expanded_nodes"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 154
line_end: 156
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
returns: "List[Node]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.graph_search.InstanceNodeGraph._check_closed"
    expr: "self._check_closed"
    call_sites: [156]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.InstanceNodeGraph.filter_expanded_nodes`

**File:** [deepxube/pathfinding/graph_search.py:154](../../../../deepxube/pathfinding/graph_search.py#L154)
**Class:** `InstanceNodeGraph`
**Visibility:** public
**Kind:** method

## Signature

```python
def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]
```

## Docstring

Filter expanded children through the closed dict; discard nodes that do not improve it. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |

## Returns

`List[Node]`

## Calls

- `self._check_closed` → `func:deepxube.pathfinding.graph_search.InstanceNodeGraph._check_closed` (lines: 156)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Filter expanded children through the closed dict; discard nodes that do not improve it. """
        return self._check_closed(nodes)
```
