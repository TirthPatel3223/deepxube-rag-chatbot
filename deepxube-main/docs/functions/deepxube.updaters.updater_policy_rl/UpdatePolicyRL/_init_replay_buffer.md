---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL._init_replay_buffer"
kind: "method"
name: "_init_replay_buffer"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRL._init_replay_buffer"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 80
line_end: 82
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
  - name: "max_size"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP"
    expr: "ReplayBufferP"
    call_sites: [82]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs:
  - "self.rb"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRL._init_replay_buffer`

**File:** [deepxube/updaters/updater_policy_rl.py:80](../../../../deepxube/updaters/updater_policy_rl.py#L80)
**Class:** `UpdatePolicyRL`
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

- `ReplayBufferP` → `func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP` (lines: 82)

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
        self.rb = ReplayBufferP(max_size)
```
