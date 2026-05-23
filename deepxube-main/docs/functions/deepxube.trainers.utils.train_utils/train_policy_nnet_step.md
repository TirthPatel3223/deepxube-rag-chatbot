---
id: "func:deepxube.trainers.utils.train_utils.train_policy_nnet_step"
kind: "function"
name: "train_policy_nnet_step"
qualified_name: "deepxube.trainers.utils.train_utils.train_policy_nnet_step"
module: "deepxube.trainers.utils.train_utils"
file: "deepxube/trainers/utils/train_utils.py"
line_start: 70
line_end: 96
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "policy"
    annotation: "PolicyNNet"
    default: null
  - name: "states_goals_actions_np"
    annotation: "List[NDArray]"
    default: null
  - name: "optimizer"
    annotation: "Optimizer"
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
returns: "float"
docstring_source: "present"
callees:
  - target: null
    expr: "policy.train"
    call_sites: [74]
  - target: null
    expr: "optimizer.zero_grad"
    call_sites: [77]
  - target: "func:deepxube.nnet.nnet_utils.to_pytorch_input"
    expr: "nnet_utils.to_pytorch_input"
    call_sites: [80]
  - target: null
    expr: "policy.train_fprop"
    call_sites: [83]
  - target: null
    expr: "loss.backward"
    call_sites: [86]
  - target: null
    expr: "optimizer.step"
    call_sites: [89]
  - target: null
    expr: "print"
    call_sites: [93]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [94]
  - target: null
    expr: "loss.item"
    call_sites: [94, 96]
  - target: null
    expr: "float"
    call_sites: [96]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_utils.train_policy_nnet_step`

**File:** [deepxube/trainers/utils/train_utils.py:70](../../../../deepxube/trainers/utils/train_utils.py#L70)
**Visibility:** public
**Kind:** function

## Signature

```python
def train_policy_nnet_step(policy: PolicyNNet, states_goals_actions_np: List[NDArray], optimizer: Optimizer, device: torch.device, train_itr: int, train_args: TrainArgs, start_time: float) -> float
```

## Docstring

Run one optimizer step on the policy network using its own VAE loss; :return: scalar loss. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `policy` | `PolicyNNet` | — |
| `states_goals_actions_np` | `List[NDArray]` | — |
| `optimizer` | `Optimizer` | — |
| `device` | `torch.device` | — |
| `train_itr` | `int` | — |
| `train_args` | `TrainArgs` | — |
| `start_time` | `float` | — |

## Returns

`float`

## Calls

- `nnet_utils.to_pytorch_input` → `func:deepxube.nnet.nnet_utils.to_pytorch_input` (lines: 80)
- `time.time` → `func:time.time` (lines: 94)

### Unresolved
- `policy.train` (lines: 74)
- `optimizer.zero_grad` (lines: 77)
- `policy.train_fprop` (lines: 83)
- `loss.backward` (lines: 86)
- `optimizer.step` (lines: 89)
- `print` (lines: 93)
- `loss.item` (lines: 94, 96)
- `float` (lines: 96)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def train_policy_nnet_step(policy: PolicyNNet, states_goals_actions_np: List[NDArray], optimizer: Optimizer, device: torch.device,
                           train_itr: int, train_args: TrainArgs, start_time: float) -> float:
    """ Run one optimizer step on the policy network using its own VAE loss; :return: scalar loss. """
    # train network
    policy.train()

    # zero the parameter gradients
    optimizer.zero_grad()

    # send data to device
    states_goals_actions: List[Tensor] = nnet_utils.to_pytorch_input(states_goals_actions_np, device)

    # forward
    loss, print_str = policy.train_fprop(states_goals_actions)

    # backwards
    loss.backward()

    # step
    optimizer.step()

    # display progress
    if (train_args.display > 0) and (train_itr % train_args.display == 0):
        print(f"Itr: %i, loss: %.2E, {print_str}, "
              f"Time: {time.time() - start_time:.2f}" % (train_itr, loss.item()))

    return float(loss.item())
```
