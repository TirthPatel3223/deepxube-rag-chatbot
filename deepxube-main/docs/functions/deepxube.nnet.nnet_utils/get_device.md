---
id: "func:deepxube.nnet.nnet_utils.get_device"
kind: "function"
name: "get_device"
qualified_name: "deepxube.nnet.nnet_utils.get_device"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 33
line_end: 46
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "Tuple[torch.device, List[int], bool]"
docstring_source: "present"
callees:
  - target: "func:torch.device"
    expr: "torch.device"
    call_sites: [35, 39]
  - target: null
    expr: "torch.cuda.is_available"
    call_sites: [38]
  - target: null
    expr: "int"
    call_sites: [40]
  - target: null
    expr: "os.environ['CUDA_VISIBLE_DEVICES'].split"
    call_sites: [40]
  - target: "func:torch.set_num_threads"
    expr: "torch.set_num_threads"
    call_sites: [42, 44]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.get_device`

**File:** [deepxube/nnet/nnet_utils.py:33](../../../../deepxube/nnet/nnet_utils.py#L33)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_device() -> Tuple[torch.device, List[int], bool]
```

## Docstring

:return: ``(device, gpu_ids, on_gpu)``; uses CUDA if ``CUDA_VISIBLE_DEVICES`` is set and CUDA is available. 

## Parameters

*(No parameters.)*

## Returns

`Tuple[torch.device, List[int], bool]`

## Calls

- `torch.device` → `func:torch.device` (lines: 35, 39)
- `torch.set_num_threads` → `func:torch.set_num_threads` (lines: 42, 44)

### Unresolved
- `torch.cuda.is_available` (lines: 38)
- `int` (lines: 40)
- `os.environ['CUDA_VISIBLE_DEVICES'].split` (lines: 40)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_device() -> Tuple[torch.device, List[int], bool]:
    """ :return: ``(device, gpu_ids, on_gpu)``; uses CUDA if ``CUDA_VISIBLE_DEVICES`` is set and CUDA is available. """
    device: torch.device = torch.device("cpu")
    devices: List[int] = []
    on_gpu: bool = False
    if ('CUDA_VISIBLE_DEVICES' in os.environ) and torch.cuda.is_available():
        device = torch.device("cuda:%i" % 0)
        devices = [int(x) for x in os.environ['CUDA_VISIBLE_DEVICES'].split(",")]
        on_gpu = True
        torch.set_num_threads(1)
    else:
        torch.set_num_threads(8)

    return device, devices, on_gpu
```
