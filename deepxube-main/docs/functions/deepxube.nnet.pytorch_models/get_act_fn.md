---
id: "func:deepxube.nnet.pytorch_models.get_act_fn"
kind: "function"
name: "get_act_fn"
qualified_name: "deepxube.nnet.pytorch_models.get_act_fn"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 122
line_end: 142
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "act"
    annotation: "str"
    default: null
returns: "nn.Module"
docstring_source: "present"
callees:
  - target: null
    expr: "act.upper"
    call_sites: [126]
  - target: "func:torch.nn.ReLU"
    expr: "nn.ReLU"
    call_sites: [128]
  - target: "func:torch.nn.ELU"
    expr: "nn.ELU"
    call_sites: [130]
  - target: "func:torch.nn.Sigmoid"
    expr: "nn.Sigmoid"
    call_sites: [132]
  - target: "func:torch.nn.Tanh"
    expr: "nn.Tanh"
    call_sites: [134]
  - target: "func:deepxube.nnet.pytorch_models.SPLASH"
    expr: "SPLASH"
    call_sites: [136]
  - target: "func:deepxube.nnet.pytorch_models.SPLASH1"
    expr: "SPLASH1"
    call_sites: [138]
  - target: "func:deepxube.nnet.pytorch_models.LinearAct"
    expr: "LinearAct"
    call_sites: [140]
  - target: null
    expr: "ValueError"
    call_sites: [142]
raises:
  - exception: "ValueError"
    call_sites: [142]
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.pytorch_models.get_act_fn`

**File:** [deepxube/nnet/pytorch_models.py:122](../../../../deepxube/nnet/pytorch_models.py#L122)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_act_fn(act: str) -> nn.Module
```

## Docstring

:return: An ``nn.Module`` for the named activation (RELU, ELU, SIGMOID, TANH, SPLASH, SPLASH1, LINEAR).
:raises ValueError: If ``act`` is not recognised.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `act` | `str` | — |

## Returns

`nn.Module`

## Calls

- `nn.ReLU` → `func:torch.nn.ReLU` (lines: 128)
- `nn.ELU` → `func:torch.nn.ELU` (lines: 130)
- `nn.Sigmoid` → `func:torch.nn.Sigmoid` (lines: 132)
- `nn.Tanh` → `func:torch.nn.Tanh` (lines: 134)
- `SPLASH` → `func:deepxube.nnet.pytorch_models.SPLASH` (lines: 136)
- `SPLASH1` → `func:deepxube.nnet.pytorch_models.SPLASH1` (lines: 138)
- `LinearAct` → `func:deepxube.nnet.pytorch_models.LinearAct` (lines: 140)

### Unresolved
- `act.upper` (lines: 126)
- `ValueError` (lines: 142)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 142)

## Source

```python
def get_act_fn(act: str) -> nn.Module:
    """ :return: An ``nn.Module`` for the named activation (RELU, ELU, SIGMOID, TANH, SPLASH, SPLASH1, LINEAR).
    :raises ValueError: If ``act`` is not recognised.
    """
    act = act.upper()
    if act == "RELU":
        return nn.ReLU()
    elif act == "ELU":
        return nn.ELU()
    elif act == "SIGMOID":
        return nn.Sigmoid()
    elif act == "TANH":
        return nn.Tanh()
    elif act == "SPLASH":
        return SPLASH()
    elif act == "SPLASH1":
        return SPLASH1()
    elif act == "LINEAR":
        return LinearAct()
    else:
        raise ValueError("Un-defined activation type %s" % act)
```
