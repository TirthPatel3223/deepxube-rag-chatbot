---
id: "class:deepxube.base.pathfinding.FNsHeurVPolicy"
kind: "class"
name: "FNsHeurVPolicy"
qualified_name: "deepxube.base.pathfinding.FNsHeurVPolicy"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 242
line_end: 244
is_abstract: false
is_dataclass: false
decorators:
  - "@dataclass(frozen=True)"
generic_parameters: []
bases:
  - name: "FNsPolicy"
    resolved_id: null
  - name: "FNsHeurV"
    resolved_id: null
methods: []
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.FNsHeurVPolicy`

**File:** [deepxube/base/pathfinding.py:242](../../../deepxube/base/pathfinding.py#L242)
**Abstract:** no
**Decorators:** `@dataclass(frozen=True)`

## Docstring

Function bundle for V + policy pathfinders. 

## Inheritance

**Direct bases:**
- `FNsPolicy`
- `FNsHeurV`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Source

```python
class FNsHeurVPolicy(FNsPolicy, FNsHeurV):
    """ Function bundle for V + policy pathfinders. """
    pass
```
