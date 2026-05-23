---
id: "func:deepxube.base.domain.NextStateNPActsEnum.expand"
kind: "method"
name: "expand"
qualified_name: "deepxube.base.domain.NextStateNPActsEnum.expand"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 553
line_end: 586
class: "NextStateNPActsEnum"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[S]"
    default: null
returns: "Tuple[List[List[S]], List[List[A]], List[List[float]]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.NextStateNPActsEnum._states_to_np"
    expr: "self._states_to_np"
    call_sites: [556]
  - target: null
    expr: "range"
    call_sites: [557, 558, 559]
  - target: null
    expr: "len"
    call_sites: [557, 558, 559, 562, 563]
  - target: "func:deepxube.base.domain.NextStateNPActsEnum.get_state_actions"
    expr: "self.get_state_actions"
    call_sites: [560]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [562]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [563]
  - target: "func:numpy.any"
    expr: "np.any"
    call_sites: [567]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [568]
  - target: null
    expr: "state_actions[idx].pop"
    call_sites: [570]
  - target: "func:deepxube.base.domain.NextStateNPActsEnum._next_state_np"
    expr: "self._next_state_np"
    call_sites: [573]
  - target: "func:deepxube.base.domain.NextStateNPActsEnum._np_to_states"
    expr: "self._np_to_states"
    call_sites: [574]
  - target: null
    expr: "enumerate"
    call_sites: [578]
  - target: null
    expr: "states_exp_l[idx].append"
    call_sites: [579]
  - target: null
    expr: "actions_exp_l[idx].append"
    call_sites: [580]
  - target: null
    expr: "tcs_l[idx].append"
    call_sites: [581]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.NextStateNPActsEnum.expand`

**File:** [deepxube/base/domain.py:553](../../../../deepxube/base/domain.py#L553)
**Class:** `NextStateNPActsEnum`
**Visibility:** public
**Kind:** method

## Signature

```python
def expand(self, states: List[S]) -> Tuple[List[List[S]], List[List[A]], List[List[float]]]
```

## Docstring

Vectorised version of ``ActsEnum.expand`` working in numpy space. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |

## Returns

`Tuple[List[List[S]], List[List[A]], List[List[float]]]`

## Calls

- `self._states_to_np` → `func:deepxube.base.domain.NextStateNPActsEnum._states_to_np` (lines: 556)
- `self.get_state_actions` → `func:deepxube.base.domain.NextStateNPActsEnum.get_state_actions` (lines: 560)
- `np.array` → `func:numpy.array` (lines: 562)
- `np.zeros` → `func:numpy.zeros` (lines: 563)
- `np.any` → `func:numpy.any` (lines: 567)
- `np.where` → `func:numpy.where` (lines: 568)
- `self._next_state_np` → `func:deepxube.base.domain.NextStateNPActsEnum._next_state_np` (lines: 573)
- `self._np_to_states` → `func:deepxube.base.domain.NextStateNPActsEnum._np_to_states` (lines: 574)

### Unresolved
- `range` (lines: 557, 558, 559)
- `len` (lines: 557, 558, 559, 562, 563)
- `state_actions[idx].pop` (lines: 570)
- `enumerate` (lines: 578)
- `states_exp_l[idx].append` (lines: 579)
- `actions_exp_l[idx].append` (lines: 580)
- `tcs_l[idx].append` (lines: 581)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def expand(self, states: List[S]) -> Tuple[List[List[S]], List[List[A]], List[List[float]]]:
        """ Vectorised version of ``ActsEnum.expand`` working in numpy space. """
        # initialize
        states_np: List[NDArray] = self._states_to_np(states)
        states_exp_l: List[List[S]] = [[] for _ in range(len(states))]
        actions_exp_l: List[List[A]] = [[] for _ in range(len(states))]
        tcs_l: List[List[float]] = [[] for _ in range(len(states))]
        state_actions: List[List[A]] = self.get_state_actions(states)

        num_actions_tot: NDArray[np.int_] = np.array([len(x) for x in state_actions])
        num_actions_taken: NDArray[np.int_] = np.zeros(len(states), dtype=int)
        actions_lt: NDArray[np.bool_] = num_actions_taken < num_actions_tot

        # for each move, get next states, transition costs, and if solved
        while np.any(actions_lt):
            idxs: NDArray[np.int_] = np.where(actions_lt)[0]
            states_np_idxs: List[NDArray] = [states_np_i[idxs] for states_np_i in states_np]
            actions_idxs: List[A] = [state_actions[idx].pop(0) for idx in idxs]

            # next state
            states_next_np, tcs_move = self._next_state_np(states_np_idxs, actions_idxs)
            states_next: List[S] = self._np_to_states(states_next_np)

            # append
            idx: int
            for exp_idx, idx in enumerate(idxs):
                states_exp_l[idx].append(states_next[exp_idx])
                actions_exp_l[idx].append(actions_idxs[exp_idx])
                tcs_l[idx].append(tcs_move[exp_idx])

            num_actions_taken[idxs] = num_actions_taken[idxs] + 1
            actions_lt[idxs] = num_actions_taken[idxs] < num_actions_tot[idxs]

        return states_exp_l, actions_exp_l, tcs_l
```
