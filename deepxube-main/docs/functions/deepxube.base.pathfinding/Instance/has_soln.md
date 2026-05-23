---
id: "func:deepxube.base.pathfinding.Instance.has_soln"
kind: "method"
name: "has_soln"
qualified_name: "deepxube.base.pathfinding.Instance.has_soln"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 199
line_end: 204
class: "Instance"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "bool"
docstring_source: "present"
callees: []
raises: []
reads_attrs:
  - "self.goal_node"
writes_attrs: []
---

# `deepxube.base.pathfinding.Instance.has_soln`

**File:** [deepxube/base/pathfinding.py:199](../../../../deepxube/base/pathfinding.py#L199)
**Class:** `Instance`
**Visibility:** public
**Kind:** method

## Signature

```python
def has_soln(self) -> bool
```

## Docstring

:return: True if a goal-matching node has been recorded. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`bool`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.goal_node`

## Source

```python
    def has_soln(self) -> bool:
        """ :return: True if a goal-matching node has been recorded. """
        if self.goal_node is None:
            return False
        else:
            return True
```
