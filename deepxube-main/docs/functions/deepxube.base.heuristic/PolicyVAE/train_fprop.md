---
id: "func:deepxube.base.heuristic.PolicyVAE.train_fprop"
kind: "method"
name: "train_fprop"
qualified_name: "deepxube.base.heuristic.PolicyVAE.train_fprop"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 145
line_end: 163
class: "PolicyVAE"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_goals_actions"
    annotation: "List[Tensor]"
    default: null
returns: "Tuple[Tensor, str]"
docstring_source: "present"
callees:
  - target: null
    expr: "self.nnet_input.states_goals_actions_split_idx"
    call_sites: [147]
  - target: "func:deepxube.base.heuristic.PolicyVAE.encode"
    expr: "self.encode"
    call_sites: [151]
  - target: null
    expr: "tuple"
    call_sites: [152]
  - target: null
    expr: "range"
    call_sites: [152]
  - target: null
    expr: "len"
    call_sites: [152]
  - target: "func:torch.mean"
    expr: "torch.mean"
    call_sites: [153]
  - target: "func:torch.sum"
    expr: "torch.sum"
    call_sites: [153]
  - target: null
    expr: "logvar.exp"
    call_sites: [153]
  - target: "func:torch.exp"
    expr: "torch.exp"
    call_sites: [155]
  - target: null
    expr: "self.norm_dist.sample(mu.shape).to"
    call_sites: [156]
  - target: null
    expr: "self.norm_dist.sample"
    call_sites: [156]
  - target: "func:deepxube.base.heuristic.PolicyVAE.decode"
    expr: "self.decode"
    call_sites: [157]
  - target: "func:deepxube.base.heuristic.PolicyVAE._compute_recon_loss"
    expr: "self._compute_recon_loss"
    call_sites: [159]
  - target: null
    expr: "loss_recon.item"
    call_sites: [162]
  - target: null
    expr: "loss_kl.item"
    call_sites: [162]
raises: []
reads_attrs:
  - "self.kl_weight"
  - "self.nnet_input"
  - "self.norm_dist"
writes_attrs: []
---

# `deepxube.base.heuristic.PolicyVAE.train_fprop`

**File:** [deepxube/base/heuristic.py:145](../../../../deepxube/base/heuristic.py#L145)
**Class:** `PolicyVAE`
**Visibility:** public
**Kind:** method

## Signature

```python
def train_fprop(self, states_goals_actions: List[Tensor]) -> Tuple[Tensor, str]
```

## Docstring

Encode → KL + reparameterised decode → MSE reconstruction; returns total loss + log string. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_goals_actions` | `List[Tensor]` | — |

## Returns

`Tuple[Tensor, str]`

## Calls

- `self.encode` → `func:deepxube.base.heuristic.PolicyVAE.encode` (lines: 151)
- `torch.mean` → `func:torch.mean` (lines: 153)
- `torch.sum` → `func:torch.sum` (lines: 153)
- `torch.exp` → `func:torch.exp` (lines: 155)
- `self.decode` → `func:deepxube.base.heuristic.PolicyVAE.decode` (lines: 157)
- `self._compute_recon_loss` → `func:deepxube.base.heuristic.PolicyVAE._compute_recon_loss` (lines: 159)

### Unresolved
- `self.nnet_input.states_goals_actions_split_idx` (lines: 147)
- `tuple` (lines: 152)
- `range` (lines: 152)
- `len` (lines: 152)
- `logvar.exp` (lines: 153)
- `self.norm_dist.sample(mu.shape).to` (lines: 156)
- `self.norm_dist.sample` (lines: 156)
- `loss_recon.item` (lines: 162)
- `loss_kl.item` (lines: 162)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.kl_weight`
- `self.nnet_input`
- `self.norm_dist`

## Source

```python
    def train_fprop(self, states_goals_actions: List[Tensor]) -> Tuple[Tensor, str]:
        """ Encode → KL + reparameterised decode → MSE reconstruction; returns total loss + log string. """
        split_idx: int = self.nnet_input.states_goals_actions_split_idx()
        states_goals: List[Tensor] = states_goals_actions[:split_idx]
        actions: List[Tensor] = states_goals_actions[split_idx:]

        actions_proc, mu, logvar = self.encode(states_goals, actions)
        sum_dims: Tuple[int, ...] = tuple(range(1, len(mu.shape)))
        loss_kl: Tensor = torch.mean(-0.5 * torch.sum(1 + logvar - mu ** 2 - logvar.exp(), dim=sum_dims), dim=0)

        sigma = torch.exp(logvar / 2.0)
        z = mu + sigma * self.norm_dist.sample(mu.shape).to(mu.device)
        actions_recon: List[Tensor] = self.decode(states_goals, z)

        loss_recon: Tensor = self._compute_recon_loss(actions_proc, actions_recon)
        loss: Tensor = loss_recon + (self.kl_weight * loss_kl)

        print_str: str = f"loss_recon: {loss_recon.item():.2E}, loss_kl: {loss_kl.item():.2E}"
        return loss, print_str
```
