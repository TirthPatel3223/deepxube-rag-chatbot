---
id: "func:deepxube.nnet.pytorch_models.SPLASH.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.nnet.pytorch_models.SPLASH.__init__"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 40
line_end: 66
class: "SPLASH"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num_hinges"
    annotation: "int"
    default: "5"
  - name: "init"
    annotation: "str"
    default: "'RELU'"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [42]
  - target: null
    expr: "super"
    call_sites: [42]
  - target: null
    expr: "init.upper"
    call_sites: [45]
  - target: null
    expr: "int"
    call_sites: [48]
  - target: null
    expr: "list"
    call_sites: [50]
  - target: "func:numpy.linspace"
    expr: "np.linspace"
    call_sites: [50]
  - target: "func:torch.nn.parameter.Parameter"
    expr: "Parameter"
    call_sites: [52, 57, 59, 61, 63]
  - target: "func:torch.zeros"
    expr: "torch.zeros"
    call_sites: [52, 57, 59, 61, 63]
  - target: "func:torch.cat"
    expr: "torch.cat"
    call_sites: [57, 61, 63]
  - target: "func:torch.ones"
    expr: "torch.ones"
    call_sites: [57, 61, 63]
  - target: null
    expr: "ValueError"
    call_sites: [66]
raises:
  - exception: "ValueError"
    call_sites: [66]
reads_attrs:
  - "self.coeffs_left"
  - "self.coeffs_right"
  - "self.hinges"
  - "self.num_each_side"
  - "self.num_hinges"
  - "self.output_bias"
writes_attrs:
  - "self.coeffs_left"
  - "self.coeffs_right"
  - "self.hinges"
  - "self.num_each_side"
  - "self.num_hinges"
  - "self.output_bias"
---

# `deepxube.nnet.pytorch_models.SPLASH.__init__`

**File:** [deepxube/nnet/pytorch_models.py:40](../../../../deepxube/nnet/pytorch_models.py#L40)
**Class:** `SPLASH`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, num_hinges: int = 5, init: str = 'RELU')
```

## Docstring

Initialise hinge positions and trainable left/right coefficients; ``init`` sets the starting shape. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_hinges` | `int` | `5` |
| `init` | `str` | `'RELU'` |

## Returns

*(Not annotated.)*

## Calls

- `np.linspace` → `func:numpy.linspace` (lines: 50)
- `Parameter` → `func:torch.nn.parameter.Parameter` (lines: 52, 57, 59, 61, 63)
- `torch.zeros` → `func:torch.zeros` (lines: 52, 57, 59, 61, 63)
- `torch.cat` → `func:torch.cat` (lines: 57, 61, 63)
- `torch.ones` → `func:torch.ones` (lines: 57, 61, 63)

### Unresolved
- `super().__init__` (lines: 42)
- `super` (lines: 42)
- `init.upper` (lines: 45)
- `int` (lines: 48)
- `list` (lines: 50)
- `ValueError` (lines: 66)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 66)

## Attribute access

**Writes:**
- `self.coeffs_left`
- `self.coeffs_right`
- `self.hinges`
- `self.num_each_side`
- `self.num_hinges`
- `self.output_bias`

**Reads:**
- `self.coeffs_left`
- `self.coeffs_right`
- `self.hinges`
- `self.num_each_side`
- `self.num_hinges`
- `self.output_bias`

## Source

```python
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
```
