---
id: "func:deepxube.base.pathfinding.Instance.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.pathfinding.Instance.__init__"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 154
line_end: 163
class: "Instance"
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
callees: []
raises: []
reads_attrs:
  - "self._edges_popped"
  - "self._nodes_curr"
  - "self._nodes_popped"
  - "self.goal_node"
  - "self.inst_info"
  - "self.itr"
  - "self.num_nodes_generated"
  - "self.root_node"
writes_attrs:
  - "self._edges_popped"
  - "self._nodes_curr"
  - "self._nodes_popped"
  - "self.goal_node"
  - "self.inst_info"
  - "self.itr"
  - "self.num_nodes_generated"
  - "self.root_node"
---

# `deepxube.base.pathfinding.Instance.__init__`

**File:** [deepxube/base/pathfinding.py:154](../../../../deepxube/base/pathfinding.py#L154)
**Class:** `Instance`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, root_node: Node, inst_info: Any)
```

## Docstring

Initialise an instance with a single-node frontier (the root). 

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

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._edges_popped`
- `self._nodes_curr`
- `self._nodes_popped`
- `self.goal_node`
- `self.inst_info`
- `self.itr`
- `self.num_nodes_generated`
- `self.root_node`

**Reads:**
- `self._edges_popped`
- `self._nodes_curr`
- `self._nodes_popped`
- `self.goal_node`
- `self.inst_info`
- `self.itr`
- `self.num_nodes_generated`
- `self.root_node`

## Source

```python
    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise an instance with a single-node frontier (the root). """
        self.root_node: Node = root_node
        self.itr: int = 0  # updater with every pathfinding iteration
        self.num_nodes_generated: int = 0
        self.inst_info: Any = inst_info
        self.goal_node: Optional[Node] = None
        self._nodes_curr: List[Node] = [self.root_node]
        self._nodes_popped: List[Node] = []
        self._edges_popped: List[EdgeQ] = []
```
