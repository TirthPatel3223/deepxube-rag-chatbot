---
id: "func:deepxube.base.domain.ActsEnum.sample_state_action"
kind: "method"
name: "sample_state_action"
qualified_name: "deepxube.base.domain.ActsEnum.sample_state_action"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 250
line_end: 253
class: "ActsEnum"
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
  - target: "func:deepxube.base.domain.ActsEnum.get_state_actions"
    expr: "self.get_state_actions"
    call_sites: [252]
  - target: "func:random.choice"
    expr: "random.choice"
    call_sites: [253]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.ActsEnum.sample_state_action`

**File:** [deepxube/base/domain.py:250](../../../../deepxube/base/domain.py#L250)
**Class:** `ActsEnum`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_state_action(self, states: List[S]) -> List[A]
```

## Docstring

Sample one applicable action per state uniformly from ``get_state_actions``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |

## Returns

`List[A]`

## Calls

- `self.get_state_actions` → `func:deepxube.base.domain.ActsEnum.get_state_actions` (lines: 252)
- `random.choice` → `func:random.choice` (lines: 253)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_state_action(self, states: List[S]) -> List[A]:
        """ Sample one applicable action per state uniformly from ``get_state_actions``. """
        state_actions_l: List[List[A]] = self.get_state_actions(states)
        return [random.choice(state_actions) for state_actions in state_actions_l]
```
