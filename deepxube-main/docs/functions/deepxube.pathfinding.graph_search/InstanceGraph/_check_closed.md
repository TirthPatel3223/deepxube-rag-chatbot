---
id: "func:deepxube.pathfinding.graph_search.InstanceGraph._check_closed"
kind: "method"
name: "_check_closed"
qualified_name: "deepxube.pathfinding.graph_search.InstanceGraph._check_closed"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 100
line_end: 108
class: "InstanceGraph"
visibility: "private"
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
  - target: null
    expr: "self.closed_dict.get"
    call_sites: [104]
  - target: null
    expr: "nodes_ret.append"
    call_sites: [107]
raises: []
reads_attrs:
  - "self.closed_dict"
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.InstanceGraph._check_closed`

**File:** [deepxube/pathfinding/graph_search.py:100](../../../../deepxube/pathfinding/graph_search.py#L100)
**Class:** `InstanceGraph`
**Visibility:** private
**Kind:** method

## Signature

```python
def _check_closed(self, nodes: List[Node]) -> List[Node]
```

## Docstring

Return only those nodes whose ``path_cost`` improves (or creates) their closed-dict entry. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |

## Returns

`List[Node]`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.closed_dict.get` (lines: 104)
- `nodes_ret.append` (lines: 107)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.closed_dict`

## Source

```python
    def _check_closed(self, nodes: List[Node]) -> List[Node]:
        """ Return only those nodes whose ``path_cost`` improves (or creates) their closed-dict entry. """
        nodes_ret: List[Node] = []
        for node in nodes:
            path_cost_prev: Optional[float] = self.closed_dict.get(node.state)
            if (path_cost_prev is None) or (path_cost_prev > node.path_cost):
                self.closed_dict[node.state] = node.path_cost
                nodes_ret.append(node)
        return nodes_ret
```
