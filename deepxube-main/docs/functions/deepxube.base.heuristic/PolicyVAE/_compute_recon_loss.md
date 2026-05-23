---
id: "func:deepxube.base.heuristic.PolicyVAE._compute_recon_loss"
kind: "method"
name: "_compute_recon_loss"
qualified_name: "deepxube.base.heuristic.PolicyVAE._compute_recon_loss"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 188
line_end: 193
class: "PolicyVAE"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "action_proc"
    annotation: "List[Tensor]"
    default: null
  - name: "actions_recon"
    annotation: "List[Tensor]"
    default: null
returns: "Tensor"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.heuristic._flatten_list"
    expr: "_flatten_list"
    call_sites: [190, 191]
  - target: "func:deepxube.base.heuristic.PolicyVAE.mse_criterion"
    expr: "self.mse_criterion"
    call_sites: [192]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.PolicyVAE._compute_recon_loss`

**File:** [deepxube/base/heuristic.py:188](../../../../deepxube/base/heuristic.py#L188)
**Class:** `PolicyVAE`
**Visibility:** private
**Kind:** method

## Signature

```python
def _compute_recon_loss(self, action_proc: List[Tensor], actions_recon: List[Tensor]) -> Tensor
```

## Docstring

MSE between flattened processed-input actions and reconstructed actions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `action_proc` | `List[Tensor]` | — |
| `actions_recon` | `List[Tensor]` | — |

## Returns

`Tensor`

## Calls

- `_flatten_list` → `func:deepxube.base.heuristic._flatten_list` (lines: 190, 191)
- `self.mse_criterion` → `func:deepxube.base.heuristic.PolicyVAE.mse_criterion` (lines: 192)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _compute_recon_loss(self, action_proc: List[Tensor], actions_recon: List[Tensor]) -> Tensor:
        """ MSE between flattened processed-input actions and reconstructed actions. """
        actions_proc_flat: Tensor = _flatten_list(action_proc)
        actions_recon_flat: Tensor = _flatten_list(actions_recon)
        loss_recon: Tensor = self.mse_criterion(actions_proc_flat, actions_recon_flat)
        return loss_recon
```
