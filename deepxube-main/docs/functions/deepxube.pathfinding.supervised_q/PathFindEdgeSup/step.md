---
id: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup.step"
kind: "method"
name: "step"
qualified_name: "deepxube.pathfinding.supervised_q.PathFindEdgeSup.step"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 50
line_end: 64
class: "PathFindEdgeSup"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "verbose"
    annotation: "bool"
    default: "False"
returns: "Tuple[List[Node], List[EdgeQ]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.EdgeQ"
    expr: "EdgeQ"
    call_sites: [55]
  - target: null
    expr: "edges.append"
    call_sites: [56]
  - target: null
    expr: "instance.add_edges_popped"
    call_sites: [59]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [60, 62]
  - target: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup.set_is_solved"
    expr: "self.set_is_solved"
    call_sites: [61]
  - target: null
    expr: "self.times.record_time"
    call_sites: [62]
raises: []
reads_attrs:
  - "self.instances"
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_q.PathFindEdgeSup.step`

**File:** [deepxube/pathfinding/supervised_q.py:50](../../../../deepxube/pathfinding/supervised_q.py#L50)
**Class:** `PathFindEdgeSup`
**Visibility:** public
**Kind:** method

## Signature

```python
def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]
```

## Docstring

Emit each instance's initial edge with its supervised path cost as Q-value. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `verbose` | `bool` | `False` |

## Returns

`Tuple[List[Node], List[EdgeQ]]`

## Calls

- `EdgeQ` → `func:deepxube.base.pathfinding.EdgeQ` (lines: 55)
- `time.time` → `func:time.time` (lines: 60, 62)
- `self.set_is_solved` → `func:deepxube.pathfinding.supervised_q.PathFindEdgeSup.set_is_solved` (lines: 61)

### Unresolved
- `edges.append` (lines: 56)
- `instance.add_edges_popped` (lines: 59)
- `self.times.record_time` (lines: 62)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.instances`
- `self.times`

## Source

```python
    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Emit each instance's initial edge with its supervised path cost as Q-value. """
        edges: List[EdgeQ] = []
        for instance in self.instances:
            node_root: Node = instance.root_node
            edge: EdgeQ = EdgeQ(node_root, instance.action, instance.path_cost_sup)
            edges.append(edge)
            node_root.backup_val = instance.path_cost_sup
            instance.itr += 1
            instance.add_edges_popped([edge])
        start_time = time.time()
        self.set_is_solved([edge.node for edge in edges])
        self.times.record_time("is_solved", time.time() - start_time)

        return [], edges
```
