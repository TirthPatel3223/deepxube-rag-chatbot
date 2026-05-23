---
id: "func:deepxube.heuristics.resnet_fc.ResnetFCHeur._forward"
kind: "method"
name: "_forward"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCHeur._forward"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 54
line_end: 58
class: "ResnetFCHeur"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "inputs"
    annotation: "List[Tensor]"
    default: null
returns: "Tensor"
docstring_source: "present"
callees:
  - target: "func:deepxube.heuristics.resnet_fc.one_hot"
    expr: "one_hot"
    call_sites: [56]
  - target: null
    expr: "zip"
    call_sites: [56]
  - target: "func:deepxube.heuristics.resnet_fc.ResnetFCHeur.heur"
    expr: "self.heur"
    call_sites: [57]
  - target: "func:torch.cat"
    expr: "torch.cat"
    call_sites: [57]
raises: []
reads_attrs:
  - "self.one_hots"
writes_attrs: []
---

# `deepxube.heuristics.resnet_fc.ResnetFCHeur._forward`

**File:** [deepxube/heuristics/resnet_fc.py:54](../../../../deepxube/heuristics/resnet_fc.py#L54)
**Class:** `ResnetFCHeur`
**Visibility:** private
**Kind:** method

## Signature

```python
def _forward(self, inputs: List[Tensor]) -> Tensor
```

## Docstring

One-hot encode each input, concatenate, and run through the residual network. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `inputs` | `List[Tensor]` | — |

## Returns

`Tensor`

## Calls

- `one_hot` → `func:deepxube.heuristics.resnet_fc.one_hot` (lines: 56)
- `self.heur` → `func:deepxube.heuristics.resnet_fc.ResnetFCHeur.heur` (lines: 57)
- `torch.cat` → `func:torch.cat` (lines: 57)

### Unresolved
- `zip` (lines: 56)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.one_hots`

## Source

```python
    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ One-hot encode each input, concatenate, and run through the residual network. """
        inputs_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(inputs, self.one_hots)]
        x: Tensor = self.heur(torch.cat(inputs_oh, dim=1))
        return x
```
