---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._rb_add"
kind: "method"
name: "_rb_add"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRL._rb_add"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 84
line_end: 88
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
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "actions"
    annotation: "List[Action]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [86, 88]
  - target: null
    expr: "self.rb.add"
    call_sites: [87]
  - target: null
    expr: "list"
    call_sites: [87]
  - target: null
    expr: "zip"
    call_sites: [87]
  - target: null
    expr: "times.record_time"
    call_sites: [88]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRL._rb_add`

**File:** [deepxube/updaters/updater_policy_rl.py:84](../../../../deepxube/updaters/updater_policy_rl.py#L84)
**Class:** `UpdatePolicyRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _rb_add(self, states: List[State], goals: List[Goal], actions: List[Action], times: Times) -> None
```

## Docstring

Push a batch of (state, goal, action) triples to the buffer. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 86, 88)

### Unresolved
- `self.rb.add` (lines: 87)
- `list` (lines: 87)
- `zip` (lines: 87)
- `times.record_time` (lines: 88)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.rb`

## Source

```python
    def _rb_add(self, states: List[State], goals: List[Goal], actions: List[Action], times: Times) -> None:
        """ Push a batch of (state, goal, action) triples to the buffer. """
        start_time = time.time()
        self.rb.add(list(zip(states, goals, actions, strict=True)))
        times.record_time("rb_add", time.time() - start_time)
```
