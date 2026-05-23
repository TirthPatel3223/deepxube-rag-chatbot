---
id: "func:deepxube.nnet.pytorch_models.SPLASH1.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.nnet.pytorch_models.SPLASH1.__init__"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 88
line_end: 102
class: "SPLASH1"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "init"
    annotation: "str"
    default: "'RELU'"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [90]
  - target: null
    expr: "super"
    call_sites: [90]
  - target: null
    expr: "init.upper"
    call_sites: [91]
  - target: "func:torch.nn.parameter.Parameter"
    expr: "Parameter"
    call_sites: [93, 95, 98, 100]
  - target: "func:torch.zeros"
    expr: "torch.zeros"
    call_sites: [93, 98]
  - target: "func:torch.ones"
    expr: "torch.ones"
    call_sites: [95, 100]
  - target: null
    expr: "ValueError"
    call_sites: [102]
raises:
  - exception: "ValueError"
    call_sites: [102]
reads_attrs:
  - "self.coeff_left"
  - "self.coeff_right"
  - "self.output_bias"
writes_attrs:
  - "self.coeff_left"
  - "self.coeff_right"
  - "self.output_bias"
---

# `deepxube.nnet.pytorch_models.SPLASH1.__init__`

**File:** [deepxube/nnet/pytorch_models.py:88](../../../../deepxube/nnet/pytorch_models.py#L88)
**Class:** `SPLASH1`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, init: str = 'RELU')
```

## Docstring

Initialise trainable right/left coefficients and output bias; ``init`` is ``"RELU"`` or ``"LINEAR"``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `init` | `str` | `'RELU'` |

## Returns

*(Not annotated.)*

## Calls

- `Parameter` → `func:torch.nn.parameter.Parameter` (lines: 93, 95, 98, 100)
- `torch.zeros` → `func:torch.zeros` (lines: 93, 98)
- `torch.ones` → `func:torch.ones` (lines: 95, 100)

### Unresolved
- `super().__init__` (lines: 90)
- `super` (lines: 90)
- `init.upper` (lines: 91)
- `ValueError` (lines: 102)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 102)

## Attribute access

**Writes:**
- `self.coeff_left`
- `self.coeff_right`
- `self.output_bias`

**Reads:**
- `self.coeff_left`
- `self.coeff_right`
- `self.output_bias`

## Source

```python
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
```
