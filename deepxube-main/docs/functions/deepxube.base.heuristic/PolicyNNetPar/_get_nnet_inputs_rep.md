---
id: "func:deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep"
kind: "method"
name: "_get_nnet_inputs_rep"
qualified_name: "deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 538
line_end: 544
class: "PolicyNNetPar"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "num_samp"
    annotation: "int"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.heuristic.PolicyNNetPar.to_np_fn"
    expr: "self.to_np_fn"
    call_sites: [540]
  - target: null
    expr: "inputs_nnet_rep_interleave.append"
    call_sites: [543]
  - target: "func:numpy.repeat"
    expr: "np.repeat"
    call_sites: [543]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep`

**File:** [deepxube/base/heuristic.py:538](../../../../deepxube/base/heuristic.py#L538)
**Class:** `PolicyNNetPar`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_nnet_inputs_rep(self, states: List[State], goals: List[Goal], num_samp: int) -> List[NDArray]
```

## Docstring

Repeat each (state, goal) input row ``num_samp`` times so the network samples multiple actions per state in one batch. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `num_samp` | `int` | — |

## Returns

`List[NDArray]`

## Calls

- `self.to_np_fn` → `func:deepxube.base.heuristic.PolicyNNetPar.to_np_fn` (lines: 540)
- `np.repeat` → `func:numpy.repeat` (lines: 543)

### Unresolved
- `inputs_nnet_rep_interleave.append` (lines: 543)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_nnet_inputs_rep(self, states: List[State], goals: List[Goal], num_samp: int) -> List[NDArray]:
        """ Repeat each (state, goal) input row ``num_samp`` times so the network samples multiple actions per state in one batch. """
        inputs_nnet: List[NDArray] = self.to_np_fn(states, goals)
        inputs_nnet_rep_interleave: List[NDArray] = []
        for inputs_nnet_i in inputs_nnet:
            inputs_nnet_rep_interleave.append(np.repeat(inputs_nnet_i, num_samp, axis=0))
        return inputs_nnet_rep_interleave
```
