---
id: "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_train"
kind: "method"
name: "to_np_train"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_train"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 346
line_end: 355
class: "PolicyNNetParConcrete"
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
  - name: "actions"
    annotation: "List[Action]"
    default: null
returns: "List[NDArray[Any]]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._get_nnet_input().to_np"
    call_sites: [355]
  - target: "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [355]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_train`

**File:** [deepxube/factories/heuristic_factory.py:346](../../../../deepxube/factories/heuristic_factory.py#L346)
**Class:** `PolicyNNetParConcrete`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_train(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]
```

## Docstring

Convert state/goal/action triples to numpy inputs for policy
training (target-action labels included).

:param states: List of state objects.
:param goals: Matching list of goal objects.
:param actions: One target action per (state, goal).
:return: List of numpy network input arrays.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |

## Returns

`List[NDArray[Any]]`

## Calls

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._get_nnet_input` (lines: 355)

### Unresolved
- `self._get_nnet_input().to_np` (lines: 355)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_train(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]:
        """ Convert state/goal/action triples to numpy inputs for policy
        training (target-action labels included).

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions: One target action per (state, goal).
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions)
```
