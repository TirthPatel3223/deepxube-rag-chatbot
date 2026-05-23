---
id: "func:deepxube.heuristics.resnet_2d.Resnet2D._forward"
kind: "method"
name: "_forward"
qualified_name: "deepxube.heuristics.resnet_2d.Resnet2D._forward"
module: "deepxube.heuristics.resnet_2d"
file: "deepxube/heuristics/resnet_2d.py"
line_start: 65
line_end: 77
class: "Resnet2D"
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
  - target: null
    expr: "zip"
    call_sites: [68]
  - target: "func:deepxube.heuristics.resnet_2d.one_hot"
    expr: "one_hot"
    call_sites: [69]
  - target: null
    expr: "len"
    call_sites: [70]
  - target: null
    expr: "input_i_oh.permute((0, 1, 4, 2, 3)).flatten"
    call_sites: [71]
  - target: null
    expr: "input_i_oh.permute"
    call_sites: [71]
  - target: null
    expr: "inputs_oh.append"
    call_sites: [72]
  - target: "func:deepxube.heuristics.resnet_2d.Resnet2D.heur"
    expr: "self.heur"
    call_sites: [75]
  - target: "func:torch.cat"
    expr: "torch.cat"
    call_sites: [75]
  - target: "func:deepxube.heuristics.resnet_2d.Resnet2D.out"
    expr: "self.out"
    call_sites: [76]
raises: []
reads_attrs:
  - "self.one_hots"
writes_attrs: []
---

# `deepxube.heuristics.resnet_2d.Resnet2D._forward`

**File:** [deepxube/heuristics/resnet_2d.py:65](../../../../deepxube/heuristics/resnet_2d.py#L65)
**Class:** `Resnet2D`
**Visibility:** private
**Kind:** method

## Signature

```python
def _forward(self, inputs: List[Tensor]) -> Tensor
```

## Docstring

One-hot encode each input channel, concatenate spatially, run the ResNet body, and apply the output head. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `inputs` | `List[Tensor]` | — |

## Returns

`Tensor`

## Calls

- `one_hot` → `func:deepxube.heuristics.resnet_2d.one_hot` (lines: 69)
- `self.heur` → `func:deepxube.heuristics.resnet_2d.Resnet2D.heur` (lines: 75)
- `torch.cat` → `func:torch.cat` (lines: 75)
- `self.out` → `func:deepxube.heuristics.resnet_2d.Resnet2D.out` (lines: 76)

### Unresolved
- `zip` (lines: 68)
- `len` (lines: 70)
- `input_i_oh.permute((0, 1, 4, 2, 3)).flatten` (lines: 71)
- `input_i_oh.permute` (lines: 71)
- `inputs_oh.append` (lines: 72)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.one_hots`

## Source

```python
    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ One-hot encode each input channel, concatenate spatially, run the ResNet body, and apply the output head. """
        inputs_oh: List[Tensor] = []
        for input_i, one_hot in zip(inputs, self.one_hots):
            input_i_oh: Tensor = one_hot(input_i)
            if len(input_i_oh.shape) == 5:
                input_i_oh = input_i_oh.permute((0, 1, 4, 2, 3)).flatten(1, 2)
            inputs_oh.append(input_i_oh)

        # inputs_oh: List[Tensor] = [one_hot(input_i).permute((0, 1, 4, 2, 3)).flatten(1, 2) for input_i, one_hot in zip(inputs, self.one_hots)]
        x: Tensor = self.heur(torch.cat(inputs_oh, dim=1))
        x = self.out(x)
        return x
```
