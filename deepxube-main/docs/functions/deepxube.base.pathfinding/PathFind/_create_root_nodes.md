---
id: "func:deepxube.base.pathfinding.PathFind._create_root_nodes"
kind: "method"
name: "_create_root_nodes"
qualified_name: "deepxube.base.pathfinding.PathFind._create_root_nodes"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 367
line_end: 381
class: "PathFind"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "compute_root_vals"
    annotation: "bool"
    default: null
returns: "List[Node]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [369, 376]
  - target: null
    expr: "zip"
    call_sites: [372]
  - target: "func:deepxube.base.pathfinding.Node"
    expr: "Node"
    call_sites: [373]
  - target: null
    expr: "root_nodes.append"
    call_sites: [374]
  - target: null
    expr: "self.times.record_time"
    call_sites: [376]
  - target: "func:deepxube.base.pathfinding.PathFind._set_node_vals"
    expr: "self._set_node_vals"
    call_sites: [379]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFind._create_root_nodes`

**File:** [deepxube/base/pathfinding.py:367](../../../../deepxube/base/pathfinding.py#L367)
**Class:** `PathFind`
**Visibility:** private
**Kind:** method

## Signature

```python
def _create_root_nodes(self, states: List[State], goals: List[Goal], compute_root_vals: bool) -> List[Node]
```

## Docstring

Build per-instance root nodes; optionally evaluate their heuristic/Q values. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `compute_root_vals` | `bool` | — |

## Returns

`List[Node]`

## Calls

- `time.time` → `func:time.time` (lines: 369, 376)
- `Node` → `func:deepxube.base.pathfinding.Node` (lines: 373)
- `self._set_node_vals` → `func:deepxube.base.pathfinding.PathFind._set_node_vals` (lines: 379)

### Unresolved
- `zip` (lines: 372)
- `root_nodes.append` (lines: 374)
- `self.times.record_time` (lines: 376)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _create_root_nodes(self, states: List[State], goals: List[Goal], compute_root_vals: bool) -> List[Node]:
        """ Build per-instance root nodes; optionally evaluate their heuristic/Q values. """
        start_time = time.time()

        root_nodes: List[Node] = []
        for state, goal in zip(states, goals, strict=True):
            root_node: Node = Node(state, goal, 0.0, 0.0, None, None, None, None, None)
            root_nodes.append(root_node)

        self.times.record_time("root", time.time() - start_time)

        if compute_root_vals:
            self._set_node_vals(root_nodes)

        return root_nodes
```
