---
id: "func:deepxube.nnet.nnet_utils.nnet_batched"
kind: "function"
name: "nnet_batched"
qualified_name: "deepxube.nnet.nnet_utils.nnet_batched"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 82
line_end: 122
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
  - name: "inputs"
    annotation: "List[NDArray[Any]]"
    default: null
  - name: "batch_size"
    annotation: "Optional[int]"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
returns: "List[NDArray[np.float64]]"
docstring_source: "present"
callees:
  - target: null
    expr: "min"
    call_sites: [98]
  - target: "func:deepxube.nnet.nnet_utils.to_pytorch_input"
    expr: "to_pytorch_input"
    call_sites: [102]
  - target: "func:deepxube.nnet.nnet_utils.nnet"
    expr: "nnet"
    call_sites: [104]
  - target: null
    expr: "outputs_batch_t.cpu().data.numpy"
    call_sites: [105]
  - target: null
    expr: "outputs_batch_t.cpu"
    call_sites: [105]
  - target: null
    expr: "len"
    call_sites: [108, 110, 112, 119]
  - target: null
    expr: "range"
    call_sites: [112, 119]
  - target: null
    expr: "outputs_batch_l[out_idx].astype"
    call_sites: [113]
  - target: null
    expr: "outputs_l_l.append"
    call_sites: [114]
  - target: "func:deepxube.utils.data_utils.combine_l_l"
    expr: "combine_l_l"
    call_sites: [118]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.nnet_batched`

**File:** [deepxube/nnet/nnet_utils.py:82](../../../../deepxube/nnet/nnet_utils.py#L82)
**Visibility:** public
**Kind:** function

## Signature

```python
def nnet_batched(nnet: nn.Module, inputs: List[NDArray[Any]], batch_size: Optional[int], device: torch.device) -> List[NDArray[np.float64]]
```

## Docstring

Run ``nnet`` on ``inputs`` in chunks of ``batch_size`` and :return: per-output arrays concatenated across all
batches. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `nnet` | `nn.Module` | — |
| `inputs` | `List[NDArray[Any]]` | — |
| `batch_size` | `Optional[int]` | — |
| `device` | `torch.device` | — |

## Returns

`List[NDArray[np.float64]]`

## Calls

- `to_pytorch_input` → `func:deepxube.nnet.nnet_utils.to_pytorch_input` (lines: 102)
- `nnet` → `func:deepxube.nnet.nnet_utils.nnet` (lines: 104)
- `combine_l_l` → `func:deepxube.utils.data_utils.combine_l_l` (lines: 118)

### Unresolved
- `min` (lines: 98)
- `outputs_batch_t.cpu().data.numpy` (lines: 105)
- `outputs_batch_t.cpu` (lines: 105)
- `len` (lines: 108, 110, 112, 119)
- `range` (lines: 112, 119)
- `outputs_batch_l[out_idx].astype` (lines: 113)
- `outputs_l_l.append` (lines: 114)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def nnet_batched(nnet: nn.Module, inputs: List[NDArray[Any]], batch_size: Optional[int],
                 device: torch.device) -> List[NDArray[np.float64]]:
    """ Run ``nnet`` on ``inputs`` in chunks of ``batch_size`` and :return: per-output arrays concatenated across all
    batches. """
    outputs_l_l: List[List[NDArray[np.float64]]] = []

    num_states: int = inputs[0].shape[0]

    batch_size_inst: int = num_states
    if batch_size is not None:
        batch_size_inst = batch_size

    start_idx: int = 0
    num_outputs: Optional[int] = None
    while start_idx < num_states:
        # get batch
        end_idx: int = min(start_idx + batch_size_inst, num_states)
        inputs_batch = [x[start_idx:end_idx] for x in inputs]

        # get nnet output
        inputs_batch_t = to_pytorch_input(inputs_batch, device)

        outputs_batch_t_l: List[Tensor] = nnet(inputs_batch_t)
        outputs_batch_l: List[NDArray[np.float64]] = [outputs_batch_t.cpu().data.numpy()
                                                      for outputs_batch_t in outputs_batch_t_l]
        if num_outputs is None:
            num_outputs = len(outputs_batch_l)
        else:
            assert len(outputs_batch_l) == num_outputs, f"{len(outputs_batch_l)} != {num_outputs}"

        for out_idx in range(len(outputs_batch_l)):
            outputs_batch_l[out_idx] = outputs_batch_l[out_idx].astype(np.float64)
        outputs_l_l.append(outputs_batch_l)

        start_idx = end_idx

    outputs_l: List[NDArray[np.float64]] = combine_l_l(outputs_l_l, "concat")
    for out_idx in range(len(outputs_l)):
        assert (outputs_l[out_idx].shape[0] == num_states)

    return outputs_l
```
