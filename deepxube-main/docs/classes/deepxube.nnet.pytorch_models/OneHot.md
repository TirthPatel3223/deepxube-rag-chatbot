---
id: "class:deepxube.nnet.pytorch_models.OneHot"
kind: "class"
name: "OneHot"
qualified_name: "deepxube.nnet.pytorch_models.OneHot"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 12
line_end: 30
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "nn.Module"
    resolved_id: null
methods:
  - "func:deepxube.nnet.pytorch_models.OneHot.__init__"
  - "func:deepxube.nnet.pytorch_models.OneHot.forward"
attributes:
  - name: "self.flatten_oh"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.one_hot_depth"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.pytorch_models.OneHot`

**File:** [deepxube/nnet/pytorch_models.py:12](../../../deepxube/nnet/pytorch_models.py#L12)
**Abstract:** no

## Docstring

nn.Module that one-hot encodes an integer tensor; optionally flattens the last two dimensions into one. 

## Inheritance

**Direct bases:**
- `nn.Module`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `forward`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.flatten_oh` | — | __init__ |
| `self.one_hot_depth` | — | __init__ |

## Source

```python
class OneHot(nn.Module):
    """ nn.Module that one-hot encodes an integer tensor; optionally flattens the last two dimensions into one. """

    def __init__(self, one_hot_depth: int, flatten_oh: bool) -> None:
        super().__init__()
        self.one_hot_depth: int = one_hot_depth
        self.flatten_oh: bool = flatten_oh

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
