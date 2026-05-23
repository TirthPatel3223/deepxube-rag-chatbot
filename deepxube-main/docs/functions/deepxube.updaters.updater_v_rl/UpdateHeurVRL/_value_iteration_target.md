---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._value_iteration_target"
kind: "method"
name: "_value_iteration_target"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRL._value_iteration_target"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 65
line_end: 85
class: "UpdateHeurVRL"
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
  - name: "tcs_l"
    annotation: "List[List[float]]"
    default: null
  - name: "states_exp"
    annotation: "List[List[State]]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[float]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [68, 83]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [70]
  - target: null
    expr: "zip"
    call_sites: [72]
  - target: null
    expr: "goals_flat.extend"
    call_sites: [73]
  - target: null
    expr: "len"
    call_sites: [73]
  - target: null
    expr: "self._get_targ_heur_fn()"
    call_sites: [74]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._get_targ_heur_fn"
    expr: "self._get_targ_heur_fn"
    call_sites: [74]
  - target: "func:numpy.concatenate"
    expr: "np.concatenate"
    call_sites: [77]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [77, 80]
  - target: "func:numpy.split"
    expr: "np.split"
    call_sites: [78]
  - target: "func:numpy.min"
    expr: "np.min"
    call_sites: [80]
  - target: "func:numpy.logical_not"
    expr: "np.logical_not"
    call_sites: [80]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [81]
  - target: null
    expr: "ctgs_backup.tolist"
    call_sites: [81]
  - target: null
    expr: "times.record_time"
    call_sites: [83]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRL._value_iteration_target`

**File:** [deepxube/updaters/updater_v_rl.py:65](../../../../deepxube/updaters/updater_v_rl.py#L65)
**Class:** `UpdateHeurVRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _value_iteration_target(self, goals: List[Goal], is_solved_l: List[bool], tcs_l: List[List[float]], states_exp: List[List[State]], times: Times) -> List[float]
```

## Docstring

Compute one-step value-iteration targets: ``min_a (tc + V(s'))`` zeroed for solved states. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `goals` | `List[Goal]` | — |
| `is_solved_l` | `List[bool]` | — |
| `tcs_l` | `List[List[float]]` | — |
| `states_exp` | `List[List[State]]` | — |
| `times` | `Times` | — |

## Returns

`List[float]`

## Calls

- `time.time` → `func:time.time` (lines: 68, 83)
- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 70)
- `self._get_targ_heur_fn` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._get_targ_heur_fn` (lines: 74)
- `np.concatenate` → `func:numpy.concatenate` (lines: 77)
- `np.array` → `func:numpy.array` (lines: 77, 80)
- `np.split` → `func:numpy.split` (lines: 78)
- `np.min` → `func:numpy.min` (lines: 80)
- `np.logical_not` → `func:numpy.logical_not` (lines: 80)
- `cast` → `func:typing.cast` (lines: 81)

### Unresolved
- `zip` (lines: 72)
- `goals_flat.extend` (lines: 73)
- `len` (lines: 73)
- `self._get_targ_heur_fn()` (lines: 74)
- `ctgs_backup.tolist` (lines: 81)
- `times.record_time` (lines: 83)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _value_iteration_target(self, goals: List[Goal], is_solved_l: List[bool], tcs_l: List[List[float]], states_exp: List[List[State]],
                                times: Times) -> List[float]:
        """ Compute one-step value-iteration targets: ``min_a (tc + V(s'))`` zeroed for solved states. """
        start_time = time.time()
        # get cost-to-go of expanded states
        states_exp_flat, split_idxs = misc_utils.flatten(states_exp)
        goals_flat: List[Goal] = []
        for goal, state_exp in zip(goals, states_exp, strict=True):
            goals_flat.extend([goal] * len(state_exp))
        ctg_next: List[float] = self._get_targ_heur_fn()(states_exp_flat, goals_flat)

        # backup cost-to-go
        ctg_next_p_tc = np.concatenate(tcs_l, axis=0) + np.array(ctg_next)
        ctg_next_p_tc_l = np.split(ctg_next_p_tc, split_idxs)

        ctgs_backup = np.array([np.min(x) for x in ctg_next_p_tc_l]) * np.logical_not(is_solved_l)
        ctgs_backup_l: List[float] = cast(List[float], ctgs_backup.tolist())

        times.record_time("vi_targ", time.time() - start_time)

        return ctgs_backup_l
```
