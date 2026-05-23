---
id: "func:deepxube.nnet.pytorch_models.SPLASH.forward"
kind: "method"
name: "forward"
qualified_name: "deepxube.nnet.pytorch_models.SPLASH.forward"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 68
line_end: 82
class: "SPLASH"
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
  - target: "func:torch.zeros_like"
    expr: "torch.zeros_like"
    call_sites: [70]
  - target: null
    expr: "range"
    call_sites: [73, 77]
  - target: "func:torch.clamp"
    expr: "torch.clamp"
    call_sites: [74, 78]
raises: []
reads_attrs:
  - "self.coeffs_left"
  - "self.coeffs_right"
  - "self.hinges"
  - "self.num_each_side"
  - "self.output_bias"
writes_attrs: []
---

# `deepxube.nnet.pytorch_models.SPLASH.forward`

**File:** [deepxube/nnet/pytorch_models.py:68](../../../../deepxube/nnet/pytorch_models.py#L68)
**Class:** `SPLASH`
**Visibility:** public
**Kind:** method

## Signature

```python
def forward(self, x: Tensor) -> Tensor
```

## Docstring

Evaluate the SPLASH activation as a sum of weighted clamped ramp functions plus a bias. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `x` | `Tensor` | — |

## Returns

`Tensor`

## Calls

- `torch.zeros_like` → `func:torch.zeros_like` (lines: 70)
- `torch.clamp` → `func:torch.clamp` (lines: 74, 78)

### Unresolved
- `range` (lines: 73, 77)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.coeffs_left`
- `self.coeffs_right`
- `self.hinges`
- `self.num_each_side`
- `self.output_bias`

## Source

```python
    def forward(self, x: Tensor) -> Tensor:
        """ Evaluate the SPLASH activation as a sum of weighted clamped ramp functions plus a bias. """
        output: Tensor = torch.zeros_like(x)

        # output for x > 0
        for idx in range(self.num_each_side):
            output = output + self.coeffs_right[idx] * torch.clamp(x - self.hinges[idx], min=0)

        # output for x < 0
        for idx in range(self.num_each_side):
            output = output + self.coeffs_left[idx] * torch.clamp(-x - self.hinges[idx], min=0)

        output = output + self.output_bias

        return output
```
