---
id: "func:deepxube.base.heuristic.DeepXubeNNet.get_optimizer"
kind: "method"
name: "get_optimizer"
qualified_name: "deepxube.base.heuristic.DeepXubeNNet.get_optimizer"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 54
line_end: 56
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
returns: "Optimizer"
docstring_source: "present"
callees:
  - target: "func:torch.optim.Adam"
    expr: "optim.Adam"
    call_sites: [56]
  - target: "func:deepxube.base.heuristic.DeepXubeNNet.parameters"
    expr: "self.parameters"
    call_sites: [56]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.DeepXubeNNet.get_optimizer`

**File:** [deepxube/base/heuristic.py:54](../../../../deepxube/base/heuristic.py#L54)
**Class:** `DeepXubeNNet`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_optimizer(self) -> Optimizer
```

## Docstring

:return: Default Adam optimiser at lr=0.001. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Optimizer`

## Calls

- `optim.Adam` → `func:torch.optim.Adam` (lines: 56)
- `self.parameters` → `func:deepxube.base.heuristic.DeepXubeNNet.parameters` (lines: 56)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_optimizer(self) -> Optimizer:
        """ :return: Default Adam optimiser at lr=0.001. """
        return optim.Adam(self.parameters(), lr=0.001)
```
