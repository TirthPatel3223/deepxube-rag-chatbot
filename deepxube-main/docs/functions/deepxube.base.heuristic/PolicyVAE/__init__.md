---
id: "func:deepxube.base.heuristic.PolicyVAE.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.heuristic.PolicyVAE.__init__"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 132
line_end: 137
class: "PolicyVAE"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nnet_input"
    annotation: "PNNetIn"
    default: null
  - name: "kl_weight"
    annotation: "float"
    default: null
  - name: "**kwargs"
    annotation: "Any"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [134]
  - target: null
    expr: "super"
    call_sites: [134]
  - target: null
    expr: "torch.distributions.Normal"
    call_sites: [135]
  - target: "func:torch.nn.MSELoss"
    expr: "nn.MSELoss"
    call_sites: [137]
raises: []
reads_attrs:
  - "self.kl_weight"
  - "self.mse_criterion"
  - "self.norm_dist"
writes_attrs:
  - "self.kl_weight"
  - "self.mse_criterion"
  - "self.norm_dist"
---

# `deepxube.base.heuristic.PolicyVAE.__init__`

**File:** [deepxube/base/heuristic.py:132](../../../../deepxube/base/heuristic.py#L132)
**Class:** `PolicyVAE`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, nnet_input: PNNetIn, kl_weight: float, **kwargs: Any)
```

## Docstring

Store the KL weight and a unit-normal prior. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_input` | `PNNetIn` | — |
| `kl_weight` | `float` | — |
| `**kwargs` | `Any` | — |

## Returns

*(Not annotated.)*

## Calls

- `nn.MSELoss` → `func:torch.nn.MSELoss` (lines: 137)

### Unresolved
- `super().__init__` (lines: 134)
- `super` (lines: 134)
- `torch.distributions.Normal` (lines: 135)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.kl_weight`
- `self.mse_criterion`
- `self.norm_dist`

**Reads:**
- `self.kl_weight`
- `self.mse_criterion`
- `self.norm_dist`

## Source

```python
    def __init__(self, nnet_input: PNNetIn, kl_weight: float, **kwargs: Any):
        """ Store the KL weight and a unit-normal prior. """
        super().__init__(nnet_input)
        self.norm_dist = torch.distributions.Normal(0, 1)
        self.kl_weight: float = kl_weight
        self.mse_criterion = nn.MSELoss()
```
