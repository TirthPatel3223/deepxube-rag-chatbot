---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRL._rb_add"
kind: "method"
name: "_rb_add"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRL._rb_add"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 100
line_end: 104
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
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "is_solved_l"
    annotation: "List[bool]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [102, 104]
  - target: null
    expr: "self.rb.add"
    call_sites: [103]
  - target: null
    expr: "list"
    call_sites: [103]
  - target: null
    expr: "zip"
    call_sites: [103]
  - target: null
    expr: "times.record_time"
    call_sites: [104]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRL._rb_add`

**File:** [deepxube/updaters/updater_v_rl.py:100](../../../../deepxube/updaters/updater_v_rl.py#L100)
**Class:** `UpdateHeurVRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _rb_add(self, states: List[State], goals: List[Goal], is_solved_l: List[bool], times: Times) -> None
```

## Docstring

Push a batch of (state, goal, is_solved) triples to the buffer. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `is_solved_l` | `List[bool]` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 102, 104)

### Unresolved
- `self.rb.add` (lines: 103)
- `list` (lines: 103)
- `zip` (lines: 103)
- `times.record_time` (lines: 104)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.rb`

## Source

```python
    def _rb_add(self, states: List[State], goals: List[Goal], is_solved_l: List[bool], times: Times) -> None:
        """ Push a batch of (state, goal, is_solved) triples to the buffer. """
        start_time = time.time()
        self.rb.add(list(zip(states, goals, is_solved_l, strict=True)))
        times.record_time("rb_add", time.time() - start_time)
```
