---
id: "func:deepxube.base.pathfinding.PathFindSetHeurV._set_node_vals"
kind: "method"
name: "_set_node_vals"
qualified_name: "deepxube.base.pathfinding.PathFindSetHeurV._set_node_vals"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 749
line_end: 763
class: "PathFindSetHeurV"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nodes"
    annotation: "List[Node]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [751, 763]
  - target: null
    expr: "self.functions.heur_fn_v"
    call_sites: [755]
  - target: null
    expr: "len"
    call_sites: [757, 758]
  - target: null
    expr: "zip"
    call_sites: [760]
  - target: null
    expr: "self.times.record_time"
    call_sites: [763]
raises: []
reads_attrs:
  - "self.functions"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindSetHeurV._set_node_vals`

**File:** [deepxube/base/pathfinding.py:749](../../../../deepxube/base/pathfinding.py#L749)
**Class:** `PathFindSetHeurV`
**Visibility:** private
**Kind:** method

## Signature

```python
def _set_node_vals(self, nodes: List[Node]) -> None
```

## Docstring

Evaluate V-heuristic on (state, goal) pairs and store on each node. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 751, 763)

### Unresolved
- `self.functions.heur_fn_v` (lines: 755)
- `len` (lines: 757, 758)
- `zip` (lines: 760)
- `self.times.record_time` (lines: 763)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.functions`
- `self.times`

## Source

```python
    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Evaluate V-heuristic on (state, goal) pairs and store on each node. """
        start_time = time.time()
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]

        heuristics: List[float] = self.functions.heur_fn_v(states, goals)

        assert len(heuristics) == len(states) == len(goals), \
            f"{len(heuristics)}, {len(states)}, {len(goals)}"

        for node, heuristic in zip(nodes, heuristics, strict=True):
            node.heuristic = heuristic

        self.times.record_time("heur", time.time() - start_time)
```
