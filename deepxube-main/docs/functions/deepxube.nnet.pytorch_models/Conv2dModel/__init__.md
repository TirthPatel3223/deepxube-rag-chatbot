---
id: "func:deepxube.nnet.pytorch_models.Conv2dModel.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.nnet.pytorch_models.Conv2dModel.__init__"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 233
line_end: 284
class: "Conv2dModel"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "chan_in"
    annotation: "int"
    default: null
  - name: "channel_sizes"
    annotation: "List[int]"
    default: null
  - name: "kernel_sizes"
    annotation: "List[int]"
    default: null
  - name: "paddings"
    annotation: "List[int]"
    default: null
  - name: "layer_acts"
    annotation: "List[str]"
    default: null
  - name: "batch_norms"
    annotation: "Optional[List[bool]]"
    default: "None"
  - name: "strides"
    annotation: "Optional[List[int]]"
    default: "None"
  - name: "transpose"
    annotation: "bool"
    default: "False"
  - name: "weight_norms"
    annotation: "Optional[List[bool]]"
    default: "None"
  - name: "dropouts"
    annotation: "Optional[List[float]]"
    default: "None"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [238]
  - target: null
    expr: "super"
    call_sites: [238]
  - target: "func:torch.nn.ModuleList"
    expr: "nn.ModuleList"
    call_sites: [239, 257]
  - target: null
    expr: "len"
    call_sites: [241, 244, 247, 250]
  - target: null
    expr: "zip"
    call_sites: [254]
  - target: "func:torch.nn.ConvTranspose2d"
    expr: "nn.ConvTranspose2d"
    call_sites: [262]
  - target: "func:torch.nn.Conv2d"
    expr: "nn.Conv2d"
    call_sites: [264]
  - target: "func:torch.nn.utils.parametrizations.weight_norm"
    expr: "parametrizations.weight_norm"
    call_sites: [267]
  - target: null
    expr: "module_list.append"
    call_sites: [269, 273, 276, 280]
  - target: "func:torch.nn.BatchNorm2d"
    expr: "nn.BatchNorm2d"
    call_sites: [273]
  - target: "func:deepxube.nnet.pytorch_models.get_act_fn"
    expr: "get_act_fn"
    call_sites: [276]
  - target: "func:torch.nn.Dropout"
    expr: "nn.Dropout"
    call_sites: [280]
  - target: null
    expr: "self.layers.append"
    call_sites: [282]
raises: []
reads_attrs:
  - "self.layers"
writes_attrs:
  - "self.layers"
---

# `deepxube.nnet.pytorch_models.Conv2dModel.__init__`

**File:** [deepxube/nnet/pytorch_models.py:233](../../../../deepxube/nnet/pytorch_models.py#L233)
**Class:** `Conv2dModel`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, chan_in: int, channel_sizes: List[int], kernel_sizes: List[int], paddings: List[int], layer_acts: List[str], batch_norms: Optional[List[bool]] = None, strides: Optional[List[int]] = None, transpose: bool = False, weight_norms: Optional[List[bool]] = None, dropouts: Optional[List[float]] = None)
```

## Docstring

Build the conv layer list from channel sizes, kernels, paddings, and normalization/activation flags. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `chan_in` | `int` | — |
| `channel_sizes` | `List[int]` | — |
| `kernel_sizes` | `List[int]` | — |
| `paddings` | `List[int]` | — |
| `layer_acts` | `List[str]` | — |
| `batch_norms` | `Optional[List[bool]]` | `None` |
| `strides` | `Optional[List[int]]` | `None` |
| `transpose` | `bool` | `False` |
| `weight_norms` | `Optional[List[bool]]` | `None` |
| `dropouts` | `Optional[List[float]]` | `None` |

## Returns

*(Not annotated.)*

## Calls

- `nn.ModuleList` → `func:torch.nn.ModuleList` (lines: 239, 257)
- `nn.ConvTranspose2d` → `func:torch.nn.ConvTranspose2d` (lines: 262)
- `nn.Conv2d` → `func:torch.nn.Conv2d` (lines: 264)
- `parametrizations.weight_norm` → `func:torch.nn.utils.parametrizations.weight_norm` (lines: 267)
- `nn.BatchNorm2d` → `func:torch.nn.BatchNorm2d` (lines: 273)
- `get_act_fn` → `func:deepxube.nnet.pytorch_models.get_act_fn` (lines: 276)
- `nn.Dropout` → `func:torch.nn.Dropout` (lines: 280)

### Unresolved
- `super().__init__` (lines: 238)
- `super` (lines: 238)
- `len` (lines: 241, 244, 247, 250)
- `zip` (lines: 254)
- `module_list.append` (lines: 269, 273, 276, 280)
- `self.layers.append` (lines: 282)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.layers`

**Reads:**
- `self.layers`

## Source

```python
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
```
