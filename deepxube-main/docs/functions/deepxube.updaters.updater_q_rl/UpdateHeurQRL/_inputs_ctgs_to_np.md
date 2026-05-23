---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._inputs_ctgs_to_np"
kind: "method"
name: "_inputs_ctgs_to_np"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRL._inputs_ctgs_to_np"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 87
line_end: 93
class: "UpdateHeurQRL"
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
  - name: "actions"
    annotation: "List[Action]"
    default: null
  - name: "ctgs_backup"
    annotation: "List[float]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [89, 91]
  - target: null
    expr: "self.get_heur_nnet_par().to_np"
    call_sites: [90]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL.get_heur_nnet_par"
    expr: "self.get_heur_nnet_par"
    call_sites: [90]
  - target: null
    expr: "times.record_time"
    call_sites: [91]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [93]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRL._inputs_ctgs_to_np`

**File:** [deepxube/updaters/updater_q_rl.py:87](../../../../deepxube/updaters/updater_q_rl.py#L87)
**Class:** `UpdateHeurQRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _inputs_ctgs_to_np(self, states: List[State], goals: List[Goal], actions: List[Action], ctgs_backup: List[float], times: Times) -> List[NDArray]
```

## Docstring

Package state/goal/action into numpy inputs and append the ctg target array. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |
| `ctgs_backup` | `List[float]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `time.time` → `func:time.time` (lines: 89, 91)
- `self.get_heur_nnet_par` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRL.get_heur_nnet_par` (lines: 90)
- `np.array` → `func:numpy.array` (lines: 93)

### Unresolved
- `self.get_heur_nnet_par().to_np` (lines: 90)
- `times.record_time` (lines: 91)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _inputs_ctgs_to_np(self, states: List[State], goals: List[Goal], actions: List[Action], ctgs_backup: List[float], times: Times) -> List[NDArray]:
        """ Package state/goal/action into numpy inputs and append the ctg target array. """
        start_time = time.time()
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])
        times.record_time("to_np", time.time() - start_time)

        return inputs_np + [np.array(ctgs_backup)]
```
