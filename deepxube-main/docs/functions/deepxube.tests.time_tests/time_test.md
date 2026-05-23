---
id: "func:deepxube.tests.time_tests.time_test"
kind: "function"
name: "time_test"
qualified_name: "deepxube.tests.time_tests.time_test"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 235
line_end: 247
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
  - name: "heur_nnet_par"
    annotation: "Optional[HeurNNetPar]"
    default: null
  - name: "policy_nnet_par"
    annotation: "Optional[PolicyNNetPar]"
    default: null
  - name: "num_states"
    annotation: "int"
    default: null
  - name: "step_max"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.tests.time_tests.test_env"
    expr: "test_env"
    call_sites: [237]
  - target: null
    expr: "isinstance"
    call_sites: [238, 240]
  - target: "func:deepxube.tests.time_tests.test_envstartgoalrw"
    expr: "test_envstartgoalrw"
    call_sites: [239]
  - target: "func:deepxube.tests.time_tests.test_envenumerableacts"
    expr: "test_envenumerableacts"
    call_sites: [241]
  - target: "func:deepxube.tests.time_tests.test_heur_nnet_par"
    expr: "test_heur_nnet_par"
    call_sites: [244]
  - target: "func:deepxube.tests.time_tests.test_policy_nnet_par"
    expr: "test_policy_nnet_par"
    call_sites: [247]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.time_test`

**File:** [deepxube/tests/time_tests.py:235](../../../../deepxube/tests/time_tests.py#L235)
**Visibility:** public
**Kind:** function

## Signature

```python
def time_test(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], policy_nnet_par: Optional[PolicyNNetPar], num_states: int, step_max: int) -> None
```

## Docstring

Run all applicable timing benchmarks for ``domain`` and optionally for heuristic and policy nnets. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `heur_nnet_par` | `Optional[HeurNNetPar]` | — |
| `policy_nnet_par` | `Optional[PolicyNNetPar]` | — |
| `num_states` | `int` | — |
| `step_max` | `int` | — |

## Returns

`None`

## Calls

- `test_env` → `func:deepxube.tests.time_tests.test_env` (lines: 237)
- `test_envstartgoalrw` → `func:deepxube.tests.time_tests.test_envstartgoalrw` (lines: 239)
- `test_envenumerableacts` → `func:deepxube.tests.time_tests.test_envenumerableacts` (lines: 241)
- `test_heur_nnet_par` → `func:deepxube.tests.time_tests.test_heur_nnet_par` (lines: 244)
- `test_policy_nnet_par` → `func:deepxube.tests.time_tests.test_policy_nnet_par` (lines: 247)

### Unresolved
- `isinstance` (lines: 238, 240)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def time_test(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], policy_nnet_par: Optional[PolicyNNetPar], num_states: int, step_max: int) -> None:
    """ Run all applicable timing benchmarks for ``domain`` and optionally for heuristic and policy nnets. """
    states, goals, actions = test_env(domain, num_states, step_max)
    if isinstance(domain, StartGoalWalkable):
        test_envstartgoalrw(domain, num_states)
    if isinstance(domain, ActsEnum):
        test_envenumerableacts(domain, states)

    if heur_nnet_par is not None:
        test_heur_nnet_par(heur_nnet_par, states, goals, actions)

    if policy_nnet_par is not None:
        test_policy_nnet_par(domain, policy_nnet_par, states, goals, actions)
```
