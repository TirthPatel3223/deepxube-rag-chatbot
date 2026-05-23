---
id: "func:deepxube.nnet.pytorch_models.ResnetModel.forward"
kind: "method"
name: "forward"
qualified_name: "deepxube.nnet.pytorch_models.ResnetModel.forward"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 162
line_end: 174
class: "ResnetModel"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "x"
    annotation: "Tensor"
    default: null
returns: "Tensor"
docstring_source: "present"
callees:
  - target: null
    expr: "zip"
    call_sites: [166]
  - target: null
    expr: "isinstance"
    call_sites: [167]
  - target: "func:deepxube.nnet.pytorch_models.module"
    expr: "module"
    call_sites: [170]
  - target: "func:deepxube.nnet.pytorch_models.act_fn"
    expr: "act_fn"
    call_sites: [172]
raises: []
reads_attrs:
  - "self.act_fns"
  - "self.blocks"
writes_attrs: []
---

# `deepxube.nnet.pytorch_models.ResnetModel.forward`

**File:** [deepxube/nnet/pytorch_models.py:162](../../../../deepxube/nnet/pytorch_models.py#L162)
**Class:** `ResnetModel`
**Visibility:** public
**Kind:** method

## Signature

```python
def forward(self, x: Tensor) -> Tensor
```

## Docstring

Pass ``x`` through each residual block (skip connection + post-addition activation). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `x` | `Tensor` | — |

## Returns

`Tensor`

## Calls

- `module` → `func:deepxube.nnet.pytorch_models.module` (lines: 170)
- `act_fn` → `func:deepxube.nnet.pytorch_models.act_fn` (lines: 172)

### Unresolved
- `zip` (lines: 166)
- `isinstance` (lines: 167)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.act_fns`
- `self.blocks`

## Source

```python
    def forward(self, x: Tensor) -> Tensor:
        """ Pass ``x`` through each residual block (skip connection + post-addition activation). """
        # resnet blocks
        module_list: nn.Module
        for module_list, act_fn in zip(self.blocks, self.act_fns, strict=True):
            assert isinstance(module_list, nn.ModuleList)
            res_inp = x
            for module in module_list:
                x = module(x)

            x = act_fn(x + res_inp)

        return x
```
