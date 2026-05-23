---
id: "class:deepxube.base.pathfinding.FNsHeurV"
kind: "class"
name: "FNsHeurV"
qualified_name: "deepxube.base.pathfinding.FNsHeurV"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 221
line_end: 223
is_abstract: false
is_dataclass: false
decorators:
  - "@dataclass(frozen=True)"
generic_parameters: []
bases: []
methods: []
attributes:
  - name: "heur_fn_v"
    annotation: "HeurFnV"
    default: null
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.FNsHeurV`

**File:** [deepxube/base/pathfinding.py:221](../../../deepxube/base/pathfinding.py#L221)
**Abstract:** no
**Decorators:** `@dataclass(frozen=True)`

## Docstring

Function bundle for V-only pathfinders. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `heur_fn_v` | `HeurFnV` | class_body |

## Source

```python
class FNsHeurV:
    """ Function bundle for V-only pathfinders. """
    heur_fn_v: HeurFnV
```
