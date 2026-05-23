---
id: "class:deepxube.base.pathfinding.FNsHeurQ"
kind: "class"
name: "FNsHeurQ"
qualified_name: "deepxube.base.pathfinding.FNsHeurQ"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 227
line_end: 229
is_abstract: false
is_dataclass: false
decorators:
  - "@dataclass(frozen=True)"
generic_parameters: []
bases: []
methods: []
attributes:
  - name: "heur_fn_q"
    annotation: "HeurFnQ"
    default: null
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.FNsHeurQ`

**File:** [deepxube/base/pathfinding.py:227](../../../deepxube/base/pathfinding.py#L227)
**Abstract:** no
**Decorators:** `@dataclass(frozen=True)`

## Docstring

Function bundle for Q-only pathfinders. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `heur_fn_q` | `HeurFnQ` | class_body |

## Source

```python
class FNsHeurQ:
    """ Function bundle for Q-only pathfinders. """
    heur_fn_q: HeurFnQ
```
