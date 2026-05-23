---
id: "func:deepxube.base.heuristic.HeurNNetParQIn._get_input"
kind: "method"
name: "_get_input"
qualified_name: "deepxube.base.heuristic.HeurNNetParQIn._get_input"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 409
line_end: 419
class: "HeurNNetParQIn"
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
  - name: "actions_l"
    annotation: "List[List[Action]]"
    default: null
returns: "Tuple[List[NDArray], List[State], List[int]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [411]
  - target: null
    expr: "zip"
    call_sites: [414]
  - target: null
    expr: "states_rep.extend"
    call_sites: [415]
  - target: null
    expr: "len"
    call_sites: [415, 416]
  - target: null
    expr: "goals_rep.extend"
    call_sites: [416]
  - target: "func:deepxube.base.heuristic.HeurNNetParQIn._to_np_one_act"
    expr: "self._to_np_one_act"
    call_sites: [417]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQIn._get_input`

**File:** [deepxube/base/heuristic.py:409](../../../../deepxube/base/heuristic.py#L409)
**Class:** `HeurNNetParQIn`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> Tuple[List[NDArray], List[State], List[int]]
```

## Docstring

Flatten per-state actions, replicate states/goals to match, and produce numpy inputs + split indices. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions_l` | `List[List[Action]]` | — |

## Returns

`Tuple[List[NDArray], List[State], List[int]]`

## Calls

- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 411)
- `self._to_np_one_act` → `func:deepxube.base.heuristic.HeurNNetParQIn._to_np_one_act` (lines: 417)

### Unresolved
- `zip` (lines: 414)
- `states_rep.extend` (lines: 415)
- `len` (lines: 415, 416)
- `goals_rep.extend` (lines: 416)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> Tuple[List[NDArray], List[State], List[int]]:
        """ Flatten per-state actions, replicate states/goals to match, and produce numpy inputs + split indices. """
        actions_flat, split_idxs = misc_utils.flatten(actions_l)
        states_rep: List[State] = []
        goals_rep: List[Goal] = []
        for state, goal, actions in zip(states, goals, actions_l, strict=True):
            states_rep.extend([state] * len(actions))
            goals_rep.extend([goal] * len(actions))
        inputs_nnet: List[NDArray] = self._to_np_one_act(states_rep, goals_rep, actions_flat)

        return inputs_nnet, states_rep, split_idxs
```
