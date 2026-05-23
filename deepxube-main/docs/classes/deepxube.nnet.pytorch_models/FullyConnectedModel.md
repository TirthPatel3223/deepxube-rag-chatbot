---
id: "class:deepxube.nnet.pytorch_models.FullyConnectedModel"
kind: "class"
name: "FullyConnectedModel"
qualified_name: "deepxube.nnet.pytorch_models.FullyConnectedModel"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 177
line_end: 227
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "nn.Module"
    resolved_id: null
methods:
  - "func:deepxube.nnet.pytorch_models.FullyConnectedModel.__init__"
  - "func:deepxube.nnet.pytorch_models.FullyConnectedModel.forward"
attributes:
  - name: "self.layers"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.pytorch_models.FullyConnectedModel`

**File:** [deepxube/nnet/pytorch_models.py:177](../../../deepxube/nnet/pytorch_models.py#L177)
**Abstract:** no

## Docstring

Configurable MLP: each layer is a Linear → optional BatchNorm/GroupNorm → activation stack. 

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
| `self.layers` | — | __init__ |

## Source

```python
class FullyConnectedModel(nn.Module):
    """ Configurable MLP: each layer is a Linear → optional BatchNorm/GroupNorm → activation stack. """

    def __init__(self, input_dim: int, dims: List[int], acts: List[str], batch_norms: Optional[List[bool]] = None,
                 weight_norms: Optional[List[bool]] = None, group_norms: Optional[List[int]] = None):
        """ Build the layer list from ``dims``, ``acts``, and normalization flags. """
        super().__init__()
        if batch_norms is None:
            batch_norms = [False] * len(dims)
        if weight_norms is None:
            weight_norms = [False] * len(dims)
        if group_norms is None:
            group_norms = [-1] * len(dims)
        self.layers: nn.ModuleList = nn.ModuleList()

        # layers
        for dim, act, batch_norm, weight_norm, group_norm in zip(dims, acts, batch_norms, weight_norms, group_norms,
                                                                 strict=True):
            module_list = nn.ModuleList()

            # linear
            if weight_norm:
                module_list.append(nn.utils.parametrizations.weight_norm(nn.Linear(input_dim, dim)))
            else:
                module_list.append(nn.Linear(input_dim, dim))

            # batch norm
            if batch_norm:
                module_list.append(nn.BatchNorm1d(dim))

            # group norm
            if group_norm > 0:
                module_list.append(nn.GroupNorm(group_norm, dim))

            # activation
            module_list.append(get_act_fn(act))
            self.layers.append(module_list)

            input_dim = dim

    def forward(self, x: Tensor) -> Tensor:
        """ Run ``x`` through all FC layers in order. """
        x = x.float()

        module_list: nn.Module
        for module_list in self.layers:
            assert isinstance(module_list, nn.ModuleList)
            for module in module_list:
                x = module(x)

        return x
```
