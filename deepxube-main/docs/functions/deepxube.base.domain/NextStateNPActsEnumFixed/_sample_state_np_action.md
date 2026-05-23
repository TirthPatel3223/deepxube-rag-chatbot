---
id: "func:deepxube.base.domain.NextStateNPActsEnumFixed._sample_state_np_action"
kind: "method"
name: "_sample_state_np_action"
qualified_name: "deepxube.base.domain.NextStateNPActsEnumFixed._sample_state_np_action"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 605
line_end: 608
class: "NextStateNPActsEnumFixed"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_np"
    annotation: "List[NDArray]"
    default: null
returns: "List[A]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.NextStateNPActsEnumFixed._get_state_np_actions"
    expr: "self._get_state_np_actions"
    call_sites: [607]
  - target: "func:random.choice"
    expr: "random.choice"
    call_sites: [608]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.NextStateNPActsEnumFixed._sample_state_np_action`

**File:** [deepxube/base/domain.py:605](../../../../deepxube/base/domain.py#L605)
**Class:** `NextStateNPActsEnumFixed`
**Visibility:** private
**Kind:** method

## Signature

```python
def _sample_state_np_action(self, states_np: List[NDArray]) -> List[A]
```

## Docstring

Uniformly sample one action per row from the fixed action list. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `List[NDArray]` | — |

## Returns

`List[A]`

## Calls

- `self._get_state_np_actions` → `func:deepxube.base.domain.NextStateNPActsEnumFixed._get_state_np_actions` (lines: 607)
- `random.choice` → `func:random.choice` (lines: 608)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _sample_state_np_action(self, states_np: List[NDArray]) -> List[A]:
        """ Uniformly sample one action per row from the fixed action list. """
        state_actions_l: List[List[A]] = self._get_state_np_actions(states_np)
        return [random.choice(state_actions) for state_actions in state_actions_l]
```
