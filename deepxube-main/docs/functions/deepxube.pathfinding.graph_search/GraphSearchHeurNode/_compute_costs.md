---
id: "func:deepxube.pathfinding.graph_search.GraphSearchHeurNode._compute_costs"
kind: "method"
name: "_compute_costs"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchHeurNode._compute_costs"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 187
line_end: 199
class: "GraphSearchHeurNode"
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
    annotation: "List[InstanceNodeGraph]"
    default: null
  - name: "nodes_by_inst"
    annotation: "List[List[Node]]"
    default: null
returns: "List[List[float]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [189, 197]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [190, 191]
  - target: null
    expr: "len"
    call_sites: [191]
  - target: null
    expr: "zip"
    call_sites: [191]
  - target: null
    expr: "(np.array(weights) * np.array(path_costs) + np.array(heuristics)).tolist"
    call_sites: [194]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [194]
  - target: "func:deepxube.utils.misc_utils.unflatten"
    expr: "misc_utils.unflatten"
    call_sites: [195]
  - target: null
    expr: "self.times.record_time"
    call_sites: [197]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.GraphSearchHeurNode._compute_costs`

**File:** [deepxube/pathfinding/graph_search.py:187](../../../../deepxube/pathfinding/graph_search.py#L187)
**Class:** `GraphSearchHeurNode`
**Visibility:** private
**Kind:** method

## Signature

```python
def _compute_costs(self, instances: List[InstanceNodeGraph], nodes_by_inst: List[List[Node]]) -> List[List[float]]
```

## Docstring

:return: Per-instance costs = weight * path_cost + heuristic (lower = higher priority). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceNodeGraph]` | — |
| `nodes_by_inst` | `List[List[Node]]` | — |

## Returns

`List[List[float]]`

## Calls

- `time.time` → `func:time.time` (lines: 189, 197)
- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 190, 191)
- `np.array` → `func:numpy.array` (lines: 194)
- `misc_utils.unflatten` → `func:deepxube.utils.misc_utils.unflatten` (lines: 195)

### Unresolved
- `len` (lines: 191)
- `zip` (lines: 191)
- `(np.array(weights) * np.array(path_costs) + np.array(heuristics)).tolist` (lines: 194)
- `self.times.record_time` (lines: 197)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _compute_costs(self, instances: List[InstanceNodeGraph], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ :return: Per-instance costs = weight * path_cost + heuristic (lower = higher priority). """
        start_time = time.time()
        nodes_c_flat: List[Node] = misc_utils.flatten(nodes_by_inst)[0]
        weights, split_idxs = misc_utils.flatten([[instance.weight] * len(nodes_c) for instance, nodes_c in zip(instances, nodes_by_inst, strict=True)])
        path_costs: List[float] = [node.path_cost for node in nodes_c_flat]
        heuristics: List[float] = [node.heuristic for node in nodes_c_flat]
        costs_flat: List[float] = ((np.array(weights) * np.array(path_costs)) + np.array(heuristics)).tolist()
        costs_by_inst: List[List[float]] = misc_utils.unflatten(costs_flat, split_idxs)

        self.times.record_time("cost", time.time() - start_time)

        return costs_by_inst
```
