---
id: "func:deepxube.base.trainer.Train.update_step"
kind: "method"
name: "update_step"
qualified_name: "deepxube.base.trainer.Train.update_step"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 267
line_end: 320
class: "Train"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "self.db.clear"
    call_sites: [269]
  - target: null
    expr: "self.updater.up_args.get_up_gen_itrs"
    call_sites: [275]
  - target: null
    expr: "start_info_l.append"
    call_sites: [276, 278]
  - target: null
    expr: "format"
    call_sites: [276]
  - target: null
    expr: "print"
    call_sites: [279, 319, 320]
  - target: null
    expr: "', '.join"
    call_sites: [279]
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [280]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [283, 285, 288, 299, 301, 313, 318]
  - target: null
    expr: "self.updater.start_update"
    call_sites: [284]
  - target: null
    expr: "self.status.step_probs.tolist"
    call_sites: [284]
  - target: null
    expr: "times.record_time"
    call_sites: [285, 301, 318]
  - target: "func:deepxube.base.trainer.Train._get_update_data"
    expr: "self._get_update_data"
    call_sites: [291]
  - target: "func:deepxube.base.trainer.Train._end_update"
    expr: "self._end_update"
    call_sites: [292, 296]
  - target: "func:deepxube.base.trainer.Train._train"
    expr: "self._train"
    call_sites: [293]
  - target: "func:deepxube.base.trainer.Train._train_sync_main"
    expr: "self._train_sync_main"
    call_sites: [295]
  - target: "func:torch.save"
    expr: "torch.save"
    call_sites: [300]
  - target: null
    expr: "self.nnet.state_dict"
    call_sites: [300]
  - target: "func:shutil.copy"
    expr: "shutil.copy"
    call_sites: [309]
  - target: "func:pickle.dump"
    expr: "pickle.dump"
    call_sites: [315, 317]
  - target: null
    expr: "open"
    call_sites: [315, 317]
  - target: null
    expr: "times.get_time_str"
    call_sites: [320]
raises: []
reads_attrs:
  - "self.db"
  - "self.device"
  - "self.nnet"
  - "self.nnet_file"
  - "self.nnet_targ_file"
  - "self.on_gpu"
  - "self.status"
  - "self.status_file"
  - "self.train_args"
  - "self.train_start_time"
  - "self.train_summary"
  - "self.train_summary_file"
  - "self.updater"
writes_attrs:
  - "self.train_start_time"
---

# `deepxube.base.trainer.Train.update_step`

**File:** [deepxube/base/trainer.py:267](../../../../deepxube/base/trainer.py#L267)
**Class:** `Train`
**Visibility:** public
**Kind:** method

## Signature

```python
def update_step(self) -> None
```

## Docstring

One outer iteration: clear data buffer, run the updater, train for ``up_itrs`` steps, save checkpoints, possibly bump the target net. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 280)
- `time.time` → `func:time.time` (lines: 283, 285, 288, 299, 301, 313, 318)
- `self._get_update_data` → `func:deepxube.base.trainer.Train._get_update_data` (lines: 291)
- `self._end_update` → `func:deepxube.base.trainer.Train._end_update` (lines: 292, 296)
- `self._train` → `func:deepxube.base.trainer.Train._train` (lines: 293)
- `self._train_sync_main` → `func:deepxube.base.trainer.Train._train_sync_main` (lines: 295)
- `torch.save` → `func:torch.save` (lines: 300)
- `shutil.copy` → `func:shutil.copy` (lines: 309)
- `pickle.dump` → `func:pickle.dump` (lines: 315, 317)

### Unresolved
- `self.db.clear` (lines: 269)
- `self.updater.up_args.get_up_gen_itrs` (lines: 275)
- `start_info_l.append` (lines: 276, 278)
- `format` (lines: 276)
- `print` (lines: 279, 319, 320)
- `', '.join` (lines: 279)
- `self.updater.start_update` (lines: 284)
- `self.status.step_probs.tolist` (lines: 284)
- `times.record_time` (lines: 285, 301, 318)
- `self.nnet.state_dict` (lines: 300)
- `open` (lines: 315, 317)
- `times.get_time_str` (lines: 320)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.train_start_time`

**Reads:**
- `self.db`
- `self.device`
- `self.nnet`
- `self.nnet_file`
- `self.nnet_targ_file`
- `self.on_gpu`
- `self.status`
- `self.status_file`
- `self.train_args`
- `self.train_start_time`
- `self.train_summary`
- `self.train_summary_file`
- `self.updater`

## Source

```python
    def update_step(self) -> None:
        """ One outer iteration: clear data buffer, run the updater, train for ``up_itrs`` steps, save checkpoints, possibly bump the target net. """
        self.db.clear()
        itr_init: int = self.status.itr

        # print info
        start_info_l: List[str] = [f"itr: {self.status.itr}", f"update_num: {self.status.update_num}", f"targ_update: {self.status.targ_update_num}"]

        num_gen: int = self.train_args.batch_size * self.updater.up_args.get_up_gen_itrs()
        start_info_l.append(f"num_gen: {format(num_gen, ',')}")
        if self.train_args.balance_steps:
            start_info_l.append(f"step max (curr): {self.status.step_max_curr}")
        print(f"\nGetting Data - {', '.join(start_info_l)}")
        times: Times = Times()

        # start updater
        start_time = time.time()
        self.updater.start_update(self.status.step_probs.tolist(), num_gen, self.train_args.batch_size, self.device, self.on_gpu)
        times.record_time("up_start", time.time() - start_time)

        # do training
        self.train_start_time = time.time()
        loss: float
        if not self.updater.up_args.sync_main:
            self._get_update_data(num_gen, times)
            self._end_update(itr_init, times)
            loss = self._train(times)
        else:
            loss = self._train_sync_main(num_gen, times)
            self._end_update(itr_init, times)

        # save nnet
        start_time = time.time()
        torch.save(self.nnet.state_dict(), self.nnet_file)
        times.record_time("save_net", time.time() - start_time)

        # update nnet
        update_targ: bool = False
        if loss < self.train_args.loss_thresh:
            update_targ = True

        if update_targ:
            shutil.copy(self.nnet_file, self.nnet_targ_file)
            self.status.targ_update_num = self.status.targ_update_num + 1
        self.status.update_num += 1

        start_time = time.time()
        # noinspection PyTypeChecker
        pickle.dump(self.status, open(self.status_file, "wb"), protocol=-1)
        # noinspection PyTypeChecker
        pickle.dump(self.train_summary, open(self.train_summary_file, "wb"), protocol=-1)
        times.record_time("save_status", time.time() - start_time)
        print(f"Train - itrs: {self.updater.up_args.up_itrs}, loss: {loss:.2E}, targ_updated: {update_targ}")
        print(f"Times - {times.get_time_str()}")
```
