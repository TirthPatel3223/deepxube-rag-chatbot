---
id: "func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete.to_np"
kind: "method"
name: "to_np"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParVConcrete.to_np"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 237
line_end: 244
class: "HeurNNetParVConcrete"
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
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._get_nnet_input().to_np"
    call_sites: [244]
  - target: "func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [244]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.HeurNNetParVConcrete.to_np`

**File:** [deepxube/factories/heuristic_factory.py:237](../../../../deepxube/factories/heuristic_factory.py#L237)
**Class:** `HeurNNetParVConcrete`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]
```

## Docstring

Convert state/goal pairs to numpy network inputs.

:param states: List of state objects.
:param goals: Matching list of goal objects.
:return: List of numpy arrays, one per network input tensor.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |

## Returns

`List[NDArray]`

## Calls

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete._get_nnet_input` (lines: 244)

### Unresolved
- `self._get_nnet_input().to_np` (lines: 244)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]:
        """ Convert state/goal pairs to numpy network inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :return: List of numpy arrays, one per network input tensor.
        """
        return self._get_nnet_input().to_np(states, goals)
```
