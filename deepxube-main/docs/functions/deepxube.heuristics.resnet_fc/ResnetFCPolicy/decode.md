---
id: "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.decode"
kind: "method"
name: "decode"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCPolicy.decode"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 120
line_end: 124
class: "ResnetFCPolicy"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_goals"
    annotation: "List[Tensor]"
    default: null
  - name: "z"
    annotation: "Tensor"
    default: null
returns: "List[Tensor]"
docstring_source: "present"
callees:
  - target: "func:deepxube.heuristics.resnet_fc.one_hot"
    expr: "one_hot"
    call_sites: [122]
  - target: null
    expr: "zip"
    call_sites: [122]
  - target: "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.decoder"
    expr: "self.decoder"
    call_sites: [123]
  - target: "func:torch.cat"
    expr: "torch.cat"
    call_sites: [123]
raises: []
reads_attrs:
  - "self.one_hots_sg"
writes_attrs: []
---

# `deepxube.heuristics.resnet_fc.ResnetFCPolicy.decode`

**File:** [deepxube/heuristics/resnet_fc.py:120](../../../../deepxube/heuristics/resnet_fc.py#L120)
**Class:** `ResnetFCPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def decode(self, states_goals: List[Tensor], z: Tensor) -> List[Tensor]
```

## Docstring

:return: Reconstructed action logit tensors decoded from latent ``z`` and the one-hot state/goal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_goals` | `List[Tensor]` | — |
| `z` | `Tensor` | — |

## Returns

`List[Tensor]`

## Calls

- `one_hot` → `func:deepxube.heuristics.resnet_fc.one_hot` (lines: 122)
- `self.decoder` → `func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.decoder` (lines: 123)
- `torch.cat` → `func:torch.cat` (lines: 123)

### Unresolved
- `zip` (lines: 122)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.one_hots_sg`

## Source

```python
    def decode(self, states_goals: List[Tensor], z: Tensor) -> List[Tensor]:
        """ :return: Reconstructed action logit tensors decoded from latent ``z`` and the one-hot state/goal. """
        states_goals_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(states_goals, self.one_hots_sg)]
        x: Tensor = self.decoder(torch.cat(states_goals_oh + [z], dim=1))
        return [x]
```
