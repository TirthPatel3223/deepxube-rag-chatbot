---
id: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.size"
kind: "method"
name: "size"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.size"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 33
line_end: 34
class: "ReplayBuffer"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "int"
docstring_source: "missing"
callees:
  - target: "func:deepxube.updaters.utils.replay_buffer_utils.len"
    expr: "len"
    call_sites: [34]
raises: []
reads_attrs:
  - "self.deque"
writes_attrs: []
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.size`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:33](../../../../deepxube/updaters/utils/replay_buffer_utils.py#L33)
**Class:** `ReplayBuffer`
**Visibility:** public
**Kind:** method

## Signature

```python
def size(self) -> int
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`int`

## Calls

- `len` → `func:deepxube.updaters.utils.replay_buffer_utils.len` (lines: 34)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.deque`

## Source

```python
    def size(self) -> int:
        return len(self.deque)
```
