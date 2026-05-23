---
id: "func:deepxube.pathfinding.graph_search.GraphSearch.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearch.__init__"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 118
line_end: 123
class: "GraphSearch"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "domain"
    annotation: "D"
    default: null
  - name: "functions"
    annotation: "FNs"
    default: null
  - name: "batch_size"
    annotation: "int"
    default: "1"
  - name: "weight"
    annotation: "float"
    default: "1.0"
  - name: "eps"
    annotation: "float"
    default: "0.0"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [120]
  - target: null
    expr: "super"
    call_sites: [120]
raises: []
reads_attrs:
  - "self.batch_size_default"
  - "self.eps_default"
  - "self.weight_default"
writes_attrs:
  - "self.batch_size_default"
  - "self.eps_default"
  - "self.weight_default"
---

# `deepxube.pathfinding.graph_search.GraphSearch.__init__`

**File:** [deepxube/pathfinding/graph_search.py:118](../../../../deepxube/pathfinding/graph_search.py#L118)
**Class:** `GraphSearch`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: D, functions: FNs, batch_size: int = 1, weight: float = 1.0, eps: float = 0.0)
```

## Docstring

Store default batch/weight/eps parameters used when constructing instances. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `domain` | `D` | — |
| `functions` | `FNs` | — |
| `batch_size` | `int` | `1` |
| `weight` | `float` | `1.0` |
| `eps` | `float` | `0.0` |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

### Unresolved
- `super().__init__` (lines: 120)
- `super` (lines: 120)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.batch_size_default`
- `self.eps_default`
- `self.weight_default`

**Reads:**
- `self.batch_size_default`
- `self.eps_default`
- `self.weight_default`

## Source

```python
    def __init__(self, domain: D, functions: FNs, batch_size: int = 1, weight: float = 1.0, eps: float = 0.0):
        """ Store default batch/weight/eps parameters used when constructing instances. """
        super().__init__(domain, functions)
        self.batch_size_default: int = batch_size
        self.weight_default: float = weight
        self.eps_default: float = eps
```
