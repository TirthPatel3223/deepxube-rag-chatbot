---
id: "func:deepxube.base.pathfinding.Node.upper_bound_parent_path"
kind: "method"
name: "upper_bound_parent_path"
qualified_name: "deepxube.base.pathfinding.Node.upper_bound_parent_path"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 66
line_end: 71
class: "Node"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "ctg_ub"
    annotation: "float"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "min"
    call_sites: [68]
  - target: null
    expr: "self.parent.upper_bound_parent_path"
    call_sites: [71]
raises: []
reads_attrs:
  - "self.backup_val"
  - "self.parent"
  - "self.parent_t_cost"
writes_attrs:
  - "self.backup_val"
---

# `deepxube.base.pathfinding.Node.upper_bound_parent_path`

**File:** [deepxube/base/pathfinding.py:66](../../../../deepxube/base/pathfinding.py#L66)
**Class:** `Node`
**Visibility:** public
**Kind:** method

## Signature

```python
def upper_bound_parent_path(self, ctg_ub: float) -> None
```

## Docstring

Recursively tighten ``backup_val`` to ``min(backup_val, ctg_ub + parent_tc + ...)`` up the parent chain. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `ctg_ub` | `float` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `min` (lines: 68)
- `self.parent.upper_bound_parent_path` (lines: 71)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.backup_val`

**Reads:**
- `self.backup_val`
- `self.parent`
- `self.parent_t_cost`

## Source

```python
    def upper_bound_parent_path(self, ctg_ub: float) -> None:
        """ Recursively tighten ``backup_val`` to ``min(backup_val, ctg_ub + parent_tc + ...)`` up the parent chain. """
        self.backup_val = min(self.backup_val, ctg_ub)
        if self.parent is not None:
            assert self.parent_t_cost is not None
            self.parent.upper_bound_parent_path(ctg_ub + self.parent_t_cost)
```
