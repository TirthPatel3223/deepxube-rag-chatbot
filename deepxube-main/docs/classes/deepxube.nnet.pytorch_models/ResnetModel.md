---
id: "class:deepxube.nnet.pytorch_models.ResnetModel"
kind: "class"
name: "ResnetModel"
qualified_name: "deepxube.nnet.pytorch_models.ResnetModel"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 145
line_end: 174
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "nn.Module"
    resolved_id: null
methods:
  - "func:deepxube.nnet.pytorch_models.ResnetModel.__init__"
  - "func:deepxube.nnet.pytorch_models.ResnetModel.forward"
attributes:
  - name: "self.act_fns"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.blocks"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.pytorch_models.ResnetModel`

**File:** [deepxube/nnet/pytorch_models.py:145](../../../deepxube/nnet/pytorch_models.py#L145)
**Abstract:** no

## Docstring

Stacked residual blocks; each block is produced by ``block_init()`` and followed by a post-addition activation. 

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
| `self.act_fns` | — | __init__ |
| `self.blocks` | — | __init__ |

## Source

```python
class ResnetModel(nn.Module):
    """ Stacked residual blocks; each block is produced by ``block_init()`` and followed by a post-addition activation. """

    def __init__(self, block_init: Callable[[], nn.Module], num_resnet_blocks: int, act_fn: str):
        """ Build ``num_resnet_blocks`` residual blocks with corresponding post-addition activations. """
        super().__init__()
        self.blocks: nn.ModuleList = nn.ModuleList()
        self.act_fns: nn.ModuleList = nn.ModuleList()

        # resnet blocks
        for block_num in range(num_resnet_blocks):
            block_net: nn.Module = block_init()
            module_list: nn.ModuleList = nn.ModuleList([block_net])

            self.blocks.append(module_list)
            self.act_fns.append(get_act_fn(act_fn))

    def forward(self, x: Tensor) -> Tensor:
        """ Pass ``x`` through each residual block (skip connection + post-addition activation). """
        # resnet blocks
        module_list: nn.Module
        for module_list, act_fn in zip(self.blocks, self.act_fns, strict=True):
            assert isinstance(module_list, nn.ModuleList)
            res_inp = x
            for module in module_list:
                x = module(x)

            x = act_fn(x + res_inp)

        return x
```
