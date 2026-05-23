---
id: "func:deepxube.base.trainer.update_optimizer"
kind: "function"
name: "update_optimizer"
qualified_name: "deepxube.base.trainer.update_optimizer"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 192
line_end: 197
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "optimizer"
    annotation: "Optimizer"
    default: null
  - name: "nnet"
    annotation: "Union[DataParallel, DeepXubeNNet]"
    default: null
  - name: "train_itr"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "isinstance"
    call_sites: [194, 196]
  - target: null
    expr: "nnet.update_optimizer"
    call_sites: [197]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.trainer.update_optimizer`

**File:** [deepxube/base/trainer.py:192](../../../../deepxube/base/trainer.py#L192)
**Visibility:** public
**Kind:** function

## Signature

```python
def update_optimizer(optimizer: Optimizer, nnet: Union[DataParallel, DeepXubeNNet], train_itr: int) -> None
```

## Docstring

Apply ``DeepXubeNNet.update_optimizer`` to ``nnet``, unwrapping ``DataParallel`` first. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `optimizer` | `Optimizer` | — |
| `nnet` | `Union[DataParallel, DeepXubeNNet]` | — |
| `train_itr` | `int` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `isinstance` (lines: 194, 196)
- `nnet.update_optimizer` (lines: 197)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def update_optimizer(optimizer: Optimizer, nnet: Union[DataParallel, DeepXubeNNet], train_itr: int) -> None:
    """ Apply ``DeepXubeNNet.update_optimizer`` to ``nnet``, unwrapping ``DataParallel`` first. """
    if isinstance(nnet, DataParallel):
        nnet = nnet.module
    assert isinstance(nnet, DeepXubeNNet)
    nnet.update_optimizer(optimizer, train_itr)
```
