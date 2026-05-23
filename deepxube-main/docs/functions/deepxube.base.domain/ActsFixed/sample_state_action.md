---
id: "func:deepxube.base.domain.ActsFixed.sample_state_action"
kind: "method"
name: "sample_state_action"
qualified_name: "deepxube.base.domain.ActsFixed.sample_state_action"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 218
line_end: 220
class: "ActsFixed"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[S]"
    default: null
returns: "List[A]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.ActsFixed.sample_action"
    expr: "self.sample_action"
    call_sites: [220]
  - target: null
    expr: "len"
    call_sites: [220]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.ActsFixed.sample_state_action`

**File:** [deepxube/base/domain.py:218](../../../../deepxube/base/domain.py#L218)
**Class:** `ActsFixed`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_state_action(self, states: List[S]) -> List[A]
```

## Docstring

Sample one random action per state, ignoring per-state availability. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |

## Returns

`List[A]`

## Calls

- `self.sample_action` → `func:deepxube.base.domain.ActsFixed.sample_action` (lines: 220)

### Unresolved
- `len` (lines: 220)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_state_action(self, states: List[S]) -> List[A]:
        """ Sample one random action per state, ignoring per-state availability. """
        return self.sample_action(len(states))
```
