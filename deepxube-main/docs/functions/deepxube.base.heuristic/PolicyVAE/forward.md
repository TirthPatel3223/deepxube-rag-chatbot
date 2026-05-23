---
id: "func:deepxube.base.heuristic.PolicyVAE.forward"
kind: "method"
name: "forward"
qualified_name: "deepxube.base.heuristic.PolicyVAE.forward"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 139
line_end: 143
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
  - name: "states_goals"
    annotation: "List[Tensor]"
    default: null
returns: "List[Tensor]"
docstring_source: "present"
callees:
  - target: null
    expr: "self.norm_dist.sample((states_goals[0].shape[0],) + self.latent_shape()).to"
    call_sites: [141]
  - target: null
    expr: "self.norm_dist.sample"
    call_sites: [141]
  - target: "func:deepxube.base.heuristic.PolicyVAE.latent_shape"
    expr: "self.latent_shape"
    call_sites: [141]
  - target: "func:deepxube.base.heuristic.PolicyVAE.decode"
    expr: "self.decode"
    call_sites: [142]
  - target: null
    expr: "self.norm_dist.log_prob(z).sum"
    call_sites: [143]
  - target: null
    expr: "self.norm_dist.log_prob"
    call_sites: [143]
raises: []
reads_attrs:
  - "self.norm_dist"
writes_attrs: []
---

# `deepxube.base.heuristic.PolicyVAE.forward`

**File:** [deepxube/base/heuristic.py:139](../../../../deepxube/base/heuristic.py#L139)
**Class:** `PolicyVAE`
**Visibility:** public
**Kind:** method

## Signature

```python
def forward(self, states_goals: List[Tensor]) -> List[Tensor]
```

## Docstring

Sample a latent from the prior and decode it into actions + log-prob. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_goals` | `List[Tensor]` | — |

## Returns

`List[Tensor]`

## Calls

- `self.latent_shape` → `func:deepxube.base.heuristic.PolicyVAE.latent_shape` (lines: 141)
- `self.decode` → `func:deepxube.base.heuristic.PolicyVAE.decode` (lines: 142)

### Unresolved
- `self.norm_dist.sample((states_goals[0].shape[0],) + self.latent_shape()).to` (lines: 141)
- `self.norm_dist.sample` (lines: 141)
- `self.norm_dist.log_prob(z).sum` (lines: 143)
- `self.norm_dist.log_prob` (lines: 143)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.norm_dist`

## Source

```python
    def forward(self, states_goals: List[Tensor]) -> List[Tensor]:
        """ Sample a latent from the prior and decode it into actions + log-prob. """
        z: Tensor = self.norm_dist.sample((states_goals[0].shape[0],) + self.latent_shape()).to(states_goals[0].device)
        recons: List[Tensor] = self.decode(states_goals, z)
        return recons + [self.norm_dist.log_prob(z).sum(dim=1, keepdim=True)]
```
