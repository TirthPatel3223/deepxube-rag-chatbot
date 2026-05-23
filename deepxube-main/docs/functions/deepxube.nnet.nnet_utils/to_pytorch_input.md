---
id: "func:deepxube.nnet.nnet_utils.to_pytorch_input"
kind: "function"
name: "to_pytorch_input"
qualified_name: "deepxube.nnet.nnet_utils.to_pytorch_input"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 22
line_end: 29
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "states_nnet"
    annotation: "List[NDArray[Any]]"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
returns: "List[Tensor]"
docstring_source: "present"
callees:
  - target: "func:torch.tensor"
    expr: "torch.tensor"
    call_sites: [26]
  - target: null
    expr: "states_nnet_tensors.append"
    call_sites: [27]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.to_pytorch_input`

**File:** [deepxube/nnet/nnet_utils.py:22](../../../../deepxube/nnet/nnet_utils.py#L22)
**Visibility:** public
**Kind:** function

## Signature

```python
def to_pytorch_input(states_nnet: List[NDArray[Any]], device: torch.device) -> List[Tensor]
```

## Docstring

:return: List of Tensors created from ``states_nnet`` numpy arrays and placed on ``device``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `states_nnet` | `List[NDArray[Any]]` | — |
| `device` | `torch.device` | — |

## Returns

`List[Tensor]`

## Calls

- `torch.tensor` → `func:torch.tensor` (lines: 26)

### Unresolved
- `states_nnet_tensors.append` (lines: 27)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def to_pytorch_input(states_nnet: List[NDArray[Any]], device: torch.device) -> List[Tensor]:
    """ :return: List of Tensors created from ``states_nnet`` numpy arrays and placed on ``device``. """
    states_nnet_tensors = []
    for tensor_np in states_nnet:
        tensor = torch.tensor(tensor_np, device=device)
        states_nnet_tensors.append(tensor)

    return states_nnet_tensors
```
