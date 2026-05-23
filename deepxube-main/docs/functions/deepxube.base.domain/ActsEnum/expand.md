---
id: "func:deepxube.base.domain.ActsEnum.expand"
kind: "method"
name: "expand"
qualified_name: "deepxube.base.domain.ActsEnum.expand"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 255
line_end: 290
class: "ActsEnum"
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
  - target: null
    expr: "range"
    call_sites: [262, 263, 264]
  - target: null
    expr: "len"
    call_sites: [262, 263, 264, 267, 268]
  - target: "func:deepxube.base.domain.ActsEnum.get_state_actions"
    expr: "self.get_state_actions"
    call_sites: [265]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [267]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [268]
  - target: "func:numpy.any"
    expr: "np.any"
    call_sites: [272]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [273]
  - target: null
    expr: "state_actions[idx].pop"
    call_sites: [275]
  - target: "func:deepxube.base.domain.ActsEnum.next_state"
    expr: "self.next_state"
    call_sites: [278]
  - target: null
    expr: "enumerate"
    call_sites: [282]
  - target: null
    expr: "states_exp_l[idx].append"
    call_sites: [283]
  - target: null
    expr: "actions_exp_l[idx].append"
    call_sites: [284]
  - target: null
    expr: "tcs_l[idx].append"
    call_sites: [285]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.ActsEnum.expand`

**File:** [deepxube/base/domain.py:255](../../../../deepxube/base/domain.py#L255)
**Class:** `ActsEnum`
**Visibility:** public
**Kind:** method

## Signature

```python
def expand(self, states: List[S]) -> Tuple[List[List[S]], List[List[A]], List[List[float]]]
```

## Docstring

Generate all children for the state, assumes there is at least one child state
:param states: List of states
:return: Children of each state, actions, transition costs for each state

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |

## Returns

`Tuple[List[List[S]], List[List[A]], List[List[float]]]`

## Calls

- `self.get_state_actions` → `func:deepxube.base.domain.ActsEnum.get_state_actions` (lines: 265)
- `np.array` → `func:numpy.array` (lines: 267)
- `np.zeros` → `func:numpy.zeros` (lines: 268)
- `np.any` → `func:numpy.any` (lines: 272)
- `np.where` → `func:numpy.where` (lines: 273)
- `self.next_state` → `func:deepxube.base.domain.ActsEnum.next_state` (lines: 278)

### Unresolved
- `range` (lines: 262, 263, 264)
- `len` (lines: 262, 263, 264, 267, 268)
- `state_actions[idx].pop` (lines: 275)
- `enumerate` (lines: 282)
- `states_exp_l[idx].append` (lines: 283)
- `actions_exp_l[idx].append` (lines: 284)
- `tcs_l[idx].append` (lines: 285)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def expand(self, states: List[S]) -> Tuple[List[List[S]], List[List[A]], List[List[float]]]:
        """ Generate all children for the state, assumes there is at least one child state
        :param states: List of states
        :return: Children of each state, actions, transition costs for each state
        """
        # TODO further validate
        # initialize
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
            states_idxs: List[S] = [states[idx] for idx in idxs]
            actions_idxs: List[A] = [state_actions[idx].pop(0) for idx in idxs]

            # next state
            states_next, tcs_move = self.next_state(states_idxs, actions_idxs)

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
