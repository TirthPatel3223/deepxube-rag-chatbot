---
id: "func:deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_fn"
kind: "method"
name: "get_nnet_fn"
qualified_name: "deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_fn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 321
line_end: 330
class: "HeurNNetParQFixOut"
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
    call_sites: [323]
  - target: "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_input"
    expr: "self._get_input"
    call_sites: [326]
  - target: "func:deepxube.nnet.nnet_utils.nnet_batched"
    expr: "nnet_batched"
    call_sites: [327]
  - target: "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_output"
    expr: "self._get_output"
    call_sites: [328]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_fn`

**File:** [deepxube/base/heuristic.py:321](../../../../deepxube/base/heuristic.py#L321)
**Class:** `HeurNNetParQFixOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnQ
```

## Docstring

In-process callable that runs the fixed-output Q network and slices per-state outputs. 

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

- `self._get_input` → `func:deepxube.base.heuristic.HeurNNetParQFixOut._get_input` (lines: 326)
- `nnet_batched` → `func:deepxube.nnet.nnet_utils.nnet_batched` (lines: 327)
- `self._get_output` → `func:deepxube.base.heuristic.HeurNNetParQFixOut._get_output` (lines: 328)

### Unresolved
- `nnet.eval` (lines: 323)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnQ:
        """ In-process callable that runs the fixed-output Q network and slices per-state outputs. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet: List[NDArray] = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray[np.float64] = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]
            return self._get_output(states, q_vals_np, update_num)

        return heuristic_fn
```
