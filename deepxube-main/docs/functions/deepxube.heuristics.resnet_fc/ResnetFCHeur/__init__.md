---
id: "func:deepxube.heuristics.resnet_fc.ResnetFCHeur.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCHeur.__init__"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 27
line_end: 52
class: "ResnetFCHeur"
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
    annotation: "FlatIn"
    default: null
  - name: "out_dim"
    annotation: "int"
    default: null
  - name: "q_fix"
    annotation: "bool"
    default: null
  - name: "res_dim"
    annotation: "int"
    default: "1000"
  - name: "num_blocks"
    annotation: "int"
    default: "4"
  - name: "batch_norm"
    annotation: "bool"
    default: "False"
  - name: "weight_norm"
    annotation: "bool"
    default: "False"
  - name: "group_norm"
    annotation: "int"
    default: "-1"
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
  - target: "func:torch.nn.ModuleList"
    expr: "nn.ModuleList"
    call_sites: [32]
  - target: null
    expr: "self.nnet_input.get_input_info"
    call_sites: [34]
  - target: null
    expr: "zip"
    call_sites: [35]
  - target: null
    expr: "self.one_hots.append"
    call_sites: [37]
  - target: "func:deepxube.nnet.pytorch_models.OneHot"
    expr: "OneHot"
    call_sites: [37]
  - target: "func:deepxube.nnet.pytorch_models.FullyConnectedModel"
    expr: "FullyConnectedModel"
    call_sites: [44]
  - target: "func:torch.nn.Sequential"
    expr: "nn.Sequential"
    call_sites: [48]
  - target: "func:torch.nn.Linear"
    expr: "nn.Linear"
    call_sites: [49, 51]
  - target: "func:deepxube.nnet.pytorch_models.ResnetModel"
    expr: "ResnetModel"
    call_sites: [50]
raises: []
reads_attrs:
  - "self.heur"
  - "self.nnet_input"
  - "self.one_hots"
  - "self.out_dim"
  - "self.res_dim"
writes_attrs:
  - "self.heur"
  - "self.one_hots"
  - "self.res_dim"
---

# `deepxube.heuristics.resnet_fc.ResnetFCHeur.__init__`

**File:** [deepxube/heuristics/resnet_fc.py:27](../../../../deepxube/heuristics/resnet_fc.py#L27)
**Class:** `ResnetFCHeur`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, nnet_input: FlatIn, out_dim: int, q_fix: bool, res_dim: int = 1000, num_blocks: int = 4, batch_norm: bool = False, weight_norm: bool = False, group_norm: int = -1, act_fn: str = 'RELU')
```

## Docstring

Build one-hot encoders, residual body, and linear output layer from ``nnet_input`` metadata. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_input` | `FlatIn` | — |
| `out_dim` | `int` | — |
| `q_fix` | `bool` | — |
| `res_dim` | `int` | `1000` |
| `num_blocks` | `int` | `4` |
| `batch_norm` | `bool` | `False` |
| `weight_norm` | `bool` | `False` |
| `group_norm` | `int` | `-1` |
| `act_fn` | `str` | `'RELU'` |

## Returns

*(Not annotated.)*

## Calls

- `nn.ModuleList` → `func:torch.nn.ModuleList` (lines: 32)
- `OneHot` → `func:deepxube.nnet.pytorch_models.OneHot` (lines: 37)
- `FullyConnectedModel` → `func:deepxube.nnet.pytorch_models.FullyConnectedModel` (lines: 44)
- `nn.Sequential` → `func:torch.nn.Sequential` (lines: 48)
- `nn.Linear` → `func:torch.nn.Linear` (lines: 49, 51)
- `ResnetModel` → `func:deepxube.nnet.pytorch_models.ResnetModel` (lines: 50)

### Unresolved
- `super().__init__` (lines: 30)
- `super` (lines: 30)
- `self.nnet_input.get_input_info` (lines: 34)
- `zip` (lines: 35)
- `self.one_hots.append` (lines: 37)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.heur`
- `self.one_hots`
- `self.res_dim`

**Reads:**
- `self.heur`
- `self.nnet_input`
- `self.one_hots`
- `self.out_dim`
- `self.res_dim`

## Source

```python
    def __init__(self, nnet_input: FlatIn, out_dim: int, q_fix: bool, res_dim: int = 1000, num_blocks: int = 4,
                 batch_norm: bool = False, weight_norm: bool = False, group_norm: int = -1, act_fn: str = "RELU"):
        """ Build one-hot encoders, residual body, and linear output layer from ``nnet_input`` metadata. """
        super().__init__(nnet_input, out_dim, q_fix)
        # one hots
        self.one_hots: nn.ModuleList = nn.ModuleList()
        input_dim_tot: int = 0
        input_dims, one_hot_depths = self.nnet_input.get_input_info()
        for input_dim, one_hot_depth in zip(input_dims, one_hot_depths, strict=True):
            assert one_hot_depth >= 1
            self.one_hots.append(OneHot(one_hot_depth, True))
            input_dim_tot += input_dim * one_hot_depth

        # res net
        self.res_dim: int = res_dim

        def res_block_init() -> nn.Module:
            return FullyConnectedModel(res_dim, [res_dim] * 2, [act_fn, "LINEAR"],
                                       batch_norms=[batch_norm] * 2, weight_norms=[weight_norm] * 2,
                                       group_norms=[group_norm] * 2)

        self.heur = nn.Sequential(
            nn.Linear(input_dim_tot, res_dim),
            ResnetModel(res_block_init, num_blocks, act_fn),
            nn.Linear(res_dim, self.out_dim)
        )
```
