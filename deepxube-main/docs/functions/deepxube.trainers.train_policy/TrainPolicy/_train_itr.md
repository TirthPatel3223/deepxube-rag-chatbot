---
id: "func:deepxube.trainers.train_policy.TrainPolicy._train_itr"
kind: "method"
name: "_train_itr"
qualified_name: "deepxube.trainers.train_policy.TrainPolicy._train_itr"
module: "deepxube.trainers.train_policy"
file: "deepxube/trainers/train_policy.py"
line_start: 23
line_end: 33
class: "TrainPolicy"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "batch"
    annotation: "List[NDArray]"
    default: null
  - name: "first_itr_in_update"
    annotation: "bool"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "float"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [25, 32]
  - target: null
    expr: "self.nnet.train"
    call_sites: [27]
  - target: "func:deepxube.base.trainer.update_optimizer"
    expr: "update_optimizer"
    call_sites: [28]
  - target: "func:deepxube.trainers.utils.train_utils.train_policy_nnet_step"
    expr: "train_policy_nnet_step"
    call_sites: [29]
  - target: null
    expr: "self.writer.add_scalar"
    call_sites: [30]
  - target: null
    expr: "times.record_time"
    call_sites: [32]
raises: []
reads_attrs:
  - "self.device"
  - "self.nnet"
  - "self.optimizer"
  - "self.status"
  - "self.train_args"
  - "self.train_start_time"
  - "self.writer"
writes_attrs: []
---

# `deepxube.trainers.train_policy.TrainPolicy._train_itr`

**File:** [deepxube/trainers/train_policy.py:23](../../../../deepxube/trainers/train_policy.py#L23)
**Class:** `TrainPolicy`
**Visibility:** private
**Kind:** method

## Signature

```python
def _train_itr(self, batch: List[NDArray], first_itr_in_update: bool, times: Times) -> float
```

## Docstring

Run one policy gradient step; :return: scalar loss for this batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `batch` | `List[NDArray]` | — |
| `first_itr_in_update` | `bool` | — |
| `times` | `Times` | — |

## Returns

`float`

## Calls

- `time.time` → `func:time.time` (lines: 25, 32)
- `update_optimizer` → `func:deepxube.base.trainer.update_optimizer` (lines: 28)
- `train_policy_nnet_step` → `func:deepxube.trainers.utils.train_utils.train_policy_nnet_step` (lines: 29)

### Unresolved
- `self.nnet.train` (lines: 27)
- `self.writer.add_scalar` (lines: 30)
- `times.record_time` (lines: 32)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.device`
- `self.nnet`
- `self.optimizer`
- `self.status`
- `self.train_args`
- `self.train_start_time`
- `self.writer`

## Source

```python
    def _train_itr(self, batch: List[NDArray], first_itr_in_update: bool, times: Times) -> float:
        """ Run one policy gradient step; :return: scalar loss for this batch. """
        start_time = time.time()

        self.nnet.train()
        update_optimizer(self.optimizer, self.nnet, self.status.itr)
        loss = train_policy_nnet_step(self.nnet, batch, self.optimizer, self.device, self.status.itr, self.train_args, self.train_start_time)
        self.writer.add_scalar("train/loss", loss, self.status.itr)

        times.record_time("train", time.time() - start_time)
        return loss
```
