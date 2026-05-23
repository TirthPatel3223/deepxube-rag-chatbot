---
id: "class:deepxube.base.heuristic.HeurFnQ"
kind: "class"
name: "HeurFnQ"
qualified_name: "deepxube.base.heuristic.HeurFnQ"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 211
line_end: 216
is_abstract: false
is_dataclass: false
decorators:
  - "@runtime_checkable"
generic_parameters: []
bases:
  - name: "Protocol"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.HeurFnQ.__call__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurFnQ`

**File:** [deepxube/base/heuristic.py:211](../../../deepxube/base/heuristic.py#L211)
**Abstract:** no
**Decorators:** `@runtime_checkable`

## Docstring

Callable protocol for Q-type heuristic functions: ``(states, goals, actions_l) -> [[q_per_action]]``. 

## Inheritance

**Direct bases:**
- `Protocol`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__call__` *(trivial, skipped)*

## Source

```python
class HeurFnQ(Protocol):
    """ Callable protocol for Q-type heuristic functions: ``(states, goals, actions_l) -> [[q_per_action]]``. """

    def __call__(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
        """ Return per-(state, goal) Q-values, one per action in the corresponding ``actions_l[i]``. """
        ...
```
