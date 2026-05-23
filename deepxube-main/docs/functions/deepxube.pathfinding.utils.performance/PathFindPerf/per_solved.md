---
id: "func:deepxube.pathfinding.utils.performance.PathFindPerf.per_solved"
kind: "method"
name: "per_solved"
qualified_name: "deepxube.pathfinding.utils.performance.PathFindPerf.per_solved"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 46
line_end: 48
class: "PathFindPerf"
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
  - target: null
    expr: "float"
    call_sites: [48]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [48]
raises: []
reads_attrs:
  - "self.is_solved_l"
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.PathFindPerf.per_solved`

**File:** [deepxube/pathfinding/utils/performance.py:46](../../../../deepxube/pathfinding/utils/performance.py#L46)
**Class:** `PathFindPerf`
**Visibility:** public
**Kind:** method

## Signature

```python
def per_solved(self) -> float
```

## Docstring

:return: Percent solved across recorded instances. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`float`

## Calls

- `np.mean` → `func:numpy.mean` (lines: 48)

### Unresolved
- `float` (lines: 48)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.is_solved_l`

## Source

```python
    def per_solved(self) -> float:
        """ :return: Percent solved across recorded instances. """
        return 100.0 * float(np.mean(self.is_solved_l))
```
