---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._sample_rb"
kind: "method"
name: "_sample_rb"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRL._sample_rb"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 90
line_end: 97
class: "UpdatePolicyRL"
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
returns: "Tuple[List[State], List[Goal], List[Action]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [93, 95]
  - target: null
    expr: "self.rb.sample"
    call_sites: [94]
  - target: null
    expr: "times.record_time"
    call_sites: [95]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRL._sample_rb`

**File:** [deepxube/updaters/updater_policy_rl.py:90](../../../../deepxube/updaters/updater_policy_rl.py#L90)
**Class:** `UpdatePolicyRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _sample_rb(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[Action]]
```

## Docstring

Uniformly sample ``num`` (state, goal, action) triples from the buffer. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |
| `times` | `Times` | — |

## Returns

`Tuple[List[State], List[Goal], List[Action]]`

## Calls

- `time.time` → `func:time.time` (lines: 93, 95)

### Unresolved
- `self.rb.sample` (lines: 94)
- `times.record_time` (lines: 95)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.rb`

## Source

```python
    def _sample_rb(self, num: int, times: Times) -> Tuple[List[State], List[Goal], List[Action]]:
        """ Uniformly sample ``num`` (state, goal, action) triples from the buffer. """
        # sample from replay buffer
        start_time = time.time()
        states, goals, actions = self.rb.sample(num)
        times.record_time("rb_samp", time.time() - start_time)

        return states, goals, actions
```
