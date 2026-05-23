---
id: "func:deepxube.base.domain.NextStateNPActsEnumFixed._get_state_np_actions"
kind: "method"
name: "_get_state_np_actions"
qualified_name: "deepxube.base.domain.NextStateNPActsEnumFixed._get_state_np_actions"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 600
line_end: 603
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
returns: "List[List[A]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.NextStateNPActsEnumFixed.get_actions_fixed"
    expr: "self.get_actions_fixed"
    call_sites: [602]
  - target: null
    expr: "state_actions.copy"
    call_sites: [603]
  - target: null
    expr: "range"
    call_sites: [603]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.NextStateNPActsEnumFixed._get_state_np_actions`

**File:** [deepxube/base/domain.py:600](../../../../deepxube/base/domain.py#L600)
**Class:** `NextStateNPActsEnumFixed`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_state_np_actions(self, states_np: List[NDArray]) -> List[List[A]]
```

## Docstring

:return: A copy of the fixed action list per row in ``states_np[0]``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `List[NDArray]` | — |

## Returns

`List[List[A]]`

## Calls

- `self.get_actions_fixed` → `func:deepxube.base.domain.NextStateNPActsEnumFixed.get_actions_fixed` (lines: 602)

### Unresolved
- `state_actions.copy` (lines: 603)
- `range` (lines: 603)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_state_np_actions(self, states_np: List[NDArray]) -> List[List[A]]:
        """ :return: A copy of the fixed action list per row in ``states_np[0]``. """
        state_actions: List[A] = self.get_actions_fixed()
        return [state_actions.copy() for _ in range(states_np[0].shape[0])]
```
