---
id: "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCPolicy.__init__"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 71
line_end: 106
class: "ResnetFCPolicy"
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
    annotation: "FlatInPolicy"
    default: null
  - name: "kl_weight"
    annotation: "float"
    default: null
  - name: "enc_dim"
    annotation: "int"
    default: "10"
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
    call_sites: [74]
  - target: null
    expr: "super"
    call_sites: [74]
  - target: null
    expr: "self.nnet_input.get_input_info"
    call_sites: [76]
  - target: null
    expr: "self.nnet_input.states_goals_actions_split_idx"
    call_sites: [77, 78, 79, 80]
  - target: "func:deepxube.nnet.pytorch_models.make_onehots"
    expr: "make_onehots"
    call_sites: [82, 83]
  - target: "func:deepxube.nnet.pytorch_models.FullyConnectedModel"
    expr: "FullyConnectedModel"
    call_sites: [92]
  - target: "func:torch.nn.Sequential"
    expr: "nn.Sequential"
    call_sites: [96, 102]
  - target: "func:torch.nn.Linear"
    expr: "nn.Linear"
    call_sites: [97, 99, 103, 105]
  - target: "func:deepxube.nnet.pytorch_models.ResnetModel"
    expr: "ResnetModel"
    call_sites: [98, 104]
raises: []
reads_attrs:
  - "self.decoder"
  - "self.enc_dim"
  - "self.encoder"
  - "self.nnet_input"
  - "self.one_hots_acts"
  - "self.one_hots_sg"
  - "self.res_dim"
writes_attrs:
  - "self.decoder"
  - "self.enc_dim"
  - "self.encoder"
  - "self.res_dim"
---

# `deepxube.heuristics.resnet_fc.ResnetFCPolicy.__init__`

**File:** [deepxube/heuristics/resnet_fc.py:71](../../../../deepxube/heuristics/resnet_fc.py#L71)
**Class:** `ResnetFCPolicy`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, nnet_input: FlatInPolicy, kl_weight: float, enc_dim: int = 10, res_dim: int = 1000, num_blocks: int = 4, batch_norm: bool = False, weight_norm: bool = False, group_norm: int = -1, act_fn: str = 'RELU')
```

## Docstring

Build encoder (state+goal+action → latent) and decoder (state+goal+z → action logits). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_input` | `FlatInPolicy` | — |
| `kl_weight` | `float` | — |
| `enc_dim` | `int` | `10` |
| `res_dim` | `int` | `1000` |
| `num_blocks` | `int` | `4` |
| `batch_norm` | `bool` | `False` |
| `weight_norm` | `bool` | `False` |
| `group_norm` | `int` | `-1` |
| `act_fn` | `str` | `'RELU'` |

## Returns

*(Not annotated.)*

## Calls

- `make_onehots` → `func:deepxube.nnet.pytorch_models.make_onehots` (lines: 82, 83)
- `FullyConnectedModel` → `func:deepxube.nnet.pytorch_models.FullyConnectedModel` (lines: 92)
- `nn.Sequential` → `func:torch.nn.Sequential` (lines: 96, 102)
- `nn.Linear` → `func:torch.nn.Linear` (lines: 97, 99, 103, 105)
- `ResnetModel` → `func:deepxube.nnet.pytorch_models.ResnetModel` (lines: 98, 104)

### Unresolved
- `super().__init__` (lines: 74)
- `super` (lines: 74)
- `self.nnet_input.get_input_info` (lines: 76)
- `self.nnet_input.states_goals_actions_split_idx` (lines: 77, 78, 79, 80)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.decoder`
- `self.enc_dim`
- `self.encoder`
- `self.res_dim`

**Reads:**
- `self.decoder`
- `self.enc_dim`
- `self.encoder`
- `self.nnet_input`
- `self.one_hots_acts`
- `self.one_hots_sg`
- `self.res_dim`

## Source

```python
    def __init__(self, nnet_input: FlatInPolicy, kl_weight: float, enc_dim: int = 10, res_dim: int = 1000, num_blocks: int = 4, batch_norm: bool = False,
                 weight_norm: bool = False, group_norm: int = -1, act_fn: str = "RELU"):
        """ Build encoder (state+goal+action → latent) and decoder (state+goal+z → action logits). """
        super().__init__(nnet_input, kl_weight)
        # one hots
        input_dims, one_hot_depths = self.nnet_input.get_input_info()
        input_dims_sg: List[int] = input_dims[:self.nnet_input.states_goals_actions_split_idx()]
        one_hot_depths_sg: List[int] = one_hot_depths[:self.nnet_input.states_goals_actions_split_idx()]
        input_dims_acts: List[int] = input_dims[self.nnet_input.states_goals_actions_split_idx():]
        one_hot_depths_acts: List[int] = one_hot_depths[self.nnet_input.states_goals_actions_split_idx():]

        self.one_hots_sg, input_dim_sg = make_onehots(input_dims_sg, one_hot_depths_sg)
        self.one_hots_acts, input_dim_acts = make_onehots(input_dims_acts, one_hot_depths_acts)
        input_dim_tot: int = input_dim_sg + input_dim_acts

        self.enc_dim: int = enc_dim

        # res net
        self.res_dim: int = res_dim

        def res_block_init() -> nn.Module:
            return FullyConnectedModel(res_dim, [res_dim] * 2, [act_fn, "LINEAR"],
                                       batch_norms=[batch_norm] * 2, weight_norms=[weight_norm] * 2,
                                       group_norms=[group_norm] * 2)

        self.encoder = nn.Sequential(
            nn.Linear(input_dim_tot, res_dim),
            ResnetModel(res_block_init, num_blocks, act_fn),
            nn.Linear(res_dim, self.enc_dim * 2)
        )

        self.decoder = nn.Sequential(
            nn.Linear(input_dim_sg + self.enc_dim, res_dim),
            ResnetModel(res_block_init, num_blocks, act_fn),
            nn.Linear(res_dim, input_dim_acts)
        )
```
