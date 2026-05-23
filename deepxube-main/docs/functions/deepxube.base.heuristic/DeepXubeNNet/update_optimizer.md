---
id: "func:deepxube.base.heuristic.DeepXubeNNet.update_optimizer"
kind: "method"
name: "update_optimizer"
qualified_name: "deepxube.base.heuristic.DeepXubeNNet.update_optimizer"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 58
line_end: 62
class: "DeepXubeNNet"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "optimizer"
    annotation: "Optimizer"
    default: null
  - name: "train_itr"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees: []
raises: []
reads_attrs:
  - "self.lr"
  - "self.lr_d"
writes_attrs: []
---

# `deepxube.base.heuristic.DeepXubeNNet.update_optimizer`

**File:** [deepxube/base/heuristic.py:58](../../../../deepxube/base/heuristic.py#L58)
**Class:** `DeepXubeNNet`
**Visibility:** public
**Kind:** method

## Signature

```python
def update_optimizer(self, optimizer: Optimizer, train_itr: int) -> None
```

## Docstring

Apply geometric LR decay ``lr * lr_d ** train_itr`` to every param group. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `optimizer` | `Optimizer` | — |
| `train_itr` | `int` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.lr`
- `self.lr_d`

## Source

```python
    def update_optimizer(self, optimizer: Optimizer, train_itr: int) -> None:
        """ Apply geometric LR decay ``lr * lr_d ** train_itr`` to every param group. """
        lr_itr: float = self.lr * (self.lr_d ** train_itr)
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr_itr
```
