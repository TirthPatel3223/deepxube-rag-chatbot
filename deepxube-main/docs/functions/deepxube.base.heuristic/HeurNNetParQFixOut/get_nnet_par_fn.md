---
id: "func:deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_par_fn"
kind: "method"
name: "get_nnet_par_fn"
qualified_name: "deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_par_fn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 332
line_end: 339
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
  - name: "nnet_par_info"
    annotation: "NNetParInfo"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "HeurFnQ"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_input"
    expr: "self._get_input"
    call_sites: [335]
  - target: "func:deepxube.nnet.nnet_utils.get_nnet_par_out"
    expr: "get_nnet_par_out"
    call_sites: [336]
  - target: "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_output"
    expr: "self._get_output"
    call_sites: [337]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQFixOut.get_nnet_par_fn`

**File:** [deepxube/base/heuristic.py:332](../../../../deepxube/base/heuristic.py#L332)
**Class:** `HeurNNetParQFixOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ
```

## Docstring

Worker-queue-routed variant of ``get_nnet_fn``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_par_info` | `NNetParInfo` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`HeurFnQ`

## Calls

- `self._get_input` → `func:deepxube.base.heuristic.HeurNNetParQFixOut._get_input` (lines: 335)
- `get_nnet_par_out` → `func:deepxube.nnet.nnet_utils.get_nnet_par_out` (lines: 336)
- `self._get_output` → `func:deepxube.base.heuristic.HeurNNetParQFixOut._get_output` (lines: 337)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet: List[NDArray] = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray[np.float64] = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]
            return self._get_output(states, q_vals_np, update_num)

        return heuristic_fn
```
