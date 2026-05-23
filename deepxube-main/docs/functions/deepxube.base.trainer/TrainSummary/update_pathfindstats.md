---
id: "func:deepxube.base.trainer.TrainSummary.update_pathfindstats"
kind: "method"
name: "update_pathfindstats"
qualified_name: "deepxube.base.trainer.TrainSummary.update_pathfindstats"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 176
line_end: 185
class: "TrainSummary"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "step_to_pathfindperf"
    annotation: "Dict[int, PathFindPerf]"
    default: null
  - name: "itr"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "dict"
    call_sites: [178, 180]
  - target: null
    expr: "step_to_pathfindperf.items"
    call_sites: [179]
  - target: null
    expr: "pathfindperf.per_solved"
    call_sites: [181]
  - target: null
    expr: "pathfindperf.stats"
    call_sites: [182, 183]
  - target: null
    expr: "float"
    call_sites: [184]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [184]
  - target: null
    expr: "len"
    call_sites: [185]
raises: []
reads_attrs:
  - "self.itr_to_steps_to_pathfindstats"
writes_attrs: []
---

# `deepxube.base.trainer.TrainSummary.update_pathfindstats`

**File:** [deepxube/base/trainer.py:176](../../../../deepxube/base/trainer.py#L176)
**Class:** `TrainSummary`
**Visibility:** public
**Kind:** method

## Signature

```python
def update_pathfindstats(self, step_to_pathfindperf: Dict[int, PathFindPerf], itr: int) -> None
```

## Docstring

Snapshot per-step solve rate / path cost / search iter / backup stats at training iteration ``itr``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `step_to_pathfindperf` | `Dict[int, PathFindPerf]` | — |
| `itr` | `int` | — |

## Returns

`None`

## Calls

- `np.mean` → `func:numpy.mean` (lines: 184)

### Unresolved
- `dict` (lines: 178, 180)
- `step_to_pathfindperf.items` (lines: 179)
- `pathfindperf.per_solved` (lines: 181)
- `pathfindperf.stats` (lines: 182, 183)
- `float` (lines: 184)
- `len` (lines: 185)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.itr_to_steps_to_pathfindstats`

## Source

```python
    def update_pathfindstats(self, step_to_pathfindperf: Dict[int, PathFindPerf], itr: int) -> None:
        """ Snapshot per-step solve rate / path cost / search iter / backup stats at training iteration ``itr``. """
        self.itr_to_steps_to_pathfindstats[itr] = dict()
        for step, pathfindperf in step_to_pathfindperf.items():
            self.itr_to_steps_to_pathfindstats[itr][step] = dict()
            self.itr_to_steps_to_pathfindstats[itr][step]["per_solved"] = pathfindperf.per_solved()
            self.itr_to_steps_to_pathfindstats[itr][step]["path_costs"] = pathfindperf.stats()[1]
            self.itr_to_steps_to_pathfindstats[itr][step]["search_itrs"] = pathfindperf.stats()[2]
            self.itr_to_steps_to_pathfindstats[itr][step]["ctgs_backup"] = float(np.mean(pathfindperf.ctgs_bkup))
            self.itr_to_steps_to_pathfindstats[itr][step]["num_instances"] = len(pathfindperf.ctgs_bkup)
```
