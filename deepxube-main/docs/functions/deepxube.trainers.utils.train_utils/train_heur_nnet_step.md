---
id: "func:deepxube.trainers.utils.train_utils.train_heur_nnet_step"
kind: "function"
name: "train_heur_nnet_step"
qualified_name: "deepxube.trainers.utils.train_utils.train_heur_nnet_step"
module: "deepxube.trainers.utils.train_utils"
file: "deepxube/trainers/utils/train_utils.py"
line_start: 36
line_end: 67
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "nnet"
    annotation: "nn.Module"
    default: null
  - name: "inputs_np"
    annotation: "List[NDArray]"
    default: null
  - name: "ctgs_np"
    annotation: "NDArray"
    default: null
  - name: "optimizer"
    annotation: "Optimizer"
    default: null
  - name: "criterion"
    annotation: "nn.Module"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "train_itr"
    annotation: "int"
    default: null
  - name: "train_args"
    annotation: "TrainArgs"
    default: null
  - name: "start_time"
    annotation: "float"
    default: null
returns: "Tuple[NDArray, float]"
docstring_source: "present"
callees:
  - target: null
    expr: "nnet.train"
    call_sites: [40]
  - target: null
    expr: "optimizer.zero_grad"
    call_sites: [43]
  - target: "func:deepxube.nnet.nnet_utils.to_pytorch_input"
    expr: "nnet_utils.to_pytorch_input"
    call_sites: [46]
  - target: "func:torch.tensor"
    expr: "torch.tensor"
    call_sites: [47]
  - target: "func:deepxube.trainers.utils.train_utils.nnet"
    expr: "nnet"
    call_sites: [50]
  - target: null
    expr: "ctgs_nnet.size"
    call_sites: [53]
  - target: null
    expr: "ctgs_batch.size"
    call_sites: [53]
  - target: "func:deepxube.trainers.utils.train_utils.criterion"
    expr: "criterion"
    call_sites: [54]
  - target: null
    expr: "loss.backward"
    call_sites: [57]
  - target: null
    expr: "optimizer.step"
    call_sites: [60]
  - target: null
    expr: "print"
    call_sites: [64]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [65]
  - target: null
    expr: "loss.item"
    call_sites: [65, 67]
  - target: null
    expr: "ctgs_batch.mean().item"
    call_sites: [65]
  - target: null
    expr: "ctgs_batch.mean"
    call_sites: [65]
  - target: null
    expr: "ctgs_nnet.mean().item"
    call_sites: [65]
  - target: null
    expr: "ctgs_nnet.mean"
    call_sites: [65]
  - target: null
    expr: "ctgs_nnet.cpu().data.numpy"
    call_sites: [67]
  - target: null
    expr: "ctgs_nnet.cpu"
    call_sites: [67]
  - target: null
    expr: "float"
    call_sites: [67]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_utils.train_heur_nnet_step`

**File:** [deepxube/trainers/utils/train_utils.py:36](../../../../deepxube/trainers/utils/train_utils.py#L36)
**Visibility:** public
**Kind:** function

## Signature

```python
def train_heur_nnet_step(nnet: nn.Module, inputs_np: List[NDArray], ctgs_np: NDArray, optimizer: Optimizer, criterion: nn.Module, device: torch.device, train_itr: int, train_args: TrainArgs, start_time: float) -> Tuple[NDArray, float]
```

## Docstring

Run one optimizer step on the heuristic network with ``criterion`` loss; :return: ``(nnet predictions, loss)``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `nnet` | `nn.Module` | — |
| `inputs_np` | `List[NDArray]` | — |
| `ctgs_np` | `NDArray` | — |
| `optimizer` | `Optimizer` | — |
| `criterion` | `nn.Module` | — |
| `device` | `torch.device` | — |
| `train_itr` | `int` | — |
| `train_args` | `TrainArgs` | — |
| `start_time` | `float` | — |

## Returns

`Tuple[NDArray, float]`

## Calls

- `nnet_utils.to_pytorch_input` → `func:deepxube.nnet.nnet_utils.to_pytorch_input` (lines: 46)
- `torch.tensor` → `func:torch.tensor` (lines: 47)
- `nnet` → `func:deepxube.trainers.utils.train_utils.nnet` (lines: 50)
- `criterion` → `func:deepxube.trainers.utils.train_utils.criterion` (lines: 54)
- `time.time` → `func:time.time` (lines: 65)

### Unresolved
- `nnet.train` (lines: 40)
- `optimizer.zero_grad` (lines: 43)
- `ctgs_nnet.size` (lines: 53)
- `ctgs_batch.size` (lines: 53)
- `loss.backward` (lines: 57)
- `optimizer.step` (lines: 60)
- `print` (lines: 64)
- `loss.item` (lines: 65, 67)
- `ctgs_batch.mean().item` (lines: 65)
- `ctgs_batch.mean` (lines: 65)
- `ctgs_nnet.mean().item` (lines: 65)
- `ctgs_nnet.mean` (lines: 65)
- `ctgs_nnet.cpu().data.numpy` (lines: 67)
- `ctgs_nnet.cpu` (lines: 67)
- `float` (lines: 67)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def train_heur_nnet_step(nnet: nn.Module, inputs_np: List[NDArray], ctgs_np: NDArray, optimizer: Optimizer,
                         criterion: nn.Module, device: torch.device, train_itr: int, train_args: TrainArgs, start_time: float) -> Tuple[NDArray, float]:
    """ Run one optimizer step on the heuristic network with ``criterion`` loss; :return: ``(nnet predictions, loss)``. """
    # train network
    nnet.train()

    # zero the parameter gradients
    optimizer.zero_grad()

    # send data to device
    inputs_batch: List[Tensor] = nnet_utils.to_pytorch_input(inputs_np, device)
    ctgs_batch: Tensor = torch.tensor(ctgs_np, device=device)

    # forward
    ctgs_nnet: Tensor = nnet(inputs_batch)[0]

    # loss
    assert ctgs_nnet.size() == ctgs_batch.size()
    loss = criterion(ctgs_nnet, ctgs_batch)

    # backwards
    loss.backward()

    # step
    optimizer.step()

    # display progress
    if (train_args.display > 0) and (train_itr % train_args.display == 0):
        print("Itr: %i, loss: %.2E, targ_ctg: %.2f, nnet_ctg: %.2f, "
              f"Time: {time.time() - start_time:.2f}" % (train_itr, loss.item(), ctgs_batch.mean().item(), ctgs_nnet.mean().item()))

    return ctgs_nnet.cpu().data.numpy(), float(loss.item())
```
