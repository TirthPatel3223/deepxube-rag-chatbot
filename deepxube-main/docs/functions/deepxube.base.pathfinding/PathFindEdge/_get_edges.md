---
id: "func:deepxube.base.pathfinding.PathFindEdge._get_edges"
kind: "method"
name: "_get_edges"
qualified_name: "deepxube.base.pathfinding.PathFindEdge._get_edges"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 690
line_end: 711
class: "PathFindEdge"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nodes_by_inst"
    annotation: "List[List[Node]]"
    default: null
returns: "List[List[EdgeQ]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [693, 709]
  - target: null
    expr: "zip"
    call_sites: [706]
  - target: null
    expr: "edges.append"
    call_sites: [707]
  - target: "func:deepxube.base.pathfinding.EdgeQ"
    expr: "EdgeQ"
    call_sites: [707]
  - target: null
    expr: "edges_by_inst.append"
    call_sites: [708]
  - target: null
    expr: "self.times.record_time"
    call_sites: [709]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindEdge._get_edges`

**File:** [deepxube/base/pathfinding.py:690](../../../../deepxube/base/pathfinding.py#L690)
**Class:** `PathFindEdge`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_edges(self, nodes_by_inst: List[List[Node]]) -> List[List[EdgeQ]]
```

## Docstring

Build per-instance edge lists from each popped node's q_values or act_probs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes_by_inst` | `List[List[Node]]` | — |

## Returns

`List[List[EdgeQ]]`

## Calls

- `time.time` → `func:time.time` (lines: 693, 709)
- `EdgeQ` → `func:deepxube.base.pathfinding.EdgeQ` (lines: 707)

### Unresolved
- `zip` (lines: 706)
- `edges.append` (lines: 707)
- `edges_by_inst.append` (lines: 708)
- `self.times.record_time` (lines: 709)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _get_edges(self, nodes_by_inst: List[List[Node]]) -> List[List[EdgeQ]]:
        """ Build per-instance edge lists from each popped node's q_values or act_probs. """
        # make edges
        start_time = time.time()
        edges_by_inst: List[List[EdgeQ]] = []

        for nodes in nodes_by_inst:
            edges: List[EdgeQ] = []
            for node in nodes:
                action_vals: Optional[Tuple[List[Action], List[float]]] = None
                if node.q_values is not None:
                    action_vals = node.q_values
                elif node.act_probs is not None:
                    action_vals = node.act_probs

                assert action_vals is not None
                for action, act_val in zip(action_vals[0], action_vals[1], strict=True):
                    edges.append(EdgeQ(node, action, act_val))
            edges_by_inst.append(edges)
        self.times.record_time("edges", time.time() - start_time)

        return edges_by_inst
```
