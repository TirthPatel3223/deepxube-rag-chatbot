---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRL._init_replay_buffer"
kind: "method"
name: "_init_replay_buffer"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRL._init_replay_buffer"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 95
line_end: 97
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
  - name: "max_size"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ"
    expr: "ReplayBufferQ"
    call_sites: [97]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs:
  - "self.rb"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRL._init_replay_buffer`

**File:** [deepxube/updaters/updater_q_rl.py:95](../../../../deepxube/updaters/updater_q_rl.py#L95)
**Class:** `UpdateHeurQRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _init_replay_buffer(self, max_size: int) -> None
```

## Docstring

Replace the replay buffer with a fresh one of the given capacity. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `max_size` | `int` | — |

## Returns

`None`

## Calls

- `ReplayBufferQ` → `func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ` (lines: 97)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.rb`

**Reads:**
- `self.rb`

## Source

```python
    def _init_replay_buffer(self, max_size: int) -> None:
        """ Replace the replay buffer with a fresh one of the given capacity. """
        self.rb = ReplayBufferQ(max_size)
```
