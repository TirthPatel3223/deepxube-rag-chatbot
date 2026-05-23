---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._q_learning_target"
kind: "method"
name: "_q_learning_target"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRL._q_learning_target"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 71
line_end: 85
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
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "is_solved_l"
    annotation: "List[bool]"
    default: null
  - name: "tcs"
    annotation: "List[float]"
    default: null
  - name: "states_next"
    annotation: "List[State]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[float]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [73, 83]
  - target: null
    expr: "self.get_pathfind().get_state_actions"
    call_sites: [75]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL.get_pathfind"
    expr: "self.get_pathfind"
    call_sites: [75]
  - target: null
    expr: "self._get_targ_heur_fn()"
    call_sites: [76]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._get_targ_heur_fn"
    expr: "self._get_targ_heur_fn"
    call_sites: [76]
  - target: null
    expr: "min"
    call_sites: [77]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [80, 81]
  - target: "func:numpy.logical_not"
    expr: "np.logical_not"
    call_sites: [81]
  - target: null
    expr: "times.record_time"
    call_sites: [83]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [85]
  - target: null
    expr: "ctg_backups.tolist"
    call_sites: [85]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRL._q_learning_target`

**File:** [deepxube/updaters/updater_q_rl.py:71](../../../../deepxube/updaters/updater_q_rl.py#L71)
**Class:** `UpdateHeurQRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _q_learning_target(self, goals: List[Goal], is_solved_l: List[bool], tcs: List[float], states_next: List[State], times: Times) -> List[float]
```

## Docstring

Compute Q-learning targets: ``tc + min_a' Q(s', a')`` zeroed for solved states. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `goals` | `List[Goal]` | — |
| `is_solved_l` | `List[bool]` | — |
| `tcs` | `List[float]` | — |
| `states_next` | `List[State]` | — |
| `times` | `Times` | — |

## Returns

`List[float]`

## Calls

- `time.time` → `func:time.time` (lines: 73, 83)
- `self.get_pathfind` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRL.get_pathfind` (lines: 75)
- `self._get_targ_heur_fn` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._get_targ_heur_fn` (lines: 76)
- `np.array` → `func:numpy.array` (lines: 80, 81)
- `np.logical_not` → `func:numpy.logical_not` (lines: 81)
- `cast` → `func:typing.cast` (lines: 85)

### Unresolved
- `self.get_pathfind().get_state_actions` (lines: 75)
- `self._get_targ_heur_fn()` (lines: 76)
- `min` (lines: 77)
- `times.record_time` (lines: 83)
- `ctg_backups.tolist` (lines: 85)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _q_learning_target(self, goals: List[Goal], is_solved_l: List[bool], tcs: List[float], states_next: List[State], times: Times) -> List[float]:
        """ Compute Q-learning targets: ``tc + min_a' Q(s', a')`` zeroed for solved states. """
        start_time = time.time()
        # min cost-to-go for next state
        actions_next: List[List[Action]] = self.get_pathfind().get_state_actions(states_next, goals)
        qvals_next_l: List[List[float]] = self._get_targ_heur_fn()(states_next, goals, actions_next)
        qvals_next_min: List[float] = [min(qvals_next) for qvals_next in qvals_next_l]

        # backup cost-to-go
        ctg_backups: NDArray = np.array(tcs) + np.array(qvals_next_min)
        ctg_backups = ctg_backups * np.logical_not(np.array(is_solved_l))

        times.record_time("qlearn_targ", time.time() - start_time)

        return cast(List[float], ctg_backups.tolist())
```
