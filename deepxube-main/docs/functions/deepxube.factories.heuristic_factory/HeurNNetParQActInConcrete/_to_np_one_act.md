---
id: "func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._to_np_one_act"
kind: "method"
name: "_to_np_one_act"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._to_np_one_act"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 310
line_end: 319
class: "HeurNNetParQActInConcrete"
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
  - name: "actions"
    annotation: "List[Action]"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._get_nnet_input().to_np"
    call_sites: [319]
  - target: "func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [319]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._to_np_one_act`

**File:** [deepxube/factories/heuristic_factory.py:310](../../../../deepxube/factories/heuristic_factory.py#L310)
**Class:** `HeurNNetParQActInConcrete`
**Visibility:** private
**Kind:** method

## Signature

```python
def _to_np_one_act(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray]
```

## Docstring

Convert state/goal plus one action per (state, goal) to numpy
inputs.

:param states: List of state objects.
:param goals: Matching list of goal objects.
:param actions: One action per (state, goal).
:return: List of numpy network input arrays.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |

## Returns

`List[NDArray]`

## Calls

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._get_nnet_input` (lines: 319)

### Unresolved
- `self._get_nnet_input().to_np` (lines: 319)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _to_np_one_act(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray]:
        """ Convert state/goal plus one action per (state, goal) to numpy
        inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions: One action per (state, goal).
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions)
```
