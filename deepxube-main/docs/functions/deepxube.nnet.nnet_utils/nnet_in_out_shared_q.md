---
id: "func:deepxube.nnet.nnet_utils.nnet_in_out_shared_q"
kind: "function"
name: "nnet_in_out_shared_q"
qualified_name: "deepxube.nnet.nnet_utils.nnet_in_out_shared_q"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 133
line_end: 148
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
  - name: "inputs_nnet_shm"
    annotation: "List[SharedNDArray]"
    default: null
  - name: "batch_size"
    annotation: "Optional[int]"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "nnet_o_q"
    annotation: "Queue"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "range"
    call_sites: [138]
  - target: null
    expr: "len"
    call_sites: [138]
  - target: null
    expr: "inputs_nnet.append"
    call_sites: [139]
  - target: "func:deepxube.nnet.nnet_utils.nnet_batched"
    expr: "nnet_batched"
    call_sites: [141]
  - target: "func:deepxube.utils.data_utils.np_to_shnd"
    expr: "np_to_shnd"
    call_sites: [144]
  - target: null
    expr: "nnet_o_q.put"
    call_sites: [145]
  - target: null
    expr: "arr_shm.close"
    call_sites: [148]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.nnet_in_out_shared_q`

**File:** [deepxube/nnet/nnet_utils.py:133](../../../../deepxube/nnet/nnet_utils.py#L133)
**Visibility:** public
**Kind:** function

## Signature

```python
def nnet_in_out_shared_q(nnet: nn.Module, inputs_nnet_shm: List[SharedNDArray], batch_size: Optional[int], device: torch.device, nnet_o_q: Queue) -> None
```

## Docstring

Read shared-memory inputs, run batched inference, and push shared-memory outputs to ``nnet_o_q``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `nnet` | `nn.Module` | — |
| `inputs_nnet_shm` | `List[SharedNDArray]` | — |
| `batch_size` | `Optional[int]` | — |
| `device` | `torch.device` | — |
| `nnet_o_q` | `Queue` | — |

## Returns

`None`

## Calls

- `nnet_batched` → `func:deepxube.nnet.nnet_utils.nnet_batched` (lines: 141)
- `np_to_shnd` → `func:deepxube.utils.data_utils.np_to_shnd` (lines: 144)

### Unresolved
- `range` (lines: 138)
- `len` (lines: 138)
- `inputs_nnet.append` (lines: 139)
- `nnet_o_q.put` (lines: 145)
- `arr_shm.close` (lines: 148)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def nnet_in_out_shared_q(nnet: nn.Module, inputs_nnet_shm: List[SharedNDArray], batch_size: Optional[int],
                         device: torch.device, nnet_o_q: Queue) -> None:
    """ Read shared-memory inputs, run batched inference, and push shared-memory outputs to ``nnet_o_q``. """
    # get outputs
    inputs_nnet: List[NDArray] = []
    for inputs_idx in range(len(inputs_nnet_shm)):
        inputs_nnet.append(inputs_nnet_shm[inputs_idx].array)

    outputs_l: List[NDArray[np.float64]] = nnet_batched(nnet, inputs_nnet, batch_size, device)

    # send outputs
    outputs_l_shm: List[SharedNDArray] = [np_to_shnd(outputs) for outputs in outputs_l]
    nnet_o_q.put(outputs_l_shm)

    for arr_shm in inputs_nnet_shm + outputs_l_shm:
        arr_shm.close()
```
