---
id: "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.encode"
kind: "method"
name: "encode"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCPolicy.encode"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 112
line_end: 118
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
  - name: "actions"
    annotation: "List[Tensor]"
    default: null
returns: "Tuple[List[Tensor], Tensor, Tensor]"
docstring_source: "present"
callees:
  - target: "func:deepxube.heuristics.resnet_fc.one_hot"
    expr: "one_hot"
    call_sites: [114, 115]
  - target: null
    expr: "zip"
    call_sites: [114, 115]
  - target: "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.encoder"
    expr: "self.encoder"
    call_sites: [116]
  - target: "func:torch.cat"
    expr: "torch.cat"
    call_sites: [116]
raises: []
reads_attrs:
  - "self.enc_dim"
  - "self.one_hots_acts"
  - "self.one_hots_sg"
writes_attrs: []
---

# `deepxube.heuristics.resnet_fc.ResnetFCPolicy.encode`

**File:** [deepxube/heuristics/resnet_fc.py:112](../../../../deepxube/heuristics/resnet_fc.py#L112)
**Class:** `ResnetFCPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def encode(self, states_goals: List[Tensor], actions: List[Tensor]) -> Tuple[List[Tensor], Tensor, Tensor]
```

## Docstring

:return: Tuple of (one-hot actions, mu, log-var) produced by the VAE encoder. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_goals` | `List[Tensor]` | — |
| `actions` | `List[Tensor]` | — |

## Returns

`Tuple[List[Tensor], Tensor, Tensor]`

## Calls

- `one_hot` → `func:deepxube.heuristics.resnet_fc.one_hot` (lines: 114, 115)
- `self.encoder` → `func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.encoder` (lines: 116)
- `torch.cat` → `func:torch.cat` (lines: 116)

### Unresolved
- `zip` (lines: 114, 115)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.enc_dim`
- `self.one_hots_acts`
- `self.one_hots_sg`

## Source

```python
    def encode(self, states_goals: List[Tensor], actions: List[Tensor]) -> Tuple[List[Tensor], Tensor, Tensor]:
        """ :return: Tuple of (one-hot actions, mu, log-var) produced by the VAE encoder. """
        states_goals_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(states_goals, self.one_hots_sg)]
        actions_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(actions, self.one_hots_acts)]
        mu_logvar: Tensor = self.encoder(torch.cat(states_goals_oh + actions_oh, dim=1))

        return actions_oh, mu_logvar[:, :self.enc_dim], mu_logvar[:, self.enc_dim:]
```
