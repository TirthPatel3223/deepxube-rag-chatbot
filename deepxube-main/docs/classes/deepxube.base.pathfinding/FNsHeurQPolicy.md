---
id: "class:deepxube.base.pathfinding.FNsHeurQPolicy"
kind: "class"
name: "FNsHeurQPolicy"
qualified_name: "deepxube.base.pathfinding.FNsHeurQPolicy"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 248
line_end: 250
is_abstract: false
is_dataclass: false
decorators:
  - "@dataclass(frozen=True)"
generic_parameters: []
bases:
  - name: "FNsPolicy"
    resolved_id: null
  - name: "FNsHeurQ"
    resolved_id: null
methods: []
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.FNsHeurQPolicy`

**File:** [deepxube/base/pathfinding.py:248](../../../deepxube/base/pathfinding.py#L248)
**Abstract:** no
**Decorators:** `@dataclass(frozen=True)`

## Docstring

Function bundle for Q + policy pathfinders. 

## Inheritance

**Direct bases:**
- `FNsPolicy`
- `FNsHeurQ`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Source

```python
class FNsHeurQPolicy(FNsPolicy, FNsHeurQ):
    """ Function bundle for Q + policy pathfinders. """
    pass
```
