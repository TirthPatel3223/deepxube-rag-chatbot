---
id: "func:deepxube.base.heuristic._flatten_list"
kind: "function"
name: "_flatten_list"
qualified_name: "deepxube.base.heuristic._flatten_list"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 123
line_end: 125
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "data_l"
    annotation: "List[Tensor]"
    default: null
returns: "Tensor"
docstring_source: "present"
callees:
  - target: "func:torch.cat"
    expr: "torch.cat"
    call_sites: [125]
  - target: "func:torch.flatten"
    expr: "torch.flatten"
    call_sites: [125]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic._flatten_list`

**File:** [deepxube/base/heuristic.py:123](../../../../deepxube/base/heuristic.py#L123)
**Visibility:** private
**Kind:** function

## Signature

```python
def _flatten_list(data_l: List[Tensor]) -> Tensor
```

## Docstring

Concatenate every tensor in ``data_l`` into a single flat tensor. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `data_l` | `List[Tensor]` | — |

## Returns

`Tensor`

## Calls

- `torch.cat` → `func:torch.cat` (lines: 125)
- `torch.flatten` → `func:torch.flatten` (lines: 125)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _flatten_list(data_l: List[Tensor]) -> Tensor:
    """ Concatenate every tensor in ``data_l`` into a single flat tensor. """
    return torch.cat([torch.flatten(data_i) for data_i in data_l])
```
