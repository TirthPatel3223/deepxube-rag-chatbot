---
id: "class:deepxube.nnet.pytorch_models.SPLASH"
kind: "class"
name: "SPLASH"
qualified_name: "deepxube.nnet.pytorch_models.SPLASH"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 33
line_end: 82
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "nn.Module"
    resolved_id: null
methods:
  - "func:deepxube.nnet.pytorch_models.SPLASH.__init__"
  - "func:deepxube.nnet.pytorch_models.SPLASH.forward"
attributes:
  - name: "self.coeffs_left"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.coeffs_right"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.hinges"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_each_side"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_hinges"
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

# `deepxube.nnet.pytorch_models.SPLASH`

**File:** [deepxube/nnet/pytorch_models.py:33](../../../deepxube/nnet/pytorch_models.py#L33)
**Abstract:** no

## Docstring

Learnable piecewise-linear activation with ``num_hinges`` symmetric break points (SPLASH).

:param num_hinges: Number of hinge points (must be odd and > 0).
:param init: Initial shape — ``"RELU"`` or ``"LINEAR"``.

## Inheritance

**Direct bases:**
- `nn.Module`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `forward`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.coeffs_left` | — | __init__ |
| `self.coeffs_right` | — | __init__ |
| `self.hinges` | — | __init__ |
| `self.num_each_side` | — | __init__ |
| `self.num_hinges` | — | __init__ |
| `self.output_bias` | — | __init__ |

## Source

```python
class SPLASH(nn.Module):
    """ Learnable piecewise-linear activation with ``num_hinges`` symmetric break points (SPLASH).

    :param num_hinges: Number of hinge points (must be odd and > 0).
    :param init: Initial shape — ``"RELU"`` or ``"LINEAR"``.
    """

    def __init__(self, num_hinges: int = 5, init: str = "RELU"):
        """ Initialise hinge positions and trainable left/right coefficients; ``init`` sets the starting shape. """
        super().__init__()
        assert num_hinges > 0, "Number of hinges should be greater than zero, but is %s" % num_hinges
        assert ((num_hinges + 1) % 2) == 0, "Number of hinges should be odd, but is %s" % num_hinges
        init = init.upper()

        self.num_hinges: int = num_hinges
        self.num_each_side: int = int((self.num_hinges + 1) / 2)

        self.hinges: List[float] = list(np.linspace(0, 2.5, self.num_each_side))

        self.output_bias: Parameter = Parameter(torch.zeros(1), requires_grad=True)

        self.coeffs_right: Parameter
        self.coeffs_left: Parameter
        if init == "RELU":
            self.coeffs_right = Parameter(torch.cat((torch.ones(1), torch.zeros(self.num_each_side - 1))),
                                          requires_grad=True)
            self.coeffs_left = Parameter(torch.zeros(self.num_each_side), requires_grad=True)
        elif init == "LINEAR":
            self.coeffs_right = Parameter(torch.cat((torch.ones(1), torch.zeros(self.num_each_side - 1))),
                                          requires_grad=True)
            self.coeffs_left = Parameter(torch.cat((-torch.ones(1), torch.zeros(self.num_each_side - 1))),
                                         requires_grad=True)
        else:
            raise ValueError("Unknown init %s" % init)

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
