---
id: "func:deepxube.nnet.nnet_utils.start_nnet_fn_runners"
kind: "function"
name: "start_nnet_fn_runners"
qualified_name: "deepxube.nnet.nnet_utils.start_nnet_fn_runners"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 193
line_end: 217
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "get_nnet"
    annotation: "Callable[[], nn.Module]"
    default: null
  - name: "nnet_par_infos"
    annotation: "List[NNetParInfo]"
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
  - name: "batch_size"
    annotation: "Optional[int]"
    default: "None"
returns: "List[BaseProcess]"
docstring_source: "present"
callees:
  - target: "func:torch.multiprocessing.get_context"
    expr: "get_context"
    call_sites: [197]
  - target: null
    expr: "len"
    call_sites: [203]
  - target: null
    expr: "int"
    call_sites: [204]
  - target: null
    expr: "os.environ['CUDA_VISIBLE_DEVICES'].split"
    call_sites: [204]
  - target: null
    expr: "ctx.Process"
    call_sites: [210]
  - target: null
    expr: "nnet_fn_procs.start"
    call_sites: [214]
  - target: null
    expr: "nnet_procs.append"
    call_sites: [215]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.start_nnet_fn_runners`

**File:** [deepxube/nnet/nnet_utils.py:193](../../../../deepxube/nnet/nnet_utils.py#L193)
**Visibility:** public
**Kind:** function

## Signature

```python
def start_nnet_fn_runners(get_nnet: Callable[[], nn.Module], nnet_par_infos: List[NNetParInfo], model_file: str, device: torch.device, on_gpu: bool, batch_size: Optional[int] = None) -> List[BaseProcess]
```

## Docstring

Spawn one nnet runner process per visible GPU (or one CPU process); :return: the list of started processes. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `get_nnet` | `Callable[[], nn.Module]` | — |
| `nnet_par_infos` | `List[NNetParInfo]` | — |
| `model_file` | `str` | — |
| `device` | `torch.device` | — |
| `on_gpu` | `bool` | — |
| `batch_size` | `Optional[int]` | `None` |

## Returns

`List[BaseProcess]`

## Calls

- `get_context` → `func:torch.multiprocessing.get_context` (lines: 197)

### Unresolved
- `len` (lines: 203)
- `int` (lines: 204)
- `os.environ['CUDA_VISIBLE_DEVICES'].split` (lines: 204)
- `ctx.Process` (lines: 210)
- `nnet_fn_procs.start` (lines: 214)
- `nnet_procs.append` (lines: 215)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def start_nnet_fn_runners(get_nnet: Callable[[], nn.Module], nnet_par_infos: List[NNetParInfo], model_file: str,
                          device: torch.device, on_gpu: bool,
                          batch_size: Optional[int] = None) -> List[BaseProcess]:
    """ Spawn one nnet runner process per visible GPU (or one CPU process); :return: the list of started processes. """
    ctx = get_context("spawn")

    nnet_i_q: Queue = nnet_par_infos[0].nnet_i_q
    nnet_o_qs: List[Queue] = [nnet_par_info.nnet_o_q for nnet_par_info in nnet_par_infos]

    # initialize heuristic procs
    if ('CUDA_VISIBLE_DEVICES' in os.environ) and (len(os.environ['CUDA_VISIBLE_DEVICES']) > 0):
        gpu_nums = [int(x) for x in os.environ['CUDA_VISIBLE_DEVICES'].split(",")]
    else:
        gpu_nums = [-1]

    nnet_procs: List[BaseProcess] = []
    for gpu_num in gpu_nums:
        nnet_fn_procs = ctx.Process(target=nnet_fn_runner,
                                    args=(nnet_i_q, nnet_o_qs, model_file, device, on_gpu, gpu_num, get_nnet,
                                          batch_size))
        nnet_fn_procs.daemon = True
        nnet_fn_procs.start()
        nnet_procs.append(nnet_fn_procs)

    return nnet_procs
```
