---
id: "func:deepxube.nnet.pytorch_models.FullyConnectedModel.forward"
kind: "method"
name: "forward"
qualified_name: "deepxube.nnet.pytorch_models.FullyConnectedModel.forward"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 217
line_end: 227
class: "FullyConnectedModel"
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
    expr: "x.float"
    call_sites: [219]
  - target: null
    expr: "isinstance"
    call_sites: [223]
  - target: "func:deepxube.nnet.pytorch_models.module"
    expr: "module"
    call_sites: [225]
raises: []
reads_attrs:
  - "self.layers"
writes_attrs: []
---

# `deepxube.nnet.pytorch_models.FullyConnectedModel.forward`

**File:** [deepxube/nnet/pytorch_models.py:217](../../../../deepxube/nnet/pytorch_models.py#L217)
**Class:** `FullyConnectedModel`
**Visibility:** public
**Kind:** method

## Signature

```python
def forward(self, x: Tensor) -> Tensor
```

## Docstring

Run ``x`` through all FC layers in order. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `x` | `Tensor` | — |

## Returns

`Tensor`

## Calls

- `module` → `func:deepxube.nnet.pytorch_models.module` (lines: 225)

### Unresolved
- `x.float` (lines: 219)
- `isinstance` (lines: 223)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.layers`

## Source

```python
    def forward(self, x: Tensor) -> Tensor:
        """ Run ``x`` through all FC layers in order. """
        x = x.float()

        module_list: nn.Module
        for module_list in self.layers:
            assert isinstance(module_list, nn.ModuleList)
            for module in module_list:
                x = module(x)

        return x
```
