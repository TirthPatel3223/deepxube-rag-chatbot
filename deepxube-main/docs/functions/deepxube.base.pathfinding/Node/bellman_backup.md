---
id: "func:deepxube.base.pathfinding.Node.bellman_backup"
kind: "method"
name: "bellman_backup"
qualified_name: "deepxube.base.pathfinding.Node.bellman_backup"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 55
line_end: 64
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
    call_sites: [62]
  - target: null
    expr: "min"
    call_sites: [63]
  - target: null
    expr: "self.edge_dict.values"
    call_sites: [63]
raises: []
reads_attrs:
  - "self.backup_val"
  - "self.edge_dict"
  - "self.is_solved"
writes_attrs:
  - "self.backup_val"
---

# `deepxube.base.pathfinding.Node.bellman_backup`

**File:** [deepxube/base/pathfinding.py:55](../../../../deepxube/base/pathfinding.py#L55)
**Class:** `Node`
**Visibility:** public
**Kind:** method

## Signature

```python
def bellman_backup(self) -> float
```

## Docstring

Update ``backup_val`` to ``min_a (tc(a) + child.heuristic)`` (or 0 if solved). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`float`

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 62)
- `min` (lines: 63)
- `self.edge_dict.values` (lines: 63)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.backup_val`

**Reads:**
- `self.backup_val`
- `self.edge_dict`
- `self.is_solved`

## Source

```python
    def bellman_backup(self) -> float:
        """ Update ``backup_val`` to ``min_a (tc(a) + child.heuristic)`` (or 0 if solved). """
        assert self.is_solved is not None

        if self.is_solved:
            self.backup_val = 0.0
        else:
            if len(self.edge_dict) > 0:
                self.backup_val = min(tc + node_c.heuristic for tc, node_c in self.edge_dict.values())
        return self.backup_val
```
