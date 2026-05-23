---
id: "func:deepxube.base.pathfinding.Node.get_all_descendants"
kind: "method"
name: "get_all_descendants"
qualified_name: "deepxube.base.pathfinding.Node.get_all_descendants"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 98
line_end: 110
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
returns: "List['Node']"
docstring_source: "present"
callees:
  - target: null
    expr: "self.edge_dict.values"
    call_sites: [103]
  - target: null
    expr: "len"
    call_sites: [105]
  - target: null
    expr: "fifo.pop"
    call_sites: [106]
  - target: null
    expr: "descendant.edge_dict.values"
    call_sites: [107]
  - target: null
    expr: "fifo.append"
    call_sites: [108]
  - target: null
    expr: "descendants.append"
    call_sites: [109]
raises: []
reads_attrs:
  - "self.edge_dict"
writes_attrs: []
---

# `deepxube.base.pathfinding.Node.get_all_descendants`

**File:** [deepxube/base/pathfinding.py:98](../../../../deepxube/base/pathfinding.py#L98)
**Class:** `Node`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_all_descendants(self) -> List['Node']
```

## Docstring

Get all descendants of node (excluding self)

:return: List of nodes that are descendants

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`List['Node']`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.edge_dict.values` (lines: 103)
- `len` (lines: 105)
- `fifo.pop` (lines: 106)
- `descendant.edge_dict.values` (lines: 107)
- `fifo.append` (lines: 108)
- `descendants.append` (lines: 109)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.edge_dict`

## Source

```python
    def get_all_descendants(self) -> List['Node']:
        """ Get all descendants of node (excluding self)

        :return: List of nodes that are descendants
        """
        fifo: List[Node] = [x[1] for x in self.edge_dict.values()]
        descendants: List[Node] = []
        while len(fifo) > 0:
            descendant: Node = fifo.pop(0)
            for _, descendant_c in descendant.edge_dict.values():
                fifo.append(descendant_c)
            descendants.append(descendant)
        return descendants
```
