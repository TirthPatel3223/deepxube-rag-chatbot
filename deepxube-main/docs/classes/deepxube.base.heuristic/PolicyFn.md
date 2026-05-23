---
id: "class:deepxube.base.heuristic.PolicyFn"
kind: "class"
name: "PolicyFn"
qualified_name: "deepxube.base.heuristic.PolicyFn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 223
line_end: 230
is_abstract: false
is_dataclass: false
decorators:
  - "@runtime_checkable"
generic_parameters: []
bases:
  - name: "Protocol"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.PolicyFn.__call__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.PolicyFn`

**File:** [deepxube/base/heuristic.py:223](../../../deepxube/base/heuristic.py#L223)
**Abstract:** no
**Decorators:** `@runtime_checkable`

## Docstring

Callable protocol for policy functions: maps states/goals to sampled actions and their pdfs. 

## Inheritance

**Direct bases:**
- `Protocol`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__call__` *(trivial, skipped)*

## Source

```python
class PolicyFn(Protocol):
    """ Callable protocol for policy functions: maps states/goals to sampled actions and their pdfs. """

    def __call__(self, domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
        """ Map states and goals to sampled actions along with their probability (or log probability) densities

        """
        ...
```
