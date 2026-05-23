---
id: "func:deepxube.base.domain.ActsEnumFixed.get_state_actions"
kind: "method"
name: "get_state_actions"
qualified_name: "deepxube.base.domain.ActsEnumFixed.get_state_actions"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 301
line_end: 303
class: "ActsEnumFixed"
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
returns: "List[List[A]]"
docstring_source: "present"
callees:
  - target: null
    expr: "self.get_actions_fixed().copy"
    call_sites: [303]
  - target: "func:deepxube.base.domain.ActsEnumFixed.get_actions_fixed"
    expr: "self.get_actions_fixed"
    call_sites: [303]
  - target: null
    expr: "range"
    call_sites: [303]
  - target: null
    expr: "len"
    call_sites: [303]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.ActsEnumFixed.get_state_actions`

**File:** [deepxube/base/domain.py:301](../../../../deepxube/base/domain.py#L301)
**Class:** `ActsEnumFixed`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_state_actions(self, states: List[S]) -> List[List[A]]
```

## Docstring

:return: A copy of the fixed action list for every input state. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |

## Returns

`List[List[A]]`

## Calls

- `self.get_actions_fixed` → `func:deepxube.base.domain.ActsEnumFixed.get_actions_fixed` (lines: 303)

### Unresolved
- `self.get_actions_fixed().copy` (lines: 303)
- `range` (lines: 303)
- `len` (lines: 303)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_state_actions(self, states: List[S]) -> List[List[A]]:
        """ :return: A copy of the fixed action list for every input state. """
        return [self.get_actions_fixed().copy() for _ in range(len(states))]
```
