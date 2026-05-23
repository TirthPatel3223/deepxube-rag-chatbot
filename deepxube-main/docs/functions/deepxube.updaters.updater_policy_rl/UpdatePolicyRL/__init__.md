---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRL.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRL.__init__"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 52
line_end: 55
class: "UpdatePolicyRL"
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
    call_sites: [54]
  - target: null
    expr: "super"
    call_sites: [54]
  - target: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP"
    expr: "ReplayBufferP"
    call_sites: [55]
raises: []
reads_attrs:
  - "self.rb"
writes_attrs:
  - "self.rb"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRL.__init__`

**File:** [deepxube/updaters/updater_policy_rl.py:52](../../../../deepxube/updaters/updater_policy_rl.py#L52)
**Class:** `UpdatePolicyRL`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs)
```

## Docstring

Initialise the base updater and create an empty policy replay buffer. 

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

- `ReplayBufferP` → `func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP` (lines: 55)

### Unresolved
- `super().__init__` (lines: 54)
- `super` (lines: 54)

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
        """ Initialise the base updater and create an empty policy replay buffer. """
        super().__init__(domain, pathfind_arg, up_args)
        self.rb: ReplayBufferP = ReplayBufferP(0)
```
