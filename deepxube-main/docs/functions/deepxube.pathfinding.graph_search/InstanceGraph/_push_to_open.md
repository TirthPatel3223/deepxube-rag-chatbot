---
id: "func:deepxube.pathfinding.graph_search.InstanceGraph._push_to_open"
kind: "method"
name: "_push_to_open"
qualified_name: "deepxube.pathfinding.graph_search.InstanceGraph._push_to_open"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 73
line_end: 77
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
  - name: "sch_over_l"
    annotation: "List[SchOver]"
    default: null
  - name: "costs"
    annotation: "List[float]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "zip"
    call_sites: [75]
  - target: "func:heapq.heappush"
    expr: "heappush"
    call_sites: [76]
raises: []
reads_attrs:
  - "self.heappush_count"
  - "self.open_set"
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.InstanceGraph._push_to_open`

**File:** [deepxube/pathfinding/graph_search.py:73](../../../../deepxube/pathfinding/graph_search.py#L73)
**Class:** `InstanceGraph`
**Visibility:** private
**Kind:** method

## Signature

```python
def _push_to_open(self, sch_over_l: List[SchOver], costs: List[float]) -> None
```

## Docstring

Push (cost, tie-break count, item) tuples onto the min-heap. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `sch_over_l` | `List[SchOver]` | — |
| `costs` | `List[float]` | — |

## Returns

`None`

## Calls

- `heappush` → `func:heapq.heappush` (lines: 76)

### Unresolved
- `zip` (lines: 75)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.heappush_count`
- `self.open_set`

## Source

```python
    def _push_to_open(self, sch_over_l: List[SchOver], costs: List[float]) -> None:
        """ Push (cost, tie-break count, item) tuples onto the min-heap. """
        for sch_over, cost in zip(sch_over_l, costs, strict=True):
            heappush(self.open_set, (cost, self.heappush_count, sch_over))
            self.heappush_count += 1
```
