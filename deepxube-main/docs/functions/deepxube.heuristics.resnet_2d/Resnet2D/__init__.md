---
id: "func:deepxube.heuristics.resnet_2d.Resnet2D.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.heuristics.resnet_2d.Resnet2D.__init__"
module: "deepxube.heuristics.resnet_2d"
file: "deepxube/heuristics/resnet_2d.py"
line_start: 27
line_end: 63
class: "Resnet2D"
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
    annotation: "TwoDIn"
    default: null
  - name: "out_dim"
    annotation: "int"
    default: null
  - name: "q_fix"
    annotation: "bool"
    default: null
  - name: "num_chan"
    annotation: "int"
    default: "64"
  - name: "num_blocks"
    annotation: "int"
    default: "4"
  - name: "batch_norm"
    annotation: "bool"
    default: "False"
  - name: "weight_norm"
    annotation: "bool"
    default: "False"
  - name: "act_fn"
    annotation: "str"
    default: "'RELU'"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [30]
  - target: null
    expr: "super"
    call_sites: [30]
  - target: null
    expr: "self.nnet_input.get_input_info"
    call_sites: [32]
  - target: "func:torch.nn.ModuleList"
    expr: "nn.ModuleList"
    call_sites: [35]
  - target: null
    expr: "zip"
    call_sites: [37]
  - target: null
    expr: "self.one_hots.append"
    call_sites: [39]
  - target: "func:deepxube.nnet.pytorch_models.OneHot"
    expr: "OneHot"
    call_sites: [39]
  - target: "func:deepxube.nnet.pytorch_models.Conv2dModel"
    expr: "Conv2dModel"
    call_sites: [44, 48, 55, 60]
  - target: "func:torch.nn.Sequential"
    expr: "nn.Sequential"
    call_sites: [47, 54, 59]
  - target: "func:deepxube.nnet.pytorch_models.ResnetModel"
    expr: "ResnetModel"
    call_sites: [49]
  - target: "func:torch.nn.Flatten"
    expr: "nn.Flatten"
    call_sites: [56, 61]
  - target: "func:torch.nn.Linear"
    expr: "nn.Linear"
    call_sites: [62]
raises: []
reads_attrs:
  - "self.heur"
  - "self.nnet_input"
  - "self.one_hots"
  - "self.out"
  - "self.q_fix"
writes_attrs:
  - "self.heur"
  - "self.one_hots"
  - "self.out"
---

# `deepxube.heuristics.resnet_2d.Resnet2D.__init__`

**File:** [deepxube/heuristics/resnet_2d.py:27](../../../../deepxube/heuristics/resnet_2d.py#L27)
**Class:** `Resnet2D`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, nnet_input: TwoDIn, out_dim: int, q_fix: bool, num_chan: int = 64, num_blocks: int = 4, batch_norm: bool = False, weight_norm: bool = False, act_fn: str = 'RELU')
```

## Docstring

Build one-hot encoders, residual body, and output head from ``nnet_input`` metadata. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_input` | `TwoDIn` | — |
| `out_dim` | `int` | — |
| `q_fix` | `bool` | — |
| `num_chan` | `int` | `64` |
| `num_blocks` | `int` | `4` |
| `batch_norm` | `bool` | `False` |
| `weight_norm` | `bool` | `False` |
| `act_fn` | `str` | `'RELU'` |

## Returns

*(Not annotated.)*

## Calls

- `nn.ModuleList` → `func:torch.nn.ModuleList` (lines: 35)
- `OneHot` → `func:deepxube.nnet.pytorch_models.OneHot` (lines: 39)
- `Conv2dModel` → `func:deepxube.nnet.pytorch_models.Conv2dModel` (lines: 44, 48, 55, 60)
- `nn.Sequential` → `func:torch.nn.Sequential` (lines: 47, 54, 59)
- `ResnetModel` → `func:deepxube.nnet.pytorch_models.ResnetModel` (lines: 49)
- `nn.Flatten` → `func:torch.nn.Flatten` (lines: 56, 61)
- `nn.Linear` → `func:torch.nn.Linear` (lines: 62)

### Unresolved
- `super().__init__` (lines: 30)
- `super` (lines: 30)
- `self.nnet_input.get_input_info` (lines: 32)
- `zip` (lines: 37)
- `self.one_hots.append` (lines: 39)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.heur`
- `self.one_hots`
- `self.out`

**Reads:**
- `self.heur`
- `self.nnet_input`
- `self.one_hots`
- `self.out`
- `self.q_fix`

## Source

```python
    def __init__(self, nnet_input: TwoDIn, out_dim: int, q_fix: bool, num_chan: int = 64, num_blocks: int = 4,
                 batch_norm: bool = False, weight_norm: bool = False, act_fn: str = "RELU"):
        """ Build one-hot encoders, residual body, and output head from ``nnet_input`` metadata. """
        super().__init__(nnet_input, out_dim, q_fix)

        chan_dims, (height, width), one_hot_depths, q_fix_1x1 = self.nnet_input.get_input_info()

        # one hots
        self.one_hots: nn.ModuleList = nn.ModuleList()
        chan_in_tot: int = 0
        for chan_dim, one_hot_depth in zip(chan_dims, one_hot_depths, strict=True):
            assert one_hot_depth >= 1
            self.one_hots.append(OneHot(one_hot_depth, False))
            chan_in_tot += chan_dim * one_hot_depth

        # res net
        def res_block_init() -> nn.Module:
            return Conv2dModel(num_chan, [num_chan] * 2, [3] * 2, [1] * 2, [act_fn, "LINEAR"],
                               batch_norms=[batch_norm] * 2, weight_norms=[weight_norm] * 2)

        self.heur = nn.Sequential(
            Conv2dModel(chan_in_tot, [num_chan], [1], [0], ["LINEAR"]),
            ResnetModel(res_block_init, num_blocks, act_fn),
        )

        if self.q_fix and (q_fix_1x1 is not None):
            assert (height * width * q_fix_1x1) == out_dim
            self.out = nn.Sequential(
                Conv2dModel(num_chan, [q_fix_1x1], [1], [0], ["LINEAR"]),
                nn.Flatten(),
            )
        else:
            self.out = nn.Sequential(
                Conv2dModel(num_chan, [1], [1], [0], ["LINEAR"]),
                nn.Flatten(),
                nn.Linear(height * width, out_dim)
            )
```
