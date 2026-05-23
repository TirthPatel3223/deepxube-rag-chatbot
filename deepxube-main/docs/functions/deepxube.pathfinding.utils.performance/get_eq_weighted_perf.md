---
id: "func:deepxube.pathfinding.utils.performance.get_eq_weighted_perf"
kind: "function"
name: "get_eq_weighted_perf"
qualified_name: "deepxube.pathfinding.utils.performance.get_eq_weighted_perf"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 66
line_end: 86
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "step_to_search_perf"
    annotation: "Dict[int, PathFindPerf]"
    default: null
returns: "Tuple[float, float, float]"
docstring_source: "present"
callees:
  - target: null
    expr: "step_to_search_perf.values"
    call_sites: [71]
  - target: null
    expr: "search_perf.stats"
    call_sites: [72]
  - target: null
    expr: "per_solved_l.append"
    call_sites: [73]
  - target: null
    expr: "path_cost_ave_l.append"
    call_sites: [75]
  - target: null
    expr: "search_itrs_ave_l.append"
    call_sites: [76]
  - target: null
    expr: "len"
    call_sites: [80]
  - target: null
    expr: "float"
    call_sites: [81, 82, 84]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [81, 82, 84]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.get_eq_weighted_perf`

**File:** [deepxube/pathfinding/utils/performance.py:66](../../../../deepxube/pathfinding/utils/performance.py#L66)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_eq_weighted_perf(step_to_search_perf: Dict[int, PathFindPerf]) -> Tuple[float, float, float]
```

## Docstring

Mean of (% solved, mean path cost, mean search iters) across step buckets, equally weighted regardless of bucket size. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `step_to_search_perf` | `Dict[int, PathFindPerf]` | — |

## Returns

`Tuple[float, float, float]`

## Calls

- `np.mean` → `func:numpy.mean` (lines: 81, 82, 84)

### Unresolved
- `step_to_search_perf.values` (lines: 71)
- `search_perf.stats` (lines: 72)
- `per_solved_l.append` (lines: 73)
- `path_cost_ave_l.append` (lines: 75)
- `search_itrs_ave_l.append` (lines: 76)
- `len` (lines: 80)
- `float` (lines: 81, 82, 84)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_eq_weighted_perf(step_to_search_perf: Dict[int, PathFindPerf]) -> Tuple[float, float, float]:
    """ Mean of (% solved, mean path cost, mean search iters) across step buckets, equally weighted regardless of bucket size. """
    per_solved_l: List[float] = []
    path_cost_ave_l: List[float] = []
    search_itrs_ave_l: List[float] = []
    for search_perf in step_to_search_perf.values():
        per_solved_i, path_cost_ave_i, search_itrs_ave_i = search_perf.stats()
        per_solved_l.append(per_solved_i)
        if per_solved_i > 0.0:
            path_cost_ave_l.append(path_cost_ave_i)
            search_itrs_ave_l.append(search_itrs_ave_i)

    path_costs_ave: float = 0.0
    search_itrs_ave: float = 0.0
    if len(path_cost_ave_l) > 0:
        path_costs_ave = float(np.mean(path_cost_ave_l))
        search_itrs_ave = float(np.mean(search_itrs_ave_l))

    per_solved_ave: float = float(np.mean(per_solved_l))

    return per_solved_ave, path_costs_ave, search_itrs_ave
```
