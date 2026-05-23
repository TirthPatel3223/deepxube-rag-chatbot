---
id: "func:deepxube.base.heuristic.HeurNNetParV.get_nnet_fn"
kind: "method"
name: "get_nnet_fn"
qualified_name: "deepxube.base.heuristic.HeurNNetParV.get_nnet_fn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 270
line_end: 280
class: "HeurNNetParV"
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
returns: "HeurFnV"
docstring_source: "present"
callees:
  - target: null
    expr: "nnet.eval"
    call_sites: [273]
  - target: "func:deepxube.base.heuristic.HeurNNetParV.to_np"
    expr: "self.to_np"
    call_sites: [276]
  - target: "func:deepxube.nnet.nnet_utils.nnet_batched"
    expr: "nnet_batched"
    call_sites: [277]
  - target: "func:deepxube.base.heuristic.HeurNNetParV._get_output"
    expr: "self._get_output"
    call_sites: [279]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParV.get_nnet_fn`

**File:** [deepxube/base/heuristic.py:270](../../../../deepxube/base/heuristic.py#L270)
**Class:** `HeurNNetParV`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnV
```

## Docstring

Build an in-process V-heuristic callable that batches through ``nnet``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet` | `nn.Module` | — |
| `batch_size` | `Optional[int]` | — |
| `device` | `torch.device` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`HeurFnV`

## Calls

- `self.to_np` → `func:deepxube.base.heuristic.HeurNNetParV.to_np` (lines: 276)
- `nnet_batched` → `func:deepxube.nnet.nnet_utils.nnet_batched` (lines: 277)
- `self._get_output` → `func:deepxube.base.heuristic.HeurNNetParV._get_output` (lines: 279)

### Unresolved
- `nnet.eval` (lines: 273)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device,
                    update_num: Optional[int]) -> HeurFnV:
        """ Build an in-process V-heuristic callable that batches through ``nnet``. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal]) -> List[float]:
            inputs_nnet: List[NDArray] = self.to_np(states, goals)
            heurs: NDArray[np.float64] = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]

            return self._get_output(heurs, update_num)
        return heuristic_fn
```
