---
id: "func:deepxube.base.pathfinding.Node.backup_act"
kind: "method"
name: "backup_act"
qualified_name: "deepxube.base.pathfinding.Node.backup_act"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 85
line_end: 96
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
  - name: "action"
    annotation: "Action"
    default: null
returns: "float"
docstring_source: "present"
callees: []
raises: []
reads_attrs:
  - "self.edge_dict"
  - "self.is_solved"
writes_attrs: []
---

# `deepxube.base.pathfinding.Node.backup_act`

**File:** [deepxube/base/pathfinding.py:85](../../../../deepxube/base/pathfinding.py#L85)
**Class:** `Node`
**Visibility:** public
**Kind:** method

## Signature

```python
def backup_act(self, action: Action) -> float
```

## Docstring

:return: One-step backup target for the Q-value of ``action`` from this node. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `action` | `Action` | — |

## Returns

`float`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.edge_dict`
- `self.is_solved`

## Source

```python
    def backup_act(self, action: Action) -> float:
        """ :return: One-step backup target for the Q-value of ``action`` from this node. """
        assert self.is_solved is not None
        if self.is_solved:
            return 0.0
        else:
            tc, node_next = self.edge_dict[action]
            # assert node_next.q_values is not None
            if node_next.backup_val < np.inf:
                return tc + node_next.backup_val
            else:
                return tc + node_next.heuristic
```
