---
id: "func:deepxube.tests.time_tests.heur_fn_out"
kind: "function"
name: "heur_fn_out"
qualified_name: "deepxube.tests.time_tests.heur_fn_out"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 147
line_end: 155
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "heur_nnet"
    annotation: "HeurNNetPar"
    default: null
  - name: "heur_fn"
    annotation: "NNetCallable"
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "actions"
    annotation: "List[Action]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "isinstance"
    call_sites: [150, 152]
  - target: "func:deepxube.tests.time_tests.heur_fn"
    expr: "heur_fn"
    call_sites: [151, 153]
  - target: null
    expr: "ValueError"
    call_sites: [155]
raises:
  - exception: "ValueError"
    call_sites: [155]
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.heur_fn_out`

**File:** [deepxube/tests/time_tests.py:147](../../../../deepxube/tests/time_tests.py#L147)
**Visibility:** public
**Kind:** function

## Signature

```python
def heur_fn_out(heur_nnet: HeurNNetPar, heur_fn: NNetCallable, states: List[State], goals: List[Goal], actions: List[Action]) -> None
```

## Docstring

Invoke ``heur_fn`` with the correct signature depending on whether it is a V or Q heuristic. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `heur_nnet` | `HeurNNetPar` | — |
| `heur_fn` | `NNetCallable` | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |

## Returns

`None`

## Calls

- `heur_fn` → `func:deepxube.tests.time_tests.heur_fn` (lines: 151, 153)

### Unresolved
- `isinstance` (lines: 150, 152)
- `ValueError` (lines: 155)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 155)

## Source

```python
def heur_fn_out(heur_nnet: HeurNNetPar, heur_fn: NNetCallable, states: List[State], goals: List[Goal],
                actions: List[Action]) -> None:
    """ Invoke ``heur_fn`` with the correct signature depending on whether it is a V or Q heuristic. """
    if isinstance(heur_nnet, HeurNNetParV):
        heur_fn(states, goals)
    elif isinstance(heur_nnet, HeurNNetParQ):
        heur_fn(states, goals, [[action] for action in actions])
    else:
        raise ValueError(f"Unknown heur fn class {heur_fn}")
```
