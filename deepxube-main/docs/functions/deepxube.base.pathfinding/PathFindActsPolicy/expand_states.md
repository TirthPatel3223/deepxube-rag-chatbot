---
id: "func:deepxube.base.pathfinding.PathFindActsPolicy.expand_states"
kind: "method"
name: "expand_states"
qualified_name: "deepxube.base.pathfinding.PathFindActsPolicy.expand_states"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 812
line_end: 832
class: "PathFindActsPolicy"
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
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
returns: "Tuple[List[List[State]], List[List[Action]], List[List[float]]]"
docstring_source: "present"
callees:
  - target: null
    expr: "self.functions.policy_fn"
    call_sites: [814]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [817]
  - target: null
    expr: "zip"
    call_sites: [820]
  - target: null
    expr: "states_flat.extend"
    call_sites: [821]
  - target: null
    expr: "len"
    call_sites: [821, 823]
  - target: null
    expr: "self.domain.next_state"
    call_sites: [826]
  - target: "func:deepxube.utils.misc_utils.unflatten"
    expr: "misc_utils.unflatten"
    call_sites: [829, 830]
raises: []
reads_attrs:
  - "self.domain"
  - "self.functions"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindActsPolicy.expand_states`

**File:** [deepxube/base/pathfinding.py:812](../../../../deepxube/base/pathfinding.py#L812)
**Class:** `PathFindActsPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def expand_states(self, states: List[State], goals: List[Goal]) -> Tuple[List[List[State]], List[List[Action]], List[List[float]]]
```

## Docstring

Sample actions from the policy and apply them via ``Domain.next_state``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |

## Returns

`Tuple[List[List[State]], List[List[Action]], List[List[float]]]`

## Calls

- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 817)
- `misc_utils.unflatten` → `func:deepxube.utils.misc_utils.unflatten` (lines: 829, 830)

### Unresolved
- `self.functions.policy_fn` (lines: 814)
- `zip` (lines: 820)
- `states_flat.extend` (lines: 821)
- `len` (lines: 821, 823)
- `self.domain.next_state` (lines: 826)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.functions`

## Source

```python
    def expand_states(self, states: List[State], goals: List[Goal]) -> Tuple[List[List[State]], List[List[Action]], List[List[float]]]:
        """ Sample actions from the policy and apply them via ``Domain.next_state``. """
        actions_l: List[List[Action]] = self.functions.policy_fn(self.domain, states, goals)[0]

        # repeat states according to actions
        actions_flat, split_idxs = misc_utils.flatten(actions_l)

        states_flat: List[State] = []
        for state, actions in zip(states, actions_l, strict=True):
            states_flat.extend([state] * len(actions))

        assert len(states_flat) == len(actions_flat), f"{len(states_flat)}, {len(actions_flat)}"

        # get next states
        states_exp_flat, tcs_flat = self.domain.next_state(states_flat, actions_flat)

        # unflatten
        states_exp: List[List[State]] = misc_utils.unflatten(states_exp_flat, split_idxs)
        tcs_l: List[List[float]] = misc_utils.unflatten(tcs_flat, split_idxs)

        return states_exp, actions_l, tcs_l
```
