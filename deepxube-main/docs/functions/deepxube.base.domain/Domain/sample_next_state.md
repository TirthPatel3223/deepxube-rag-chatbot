---
id: "func:deepxube.base.domain.Domain.sample_next_state"
kind: "method"
name: "sample_next_state"
qualified_name: "deepxube.base.domain.Domain.sample_next_state"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 130
line_end: 137
class: "Domain"
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
returns: "Tuple[List[S], List[float]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.Domain.sample_state_action"
    expr: "self.sample_state_action"
    call_sites: [136]
  - target: "func:deepxube.base.domain.Domain.next_state"
    expr: "self.next_state"
    call_sites: [137]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.Domain.sample_next_state`

**File:** [deepxube/base/domain.py:130](../../../../deepxube/base/domain.py#L130)
**Class:** `Domain`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_next_state(self, states: List[S]) -> Tuple[List[S], List[float]]
```

## Docstring

Get random next state and transition cost given the current state

:param states: List of states
:return: Next states, transition costs

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |

## Returns

`Tuple[List[S], List[float]]`

## Calls

- `self.sample_state_action` → `func:deepxube.base.domain.Domain.sample_state_action` (lines: 136)
- `self.next_state` → `func:deepxube.base.domain.Domain.next_state` (lines: 137)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_next_state(self, states: List[S]) -> Tuple[List[S], List[float]]:
        """ Get random next state and transition cost given the current state

        :param states: List of states
        :return: Next states, transition costs
        """
        actions_rand: List[A] = self.sample_state_action(states)
        return self.next_state(states, actions_rand)
```
