---
id: "func:deepxube.base.heuristic.HeurNNetParQFixOut.to_np"
kind: "method"
name: "to_np"
qualified_name: "deepxube.base.heuristic.HeurNNetParQFixOut.to_np"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 341
line_end: 344
class: "HeurNNetParQFixOut"
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
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "actions_l"
    annotation: "List[List[Action]]"
    default: null
returns: "List[NDArray[Any]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.heuristic.HeurNNetParQFixOut._check_same_num_acts"
    expr: "self._check_same_num_acts"
    call_sites: [343]
  - target: "func:deepxube.base.heuristic.HeurNNetParQFixOut._to_np_fixed_acts"
    expr: "self._to_np_fixed_acts"
    call_sites: [344]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQFixOut.to_np`

**File:** [deepxube/base/heuristic.py:341](../../../../deepxube/base/heuristic.py#L341)
**Class:** `HeurNNetParQFixOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]
```

## Docstring

Validate equal action counts then delegate to ``_to_np_fixed_acts``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions_l` | `List[List[Action]]` | — |

## Returns

`List[NDArray[Any]]`

## Calls

- `self._check_same_num_acts` → `func:deepxube.base.heuristic.HeurNNetParQFixOut._check_same_num_acts` (lines: 343)
- `self._to_np_fixed_acts` → `func:deepxube.base.heuristic.HeurNNetParQFixOut._to_np_fixed_acts` (lines: 344)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Validate equal action counts then delegate to ``_to_np_fixed_acts``. """
        self._check_same_num_acts(actions_l)
        return self._to_np_fixed_acts(states, goals, actions_l)
```
