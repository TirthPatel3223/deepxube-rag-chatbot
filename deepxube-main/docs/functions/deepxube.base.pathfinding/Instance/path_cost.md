---
id: "func:deepxube.base.pathfinding.Instance.path_cost"
kind: "method"
name: "path_cost"
qualified_name: "deepxube.base.pathfinding.Instance.path_cost"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 206
line_end: 212
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
returns: "float"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.Instance.has_soln"
    expr: "self.has_soln"
    call_sites: [208]
raises: []
reads_attrs:
  - "self.goal_node"
writes_attrs: []
---

# `deepxube.base.pathfinding.Instance.path_cost`

**File:** [deepxube/base/pathfinding.py:206](../../../../deepxube/base/pathfinding.py#L206)
**Class:** `Instance`
**Visibility:** public
**Kind:** method

## Signature

```python
def path_cost(self) -> float
```

## Docstring

:return: Path cost of the recorded goal, or ``inf`` if none. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`float`

## Calls

- `self.has_soln` → `func:deepxube.base.pathfinding.Instance.has_soln` (lines: 208)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.goal_node`

## Source

```python
    def path_cost(self) -> float:
        """ :return: Path cost of the recorded goal, or ``inf`` if none. """
        if not self.has_soln():
            return np.inf
        else:
            assert self.goal_node is not None
            return self.goal_node.path_cost
```
