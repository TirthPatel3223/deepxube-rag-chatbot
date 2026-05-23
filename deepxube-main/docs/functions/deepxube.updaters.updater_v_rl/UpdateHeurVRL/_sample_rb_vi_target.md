---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._sample_rb_vi_target"
kind: "method"
name: "_sample_rb_vi_target"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRL._sample_rb_vi_target"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 106
line_end: 121
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
  - name: "num"
    annotation: "int"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "Tuple[List[State], List[Goal], List[float]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [109, 111, 114, 116]
  - target: null
    expr: "self.rb.sample"
    call_sites: [110]
  - target: null
    expr: "times.record_time"
    call_sites: [111, 116]
  - target: null
    expr: "self.get_pathfind().expand_states"
    call_sites: [115]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL.get_pathfind"
    expr: "self.get_pathfind"
    call_sites: [115]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._value_iteration_target"
    expr: "self._value_iteration_target"
    call_sites: [119]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRL._sample_rb_vi_target`

**File:** [deepxube/updaters/updater_v_rl.py:106](../../../../deepxube/updaters/updater_v_rl.py#L106)
**Class:** `UpdateHeurVRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _sample_rb_vi_target(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[float]]
```

## Docstring

Sample ``num`` items, expand their next states, and return VI-targeted ctgs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |
| `times` | `Times` | — |

## Returns

`Tuple[List[State], List[Goal], List[float]]`

## Calls

- `time.time` → `func:time.time` (lines: 109, 111, 114, 116)
- `self.get_pathfind` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRL.get_pathfind` (lines: 115)
- `self._value_iteration_target` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._value_iteration_target` (lines: 119)

### Unresolved
- `self.rb.sample` (lines: 110)
- `times.record_time` (lines: 111, 116)
- `self.get_pathfind().expand_states` (lines: 115)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.rb`

## Source

```python
    def _sample_rb_vi_target(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[float]]:
        """ Sample ``num`` items, expand their next states, and return VI-targeted ctgs. """
        # sample from replay buffer
        start_time = time.time()
        states, goals, is_solved_l = self.rb.sample(num)
        times.record_time("rb_samp", time.time() - start_time)

        # expand states
        start_time = time.time()
        states_exp, _, tcs_l = self.get_pathfind().expand_states(states, goals)
        times.record_time("vi_expand", time.time() - start_time)

        # value iteration update
        ctgs_backup: List[float] = self._value_iteration_target(goals, is_solved_l, tcs_l, states_exp, times)

        return states, goals, ctgs_backup
```
