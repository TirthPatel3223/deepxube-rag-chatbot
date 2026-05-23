---
id: "class:deepxube.nnet.pytorch_models.SPLASH1"
kind: "class"
name: "SPLASH1"
qualified_name: "deepxube.nnet.pytorch_models.SPLASH1"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 85
line_end: 107
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "nn.Module"
    resolved_id: null
methods:
  - "func:deepxube.nnet.pytorch_models.SPLASH1.__init__"
  - "func:deepxube.nnet.pytorch_models.SPLASH1.forward"
attributes:
  - name: "self.coeff_left"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.coeff_right"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.output_bias"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.pytorch_models.SPLASH1`

**File:** [deepxube/nnet/pytorch_models.py:85](../../../deepxube/nnet/pytorch_models.py#L85)
**Abstract:** no

## Docstring

Single-hinge learnable activation (SPLASH1): weighted ReLU + weighted negative-ReLU + scalar bias. 

## Inheritance

**Direct bases:**
- `nn.Module`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `forward` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.coeff_left` | — | __init__ |
| `self.coeff_right` | — | __init__ |
| `self.output_bias` | — | __init__ |

## Source

```python
class SPLASH1(nn.Module):
    """ Single-hinge learnable activation (SPLASH1): weighted ReLU + weighted negative-ReLU + scalar bias. """

    def __init__(self, init: str = "RELU"):
        """ Initialise trainable right/left coefficients and output bias; ``init`` is ``"RELU"`` or ``"LINEAR"``. """
        super().__init__()
        init = init.upper()

        self.output_bias: Parameter = Parameter(torch.zeros(1), requires_grad=True)

        self.coeff_right: Parameter = Parameter(torch.ones(1), requires_grad=True)
        self.coeff_left: Parameter
        if init == "RELU":
            self.coeff_left = Parameter(torch.zeros(1), requires_grad=True)
        elif init == "LINEAR":
            self.coeff_left = Parameter(-torch.ones(1), requires_grad=True)
        else:
            raise ValueError("Unknown init %s" % init)

    def forward(self, x: Tensor) -> Tensor:
        x = (self.coeff_right * nn.functional.relu(x)) - (self.coeff_left * nn.functional.relu(-x)) + self.output_bias

        return x
```
