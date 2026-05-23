---
id: "func:deepxube.pathfinding.supervised_v.PathFindNodeSup._make_instances"
kind: "method"
name: "_make_instances"
qualified_name: "deepxube.pathfinding.supervised_v.PathFindNodeSup._make_instances"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 68
line_end: 81
class: "PathFindNodeSup"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_start"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "path_costs"
    annotation: "List[float]"
    default: null
  - name: "inst_infos"
    annotation: "Optional[List[Any]]"
    default: null
returns: "List[InstanceNodeSup]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.supervised_v.PathFindNodeSup._create_root_nodes"
    expr: "self._create_root_nodes"
    call_sites: [70]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [72, 79]
  - target: null
    expr: "zip"
    call_sites: [77]
  - target: null
    expr: "instances.append"
    call_sites: [78]
  - target: "func:deepxube.pathfinding.supervised_v.InstanceNodeSup"
    expr: "InstanceNodeSup"
    call_sites: [78]
  - target: null
    expr: "self.times.record_time"
    call_sites: [79]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_v.PathFindNodeSup._make_instances`

**File:** [deepxube/pathfinding/supervised_v.py:68](../../../../deepxube/pathfinding/supervised_v.py#L68)
**Class:** `PathFindNodeSup`
**Visibility:** private
**Kind:** method

## Signature

```python
def _make_instances(self, states_start: List[State], goals: List[Goal], path_costs: List[float], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]
```

## Docstring

Build one ``InstanceNodeSup`` per (state, goal, target path-cost) triple. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_start` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `path_costs` | `List[float]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |

## Returns

`List[InstanceNodeSup]`

## Calls

- `self._create_root_nodes` → `func:deepxube.pathfinding.supervised_v.PathFindNodeSup._create_root_nodes` (lines: 70)
- `time.time` → `func:time.time` (lines: 72, 79)
- `InstanceNodeSup` → `func:deepxube.pathfinding.supervised_v.InstanceNodeSup` (lines: 78)

### Unresolved
- `zip` (lines: 77)
- `instances.append` (lines: 78)
- `self.times.record_time` (lines: 79)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _make_instances(self, states_start: List[State], goals: List[Goal], path_costs: List[float], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Build one ``InstanceNodeSup`` per (state, goal, target path-cost) triple. """
        nodes_root: List[Node] = self._create_root_nodes(states_start, goals, False)

        start_time = time.time()
        if inst_infos is None:
            inst_infos = [None for _ in states_start]

        instances: List[InstanceNodeSup] = []
        for node_root, path_cost, inst_info in zip(nodes_root, path_costs, inst_infos):
            instances.append(InstanceNodeSup(node_root, path_cost, inst_info))
        self.times.record_time("instances", time.time() - start_time)

        return instances
```
