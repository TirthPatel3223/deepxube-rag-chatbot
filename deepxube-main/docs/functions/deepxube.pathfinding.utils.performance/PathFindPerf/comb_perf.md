---
id: "func:deepxube.pathfinding.utils.performance.PathFindPerf.comb_perf"
kind: "method"
name: "comb_perf"
qualified_name: "deepxube.pathfinding.utils.performance.PathFindPerf.comb_perf"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 35
line_end: 44
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
  - name: "search_perf2"
    annotation: "'PathFindPerf'"
    default: null
returns: "'PathFindPerf'"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.utils.performance.PathFindPerf"
    expr: "PathFindPerf"
    call_sites: [37]
raises: []
reads_attrs:
  - "self.ctgs"
  - "self.ctgs_bkup"
  - "self.is_solved_l"
  - "self.path_costs"
  - "self.search_itrs_l"
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.PathFindPerf.comb_perf`

**File:** [deepxube/pathfinding/utils/performance.py:35](../../../../deepxube/pathfinding/utils/performance.py#L35)
**Class:** `PathFindPerf`
**Visibility:** public
**Kind:** method

## Signature

```python
def comb_perf(self, search_perf2: 'PathFindPerf') -> 'PathFindPerf'
```

## Docstring

Concatenate stats from another ``PathFindPerf`` into a new one. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `search_perf2` | `'PathFindPerf'` | — |

## Returns

`'PathFindPerf'`

## Calls

- `PathFindPerf` → `func:deepxube.pathfinding.utils.performance.PathFindPerf` (lines: 37)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.ctgs`
- `self.ctgs_bkup`
- `self.is_solved_l`
- `self.path_costs`
- `self.search_itrs_l`

## Source

```python
    def comb_perf(self, search_perf2: 'PathFindPerf') -> 'PathFindPerf':
        """ Concatenate stats from another ``PathFindPerf`` into a new one. """
        search_perf_new: PathFindPerf = PathFindPerf()
        search_perf_new.is_solved_l = self.is_solved_l + search_perf2.is_solved_l
        search_perf_new.path_costs = self.path_costs + search_perf2.path_costs
        search_perf_new.search_itrs_l = self.search_itrs_l + search_perf2.search_itrs_l
        search_perf_new.ctgs = self.ctgs + search_perf2.ctgs
        search_perf_new.ctgs_bkup = self.ctgs_bkup + search_perf2.ctgs_bkup

        return search_perf_new
```
