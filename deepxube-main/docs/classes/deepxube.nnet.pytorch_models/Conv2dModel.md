---
id: "class:deepxube.nnet.pytorch_models.Conv2dModel"
kind: "class"
name: "Conv2dModel"
qualified_name: "deepxube.nnet.pytorch_models.Conv2dModel"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 230
line_end: 296
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "nn.Module"
    resolved_id: null
methods:
  - "func:deepxube.nnet.pytorch_models.Conv2dModel.__init__"
  - "func:deepxube.nnet.pytorch_models.Conv2dModel.forward"
attributes:
  - name: "self.layers"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.pytorch_models.Conv2dModel`

**File:** [deepxube/nnet/pytorch_models.py:230](../../../deepxube/nnet/pytorch_models.py#L230)
**Abstract:** no

## Docstring

Configurable 2-D conv stack: each layer is Conv2d(Transpose) → optional BatchNorm → activation → optional Dropout. 

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
class Conv2dModel(nn.Module):
    """ Configurable 2-D conv stack: each layer is Conv2d(Transpose) → optional BatchNorm → activation → optional Dropout. """

    def __init__(self, chan_in: int, channel_sizes: List[int], kernel_sizes: List[int], paddings: List[int],
                 layer_acts: List[str], batch_norms: Optional[List[bool]] = None, strides: Optional[List[int]] = None,
                 transpose: bool = False, weight_norms: Optional[List[bool]] = None,
                 dropouts: Optional[List[float]] = None):
        """ Build the conv layer list from channel sizes, kernels, paddings, and normalization/activation flags. """
        super().__init__()
        self.layers: nn.ModuleList = nn.ModuleList()
        if strides is None:
            strides = [1] * len(channel_sizes)

        if batch_norms is None:
            batch_norms = [False] * len(channel_sizes)

        if weight_norms is None:
            weight_norms = [False] * len(channel_sizes)

        if dropouts is None:
            dropouts = [0.0] * len(channel_sizes)

        # layers
        for chan_out, kernel_size, padding, batch_norm, act, stride, weight_norm, dropout in \
                zip(channel_sizes, kernel_sizes, paddings, batch_norms, layer_acts, strides, weight_norms,
                    dropouts, strict=True):

            module_list = nn.ModuleList()

            # linear
            conv_layer: Union[nn.Conv2d, nn.ConvTranspose2d]
            if transpose:
                conv_layer = nn.ConvTranspose2d(chan_in, chan_out, kernel_size, padding=padding, stride=stride)
            else:
                conv_layer = nn.Conv2d(chan_in, chan_out, kernel_size, padding=padding, stride=stride)

            if weight_norm:
                conv_layer = parametrizations.weight_norm(conv_layer)

            module_list.append(conv_layer)

            # batch norm
            if batch_norm:
                module_list.append(nn.BatchNorm2d(chan_out))

            # activation
            module_list.append(get_act_fn(act))

            # dropout
            if dropout > 0.0:
                module_list.append(nn.Dropout(dropout))

            self.layers.append(module_list)

            chan_in = chan_out

    def forward(self, x: Tensor) -> Tensor:
        """ Run ``x`` through all conv layers in order. """
        x = x.float()

        module_list: nn.Module
        for module_list in self.layers:
            assert isinstance(module_list, nn.ModuleList)
            for module in module_list:
                x = module(x)

        return x
```
