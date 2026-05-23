---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._sample_rb_qlearn_target"
kind: "method"
name: "_sample_rb_qlearn_target"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRL._sample_rb_qlearn_target"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 106
line_end: 116
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
  - name: "num"
    annotation: "int"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "Tuple[List[State], List[Goal], List[Action], List[float]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [109, 111]
  - target: null
    expr: "self.rb.sample"
    call_sites: [110]
  - target: null
    expr: "times.record_time"
    call_sites: [111]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._q_learning_target"
    expr: "self._q_learning_target"
    call_sites: [114]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRL._sample_rb_qlearn_target`

**File:** [deepxube/updaters/updater_q_rl.py:106](../../../../deepxube/updaters/updater_q_rl.py#L106)
**Class:** `UpdateHeurQRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _sample_rb_qlearn_target(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[Action], List[float]]
```

## Docstring

Sample ``num`` items from the buffer and compute Q-learning targets for them. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |
| `times` | `Times` | — |

## Returns

`Tuple[List[State], List[Goal], List[Action], List[float]]`

## Calls

- `time.time` → `func:time.time` (lines: 109, 111)
- `self._q_learning_target` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._q_learning_target` (lines: 114)

### Unresolved
- `self.rb.sample` (lines: 110)
- `times.record_time` (lines: 111)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.rb`

## Source

```python
    def _sample_rb_qlearn_target(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[Action], List[float]]:
        """ Sample ``num`` items from the buffer and compute Q-learning targets for them. """
        # sample from replay buffer
        start_time = time.time()
        states, goals, is_solved_l, actions, tcs, states_next = self.rb.sample(num)
        times.record_time("rb_samp", time.time() - start_time)

        # value iteration update
        ctgs_backup: List[float] = self._q_learning_target(goals, is_solved_l, tcs, states_next, times)

        return states, goals, actions, ctgs_backup
```
