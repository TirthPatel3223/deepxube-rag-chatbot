---
id: "func:deepxube.pathfinding.graph_search.GraphSearchHeurEdge._compute_costs"
kind: "method"
name: "_compute_costs"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurEdge._compute_costs"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 212
line_end: 224
class: "GraphSearchHeurEdge"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instances"
    annotation: "List[InstanceEdgeGraph]"
    default: null
  - name: "edges_by_inst"
    annotation: "List[List[EdgeQ]]"
    default: null
returns: "List[List[float]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [214, 222]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [215, 216]
  - target: null
    expr: "len"
    call_sites: [216]
  - target: null
    expr: "zip"
    call_sites: [216]
  - target: null
    expr: "(np.array(weights_flat) * np.array(path_costs_flat) + np.array(qvals_flat)).tolist"
    call_sites: [219]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [219]
  - target: "func:deepxube.utils.misc_utils.unflatten"
    expr: "misc_utils.unflatten"
    call_sites: [220]
  - target: null
    expr: "self.times.record_time"
    call_sites: [222]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurEdge._compute_costs`

**File:** [deepxube/pathfinding/graph_search.py:212](../../../../deepxube/pathfinding/graph_search.py#L212)
**Class:** `GraphSearchHeurEdge`
**Visibility:** private
**Kind:** method

## Signature

```python
def _compute_costs(self, instances: List[InstanceEdgeGraph], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]
```

## Docstring

:return: Per-instance costs = weight * node.path_cost + q_val (lower = higher priority). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceEdgeGraph]` | — |
| `edges_by_inst` | `List[List[EdgeQ]]` | — |

## Returns

`List[List[float]]`

## Calls

- `time.time` → `func:time.time` (lines: 214, 222)
- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 215, 216)
- `np.array` → `func:numpy.array` (lines: 219)
- `misc_utils.unflatten` → `func:deepxube.utils.misc_utils.unflatten` (lines: 220)

### Unresolved
- `len` (lines: 216)
- `zip` (lines: 216)
- `(np.array(weights_flat) * np.array(path_costs_flat) + np.array(qvals_flat)).tolist` (lines: 219)
- `self.times.record_time` (lines: 222)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _compute_costs(self, instances: List[InstanceEdgeGraph], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ :return: Per-instance costs = weight * node.path_cost + q_val (lower = higher priority). """
        start_time = time.time()
        edges_flat: List[EdgeQ] = misc_utils.flatten(edges_by_inst)[0]
        weights_flat, split_idxs = misc_utils.flatten([[instance.weight] * len(edges) for instance, edges in zip(instances, edges_by_inst, strict=True)])
        path_costs_flat: List[float] = [edge.node.path_cost for edge in edges_flat]
        qvals_flat: List[float] = [edge.q_val for edge in edges_flat]
        costs_flat: List[float] = ((np.array(weights_flat) * np.array(path_costs_flat)) + np.array(qvals_flat)).tolist()
        costs_by_inst: List[List[float]] = misc_utils.unflatten(costs_flat, split_idxs)

        self.times.record_time("cost", time.time() - start_time)

        return costs_by_inst
```
