---
id: "func:deepxube.nnet.pytorch_models.Conv2dModel.forward"
kind: "method"
name: "forward"
qualified_name: "deepxube.nnet.pytorch_models.Conv2dModel.forward"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 286
line_end: 296
class: "Conv2dModel"
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
    call_sites: [288]
  - target: null
    expr: "isinstance"
    call_sites: [292]
  - target: "func:deepxube.nnet.pytorch_models.module"
    expr: "module"
    call_sites: [294]
raises: []
reads_attrs:
  - "self.layers"
writes_attrs: []
---

# `deepxube.nnet.pytorch_models.Conv2dModel.forward`

**File:** [deepxube/nnet/pytorch_models.py:286](../../../../deepxube/nnet/pytorch_models.py#L286)
**Class:** `Conv2dModel`
**Visibility:** public
**Kind:** method

## Signature

```python
def forward(self, x: Tensor) -> Tensor
```

## Docstring

Run ``x`` through all conv layers in order. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `x` | `Tensor` | — |

## Returns

`Tensor`

## Calls

- `module` → `func:deepxube.nnet.pytorch_models.module` (lines: 294)

### Unresolved
- `x.float` (lines: 288)
- `isinstance` (lines: 292)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.layers`

## Source

```python
    def forward(self, x: Tensor) -> Tensor:
        """ Run ``x`` through all conv layers in order. """
        x = x.float()

        module_list: nn.Module
        for module_list in self.layers:
            assert isinstance(module_list, nn.ModuleList)
            for module in module_list:
                x = module(x)

        return x
```
