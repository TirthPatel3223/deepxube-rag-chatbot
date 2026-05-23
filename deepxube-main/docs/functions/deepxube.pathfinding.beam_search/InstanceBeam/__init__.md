---
id: "func:deepxube.pathfinding.beam_search.InstanceBeam.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.pathfinding.beam_search.InstanceBeam.__init__"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 24
line_end: 29
class: "InstanceBeam"
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
    call_sites: [26]
  - target: null
    expr: "super"
    call_sites: [26]
raises: []
reads_attrs:
  - "self.beam_size"
  - "self.eps"
  - "self.temp"
writes_attrs:
  - "self.beam_size"
  - "self.eps"
  - "self.temp"
---

# `deepxube.pathfinding.beam_search.InstanceBeam.__init__`

**File:** [deepxube/pathfinding/beam_search.py:24](../../../../deepxube/pathfinding/beam_search.py#L24)
**Class:** `InstanceBeam`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, root_node: Node, inst_info: Any)
```

## Docstring

Initialise with default beam_size=1, temp=0, eps=0. 

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
- `super().__init__` (lines: 26)
- `super` (lines: 26)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.beam_size`
- `self.eps`
- `self.temp`

**Reads:**
- `self.beam_size`
- `self.eps`
- `self.temp`

## Source

```python
    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise with default beam_size=1, temp=0, eps=0. """
        super().__init__(root_node, inst_info)
        self.beam_size: int = 1
        self.temp: float = 0.0
        self.eps: float = 0.0
```
