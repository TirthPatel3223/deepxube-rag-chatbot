---
id: "func:deepxube.tests.time_tests.init_nnet"
kind: "function"
name: "init_nnet"
qualified_name: "deepxube.tests.time_tests.init_nnet"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 132
line_end: 144
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "nnet_par"
    annotation: "NNetPar"
    default: null
returns: "Tuple[nn.Module, torch.device]"
docstring_source: "present"
callees:
  - target: "func:deepxube.nnet.nnet_utils.get_device"
    expr: "nnet_utils.get_device"
    call_sites: [136]
  - target: null
    expr: "print"
    call_sites: [137]
  - target: null
    expr: "nnet_par.get_nnet"
    call_sites: [139]
  - target: null
    expr: "nnet.to"
    call_sites: [140]
  - target: "func:torch.nn.DataParallel"
    expr: "nn.DataParallel"
    call_sites: [142]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.init_nnet`

**File:** [deepxube/tests/time_tests.py:132](../../../../deepxube/tests/time_tests.py#L132)
**Visibility:** public
**Kind:** function

## Signature

```python
def init_nnet(nnet_par: NNetPar) -> Tuple[nn.Module, torch.device]
```

## Docstring

:return: Initialised nnet module placed on the best available device. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `nnet_par` | `NNetPar` | — |

## Returns

`Tuple[nn.Module, torch.device]`

## Calls

- `nnet_utils.get_device` → `func:deepxube.nnet.nnet_utils.get_device` (lines: 136)
- `nn.DataParallel` → `func:torch.nn.DataParallel` (lines: 142)

### Unresolved
- `print` (lines: 137)
- `nnet_par.get_nnet` (lines: 139)
- `nnet.to` (lines: 140)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def init_nnet(nnet_par: NNetPar) -> Tuple[nn.Module, torch.device]:
    """ :return: Initialised nnet module placed on the best available device. """
    on_gpu: bool
    device: torch.device
    device, devices, on_gpu = nnet_utils.get_device()
    print("device: %s, devices: %s, on_gpu: %s" % (device, devices, on_gpu))

    nnet: nn.Module = nnet_par.get_nnet()
    nnet.to(device)
    if on_gpu:
        nnet = nn.DataParallel(nnet)

    return nnet, device
```
