---
id: "func:deepxube.nnet.nnet_utils.get_available_gpu_nums"
kind: "function"
name: "get_available_gpu_nums"
qualified_name: "deepxube.nnet.nnet_utils.get_available_gpu_nums"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 73
line_end: 79
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "List[int]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [76]
  - target: null
    expr: "int"
    call_sites: [77]
  - target: null
    expr: "os.environ['CUDA_VISIBLE_DEVICES'].split"
    call_sites: [77]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.get_available_gpu_nums`

**File:** [deepxube/nnet/nnet_utils.py:73](../../../../deepxube/nnet/nnet_utils.py#L73)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_available_gpu_nums() -> List[int]
```

## Docstring

:return: GPU indices parsed from ``CUDA_VISIBLE_DEVICES``, or ``[]`` if not set. 

## Parameters

*(No parameters.)*

## Returns

`List[int]`

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 76)
- `int` (lines: 77)
- `os.environ['CUDA_VISIBLE_DEVICES'].split` (lines: 77)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_available_gpu_nums() -> List[int]:
    """ :return: GPU indices parsed from ``CUDA_VISIBLE_DEVICES``, or ``[]`` if not set. """
    gpu_nums: List[int] = []
    if ('CUDA_VISIBLE_DEVICES' in os.environ) and (len(os.environ['CUDA_VISIBLE_DEVICES']) > 0):
        gpu_nums = [int(x) for x in os.environ['CUDA_VISIBLE_DEVICES'].split(",")]

    return gpu_nums
```
