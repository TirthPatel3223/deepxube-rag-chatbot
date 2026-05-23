---
id: "func:deepxube.nnet.nnet_utils.nnet_fn_runner"
kind: "function"
name: "nnet_fn_runner"
qualified_name: "deepxube.nnet.nnet_utils.nnet_fn_runner"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 152
line_end: 175
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "nnet_i_q"
    annotation: "Queue"
    default: null
  - name: "nnet_o_qs"
    annotation: "List[Queue]"
    default: null
  - name: "model_file"
    annotation: "str"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "on_gpu"
    annotation: "bool"
    default: null
  - name: "gpu_num"
    annotation: "int"
    default: null
  - name: "get_nnet"
    annotation: "Callable[[], nn.Module]"
    default: null
  - name: "batch_size"
    annotation: "Optional[int]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "str"
    call_sites: [157]
  - target: "func:torch.set_num_threads"
    expr: "torch.set_num_threads"
    call_sites: [159]
  - target: "func:deepxube.nnet.nnet_utils.get_nnet"
    expr: "get_nnet"
    call_sites: [160]
  - target: "func:deepxube.nnet.nnet_utils.load_nnet"
    expr: "load_nnet"
    call_sites: [161]
  - target: null
    expr: "nnet.eval"
    call_sites: [162]
  - target: null
    expr: "nnet.to"
    call_sites: [163]
  - target: null
    expr: "nnet_i_q.get"
    call_sites: [170]
  - target: "func:deepxube.nnet.nnet_utils.nnet_in_out_shared_q"
    expr: "nnet_in_out_shared_q"
    call_sites: [175]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.nnet_fn_runner`

**File:** [deepxube/nnet/nnet_utils.py:152](../../../../deepxube/nnet/nnet_utils.py#L152)
**Visibility:** public
**Kind:** function

## Signature

```python
def nnet_fn_runner(nnet_i_q: Queue, nnet_o_qs: List[Queue], model_file: str, device: torch.device, on_gpu: bool, gpu_num: int, get_nnet: Callable[[], nn.Module], batch_size: Optional[int]) -> None
```

## Docstring

Worker loop: load the nnet from ``model_file``, serve inference requests from ``nnet_i_q``, and exit on the
``(None, None)`` sentinel. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `nnet_i_q` | `Queue` | — |
| `nnet_o_qs` | `List[Queue]` | — |
| `model_file` | `str` | — |
| `device` | `torch.device` | — |
| `on_gpu` | `bool` | — |
| `gpu_num` | `int` | — |
| `get_nnet` | `Callable[[], nn.Module]` | — |
| `batch_size` | `Optional[int]` | — |

## Returns

`None`

## Calls

- `torch.set_num_threads` → `func:torch.set_num_threads` (lines: 159)
- `get_nnet` → `func:deepxube.nnet.nnet_utils.get_nnet` (lines: 160)
- `load_nnet` → `func:deepxube.nnet.nnet_utils.load_nnet` (lines: 161)
- `nnet_in_out_shared_q` → `func:deepxube.nnet.nnet_utils.nnet_in_out_shared_q` (lines: 175)

### Unresolved
- `str` (lines: 157)
- `nnet.eval` (lines: 162)
- `nnet.to` (lines: 163)
- `nnet_i_q.get` (lines: 170)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def nnet_fn_runner(nnet_i_q: Queue, nnet_o_qs: List[Queue], model_file: str, device: torch.device, on_gpu: bool,
                   gpu_num: int, get_nnet: Callable[[], nn.Module], batch_size: Optional[int]) -> None:
    """ Worker loop: load the nnet from ``model_file``, serve inference requests from ``nnet_i_q``, and exit on the
    ``(None, None)`` sentinel. """
    if (gpu_num is not None) and on_gpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu_num)

    torch.set_num_threads(1)
    nnet: nn.Module = get_nnet()
    nnet = load_nnet(model_file, nnet, device=device)
    nnet.eval()
    nnet.to(device)
    # if on_gpu:
    #    nnet = nn.DataParallel(nnet)

    while True:
        # get from input q
        inputs_nnet_shm: Optional[List[SharedNDArray]]
        proc_id, inputs_nnet_shm = nnet_i_q.get()
        if proc_id is None:
            break

        # nnet in/out
        nnet_in_out_shared_q(nnet, inputs_nnet_shm, batch_size, device, nnet_o_qs[proc_id])
```
