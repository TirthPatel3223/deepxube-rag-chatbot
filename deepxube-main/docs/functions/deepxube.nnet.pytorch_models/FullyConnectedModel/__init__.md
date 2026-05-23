---
id: "func:deepxube.nnet.pytorch_models.FullyConnectedModel.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.nnet.pytorch_models.FullyConnectedModel.__init__"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 180
line_end: 215
class: "FullyConnectedModel"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "input_dim"
    annotation: "int"
    default: null
  - name: "dims"
    annotation: "List[int]"
    default: null
  - name: "acts"
    annotation: "List[str]"
    default: null
  - name: "batch_norms"
    annotation: "Optional[List[bool]]"
    default: "None"
  - name: "weight_norms"
    annotation: "Optional[List[bool]]"
    default: "None"
  - name: "group_norms"
    annotation: "Optional[List[int]]"
    default: "None"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [183]
  - target: null
    expr: "super"
    call_sites: [183]
  - target: null
    expr: "len"
    call_sites: [185, 187, 189]
  - target: "func:torch.nn.ModuleList"
    expr: "nn.ModuleList"
    call_sites: [190, 195]
  - target: null
    expr: "zip"
    call_sites: [193]
  - target: null
    expr: "module_list.append"
    call_sites: [199, 201, 205, 209, 212]
  - target: null
    expr: "nn.utils.parametrizations.weight_norm"
    call_sites: [199]
  - target: "func:torch.nn.Linear"
    expr: "nn.Linear"
    call_sites: [199, 201]
  - target: "func:torch.nn.BatchNorm1d"
    expr: "nn.BatchNorm1d"
    call_sites: [205]
  - target: "func:torch.nn.GroupNorm"
    expr: "nn.GroupNorm"
    call_sites: [209]
  - target: "func:deepxube.nnet.pytorch_models.get_act_fn"
    expr: "get_act_fn"
    call_sites: [212]
  - target: null
    expr: "self.layers.append"
    call_sites: [213]
raises: []
reads_attrs:
  - "self.layers"
writes_attrs:
  - "self.layers"
---

# `deepxube.nnet.pytorch_models.FullyConnectedModel.__init__`

**File:** [deepxube/nnet/pytorch_models.py:180](../../../../deepxube/nnet/pytorch_models.py#L180)
**Class:** `FullyConnectedModel`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, input_dim: int, dims: List[int], acts: List[str], batch_norms: Optional[List[bool]] = None, weight_norms: Optional[List[bool]] = None, group_norms: Optional[List[int]] = None)
```

## Docstring

Build the layer list from ``dims``, ``acts``, and normalization flags. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `input_dim` | `int` | — |
| `dims` | `List[int]` | — |
| `acts` | `List[str]` | — |
| `batch_norms` | `Optional[List[bool]]` | `None` |
| `weight_norms` | `Optional[List[bool]]` | `None` |
| `group_norms` | `Optional[List[int]]` | `None` |

## Returns

*(Not annotated.)*

## Calls

- `nn.ModuleList` → `func:torch.nn.ModuleList` (lines: 190, 195)
- `nn.Linear` → `func:torch.nn.Linear` (lines: 199, 201)
- `nn.BatchNorm1d` → `func:torch.nn.BatchNorm1d` (lines: 205)
- `nn.GroupNorm` → `func:torch.nn.GroupNorm` (lines: 209)
- `get_act_fn` → `func:deepxube.nnet.pytorch_models.get_act_fn` (lines: 212)

### Unresolved
- `super().__init__` (lines: 183)
- `super` (lines: 183)
- `len` (lines: 185, 187, 189)
- `zip` (lines: 193)
- `module_list.append` (lines: 199, 201, 205, 209, 212)
- `nn.utils.parametrizations.weight_norm` (lines: 199)
- `self.layers.append` (lines: 213)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.layers`

**Reads:**
- `self.layers`

## Source

```python
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
```
