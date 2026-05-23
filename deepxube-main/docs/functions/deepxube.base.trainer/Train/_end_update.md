---
id: "func:deepxube.base.trainer.Train._end_update"
kind: "method"
name: "_end_update"
qualified_name: "deepxube.base.trainer.Train._end_update"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 392
line_end: 411
class: "Train"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "itr_init"
    annotation: "int"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [394, 411]
  - target: null
    expr: "self.updater.end_update"
    call_sites: [395]
  - target: null
    expr: "self.train_summary.update_pathfindstats"
    call_sites: [396]
  - target: null
    expr: "self.status.update_step_probs"
    call_sites: [398]
  - target: "func:deepxube.pathfinding.utils.performance.get_eq_weighted_perf"
    expr: "get_eq_weighted_perf"
    call_sites: [400]
  - target: null
    expr: "self.writer.add_scalar"
    call_sites: [402, 403, 404]
  - target: "func:deepxube.base.trainer.Train._add_post_up_info"
    expr: "self._add_post_up_info"
    call_sites: [407]
  - target: null
    expr: "print"
    call_sites: [409]
  - target: null
    expr: "', '.join"
    call_sites: [409]
  - target: null
    expr: "times.record_time"
    call_sites: [411]
raises: []
reads_attrs:
  - "self.status"
  - "self.train_args"
  - "self.train_summary"
  - "self.updater"
  - "self.writer"
writes_attrs: []
---

# `deepxube.base.trainer.Train._end_update`

**File:** [deepxube/base/trainer.py:392](../../../../deepxube/base/trainer.py#L392)
**Class:** `Train`
**Visibility:** private
**Kind:** method

## Signature

```python
def _end_update(self, itr_init: int, times: Times) -> None
```

## Docstring

Wrap up the updater round: collect performance, push to TensorBoard, optionally rebalance step probs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `itr_init` | `int` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 394, 411)
- `get_eq_weighted_perf` → `func:deepxube.pathfinding.utils.performance.get_eq_weighted_perf` (lines: 400)
- `self._add_post_up_info` → `func:deepxube.base.trainer.Train._add_post_up_info` (lines: 407)

### Unresolved
- `self.updater.end_update` (lines: 395)
- `self.train_summary.update_pathfindstats` (lines: 396)
- `self.status.update_step_probs` (lines: 398)
- `self.writer.add_scalar` (lines: 402, 403, 404)
- `print` (lines: 409)
- `', '.join` (lines: 409)
- `times.record_time` (lines: 411)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.status`
- `self.train_args`
- `self.train_summary`
- `self.updater`
- `self.writer`

## Source

```python
    def _end_update(self, itr_init: int, times: Times) -> None:
        """ Wrap up the updater round: collect performance, push to TensorBoard, optionally rebalance step probs. """
        start_time = time.time()
        step_to_search_perf: Dict[int, PathFindPerf] = self.updater.end_update()
        self.train_summary.update_pathfindstats(step_to_search_perf, itr_init)
        if self.train_args.balance_steps:
            self.status.update_step_probs(step_to_search_perf)

        per_solved_ave, path_costs_ave, search_itrs_ave = get_eq_weighted_perf(step_to_search_perf)

        self.writer.add_scalar("train/pathfind/solved", per_solved_ave, self.status.itr)
        self.writer.add_scalar("train/pathfind/path_cost", path_costs_ave, self.status.itr)
        self.writer.add_scalar("train/pathfind/search_itrs", search_itrs_ave, self.status.itr)

        post_up_info_l: List[str] = [f"%solved: {per_solved_ave:.2f}", f"path_costs: {path_costs_ave:.3f}",
                                     f"search_itrs: {search_itrs_ave:.3f}"] + self._add_post_up_info()

        print(f"Data - {', '.join(post_up_info_l)}")

        times.record_time("up_end", time.time() - start_time)
```
