---
id: "func:deepxube.pathfinding.graph_search.InstanceGraph.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.pathfinding.graph_search.InstanceGraph.__init__"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 27
line_end: 37
class: "InstanceGraph"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "root_node"
    annotation: "Node"
    default: null
  - name: "inst_info"
    annotation: "Any"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [29]
  - target: null
    expr: "super"
    call_sites: [29]
raises: []
reads_attrs:
  - "self.batch_size"
  - "self.closed_dict"
  - "self.eps"
  - "self.heappush_count"
  - "self.lb"
  - "self.open_set"
  - "self.root_node"
  - "self.ub"
  - "self.weight"
writes_attrs:
  - "self.batch_size"
  - "self.closed_dict"
  - "self.eps"
  - "self.heappush_count"
  - "self.lb"
  - "self.open_set"
  - "self.ub"
  - "self.weight"
---

# `deepxube.pathfinding.graph_search.InstanceGraph.__init__`

**File:** [deepxube/pathfinding/graph_search.py:27](../../../../deepxube/pathfinding/graph_search.py#L27)
**Class:** `InstanceGraph`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, root_node: Node, inst_info: Any)
```

## Docstring

Initialise heap, closed dict, ub=inf, lb=root heuristic; default batch_size=1, weight=1.0, eps=0.0. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `root_node` | `Node` | — |
| `inst_info` | `Any` | — |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

### Unresolved
- `super().__init__` (lines: 29)
- `super` (lines: 29)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.batch_size`
- `self.closed_dict`
- `self.eps`
- `self.heappush_count`
- `self.lb`
- `self.open_set`
- `self.ub`
- `self.weight`

**Reads:**
- `self.batch_size`
- `self.closed_dict`
- `self.eps`
- `self.heappush_count`
- `self.lb`
- `self.open_set`
- `self.root_node`
- `self.ub`
- `self.weight`

## Source

```python
    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise heap, closed dict, ub=inf, lb=root heuristic; default batch_size=1, weight=1.0, eps=0.0. """
        super().__init__(root_node, inst_info)
        self.open_set: List[Tuple[float, int, SchOver]] = []
        self.heappush_count: int = 0
        self.closed_dict: Dict[State, float] = {}
        self.ub: float = np.inf
        self.lb: float = self.root_node.heuristic
        self.batch_size: int = 1
        self.weight: float = 1.0
        self.eps: float = 0.0
```
