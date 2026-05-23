---
id: "class:deepxube.nnet.pytorch_models.LinearAct"
kind: "class"
name: "LinearAct"
qualified_name: "deepxube.nnet.pytorch_models.LinearAct"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 110
line_end: 119
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "nn.Module"
    resolved_id: null
methods:
  - "func:deepxube.nnet.pytorch_models.LinearAct.__init__"
  - "func:deepxube.nnet.pytorch_models.LinearAct.forward"
attributes:
  - name: "self.dummy"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.pytorch_models.LinearAct`

**File:** [deepxube/nnet/pytorch_models.py:110](../../../deepxube/nnet/pytorch_models.py#L110)
**Abstract:** no

## Docstring

Identity activation used as a no-op placeholder in layer stacks. 

## Inheritance

**Direct bases:**
- `nn.Module`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)* — *(no docstring)*
- `forward` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.dummy` | — | __init__ |

## Source

```python
class LinearAct(nn.Module):
    """ Identity activation used as a no-op placeholder in layer stacks. """

    def __init__(self) -> None:
        super().__init__()
        self.dummy = 1

    def forward(self, x: Tensor) -> Tensor:
        self.dummy = 1  # so PyCharm does not complain
        return x
```
