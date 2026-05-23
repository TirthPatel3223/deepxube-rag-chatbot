---
id: "func:deepxube.base.updater.Update.update_runner"
kind: "method"
name: "update_runner"
qualified_name: "deepxube.base.updater.Update.update_runner"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 374
line_end: 445
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
  - name: "to_q"
    annotation: "Queue"
    default: null
  - name: "from_q"
    annotation: "Queue"
    default: null
  - name: "rb_size"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.Update._init_replay_buffer"
    expr: "self._init_replay_buffer"
    call_sites: [380]
  - target: null
    expr: "self.from_main_q.get"
    call_sites: [384]
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [387]
  - target: null
    expr: "targ_update_nums.items"
    call_sites: [390]
  - target: "func:deepxube.base.updater.Update.set_targ_update_num"
    expr: "self.set_targ_update_num"
    call_sites: [391]
  - target: "func:deepxube.base.updater.Update.initialize_fns"
    expr: "self.initialize_fns"
    call_sites: [392]
  - target: null
    expr: "dict"
    call_sites: [394]
  - target: null
    expr: "to_q.get"
    call_sites: [396]
  - target: "func:deepxube.base.updater.Update.get_pathfind"
    expr: "self.get_pathfind"
    call_sites: [400]
  - target: null
    expr: "range"
    call_sites: [405]
  - target: "func:deepxube.base.updater.Update._add_instances"
    expr: "self._add_instances"
    call_sites: [407]
  - target: null
    expr: "len"
    call_sites: [408, 419, 428]
  - target: "func:deepxube.base.updater.Update._step_sync_main"
    expr: "self._step_sync_main"
    call_sites: [412]
  - target: "func:deepxube.base.updater._put_from_q"
    expr: "_put_from_q"
    call_sites: [413, 430]
  - target: "func:deepxube.base.updater.Update._step"
    expr: "self._step"
    call_sites: [415]
  - target: null
    expr: "pathfind.remove_finished_instances"
    call_sites: [418]
  - target: null
    expr: "put_from_q.append"
    call_sites: [420, 429]
  - target: "func:deepxube.base.updater.Update._get_instance_data"
    expr: "self._get_instance_data"
    call_sites: [420, 429]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [423, 425, 434, 439]
  - target: "func:deepxube.base.updater.Update._update_perf"
    expr: "self._update_perf"
    call_sites: [424]
  - target: null
    expr: "times.record_time"
    call_sites: [425, 439]
  - target: null
    expr: "times.add_times"
    call_sites: [432]
  - target: "func:gc.collect"
    expr: "gc.collect"
    call_sites: [438]
  - target: null
    expr: "from_q.put"
    call_sites: [441]
  - target: "func:deepxube.base.updater.Update.clear_nnet_fn_dict"
    expr: "self.clear_nnet_fn_dict"
    call_sites: [442]
raises: []
reads_attrs:
  - "self.from_main_q"
  - "self.nnet_par_info_main"
  - "self.to_main_q"
  - "self.up_args"
writes_attrs:
  - "self.from_main_q"
  - "self.nnet_par_info_main"
  - "self.to_main_q"
---

# `deepxube.base.updater.Update.update_runner`

**File:** [deepxube/base/updater.py:374](../../../../deepxube/base/updater.py#L374)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def update_runner(self, to_q: Queue, from_q: Queue, rb_size: int) -> None
```

## Docstring

Worker entry point. Runs the generation loop until ``None`` is
received on ``from_main_q``: for each batch, add instances, step
the pathfinder, harvest finished-instance data, and push it back. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `to_q` | `Queue` | — |
| `from_q` | `Queue` | — |
| `rb_size` | `int` | — |

## Returns

`None`

## Calls

- `self._init_replay_buffer` → `func:deepxube.base.updater.Update._init_replay_buffer` (lines: 380)
- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 387)
- `self.set_targ_update_num` → `func:deepxube.base.updater.Update.set_targ_update_num` (lines: 391)
- `self.initialize_fns` → `func:deepxube.base.updater.Update.initialize_fns` (lines: 392)
- `self.get_pathfind` → `func:deepxube.base.updater.Update.get_pathfind` (lines: 400)
- `self._add_instances` → `func:deepxube.base.updater.Update._add_instances` (lines: 407)
- `self._step_sync_main` → `func:deepxube.base.updater.Update._step_sync_main` (lines: 412)
- `_put_from_q` → `func:deepxube.base.updater._put_from_q` (lines: 413, 430)
- `self._step` → `func:deepxube.base.updater.Update._step` (lines: 415)
- `self._get_instance_data` → `func:deepxube.base.updater.Update._get_instance_data` (lines: 420, 429)
- `time.time` → `func:time.time` (lines: 423, 425, 434, 439)
- `self._update_perf` → `func:deepxube.base.updater.Update._update_perf` (lines: 424)
- `gc.collect` → `func:gc.collect` (lines: 438)
- `self.clear_nnet_fn_dict` → `func:deepxube.base.updater.Update.clear_nnet_fn_dict` (lines: 442)

### Unresolved
- `self.from_main_q.get` (lines: 384)
- `targ_update_nums.items` (lines: 390)
- `dict` (lines: 394)
- `to_q.get` (lines: 396)
- `range` (lines: 405)
- `len` (lines: 408, 419, 428)
- `pathfind.remove_finished_instances` (lines: 418)
- `put_from_q.append` (lines: 420, 429)
- `times.record_time` (lines: 425, 439)
- `times.add_times` (lines: 432)
- `from_q.put` (lines: 441)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.from_main_q`
- `self.nnet_par_info_main`
- `self.to_main_q`

**Reads:**
- `self.from_main_q`
- `self.nnet_par_info_main`
- `self.to_main_q`
- `self.up_args`

## Source

```python
    def update_runner(self, to_q: Queue, from_q: Queue, rb_size: int) -> None:
        """ Worker entry point. Runs the generation loop until ``None`` is
        received on ``from_main_q``: for each batch, add instances, step
        the pathfinder, harvest finished-instance data, and push it back. """
        if self.up_args.sync_main:
            assert rb_size > 0, "must use a replay buffer if doing sync_main"
        self._init_replay_buffer(rb_size)

        while True:
            assert self.from_main_q is not None
            data_q: Optional[Tuple[List[int], Dict[str, int]]] = self.from_main_q.get()
            if data_q is None:
                break
            times: Times = Times()

            step_probs, targ_update_nums = data_q
            for nnet_name, targ_update_num in targ_update_nums.items():
                self.set_targ_update_num(nnet_name, targ_update_num)
            self.initialize_fns()

            step_to_pathperf: Dict[int, PathFindPerf] = dict()
            while True:
                batch_size = to_q.get()
                if batch_size is None:
                    break

                pathfind: P = self.get_pathfind()
                # self._set_pathfind_nnet_fns(pathfind)

                insts_rem_last_itr: List[Inst] = []
                put_from_q: List[List[NDArray]] = []
                for _ in range(self.up_args.search_itrs):
                    # add instances
                    self._add_instances(pathfind, insts_rem_last_itr, batch_size, step_probs, times)
                    assert len(pathfind.instances) == batch_size, f"Values were {len(pathfind.instances)} and {batch_size}"

                    # step
                    if self.up_args.sync_main:
                        data: List[NDArray] = self._step_sync_main(pathfind, times)
                        _put_from_q([data], from_q, times)
                    else:
                        self._step(pathfind, times)

                    # remove instances
                    insts_rem_last_itr = pathfind.remove_finished_instances(self.up_args.search_itrs)
                    if len(insts_rem_last_itr) > 0:
                        put_from_q.append(self._get_instance_data(insts_rem_last_itr, rb_size, times))

                    # performance
                    start_time = time.time()
                    self._update_perf(insts_rem_last_itr, step_to_pathperf)
                    times.record_time("update_perf", time.time() - start_time)

                if not self.up_args.sync_main:
                    if len(pathfind.instances) > 0:
                        put_from_q.append(self._get_instance_data(pathfind.instances, rb_size, times))
                    _put_from_q(put_from_q, from_q, times)

                times.add_times(pathfind.times, path=["pathfinding"])

                start_time = time.time()
                del insts_rem_last_itr
                del put_from_q
                del pathfind
                gc.collect()
                times.record_time("gc", time.time() - start_time)

            from_q.put((times, step_to_pathperf))
            self.clear_nnet_fn_dict()
        self.to_main_q = None
        self.from_main_q = None
        self.nnet_par_info_main = None
```
