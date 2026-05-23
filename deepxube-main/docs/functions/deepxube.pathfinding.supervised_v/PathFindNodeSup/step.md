---
id: "func:deepxube.pathfinding.supervised_v.PathFindNodeSup.step"
kind: "method"
name: "step"
qualified_name: "deepxube.pathfinding.supervised_v.PathFindNodeSup.step"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 48
line_end: 62
class: "PathFindNodeSup"
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
  - target: null
    expr: "nodes.append"
    call_sites: [55]
  - target: null
    expr: "instance.add_nodes_popped"
    call_sites: [56]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [58, 60]
  - target: "func:deepxube.pathfinding.supervised_v.PathFindNodeSup.set_is_solved"
    expr: "self.set_is_solved"
    call_sites: [59]
  - target: null
    expr: "self.times.record_time"
    call_sites: [60]
raises: []
reads_attrs:
  - "self.instances"
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_v.PathFindNodeSup.step`

**File:** [deepxube/pathfinding/supervised_v.py:48](../../../../deepxube/pathfinding/supervised_v.py#L48)
**Class:** `PathFindNodeSup`
**Visibility:** public
**Kind:** method

## Signature

```python
def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]
```

## Docstring

Emit each instance's root node with its supervised path cost as heuristic. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `verbose` | `bool` | `False` |

## Returns

`Tuple[List[Node], List[EdgeQ]]`

## Calls

- `time.time` → `func:time.time` (lines: 58, 60)
- `self.set_is_solved` → `func:deepxube.pathfinding.supervised_v.PathFindNodeSup.set_is_solved` (lines: 59)

### Unresolved
- `nodes.append` (lines: 55)
- `instance.add_nodes_popped` (lines: 56)
- `self.times.record_time` (lines: 60)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.instances`
- `self.times`

## Source

```python
    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Emit each instance's root node with its supervised path cost as heuristic. """
        nodes: List[Node] = []
        for instance in self.instances:
            node_root: Node = instance.root_node
            node_root.heuristic = instance.path_cost_sup
            node_root.backup_val = instance.path_cost_sup
            nodes.append(node_root)
            instance.add_nodes_popped([node_root])
            instance.itr += 1
        start_time = time.time()
        self.set_is_solved(nodes)
        self.times.record_time("is_solved", time.time() - start_time)

        return nodes, []
```
