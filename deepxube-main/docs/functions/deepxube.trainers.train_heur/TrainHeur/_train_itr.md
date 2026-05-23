---
id: "func:deepxube.trainers.train_heur.TrainHeur._train_itr"
kind: "method"
name: "_train_itr"
qualified_name: "deepxube.trainers.train_heur.TrainHeur._train_itr"
module: "deepxube.trainers.train_heur"
file: "deepxube/trainers/train_heur.py"
line_start: 25
line_end: 41
class: "TrainHeur"
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
    call_sites: [27, 40]
  - target: "func:numpy.expand_dims"
    expr: "np.expand_dims"
    call_sites: [30]
  - target: null
    expr: "ctgs_batch_np.astype"
    call_sites: [30]
  - target: null
    expr: "self.nnet.train"
    call_sites: [32]
  - target: "func:deepxube.base.trainer.update_optimizer"
    expr: "update_optimizer"
    call_sites: [33]
  - target: "func:deepxube.trainers.utils.train_utils.train_heur_nnet_step"
    expr: "train_heur_nnet_step"
    call_sites: [34]
  - target: "func:torch.nn.MSELoss"
    expr: "nn.MSELoss"
    call_sites: [34]
  - target: null
    expr: "self.writer.add_scalar"
    call_sites: [36]
  - target: null
    expr: "times.record_time"
    call_sites: [40]
raises: []
reads_attrs:
  - "self.device"
  - "self.nnet"
  - "self.optimizer"
  - "self.status"
  - "self.train_args"
  - "self.train_start_time"
  - "self.train_summary"
  - "self.writer"
writes_attrs: []
---

# `deepxube.trainers.train_heur.TrainHeur._train_itr`

**File:** [deepxube/trainers/train_heur.py:25](../../../../deepxube/trainers/train_heur.py#L25)
**Class:** `TrainHeur`
**Visibility:** private
**Kind:** method

## Signature

```python
def _train_itr(self, batch: List[NDArray], first_itr_in_update: bool, times: Times) -> float
```

## Docstring

Run one MSE gradient step on the heuristic network; :return: scalar loss for this batch. 

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

- `time.time` → `func:time.time` (lines: 27, 40)
- `np.expand_dims` → `func:numpy.expand_dims` (lines: 30)
- `update_optimizer` → `func:deepxube.base.trainer.update_optimizer` (lines: 33)
- `train_heur_nnet_step` → `func:deepxube.trainers.utils.train_utils.train_heur_nnet_step` (lines: 34)
- `nn.MSELoss` → `func:torch.nn.MSELoss` (lines: 34)

### Unresolved
- `ctgs_batch_np.astype` (lines: 30)
- `self.nnet.train` (lines: 32)
- `self.writer.add_scalar` (lines: 36)
- `times.record_time` (lines: 40)

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
- `self.train_summary`
- `self.writer`

## Source

```python
    def _train_itr(self, batch: List[NDArray], first_itr_in_update: bool, times: Times) -> float:
        """ Run one MSE gradient step on the heuristic network; :return: scalar loss for this batch. """
        start_time = time.time()
        inputs_batch_np: List[NDArray] = batch[:-1]
        ctgs_batch_np: NDArray = batch[-1]
        ctgs_batch_np = np.expand_dims(ctgs_batch_np.astype(np.float32), 1)

        self.nnet.train()
        update_optimizer(self.optimizer, self.nnet, self.status.itr)
        ctgs_batch_nnet, loss = train_heur_nnet_step(self.nnet, inputs_batch_np, ctgs_batch_np, self.optimizer, nn.MSELoss(), self.device,
                                                     self.status.itr, self.train_args, self.train_start_time)
        self.writer.add_scalar("train/loss", loss, self.status.itr)

        if first_itr_in_update:
            self.train_summary.itr_to_in_out[self.status.itr] = (ctgs_batch_np, ctgs_batch_nnet)
        times.record_time("train", time.time() - start_time)
        return loss
```
