---
id: "func:deepxube.base.domain.NextStateNP.next_state"
kind: "method"
name: "next_state"
qualified_name: "deepxube.base.domain.NextStateNP.next_state"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 486
line_end: 492
class: "NextStateNP"
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
    annotation: "List[S]"
    default: null
  - name: "actions"
    annotation: "List[A]"
    default: null
returns: "Tuple[List[S], List[float]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.NextStateNP._states_to_np"
    expr: "self._states_to_np"
    call_sites: [488]
  - target: "func:deepxube.base.domain.NextStateNP._next_state_np"
    expr: "self._next_state_np"
    call_sites: [489]
  - target: "func:deepxube.base.domain.NextStateNP._np_to_states"
    expr: "self._np_to_states"
    call_sites: [490]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.NextStateNP.next_state`

**File:** [deepxube/base/domain.py:486](../../../../deepxube/base/domain.py#L486)
**Class:** `NextStateNP`
**Visibility:** public
**Kind:** method

## Signature

```python
def next_state(self, states: List[S], actions: List[A]) -> Tuple[List[S], List[float]]
```

## Docstring

``next_state`` via numpy: convert states, run ``_next_state_np``, convert back. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |
| `actions` | `List[A]` | — |

## Returns

`Tuple[List[S], List[float]]`

## Calls

- `self._states_to_np` → `func:deepxube.base.domain.NextStateNP._states_to_np` (lines: 488)
- `self._next_state_np` → `func:deepxube.base.domain.NextStateNP._next_state_np` (lines: 489)
- `self._np_to_states` → `func:deepxube.base.domain.NextStateNP._np_to_states` (lines: 490)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def next_state(self, states: List[S], actions: List[A]) -> Tuple[List[S], List[float]]:
        """ ``next_state`` via numpy: convert states, run ``_next_state_np``, convert back. """
        states_np: List[NDArray] = self._states_to_np(states)
        states_next_np, tcs = self._next_state_np(states_np, actions)
        states_next: List[S] = self._np_to_states(states_next_np)

        return states_next, tcs
```
