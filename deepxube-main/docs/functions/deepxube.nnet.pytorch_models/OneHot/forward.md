---
id: "func:deepxube.nnet.pytorch_models.OneHot.forward"
kind: "method"
name: "forward"
qualified_name: "deepxube.nnet.pytorch_models.OneHot.forward"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 20
line_end: 30
class: "OneHot"
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
    expr: "nn.functional.one_hot(x.long(), self.one_hot_depth).float"
    call_sites: [23]
  - target: null
    expr: "nn.functional.one_hot"
    call_sites: [23]
  - target: null
    expr: "x.long"
    call_sites: [23]
  - target: null
    expr: "x.reshape"
    call_sites: [28]
  - target: null
    expr: "x.float"
    call_sites: [30]
raises: []
reads_attrs:
  - "self.flatten_oh"
  - "self.one_hot_depth"
writes_attrs: []
---

# `deepxube.nnet.pytorch_models.OneHot.forward`

**File:** [deepxube/nnet/pytorch_models.py:20](../../../../deepxube/nnet/pytorch_models.py#L20)
**Class:** `OneHot`
**Visibility:** public
**Kind:** method

## Signature

```python
def forward(self, x: Tensor) -> Tensor
```

## Docstring

One-hot encode ``x`` when depth > 1 (flatten if ``flatten_oh``); otherwise cast to float. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `x` | `Tensor` | — |

## Returns

`Tensor`

## Calls

*(No resolved calls.)*

### Unresolved
- `nn.functional.one_hot(x.long(), self.one_hot_depth).float` (lines: 23)
- `nn.functional.one_hot` (lines: 23)
- `x.long` (lines: 23)
- `x.reshape` (lines: 28)
- `x.float` (lines: 30)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.flatten_oh`
- `self.one_hot_depth`

## Source

```python
    def forward(self, x: Tensor) -> Tensor:
        """ One-hot encode ``x`` when depth > 1 (flatten if ``flatten_oh``); otherwise cast to float. """
        if self.one_hot_depth > 1:
            x = nn.functional.one_hot(x.long(), self.one_hot_depth).float()
            if not self.flatten_oh:
                return x
            else:
                *leading, d, c = x.shape
                return x.reshape(*leading, d * c)
        else:
            return x.float()
```
