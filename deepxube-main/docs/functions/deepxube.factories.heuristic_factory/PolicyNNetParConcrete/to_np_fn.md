---
id: "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_fn"
kind: "method"
name: "to_np_fn"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_fn"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 336
line_end: 344
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
returns: "List[NDArray[Any]]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._get_nnet_input().to_np_fn"
    call_sites: [344]
  - target: "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [344]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_fn`

**File:** [deepxube/factories/heuristic_factory.py:336](../../../../deepxube/factories/heuristic_factory.py#L336)
**Class:** `PolicyNNetParConcrete`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_fn(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]
```

## Docstring

Convert state/goal pairs to numpy inputs for policy inference
(no actions supplied).

:param states: List of state objects.
:param goals: Matching list of goal objects.
:return: List of numpy network input arrays.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |

## Returns

`List[NDArray[Any]]`

## Calls

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._get_nnet_input` (lines: 344)

### Unresolved
- `self._get_nnet_input().to_np_fn` (lines: 344)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_fn(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]:
        """ Convert state/goal pairs to numpy inputs for policy inference
        (no actions supplied).

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np_fn(states, goals)
```
