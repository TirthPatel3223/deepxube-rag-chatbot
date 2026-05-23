---
id: "func:deepxube.base.trainer.Train._train"
kind: "method"
name: "_train"
qualified_name: "deepxube.base.trainer.Train._train"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 331
line_end: 346
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
  - name: "times"
    annotation: "Times"
    default: null
returns: "float"
docstring_source: "present"
callees:
  - target: null
    expr: "range"
    call_sites: [335]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [337, 339]
  - target: null
    expr: "self.db.sample"
    call_sites: [338]
  - target: null
    expr: "times.record_time"
    call_sites: [339]
  - target: "func:deepxube.base.trainer.Train._train_itr"
    expr: "self._train_itr"
    call_sites: [342]
raises: []
reads_attrs:
  - "self.db"
  - "self.status"
  - "self.train_args"
  - "self.updater"
writes_attrs: []
---

# `deepxube.base.trainer.Train._train`

**File:** [deepxube/base/trainer.py:331](../../../../deepxube/base/trainer.py#L331)
**Class:** `Train`
**Visibility:** private
**Kind:** method

## Signature

```python
def _train(self, times: Times) -> float
```

## Docstring

Run ``up_itrs`` training iterations against the data buffer; return the last loss. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `times` | `Times` | — |

## Returns

`float`

## Calls

- `time.time` → `func:time.time` (lines: 337, 339)
- `self._train_itr` → `func:deepxube.base.trainer.Train._train_itr` (lines: 342)

### Unresolved
- `range` (lines: 335)
- `self.db.sample` (lines: 338)
- `times.record_time` (lines: 339)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.db`
- `self.status`
- `self.train_args`
- `self.updater`

## Source

```python
    def _train(self, times: Times) -> float:
        """ Run ``up_itrs`` training iterations against the data buffer; return the last loss. """
        loss: float = np.inf
        first_itr_in_update: bool = True
        for _ in range(self.updater.up_args.up_itrs):
            # sample data
            start_time = time.time()
            batch: List[NDArray] = self.db.sample(self.train_args.batch_size)
            times.record_time("data_samp", time.time() - start_time)

            # train
            loss = self._train_itr(batch, first_itr_in_update, times)
            first_itr_in_update = False
            self.status.itr += 1

        return loss
```
