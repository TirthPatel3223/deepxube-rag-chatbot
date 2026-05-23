---
id: "func:deepxube.nnet.pytorch_models.make_onehots"
kind: "function"
name: "make_onehots"
qualified_name: "deepxube.nnet.pytorch_models.make_onehots"
module: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_start: 299
line_end: 308
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "input_dims"
    annotation: "List[int]"
    default: null
  - name: "one_hot_depths"
    annotation: "List[int]"
    default: null
returns: "Tuple[nn.ModuleList, int]"
docstring_source: "present"
callees:
  - target: "func:torch.nn.ModuleList"
    expr: "nn.ModuleList"
    call_sites: [301]
  - target: null
    expr: "zip"
    call_sites: [303]
  - target: null
    expr: "one_hots.append"
    call_sites: [305]
  - target: "func:deepxube.nnet.pytorch_models.OneHot"
    expr: "OneHot"
    call_sites: [305]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.pytorch_models.make_onehots`

**File:** [deepxube/nnet/pytorch_models.py:299](../../../../deepxube/nnet/pytorch_models.py#L299)
**Visibility:** public
**Kind:** function

## Signature

```python
def make_onehots(input_dims: List[int], one_hot_depths: List[int]) -> Tuple[nn.ModuleList, int]
```

## Docstring

:return: ``(nn.ModuleList of OneHot encoders, total flattened dimension)`` for a list of flat inputs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `input_dims` | `List[int]` | — |
| `one_hot_depths` | `List[int]` | — |

## Returns

`Tuple[nn.ModuleList, int]`

## Calls

- `nn.ModuleList` → `func:torch.nn.ModuleList` (lines: 301)
- `OneHot` → `func:deepxube.nnet.pytorch_models.OneHot` (lines: 305)

### Unresolved
- `zip` (lines: 303)
- `one_hots.append` (lines: 305)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def make_onehots(input_dims: List[int], one_hot_depths: List[int]) -> Tuple[nn.ModuleList, int]:
    """ :return: ``(nn.ModuleList of OneHot encoders, total flattened dimension)`` for a list of flat inputs. """
    one_hots: nn.ModuleList = nn.ModuleList()
    input_dim_tot: int = 0
    for input_dim, one_hot_depth in zip(input_dims, one_hot_depths, strict=True):
        assert one_hot_depth >= 1
        one_hots.append(OneHot(one_hot_depth, True))
        input_dim_tot += input_dim * one_hot_depth

    return one_hots, input_dim_tot
```
