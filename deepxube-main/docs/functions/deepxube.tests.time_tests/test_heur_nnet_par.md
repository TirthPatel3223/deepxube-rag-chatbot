---
id: "func:deepxube.tests.time_tests.test_heur_nnet_par"
kind: "function"
name: "test_heur_nnet_par"
qualified_name: "deepxube.tests.time_tests.test_heur_nnet_par"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 158
line_end: 185
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "heur_nnet_par"
    annotation: "HeurNNetPar"
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
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [161, 168, 180, 183]
  - target: null
    expr: "isinstance"
    call_sites: [162, 164]
  - target: null
    expr: "heur_nnet_par.to_np"
    call_sites: [163, 165]
  - target: null
    expr: "ValueError"
    call_sites: [167]
  - target: null
    expr: "len"
    call_sites: [169, 171, 184, 185]
  - target: null
    expr: "print"
    call_sites: [170, 175, 185]
  - target: "func:deepxube.tests.time_tests.init_nnet"
    expr: "init_nnet"
    call_sites: [174]
  - target: null
    expr: "heur_nnet_par.get_nnet_fn"
    call_sites: [176]
  - target: "func:deepxube.tests.time_tests.heur_fn_out"
    expr: "heur_fn_out"
    call_sites: [177, 181]
raises:
  - exception: "ValueError"
    call_sites: [167]
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.test_heur_nnet_par`

**File:** [deepxube/tests/time_tests.py:158](../../../../deepxube/tests/time_tests.py#L158)
**Visibility:** public
**Kind:** function

## Signature

```python
def test_heur_nnet_par(heur_nnet_par: HeurNNetPar, states: List[State], goals: List[Goal], actions: List[Action]) -> None
```

## Docstring

Time numpy conversion and heuristic inference for a loaded heuristic nnet. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `heur_nnet_par` | `HeurNNetPar` | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 161, 168, 180, 183)
- `init_nnet` → `func:deepxube.tests.time_tests.init_nnet` (lines: 174)
- `heur_fn_out` → `func:deepxube.tests.time_tests.heur_fn_out` (lines: 177, 181)

### Unresolved
- `isinstance` (lines: 162, 164)
- `heur_nnet_par.to_np` (lines: 163, 165)
- `ValueError` (lines: 167)
- `len` (lines: 169, 171, 184, 185)
- `print` (lines: 170, 175, 185)
- `heur_nnet_par.get_nnet_fn` (lines: 176)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 167)

## Source

```python
def test_heur_nnet_par(heur_nnet_par: HeurNNetPar, states: List[State], goals: List[Goal], actions: List[Action]) -> None:
    """ Time numpy conversion and heuristic inference for a loaded heuristic nnet. """
    # nnet format
    start_time = time.time()
    if isinstance(heur_nnet_par, HeurNNetParV):
        heur_nnet_par.to_np(states, goals)
    elif isinstance(heur_nnet_par, HeurNNetParQ):
        heur_nnet_par.to_np(states, goals, [[action] for action in actions])
    else:
        raise ValueError(f"Unknown heur nnet class {heur_nnet_par}")
    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Converted %i states and goals to nnet format in "
          "%s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # initialize nnet
    nnet, device = init_nnet(heur_nnet_par)
    print("")
    heur_fn: NNetCallable = heur_nnet_par.get_nnet_fn(nnet, None, device, None)
    heur_fn_out(heur_nnet_par, heur_fn, states, goals, actions)

    # nnet heuristic
    start_time = time.time()
    heur_fn_out(heur_nnet_par, heur_fn, states, goals, actions)

    nnet_time = time.time() - start_time
    states_per_sec = len(states) / nnet_time
    print("Computed heuristic for %i states in %s seconds (%.2f/second)" % (len(states), nnet_time, states_per_sec))
```
