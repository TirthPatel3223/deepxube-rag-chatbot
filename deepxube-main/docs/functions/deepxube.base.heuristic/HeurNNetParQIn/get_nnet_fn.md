---
id: "func:deepxube.base.heuristic.HeurNNetParQIn.get_nnet_fn"
kind: "method"
name: "get_nnet_fn"
qualified_name: "deepxube.base.heuristic.HeurNNetParQIn.get_nnet_fn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 377
line_end: 387
class: "HeurNNetParQIn"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nnet"
    annotation: "nn.Module"
    default: null
  - name: "batch_size"
    annotation: "Optional[int]"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "HeurFnQ"
docstring_source: "present"
callees:
  - target: null
    expr: "nnet.eval"
    call_sites: [380]
  - target: "func:deepxube.base.heuristic.HeurNNetParQIn._get_input"
    expr: "self._get_input"
    call_sites: [383]
  - target: "func:deepxube.nnet.nnet_utils.nnet_batched"
    expr: "nnet_batched"
    call_sites: [384]
  - target: "func:deepxube.base.heuristic.HeurNNetParQIn._get_output"
    expr: "self._get_output"
    call_sites: [385]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQIn.get_nnet_fn`

**File:** [deepxube/base/heuristic.py:377](../../../../deepxube/base/heuristic.py#L377)
**Class:** `HeurNNetParQIn`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnQ
```

## Docstring

In-process callable that flattens per-state actions, runs the action-input Q network, and unflattens the result. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet` | `nn.Module` | — |
| `batch_size` | `Optional[int]` | — |
| `device` | `torch.device` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`HeurFnQ`

## Calls

- `self._get_input` → `func:deepxube.base.heuristic.HeurNNetParQIn._get_input` (lines: 383)
- `nnet_batched` → `func:deepxube.nnet.nnet_utils.nnet_batched` (lines: 384)
- `self._get_output` → `func:deepxube.base.heuristic.HeurNNetParQIn._get_output` (lines: 385)

### Unresolved
- `nnet.eval` (lines: 380)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device,
                    update_num: Optional[int]) -> HeurFnQ:
        """ In-process callable that flattens per-state actions, runs the action-input Q network, and unflattens the result. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet, states_rep, split_idxs = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]
            return self._get_output(states_rep, q_vals_np, split_idxs, update_num)

        return heuristic_fn
```
