---
id: "func:deepxube.base.pathfinding.Node.tree_backup"
kind: "method"
name: "tree_backup"
qualified_name: "deepxube.base.pathfinding.Node.tree_backup"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 73
line_end: 83
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
returns: "float"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [78]
  - target: null
    expr: "max"
    call_sites: [79]
  - target: null
    expr: "min"
    call_sites: [81]
  - target: null
    expr: "node_c.tree_backup"
    call_sites: [81]
  - target: null
    expr: "self.edge_dict.values"
    call_sites: [81]
raises: []
reads_attrs:
  - "self.backup_val"
  - "self.edge_dict"
  - "self.heuristic"
  - "self.is_solved"
writes_attrs:
  - "self.backup_val"
---

# `deepxube.base.pathfinding.Node.tree_backup`

**File:** [deepxube/base/pathfinding.py:73](../../../../deepxube/base/pathfinding.py#L73)
**Class:** `Node`
**Visibility:** public
**Kind:** method

## Signature

```python
def tree_backup(self) -> float
```

## Docstring

Recursive tree backup: ``min`` over child sub-trees, leaf = ``max(heuristic, 0)``; for Limited-Horizon Bellman learning. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`float`

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 78)
- `max` (lines: 79)
- `min` (lines: 81)
- `node_c.tree_backup` (lines: 81)
- `self.edge_dict.values` (lines: 81)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.backup_val`

**Reads:**
- `self.backup_val`
- `self.edge_dict`
- `self.heuristic`
- `self.is_solved`

## Source

```python
    def tree_backup(self) -> float:
        """ Recursive tree backup: ``min`` over child sub-trees, leaf = ``max(heuristic, 0)``; for Limited-Horizon Bellman learning. """
        if (self.is_solved is not None) and self.is_solved:
            self.backup_val = 0.0
        else:
            if len(self.edge_dict) == 0:
                self.backup_val = max(self.heuristic, 0.0)
            else:
                self.backup_val = min(tc + node_c.tree_backup() for tc, node_c in self.edge_dict.values())

        return self.backup_val
```
