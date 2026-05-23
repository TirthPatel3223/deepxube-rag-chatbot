---
id: "func:deepxube.base.trainer.Train._train_sync_main"
kind: "method"
name: "_train_sync_main"
qualified_name: "deepxube.base.trainer.Train._train_sync_main"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 348
line_end: 385
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
  - name: "num_gen"
    annotation: "int"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "float"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [356, 377]
  - target: null
    expr: "self.db.size"
    call_sites: [357, 361]
  - target: null
    expr: "self.db.sample"
    call_sites: [358]
  - target: null
    expr: "self.nnet.eval"
    call_sites: [360]
  - target: "func:deepxube.utils.data_utils.get_nowait_noerr"
    expr: "get_nowait_noerr"
    call_sites: [363]
  - target: "func:deepxube.nnet.nnet_utils.nnet_in_out_shared_q"
    expr: "nnet_in_out_shared_q"
    call_sites: [366]
  - target: null
    expr: "self.updater.get_update_data"
    call_sites: [370]
  - target: null
    expr: "self.db.add"
    call_sites: [372]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [373]
  - target: "func:deepxube.utils.data_utils.sel_l"
    expr: "sel_l"
    call_sites: [375]
  - target: null
    expr: "times.record_time"
    call_sites: [377]
  - target: "func:deepxube.base.trainer.Train._train_itr"
    expr: "self._train_itr"
    call_sites: [380]
raises: []
reads_attrs:
  - "self.db"
  - "self.device"
  - "self.from_main_qs"
  - "self.nnet"
  - "self.status"
  - "self.to_main_q"
  - "self.train_args"
  - "self.updater"
writes_attrs: []
---

# `deepxube.base.trainer.Train._train_sync_main`

**File:** [deepxube/base/trainer.py:348](../../../../deepxube/base/trainer.py#L348)
**Class:** `Train`
**Visibility:** private
**Kind:** method

## Signature

```python
def _train_sync_main(self, num_gen: int, times: Times) -> float
```

## Docstring

``sync_main`` variant: interleave training iterations with serving worker NNet inference requests on the main process. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_gen` | `int` | — |
| `times` | `Times` | — |

## Returns

`float`

## Calls

- `time.time` → `func:time.time` (lines: 356, 377)
- `get_nowait_noerr` → `func:deepxube.utils.data_utils.get_nowait_noerr` (lines: 363)
- `nnet_in_out_shared_q` → `func:deepxube.nnet.nnet_utils.nnet_in_out_shared_q` (lines: 366)
- `np.arange` → `func:numpy.arange` (lines: 373)
- `sel_l` → `func:deepxube.utils.data_utils.sel_l` (lines: 375)
- `self._train_itr` → `func:deepxube.base.trainer.Train._train_itr` (lines: 380)

### Unresolved
- `self.db.size` (lines: 357, 361)
- `self.db.sample` (lines: 358)
- `self.nnet.eval` (lines: 360)
- `self.updater.get_update_data` (lines: 370)
- `self.db.add` (lines: 372)
- `times.record_time` (lines: 377)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.db`
- `self.device`
- `self.from_main_qs`
- `self.nnet`
- `self.status`
- `self.to_main_q`
- `self.train_args`
- `self.updater`

## Source

```python
    def _train_sync_main(self, num_gen: int, times: Times) -> float:
        """ ``sync_main`` variant: interleave training iterations with serving worker NNet inference requests on the main process. """
        loss: float = np.inf
        update_train_itr: int = 0
        first_itr_in_update: bool = True
        while update_train_itr < self.updater.up_args.up_itrs:
            batch: List[NDArray]
            # data from updater should not be more that train_args.batch_size
            start_time = time.time()
            if self.db.size() == num_gen:
                batch = self.db.sample(self.train_args.batch_size)
            else:
                self.nnet.eval()
                while self.db.size() < ((update_train_itr + 1) * self.train_args.batch_size):
                    # get heuristic values for ongoing search
                    q_res: Optional[Tuple[int, List[SharedNDArray]]] = get_nowait_noerr(self.to_main_q)
                    if q_res is not None:
                        proc_id, inputs_np_shm = q_res
                        nnet_in_out_shared_q(self.nnet, inputs_np_shm, self.updater.up_args.nnet_batch_size,
                                             self.device, self.from_main_qs[proc_id])

                    # get update data
                    data_l_i: List[List[NDArray]] = self.updater.get_update_data(nowait=True)
                    for data in data_l_i:
                        self.db.add(data)
                sel_idxs: NDArray = np.arange(update_train_itr * self.train_args.batch_size,
                                              (update_train_itr + 1) * self.train_args.batch_size)
                batch = sel_l(self.db.arrays, sel_idxs)

            times.record_time("up_data", time.time() - start_time)

            # train
            loss = self._train_itr(batch, first_itr_in_update, times)
            update_train_itr += 1
            first_itr_in_update = False
            self.status.itr += 1

        return loss
```
