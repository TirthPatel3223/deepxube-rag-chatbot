---
id: "func:deepxube.nnet.pytorch_models.ResnetModel.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.nnet.pytorch_models.ResnetModel.__init__"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 148
line_end: 160
class: "ResnetModel"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "block_init"
    annotation: "Callable[[], nn.Module]"
    default: null
  - name: "num_resnet_blocks"
    annotation: "int"
    default: null
  - name: "act_fn"
    annotation: "str"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [150]
  - target: null
    expr: "super"
    call_sites: [150]
  - target: "func:torch.nn.ModuleList"
    expr: "nn.ModuleList"
    call_sites: [151, 152, 157]
  - target: null
    expr: "range"
    call_sites: [155]
  - target: "func:deepxube.nnet.pytorch_models.block_init"
    expr: "block_init"
    call_sites: [156]
  - target: null
    expr: "self.blocks.append"
    call_sites: [159]
  - target: null
    expr: "self.act_fns.append"
    call_sites: [160]
  - target: "func:deepxube.nnet.pytorch_models.get_act_fn"
    expr: "get_act_fn"
    call_sites: [160]
raises: []
reads_attrs:
  - "self.act_fns"
  - "self.blocks"
writes_attrs:
  - "self.act_fns"
  - "self.blocks"
---

# `deepxube.nnet.pytorch_models.ResnetModel.__init__`

**File:** [deepxube/nnet/pytorch_models.py:148](../../../../deepxube/nnet/pytorch_models.py#L148)
**Class:** `ResnetModel`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, block_init: Callable[[], nn.Module], num_resnet_blocks: int, act_fn: str)
```

## Docstring

Build ``num_resnet_blocks`` residual blocks with corresponding post-addition activations. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `block_init` | `Callable[[], nn.Module]` | — |
| `num_resnet_blocks` | `int` | — |
| `act_fn` | `str` | — |

## Returns

*(Not annotated.)*

## Calls

- `nn.ModuleList` → `func:torch.nn.ModuleList` (lines: 151, 152, 157)
- `block_init` → `func:deepxube.nnet.pytorch_models.block_init` (lines: 156)
- `get_act_fn` → `func:deepxube.nnet.pytorch_models.get_act_fn` (lines: 160)

### Unresolved
- `super().__init__` (lines: 150)
- `super` (lines: 150)
- `range` (lines: 155)
- `self.blocks.append` (lines: 159)
- `self.act_fns.append` (lines: 160)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.act_fns`
- `self.blocks`

**Reads:**
- `self.act_fns`
- `self.blocks`

## Source

```python
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
```
