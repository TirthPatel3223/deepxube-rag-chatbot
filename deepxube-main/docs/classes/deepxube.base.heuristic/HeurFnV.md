---
id: "class:deepxube.base.heuristic.HeurFnV"
kind: "class"
name: "HeurFnV"
qualified_name: "deepxube.base.heuristic.HeurFnV"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 202
line_end: 207
is_abstract: false
is_dataclass: false
decorators:
  - "@runtime_checkable"
generic_parameters: []
bases:
  - name: "Protocol"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.HeurFnV.__call__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurFnV`

**File:** [deepxube/base/heuristic.py:202](../../../deepxube/base/heuristic.py#L202)
**Abstract:** no
**Decorators:** `@runtime_checkable`

## Docstring

Callable protocol for V-type heuristic functions: ``(states, goals) -> [ctg]``. 

## Inheritance

**Direct bases:**
- `Protocol`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__call__` *(trivial, skipped)*

## Source

```python
class HeurFnV(Protocol):
    """ Callable protocol for V-type heuristic functions: ``(states, goals) -> [ctg]``. """

    def __call__(self, states: List[State], goals: List[Goal]) -> List[float]:
        """ Return one cost-to-go per (state, goal) pair. """
        ...
```
