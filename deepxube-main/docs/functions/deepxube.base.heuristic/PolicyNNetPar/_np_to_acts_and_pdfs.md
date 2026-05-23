---
id: "func:deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs"
kind: "method"
name: "_np_to_acts_and_pdfs"
qualified_name: "deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 546
line_end: 563
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
  - name: "actions_np"
    annotation: "List[NDArray[np.float64]]"
    default: null
  - name: "pdfs_np"
    annotation: "NDArray[np.float64]"
    default: null
  - name: "num_states"
    annotation: "int"
    default: null
  - name: "num_samp"
    annotation: "int"
    default: null
returns: "Tuple[List[List[Action]], List[List[float]]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [549]
  - target: null
    expr: "range"
    call_sites: [554]
  - target: null
    expr: "pdfs_np[start_idx:end_idx, 0].tolist"
    call_sites: [558]
  - target: null
    expr: "actions_l.append"
    call_sites: [560]
  - target: "func:deepxube.base.heuristic.PolicyNNetPar._nnet_out_to_actions"
    expr: "self._nnet_out_to_actions"
    call_sites: [560]
  - target: null
    expr: "pdfs_l.append"
    call_sites: [561]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs`

**File:** [deepxube/base/heuristic.py:546](../../../../deepxube/base/heuristic.py#L546)
**Class:** `PolicyNNetPar`
**Visibility:** private
**Kind:** method

## Signature

```python
def _np_to_acts_and_pdfs(self, actions_np: List[NDArray[np.float64]], pdfs_np: NDArray[np.float64], num_states: int, num_samp: int) -> Tuple[List[List[Action]], List[List[float]]]
```

## Docstring

Slice the interleaved (state, sample) outputs back into per-state lists of actions and pdfs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `actions_np` | `List[NDArray[np.float64]]` | — |
| `pdfs_np` | `NDArray[np.float64]` | — |
| `num_states` | `int` | — |
| `num_samp` | `int` | — |

## Returns

`Tuple[List[List[Action]], List[List[float]]]`

## Calls

- `self._nnet_out_to_actions` → `func:deepxube.base.heuristic.PolicyNNetPar._nnet_out_to_actions` (lines: 560)

### Unresolved
- `len` (lines: 549)
- `range` (lines: 554)
- `pdfs_np[start_idx:end_idx, 0].tolist` (lines: 558)
- `actions_l.append` (lines: 560)
- `pdfs_l.append` (lines: 561)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _np_to_acts_and_pdfs(self, actions_np: List[NDArray[np.float64]], pdfs_np: NDArray[np.float64], num_states: int,
                             num_samp: int) -> Tuple[List[List[Action]], List[List[float]]]:
        """ Slice the interleaved (state, sample) outputs back into per-state lists of actions and pdfs. """
        assert len(pdfs_np.shape) == 2
        assert pdfs_np.shape[1] == 1

        actions_l: List[List[Action]] = []
        pdfs_l: List[List[float]] = []
        for state_idx in range(num_states):
            start_idx: int = state_idx * num_samp
            end_idx: int = start_idx + num_samp
            actions_np_state: List[NDArray[np.float64]] = [actions_np_i[start_idx:end_idx] for actions_np_i in actions_np]
            pdfs_state: List[float] = pdfs_np[start_idx:end_idx, 0].tolist()

            actions_l.append(self._nnet_out_to_actions(actions_np_state))
            pdfs_l.append(pdfs_state)

        return actions_l, pdfs_l
```
