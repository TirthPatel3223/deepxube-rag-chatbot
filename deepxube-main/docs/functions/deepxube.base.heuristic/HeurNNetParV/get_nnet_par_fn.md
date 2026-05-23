---
id: "func:deepxube.base.heuristic.HeurNNetParV.get_nnet_par_fn"
kind: "method"
name: "get_nnet_par_fn"
qualified_name: "deepxube.base.heuristic.HeurNNetParV.get_nnet_par_fn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 282
line_end: 290
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
  - name: "nnet_par_info"
    annotation: "NNetParInfo"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "HeurFnV"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.heuristic.HeurNNetParV.to_np"
    expr: "self.to_np"
    call_sites: [285]
  - target: "func:deepxube.nnet.nnet_utils.get_nnet_par_out"
    expr: "get_nnet_par_out"
    call_sites: [286]
  - target: "func:deepxube.base.heuristic.HeurNNetParV._get_output"
    expr: "self._get_output"
    call_sites: [288]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParV.get_nnet_par_fn`

**File:** [deepxube/base/heuristic.py:282](../../../../deepxube/base/heuristic.py#L282)
**Class:** `HeurNNetParV`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnV
```

## Docstring

Build a V-heuristic callable that delegates to a worker NNet runner. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_par_info` | `NNetParInfo` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`HeurFnV`

## Calls

- `self.to_np` → `func:deepxube.base.heuristic.HeurNNetParV.to_np` (lines: 285)
- `get_nnet_par_out` → `func:deepxube.nnet.nnet_utils.get_nnet_par_out` (lines: 286)
- `self._get_output` → `func:deepxube.base.heuristic.HeurNNetParV._get_output` (lines: 288)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnV:
        """ Build a V-heuristic callable that delegates to a worker NNet runner. """
        def heuristic_fn(states: List[State], goals: List[Goal]) -> List[float]:
            inputs_nnet: List[NDArray] = self.to_np(states, goals)
            heurs: NDArray[np.float64] = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]

            return self._get_output(heurs, update_num)

        return heuristic_fn
```
