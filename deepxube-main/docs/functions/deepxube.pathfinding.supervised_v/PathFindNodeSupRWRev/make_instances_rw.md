---
id: "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev.make_instances_rw"
kind: "method"
name: "make_instances_rw"
qualified_name: "deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev.make_instances_rw"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 123
line_end: 133
class: "PathFindNodeSupRWRev"
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
    call_sites: [125, 127, 129, 131]
  - target: null
    expr: "self.domain.sample_goalstate_goal_pairs"
    call_sites: [126]
  - target: null
    expr: "len"
    call_sites: [126]
  - target: null
    expr: "self.times.record_time"
    call_sites: [127, 131]
  - target: null
    expr: "self.domain.random_walk"
    call_sites: [130]
  - target: "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev._make_instances"
    expr: "self._make_instances"
    call_sites: [133]
raises: []
reads_attrs:
  - "self.domain"
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev.make_instances_rw`

**File:** [deepxube/pathfinding/supervised_v.py:123](../../../../deepxube/pathfinding/supervised_v.py#L123)
**Class:** `PathFindNodeSupRWRev`
**Visibility:** public
**Kind:** method

## Signature

```python
def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]
```

## Docstring

Sample (goal-state, goal) pairs, walk backwards to derive starts. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `steps_gen` | `List[int]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |

## Returns

`List[InstanceNodeSup]`

## Calls

- `time.time` → `func:time.time` (lines: 125, 127, 129, 131)
- `self._make_instances` → `func:deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev._make_instances` (lines: 133)

### Unresolved
- `self.domain.sample_goalstate_goal_pairs` (lines: 126)
- `len` (lines: 126)
- `self.times.record_time` (lines: 127, 131)
- `self.domain.random_walk` (lines: 130)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.times`

## Source

```python
    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Sample (goal-state, goal) pairs, walk backwards to derive starts. """
        start_time = time.time()
        states_goal, goals = self.domain.sample_goalstate_goal_pairs(len(steps_gen))
        self.times.record_time("samp_goal_state_goal", time.time() - start_time)

        start_time = time.time()
        states_start, path_costs = self.domain.random_walk(states_goal, steps_gen)
        self.times.record_time("random_walk", time.time() - start_time)

        return self._make_instances(states_start, goals, path_costs, inst_infos)
```
