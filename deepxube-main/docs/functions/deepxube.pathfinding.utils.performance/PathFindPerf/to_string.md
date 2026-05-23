---
id: "func:deepxube.pathfinding.utils.performance.PathFindPerf.to_string"
kind: "method"
name: "to_string"
qualified_name: "deepxube.pathfinding.utils.performance.PathFindPerf.to_string"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 60
line_end: 63
class: "PathFindPerf"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "str"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.utils.performance.PathFindPerf.stats"
    expr: "self.stats"
    call_sites: [62]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.PathFindPerf.to_string`

**File:** [deepxube/pathfinding/utils/performance.py:60](../../../../deepxube/pathfinding/utils/performance.py#L60)
**Class:** `PathFindPerf`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_string(self) -> str
```

## Docstring

:return: One-line human summary of the stats. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`str`

## Calls

- `self.stats` → `func:deepxube.pathfinding.utils.performance.PathFindPerf.stats` (lines: 62)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_string(self) -> str:
        """ :return: One-line human summary of the stats. """
        per_solved, path_cost_ave, search_itrs_ave = self.stats()
        return f"%solved: {per_solved:.2f}, path_costs: {path_cost_ave:.3f}, search_itrs: {search_itrs_ave:.3f}"
```
