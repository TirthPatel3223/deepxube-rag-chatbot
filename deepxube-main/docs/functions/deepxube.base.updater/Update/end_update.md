---
id: "func:deepxube.base.updater.Update.end_update"
kind: "method"
name: "end_update"
qualified_name: "deepxube.base.updater.Update.end_update"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 304
line_end: 338
class: "Update"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "Dict[int, PathFindPerf]"
docstring_source: "present"
callees:
  - target: null
    expr: "self.to_q.put"
    call_sites: [311]
  - target: null
    expr: "dict"
    call_sites: [314, 336]
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [315]
  - target: null
    expr: "self.from_q.get"
    call_sites: [317]
  - target: null
    expr: "times_up.add_times"
    call_sites: [318]
  - target: null
    expr: "step_to_pathperf_i.items"
    call_sites: [319]
  - target: null
    expr: "step_to_pathperf.keys"
    call_sites: [320]
  - target: "func:deepxube.pathfinding.utils.performance.PathFindPerf"
    expr: "PathFindPerf"
    call_sites: [321]
  - target: null
    expr: "step_to_pathperf[step_num_perf].comb_perf"
    call_sites: [322]
  - target: null
    expr: "print"
    call_sites: [325, 327]
  - target: null
    expr: "times_up.get_time_str"
    call_sites: [325]
  - target: null
    expr: "format"
    call_sites: [327]
  - target: "func:deepxube.pathfinding.utils.performance.print_pathfindperf"
    expr: "print_pathfindperf"
    call_sites: [328]
  - target: null
    expr: "self.nnet_par_info_l_dict.items"
    call_sites: [331]
  - target: "func:deepxube.nnet.nnet_utils.stop_nnet_runners"
    expr: "stop_nnet_runners"
    call_sites: [333]
raises: []
reads_attrs:
  - "self.from_q"
  - "self.nnet_par_info_l_dict"
  - "self.nnet_runner_proc_l_dict"
  - "self.num_generated"
  - "self.procs"
  - "self.to_q"
  - "self.up_args"
writes_attrs:
  - "self.nnet_runner_proc_l_dict"
  - "self.num_generated"
---

# `deepxube.base.updater.Update.end_update`

**File:** [deepxube/base/updater.py:304](../../../../deepxube/base/updater.py#L304)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def end_update(self) -> Dict[int, PathFindPerf]
```

## Docstring

Send stop signals to workers, collect their time/performance
summaries, stop the NNet runners, and return the merged per-step
performance map. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Dict[int, PathFindPerf]`

## Calls

- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 315)
- `PathFindPerf` → `func:deepxube.pathfinding.utils.performance.PathFindPerf` (lines: 321)
- `print_pathfindperf` → `func:deepxube.pathfinding.utils.performance.print_pathfindperf` (lines: 328)
- `stop_nnet_runners` → `func:deepxube.nnet.nnet_utils.stop_nnet_runners` (lines: 333)

### Unresolved
- `self.to_q.put` (lines: 311)
- `dict` (lines: 314, 336)
- `self.from_q.get` (lines: 317)
- `times_up.add_times` (lines: 318)
- `step_to_pathperf_i.items` (lines: 319)
- `step_to_pathperf.keys` (lines: 320)
- `step_to_pathperf[step_num_perf].comb_perf` (lines: 322)
- `print` (lines: 325, 327)
- `times_up.get_time_str` (lines: 325)
- `format` (lines: 327)
- `self.nnet_par_info_l_dict.items` (lines: 331)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.nnet_runner_proc_l_dict`
- `self.num_generated`

**Reads:**
- `self.from_q`
- `self.nnet_par_info_l_dict`
- `self.nnet_runner_proc_l_dict`
- `self.num_generated`
- `self.procs`
- `self.to_q`
- `self.up_args`

## Source

```python
    def end_update(self) -> Dict[int, PathFindPerf]:
        """ Send stop signals to workers, collect their time/performance
        summaries, stop the NNet runners, and return the merged per-step
        performance map. """
        assert (self.to_q is not None) and (self.from_q is not None)
        # sending stop signal
        for _ in self.procs:
            self.to_q.put(None)

        # get summary from processes
        step_to_pathperf: Dict[int, PathFindPerf] = dict()
        times_up: Times = Times()
        for _ in self.procs:
            times_up_i, step_to_pathperf_i = self.from_q.get()
            times_up.add_times(times_up_i)
            for step_num_perf, pathperf in step_to_pathperf_i.items():
                if step_num_perf not in step_to_pathperf.keys():
                    step_to_pathperf[step_num_perf] = PathFindPerf()
                step_to_pathperf[step_num_perf] = step_to_pathperf[step_num_perf].comb_perf(pathperf)

        # print
        print(f"Times - {times_up.get_time_str()}")
        if self.up_args.v:
            print(f"Generated {format(self.num_generated, ',')} training instances")
            print_pathfindperf(step_to_pathperf)

        # clean up clean up everybody do your share
        for nnet_name, nnet_par_infos in self.nnet_par_info_l_dict.items():
            nnet_procs: List[BaseProcess] = self.nnet_runner_proc_l_dict[nnet_name]
            stop_nnet_runners(nnet_procs, nnet_par_infos)

        self.num_generated = 0
        self.nnet_runner_proc_l_dict = dict()

        return step_to_pathperf
```
