---
id: "func:deepxube.pathfinding.utils.performance.PathFindPerf.stats"
kind: "method"
name: "stats"
qualified_name: "deepxube.pathfinding.utils.performance.PathFindPerf.stats"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 50
line_end: 58
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
returns: "Tuple[float, float, float]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [54]
  - target: null
    expr: "float"
    call_sites: [55, 56]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [55, 56]
  - target: "func:deepxube.pathfinding.utils.performance.PathFindPerf.per_solved"
    expr: "self.per_solved"
    call_sites: [58]
raises: []
reads_attrs:
  - "self.path_costs"
  - "self.search_itrs_l"
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.PathFindPerf.stats`

**File:** [deepxube/pathfinding/utils/performance.py:50](../../../../deepxube/pathfinding/utils/performance.py#L50)
**Class:** `PathFindPerf`
**Visibility:** public
**Kind:** method

## Signature

```python
def stats(self) -> Tuple[float, float, float]
```

## Docstring

:return: ``(percent_solved, mean_path_cost, mean_search_itrs)`` over solved instances. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Tuple[float, float, float]`

## Calls

- `np.mean` → `func:numpy.mean` (lines: 55, 56)
- `self.per_solved` → `func:deepxube.pathfinding.utils.performance.PathFindPerf.per_solved` (lines: 58)

### Unresolved
- `len` (lines: 54)
- `float` (lines: 55, 56)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.path_costs`
- `self.search_itrs_l`

## Source

```python
    def stats(self) -> Tuple[float, float, float]:
        """ :return: ``(percent_solved, mean_path_cost, mean_search_itrs)`` over solved instances. """
        path_cost_ave: float = 0.0
        search_itrs_ave: float = 0.0
        if len(self.path_costs) > 0:
            path_cost_ave = float(np.mean(self.path_costs))
            search_itrs_ave = float(np.mean(self.search_itrs_l))

        return self.per_solved(), path_cost_ave, search_itrs_ave
```
