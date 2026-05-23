---
id: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup._make_instances"
kind: "method"
name: "_make_instances"
qualified_name: "deepxube.pathfinding.supervised_q.PathFindEdgeSup._make_instances"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 70
line_end: 86
class: "PathFindEdgeSup"
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
  - name: "acts_init"
    annotation: "List[Action]"
    default: null
  - name: "path_costs"
    annotation: "List[float]"
    default: null
  - name: "inst_infos"
    annotation: "Optional[List[Any]]"
    default: null
returns: "List[InstanceEdgeSup]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup._create_root_nodes"
    expr: "self._create_root_nodes"
    call_sites: [74]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [77, 84]
  - target: null
    expr: "zip"
    call_sites: [82]
  - target: null
    expr: "instances.append"
    call_sites: [83]
  - target: "func:deepxube.pathfinding.supervised_q.InstanceEdgeSup"
    expr: "InstanceEdgeSup"
    call_sites: [83]
  - target: null
    expr: "self.times.record_time"
    call_sites: [84]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_q.PathFindEdgeSup._make_instances`

**File:** [deepxube/pathfinding/supervised_q.py:70](../../../../deepxube/pathfinding/supervised_q.py#L70)
**Class:** `PathFindEdgeSup`
**Visibility:** private
**Kind:** method

## Signature

```python
def _make_instances(self, states_start: List[State], goals: List[Goal], acts_init: List[Action], path_costs: List[float], inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]
```

## Docstring

Build one ``InstanceEdgeSup`` per (state, goal, action, target path-cost) tuple. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_start` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `acts_init` | `List[Action]` | — |
| `path_costs` | `List[float]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |

## Returns

`List[InstanceEdgeSup]`

## Calls

- `self._create_root_nodes` → `func:deepxube.pathfinding.supervised_q.PathFindEdgeSup._create_root_nodes` (lines: 74)
- `time.time` → `func:time.time` (lines: 77, 84)
- `InstanceEdgeSup` → `func:deepxube.pathfinding.supervised_q.InstanceEdgeSup` (lines: 83)

### Unresolved
- `zip` (lines: 82)
- `instances.append` (lines: 83)
- `self.times.record_time` (lines: 84)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _make_instances(self, states_start: List[State], goals: List[Goal], acts_init: List[Action], path_costs: List[float],
                        inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]:
        """ Build one ``InstanceEdgeSup`` per (state, goal, action, target path-cost) tuple. """
        # make root nodes
        nodes_root: List[Node] = self._create_root_nodes(states_start, goals, False)

        # make instances
        start_time = time.time()
        if inst_infos is None:
            inst_infos = [None for _ in states_start]

        instances: List[InstanceEdgeSup] = []
        for node_root, act_init, path_cost, inst_info in zip(nodes_root, acts_init, path_costs, inst_infos):
            instances.append(InstanceEdgeSup(node_root, act_init, path_cost, inst_info))
        self.times.record_time("instances", time.time() - start_time)

        return instances
```
