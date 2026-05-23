---
id: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.__init__"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 36
line_end: 42
class: "ReplayBuffer"
visibility: "dunder"
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
returns: null
docstring_source: "present"
callees:
  - target: "func:collections.deque"
    expr: "deque"
    call_sites: [42]
raises: []
reads_attrs:
  - "self.deque"
writes_attrs:
  - "self.deque"
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.__init__`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:36](../../../../deepxube/updaters/utils/replay_buffer_utils.py#L36)
**Class:** `ReplayBuffer`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, max_size: int)
```

## Docstring

Create an empty buffer of the given capacity.

:param max_size: Maximum number of elements; once exceeded, the
    oldest elements are dropped (``deque`` semantics).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `max_size` | `int` | — |

## Returns

*(Not annotated.)*

## Calls

- `deque` → `func:collections.deque` (lines: 42)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.deque`

**Reads:**
- `self.deque`

## Source

```python
    def __init__(self, max_size: int):
        """ Create an empty buffer of the given capacity.

        :param max_size: Maximum number of elements; once exceeded, the
            oldest elements are dropped (``deque`` semantics).
        """
        self.deque: Deque[Elem] = deque([], max_size)
```
