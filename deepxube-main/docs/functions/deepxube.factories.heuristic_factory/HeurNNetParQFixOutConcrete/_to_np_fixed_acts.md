---
id: "func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._to_np_fixed_acts"
kind: "method"
name: "_to_np_fixed_acts"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._to_np_fixed_acts"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 272
line_end: 281
class: "HeurNNetParQFixOutConcrete"
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
  - target: null
    expr: "self._get_nnet_input().to_np"
    call_sites: [281]
  - target: "func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [281]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._to_np_fixed_acts`

**File:** [deepxube/factories/heuristic_factory.py:272](../../../../deepxube/factories/heuristic_factory.py#L272)
**Class:** `HeurNNetParQFixOutConcrete`
**Visibility:** private
**Kind:** method

## Signature

```python
def _to_np_fixed_acts(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]
```

## Docstring

Convert state/goal plus per-state action lists to numpy inputs.

:param states: List of state objects.
:param goals: Matching list of goal objects.
:param actions_l: One list of actions per (state, goal), all drawn
    from the fixed-action set.
:return: List of numpy network input arrays.

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

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._get_nnet_input` (lines: 281)

### Unresolved
- `self._get_nnet_input().to_np` (lines: 281)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _to_np_fixed_acts(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
        """ Convert state/goal plus per-state action lists to numpy inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions_l: One list of actions per (state, goal), all drawn
            from the fixed-action set.
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions_l)
```
