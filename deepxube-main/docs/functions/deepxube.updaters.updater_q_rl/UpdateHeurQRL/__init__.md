---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRL.__init__"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 62
line_end: 65
class: "UpdateHeurQRL"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "domain"
    annotation: "D"
    default: null
  - name: "pathfind_arg"
    annotation: "str"
    default: null
  - name: "up_args"
    annotation: "UpArgs"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [64]
  - target: null
    expr: "super"
    call_sites: [64]
  - target: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ"
    expr: "ReplayBufferQ"
    call_sites: [65]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs:
  - "self.rb"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRL.__init__`

**File:** [deepxube/updaters/updater_q_rl.py:62](../../../../deepxube/updaters/updater_q_rl.py#L62)
**Class:** `UpdateHeurQRL`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs)
```

## Docstring

Initialise the base updater and create an empty Q replay buffer. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `domain` | `D` | — |
| `pathfind_arg` | `str` | — |
| `up_args` | `UpArgs` | — |

## Returns

*(Not annotated.)*

## Calls

- `ReplayBufferQ` → `func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ` (lines: 65)

### Unresolved
- `super().__init__` (lines: 64)
- `super` (lines: 64)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.rb`

**Reads:**
- `self.rb`

## Source

```python
    def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs):
        """ Initialise the base updater and create an empty Q replay buffer. """
        super().__init__(domain, pathfind_arg, up_args)
        self.rb: ReplayBufferQ = ReplayBufferQ(0)
```
