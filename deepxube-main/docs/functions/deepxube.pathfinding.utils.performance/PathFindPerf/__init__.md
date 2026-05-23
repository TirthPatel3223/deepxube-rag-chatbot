---
id: "func:deepxube.pathfinding.utils.performance.PathFindPerf.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.pathfinding.utils.performance.PathFindPerf.__init__"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 18
line_end: 24
class: "PathFindPerf"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees: []
raises: []
reads_attrs:
  - "self.ctgs"
  - "self.ctgs_bkup"
  - "self.is_solved_l"
  - "self.path_costs"
  - "self.search_itrs_l"
writes_attrs:
  - "self.ctgs"
  - "self.ctgs_bkup"
  - "self.is_solved_l"
  - "self.path_costs"
  - "self.search_itrs_l"
---

# `deepxube.pathfinding.utils.performance.PathFindPerf.__init__`

**File:** [deepxube/pathfinding/utils/performance.py:18](../../../../deepxube/pathfinding/utils/performance.py#L18)
**Class:** `PathFindPerf`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self) -> None
```

## Docstring

Initialise empty stat lists. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.ctgs`
- `self.ctgs_bkup`
- `self.is_solved_l`
- `self.path_costs`
- `self.search_itrs_l`

**Reads:**
- `self.ctgs`
- `self.ctgs_bkup`
- `self.is_solved_l`
- `self.path_costs`
- `self.search_itrs_l`

## Source

```python
    def __init__(self) -> None:
        """ Initialise empty stat lists. """
        self.is_solved_l: List[bool] = []
        self.path_costs: List[float] = []
        self.search_itrs_l: List[int] = []
        self.ctgs: List[float] = []
        self.ctgs_bkup: List[float] = []
```
