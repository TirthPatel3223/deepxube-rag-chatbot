---
id: "class:deepxube.base.pathfinding.FNsPolicy"
kind: "class"
name: "FNsPolicy"
qualified_name: "deepxube.base.pathfinding.FNsPolicy"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 236
line_end: 238
is_abstract: false
is_dataclass: false
decorators:
  - "@dataclass(frozen=True)"
generic_parameters: []
bases: []
methods: []
attributes:
  - name: "policy_fn"
    annotation: "PolicyFn"
    default: null
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.FNsPolicy`

**File:** [deepxube/base/pathfinding.py:236](../../../deepxube/base/pathfinding.py#L236)
**Abstract:** no
**Decorators:** `@dataclass(frozen=True)`

## Docstring

Function bundle for policy-only pathfinders. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `policy_fn` | `PolicyFn` | class_body |

## Source

```python
class FNsPolicy:
    """ Function bundle for policy-only pathfinders. """
    policy_fn: PolicyFn
```
