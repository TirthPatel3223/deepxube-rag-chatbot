---
id: "func:deepxube.nnet.nnet_utils.load_nnet"
kind: "function"
name: "load_nnet"
qualified_name: "deepxube.nnet.nnet_utils.load_nnet"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 50
line_end: 70
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "model_file"
    annotation: "str"
    default: null
  - name: "nnet"
    annotation: "nn.Module"
    default: null
  - name: "device"
    annotation: "Optional[torch.device]"
    default: "None"
returns: "nn.Module"
docstring_source: "present"
callees:
  - target: "func:torch.load"
    expr: "torch.load"
    call_sites: [55, 57]
  - target: "func:torch.device"
    expr: "torch.device"
    call_sites: [55]
  - target: "func:collections.OrderedDict"
    expr: "OrderedDict"
    call_sites: [60]
  - target: null
    expr: "state_dict.items"
    call_sites: [61]
  - target: "func:re.sub"
    expr: "re.sub"
    call_sites: [62]
  - target: null
    expr: "nnet.load_state_dict"
    call_sites: [66]
  - target: null
    expr: "nnet.eval"
    call_sites: [68]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.load_nnet`

**File:** [deepxube/nnet/nnet_utils.py:50](../../../../deepxube/nnet/nnet_utils.py#L50)
**Visibility:** public
**Kind:** function

## Signature

```python
def load_nnet(model_file: str, nnet: nn.Module, device: Optional[torch.device] = None) -> nn.Module
```

## Docstring

Load weights from ``model_file`` into ``nnet``, strip any ``module.`` DataParallel prefix, and :return: nnet
in eval mode. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `model_file` | `str` | — |
| `nnet` | `nn.Module` | — |
| `device` | `Optional[torch.device]` | `None` |

## Returns

`nn.Module`

## Calls

- `torch.load` → `func:torch.load` (lines: 55, 57)
- `torch.device` → `func:torch.device` (lines: 55)
- `OrderedDict` → `func:collections.OrderedDict` (lines: 60)
- `re.sub` → `func:re.sub` (lines: 62)

### Unresolved
- `state_dict.items` (lines: 61)
- `nnet.load_state_dict` (lines: 66)
- `nnet.eval` (lines: 68)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def load_nnet(model_file: str, nnet: nn.Module, device: Optional[torch.device] = None) -> nn.Module:
    """ Load weights from ``model_file`` into ``nnet``, strip any ``module.`` DataParallel prefix, and :return: nnet
    in eval mode. """
    # get state dict
    if device is None:
        state_dict = torch.load(model_file, map_location=torch.device('cpu'), weights_only=True)
    else:
        state_dict = torch.load(model_file, map_location=device, weights_only=False)

    # remove module prefix
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        k = re.sub(r'^module\.', '', k)
        new_state_dict[k] = v

    # set state dict
    nnet.load_state_dict(new_state_dict)

    nnet.eval()

    return nnet
```
