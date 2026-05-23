---
id: "func:deepxube.pathfinding.utils.performance.print_pathfindperf"
kind: "function"
name: "print_pathfindperf"
qualified_name: "deepxube.pathfinding.utils.performance.print_pathfindperf"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 89
line_end: 115
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "step_to_pathfindperf"
    annotation: "Dict[int, PathFindPerf]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "list"
    call_sites: [91, 93]
  - target: null
    expr: "step_to_pathfindperf.keys"
    call_sites: [91]
  - target: null
    expr: "sorted"
    call_sites: [92]
  - target: "func:numpy.unique"
    expr: "np.unique"
    call_sites: [93]
  - target: "func:numpy.linspace"
    expr: "np.linspace"
    call_sites: [93]
  - target: null
    expr: "len"
    call_sites: [93, 103]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [98, 100]
  - target: null
    expr: "float"
    call_sites: [103, 107, 108, 113, 114, 115]
  - target: null
    expr: "sum"
    call_sites: [103]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [107, 108, 113]
  - target: null
    expr: "print"
    call_sites: [111]
  - target: "func:numpy.std"
    expr: "np.std"
    call_sites: [114]
  - target: "func:numpy.min"
    expr: "np.min"
    call_sites: [114]
  - target: "func:numpy.max"
    expr: "np.max"
    call_sites: [115]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.print_pathfindperf`

**File:** [deepxube/pathfinding/utils/performance.py:89](../../../../deepxube/pathfinding/utils/performance.py#L89)
**Visibility:** public
**Kind:** function

## Signature

```python
def print_pathfindperf(step_to_pathfindperf: Dict[int, PathFindPerf]) -> None
```

## Docstring

Print a tabular summary of solve rate / path costs / iters / backups for ~30 sampled step buckets. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `step_to_pathfindperf` | `Dict[int, PathFindPerf]` | — |

## Returns

`None`

## Calls

- `np.unique` → `func:numpy.unique` (lines: 93)
- `np.linspace` → `func:numpy.linspace` (lines: 93)
- `np.array` → `func:numpy.array` (lines: 98, 100)
- `np.mean` → `func:numpy.mean` (lines: 107, 108, 113)
- `np.std` → `func:numpy.std` (lines: 114)
- `np.min` → `func:numpy.min` (lines: 114)
- `np.max` → `func:numpy.max` (lines: 115)

### Unresolved
- `list` (lines: 91, 93)
- `step_to_pathfindperf.keys` (lines: 91)
- `sorted` (lines: 92)
- `len` (lines: 93, 103)
- `float` (lines: 103, 107, 108, 113, 114, 115)
- `sum` (lines: 103)
- `print` (lines: 111)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def print_pathfindperf(step_to_pathfindperf: Dict[int, PathFindPerf]) -> None:
    """ Print a tabular summary of solve rate / path costs / iters / backups for ~30 sampled step buckets. """
    steps: List[int] = list(step_to_pathfindperf.keys())
    steps = sorted(steps)
    step_show_idxs: List[int] = list(np.unique(np.linspace(0, len(steps) - 1, 30, dtype=int)))
    for step_show_idx in step_show_idxs:
        step_show: int = steps[step_show_idx]
        pathfindperf: PathFindPerf = step_to_pathfindperf[step_show]

        is_solved: NDArray[np.bool_] = np.array(pathfindperf.is_solved_l)
        # ctgs: NDArray[np.float64] = np.array(pathfindperf.ctgs)
        ctgs_bkup: NDArray[np.float64] = np.array(pathfindperf.ctgs_bkup)

        # Get stats
        per_solved = 100 * float(sum(is_solved)) / float(len(is_solved))
        avg_itrs: float = 0.0
        avg_path_costs: float = 0.0
        if per_solved > 0.0:
            avg_itrs = float(np.mean(pathfindperf.search_itrs_l))
            avg_path_costs = float(np.mean(pathfindperf.path_costs))

        # Print results
        print(f"Steps: %i, %%Solved: %.2f, avgItrs: {avg_itrs:.2f}, avgPathCosts: {avg_path_costs:.2f}, "
              f"CTG_Backup: %.2f(%.2f/%.2f/%.2f), "
              f"Num: {ctgs_bkup.shape[0]}" % (step_show, per_solved, float(np.mean(ctgs_bkup)),
                                              float(np.std(ctgs_bkup)), float(np.min(ctgs_bkup)),
                                              float(np.max(ctgs_bkup))))
```
