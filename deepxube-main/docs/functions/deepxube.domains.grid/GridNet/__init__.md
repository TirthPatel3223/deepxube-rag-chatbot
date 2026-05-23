---
id: "func:deepxube.domains.grid.GridNet.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.grid.GridNet.__init__"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 188
line_end: 200
class: "GridNet"
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
    annotation: "GridNNetInput"
    default: null
  - name: "out_dim"
    annotation: "int"
    default: null
  - name: "q_fix"
    annotation: "bool"
    default: null
  - name: "chan_size"
    annotation: "int"
    default: "8"
  - name: "fc_size"
    annotation: "int"
    default: "100"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [190]
  - target: null
    expr: "super"
    call_sites: [190]
  - target: "func:torch.nn.ModuleList"
    expr: "nn.ModuleList"
    call_sites: [192]
  - target: null
    expr: "self.nnet_input.get_input_info"
    call_sites: [193]
  - target: "func:torch.nn.Sequential"
    expr: "nn.Sequential"
    call_sites: [195]
  - target: "func:deepxube.nnet.pytorch_models.Conv2dModel"
    expr: "Conv2dModel"
    call_sites: [196]
  - target: "func:torch.nn.Flatten"
    expr: "nn.Flatten"
    call_sites: [197]
  - target: "func:deepxube.nnet.pytorch_models.FullyConnectedModel"
    expr: "FullyConnectedModel"
    call_sites: [198]
  - target: "func:torch.nn.Linear"
    expr: "nn.Linear"
    call_sites: [199]
raises: []
reads_attrs:
  - "self.heur"
  - "self.nnet_input"
  - "self.one_hots"
  - "self.out_dim"
writes_attrs:
  - "self.heur"
  - "self.one_hots"
---

# `deepxube.domains.grid.GridNet.__init__`

**File:** [deepxube/domains/grid.py:188](../../../../deepxube/domains/grid.py#L188)
**Class:** `GridNet`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, nnet_input: GridNNetInput, out_dim: int, q_fix: bool, chan_size: int = 8, fc_size: int = 100)
```

## Docstring

Build the Conv2d and FC layers from grid dimensions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_input` | `GridNNetInput` | — |
| `out_dim` | `int` | — |
| `q_fix` | `bool` | — |
| `chan_size` | `int` | `8` |
| `fc_size` | `int` | `100` |

## Returns

*(Not annotated.)*

## Calls

- `nn.ModuleList` → `func:torch.nn.ModuleList` (lines: 192)
- `nn.Sequential` → `func:torch.nn.Sequential` (lines: 195)
- `Conv2dModel` → `func:deepxube.nnet.pytorch_models.Conv2dModel` (lines: 196)
- `nn.Flatten` → `func:torch.nn.Flatten` (lines: 197)
- `FullyConnectedModel` → `func:deepxube.nnet.pytorch_models.FullyConnectedModel` (lines: 198)
- `nn.Linear` → `func:torch.nn.Linear` (lines: 199)

### Unresolved
- `super().__init__` (lines: 190)
- `super` (lines: 190)
- `self.nnet_input.get_input_info` (lines: 193)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.heur`
- `self.one_hots`

**Reads:**
- `self.heur`
- `self.nnet_input`
- `self.one_hots`
- `self.out_dim`

## Source

```python
    def __init__(self, nnet_input: GridNNetInput, out_dim: int, q_fix: bool, chan_size: int = 8, fc_size: int = 100):
        """ Build the Conv2d and FC layers from grid dimensions. """
        super().__init__(nnet_input, out_dim, q_fix)
        # one hots
        self.one_hots: nn.ModuleList = nn.ModuleList()
        grid_dim: int = self.nnet_input.get_input_info()

        self.heur: nn.Module = nn.Sequential(
            Conv2dModel(2, [chan_size, chan_size], [3, 3], [1, 1], ["RELU", "RELU"], batch_norms=[True, True]),
            nn.Flatten(),
            FullyConnectedModel(grid_dim * grid_dim * chan_size, [fc_size], ["RELU"], batch_norms=[True]),
            nn.Linear(fc_size, self.out_dim)
        )
```
