---
id: "func:deepxube.base.heuristic.HeurNNetParQFixOut._get_input"
kind: "method"
name: "_get_input"
qualified_name: "deepxube.base.heuristic.HeurNNetParQFixOut._get_input"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 351
line_end: 354
class: "HeurNNetParQFixOut"
visibility: "private"
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
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.heuristic.HeurNNetParQFixOut.to_np"
    expr: "self.to_np"
    call_sites: [353]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParQFixOut._get_input`

**File:** [deepxube/base/heuristic.py:351](../../../../deepxube/base/heuristic.py#L351)
**Class:** `HeurNNetParQFixOut`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]
```

## Docstring

Prepare numpy inputs for the network (delegates to ``to_np``). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions_l` | `List[List[Action]]` | — |

## Returns

`List[NDArray]`

## Calls

- `self.to_np` → `func:deepxube.base.heuristic.HeurNNetParQFixOut.to_np` (lines: 353)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
        """ Prepare numpy inputs for the network (delegates to ``to_np``). """
        inputs_nnet: List[NDArray] = self.to_np(states, goals, actions_l)
        return inputs_nnet
```
