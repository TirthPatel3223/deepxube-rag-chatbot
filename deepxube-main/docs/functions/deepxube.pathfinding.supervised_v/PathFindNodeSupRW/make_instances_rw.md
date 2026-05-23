---
id: "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRW.make_instances_rw"
kind: "method"
name: "make_instances_rw"
qualified_name: "deepxube.pathfinding.supervised_v.PathFindNodeSupRW.make_instances_rw"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 96
line_end: 111
class: "PathFindNodeSupRW"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "steps_gen"
    annotation: "List[int]"
    default: null
  - name: "inst_infos"
    annotation: "Optional[List[Any]]"
    default: null
returns: "List[InstanceNodeSup]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [98, 100, 102, 104, 107, 109]
  - target: null
    expr: "self.domain.sample_start_states"
    call_sites: [99]
  - target: null
    expr: "len"
    call_sites: [99]
  - target: null
    expr: "self.times.record_time"
    call_sites: [100, 104, 109]
  - target: null
    expr: "self.domain.random_walk"
    call_sites: [103]
  - target: null
    expr: "self.domain.sample_goal_from_state"
    call_sites: [108]
  - target: "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRW._make_instances"
    expr: "self._make_instances"
    call_sites: [111]
raises: []
reads_attrs:
  - "self.domain"
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_v.PathFindNodeSupRW.make_instances_rw`

**File:** [deepxube/pathfinding/supervised_v.py:96](../../../../deepxube/pathfinding/supervised_v.py#L96)
**Class:** `PathFindNodeSupRW`
**Visibility:** public
**Kind:** method

## Signature

```python
def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]
```

## Docstring

Sample start states, walk forward, derive goals from the walked states. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `steps_gen` | `List[int]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |

## Returns

`List[InstanceNodeSup]`

## Calls

- `time.time` → `func:time.time` (lines: 98, 100, 102, 104, 107, 109)
- `self._make_instances` → `func:deepxube.pathfinding.supervised_v.PathFindNodeSupRW._make_instances` (lines: 111)

### Unresolved
- `self.domain.sample_start_states` (lines: 99)
- `len` (lines: 99)
- `self.times.record_time` (lines: 100, 104, 109)
- `self.domain.random_walk` (lines: 103)
- `self.domain.sample_goal_from_state` (lines: 108)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.times`

## Source

```python
    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Sample start states, walk forward, derive goals from the walked states. """
        start_time = time.time()
        states_start: List[State] = self.domain.sample_start_states(len(steps_gen))
        self.times.record_time("get_start_states", time.time() - start_time)

        start_time = time.time()
        states_goal, path_costs = self.domain.random_walk(states_start, steps_gen)
        self.times.record_time("random_walk", time.time() - start_time)

        # state to goal
        start_time = time.time()
        goals: List[Goal] = self.domain.sample_goal_from_state(states_start, states_goal)
        self.times.record_time("sample_goal", time.time() - start_time)

        return self._make_instances(states_start, goals, path_costs, inst_infos)
```
