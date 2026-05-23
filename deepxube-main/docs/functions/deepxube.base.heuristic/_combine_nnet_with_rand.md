---
id: "func:deepxube.base.heuristic._combine_nnet_with_rand"
kind: "function"
name: "_combine_nnet_with_rand"
qualified_name: "deepxube.base.heuristic._combine_nnet_with_rand"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 455
line_end: 469
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain"
    annotation: "Domain"
    default: null
  - name: "actions_l"
    annotation: "List[List[Action]]"
    default: null
  - name: "pdfs_l"
    annotation: "List[List[float]]"
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
  - target: "func:deepxube.base.heuristic.policy_fn_rand"
    expr: "policy_fn_rand"
    call_sites: [458]
  - target: null
    expr: "range"
    call_sites: [463]
  - target: null
    expr: "len"
    call_sites: [463, 467]
  - target: null
    expr: "actions_comb_l.append"
    call_sites: [465]
  - target: null
    expr: "pdfs_comb_l.append"
    call_sites: [467]
  - target: "func:random.choices"
    expr: "random.choices"
    call_sites: [467]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic._combine_nnet_with_rand`

**File:** [deepxube/base/heuristic.py:455](../../../../deepxube/base/heuristic.py#L455)
**Visibility:** private
**Kind:** function

## Signature

```python
def _combine_nnet_with_rand(domain: Domain, actions_l: List[List[Action]], pdfs_l: List[List[float]], states: List[State], num_rand: int) -> Tuple[List[List[Action]], List[List[float]]]
```

## Docstring

Append ``num_rand`` random actions (with sampled-pdf placeholders) to each per-state action list. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `actions_l` | `List[List[Action]]` | — |
| `pdfs_l` | `List[List[float]]` | — |
| `states` | `List[State]` | — |
| `num_rand` | `int` | — |

## Returns

`Tuple[List[List[Action]], List[List[float]]]`

## Calls

- `policy_fn_rand` → `func:deepxube.base.heuristic.policy_fn_rand` (lines: 458)
- `random.choices` → `func:random.choices` (lines: 467)

### Unresolved
- `range` (lines: 463)
- `len` (lines: 463, 467)
- `actions_comb_l.append` (lines: 465)
- `pdfs_comb_l.append` (lines: 467)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _combine_nnet_with_rand(domain: Domain, actions_l: List[List[Action]], pdfs_l: List[List[float]], states: List[State],
                            num_rand: int) -> Tuple[List[List[Action]], List[List[float]]]:
    """ Append ``num_rand`` random actions (with sampled-pdf placeholders) to each per-state action list. """
    actions_rand_l: List[List[Action]] = policy_fn_rand(domain, states, num_rand)[0]

    actions_comb_l: List[List[Action]] = []
    pdfs_comb_l: List[List[float]] = []
    # get nnet actions
    for state_idx in range(len(states)):
        actions_rand_i: List[Action] = actions_rand_l[state_idx]
        actions_comb_l.append(actions_l[state_idx] + actions_rand_i)
        pdfs_i: List[float] = pdfs_l[state_idx]
        pdfs_comb_l.append(pdfs_i + random.choices(pdfs_i, k=len(actions_rand_i)))

    return actions_comb_l, pdfs_comb_l
```
