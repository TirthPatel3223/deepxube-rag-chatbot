---
id: "func:deepxube.base.heuristic.policy_fn_rand"
kind: "function"
name: "policy_fn_rand"
qualified_name: "deepxube.base.heuristic.policy_fn_rand"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 434
line_end: 452
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain"
    annotation: "Domain"
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "num_rand"
    annotation: "int"
    default: null
returns: "Tuple[List[List[Action]], List[List[float]]]"
docstring_source: "present"
callees:
  - target: null
    expr: "states_rep.append"
    call_sites: [441]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [443]
  - target: null
    expr: "domain.sample_state_action"
    call_sites: [445]
  - target: "func:deepxube.utils.misc_utils.unflatten"
    expr: "misc_utils.unflatten"
    call_sites: [446]
  - target: null
    expr: "probs_l.append"
    call_sites: [450]
  - target: null
    expr: "len"
    call_sites: [450]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.policy_fn_rand`

**File:** [deepxube/base/heuristic.py:434](../../../../deepxube/base/heuristic.py#L434)
**Visibility:** public
**Kind:** function

## Signature

```python
def policy_fn_rand(domain: Domain, states: List[State], num_rand: int) -> Tuple[List[List[Action]], List[List[float]]]
```

## Docstring

Sample ``num_rand`` random actions per state from the domain, with uniform pdf. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `states` | `List[State]` | — |
| `num_rand` | `int` | — |

## Returns

`Tuple[List[List[Action]], List[List[float]]]`

## Calls

- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 443)
- `misc_utils.unflatten` → `func:deepxube.utils.misc_utils.unflatten` (lines: 446)

### Unresolved
- `states_rep.append` (lines: 441)
- `domain.sample_state_action` (lines: 445)
- `probs_l.append` (lines: 450)
- `len` (lines: 450)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def policy_fn_rand(domain: Domain, states: List[State], num_rand: int) -> Tuple[List[List[Action]], List[List[float]]]:
    """ Sample ``num_rand`` random actions per state from the domain, with uniform pdf. """
    if num_rand == 0:
        return [[] for _ in states], [[] for _ in states]

    states_rep: List[List[State]] = []
    for state in states:
        states_rep.append([state] * num_rand)

    states_rep_flat, split_idxs = misc_utils.flatten(states_rep)

    actions_samp_flat: List[Action] = domain.sample_state_action(states_rep_flat)
    actions_samp_l: List[List[Action]] = misc_utils.unflatten(actions_samp_flat, split_idxs)

    probs_l: List[List[float]] = []
    for actions_samp_i in actions_samp_l:
        probs_l.append([1.0 / len(actions_samp_i)] * len(actions_samp_i))

    return actions_samp_l, probs_l
```
