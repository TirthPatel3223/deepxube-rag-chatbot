---
id: "func:deepxube.base.heuristic.HeurNNetParQIn.to_np"
kind: "method"
name: "to_np"
qualified_name: "deepxube.base.heuristic.HeurNNetParQIn.to_np"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 398
line_end: 402
class: "HeurNNetParQIn"
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
  - target: null
    expr: "all"
    call_sites: [400]
  - target: null
    expr: "len"
    call_sites: [400]
  - target: "func:deepxube.base.heuristic.HeurNNetParQIn._to_np_one_act"
    expr: "self._to_np_one_act"
    call_sites: [402]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQIn.to_np`

**File:** [deepxube/base/heuristic.py:398](../../../../deepxube/base/heuristic.py#L398)
**Class:** `HeurNNetParQIn`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]
```

## Docstring

Assert one action per state, then delegate to ``_to_np_one_act``. 

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

- `self._to_np_one_act` → `func:deepxube.base.heuristic.HeurNNetParQIn._to_np_one_act` (lines: 402)

### Unresolved
- `all` (lines: 400)
- `len` (lines: 400)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Assert one action per state, then delegate to ``_to_np_one_act``. """
        assert all((len(actions) == 1) for actions in actions_l), "there should only be one action per state/goal pair"
        actions_one: List[Action] = [actions[0] for actions in actions_l]
        return self._to_np_one_act(states, goals, actions_one)
```
