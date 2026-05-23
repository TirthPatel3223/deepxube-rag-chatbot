---
id: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRW.make_instances_rw"
kind: "method"
name: "make_instances_rw"
qualified_name: "deepxube.pathfinding.supervised_q.PathFindEdgeSupRW.make_instances_rw"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 101
line_end: 129
class: "PathFindEdgeSupRW"
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
returns: "List[InstanceEdgeSup]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [104, 106, 109, 115, 118, 122, 125, 127]
  - target: null
    expr: "self.domain.sample_start_states"
    call_sites: [105]
  - target: null
    expr: "len"
    call_sites: [105]
  - target: null
    expr: "self.times.record_time"
    call_sites: [106, 115, 122, 127]
  - target: null
    expr: "self.domain.sample_state_action"
    call_sites: [110]
  - target: null
    expr: "self.domain.next_state"
    call_sites: [111]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [112]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [112, 119, 121]
  - target: null
    expr: "np.maximum(np.array(steps_gen) - 1, 0).tolist"
    call_sites: [119]
  - target: "func:numpy.maximum"
    expr: "np.maximum"
    call_sites: [119]
  - target: null
    expr: "self.domain.random_walk"
    call_sites: [120]
  - target: null
    expr: "(np.array(path_costs_1step) + np.array(path_costs)).tolist"
    call_sites: [121]
  - target: null
    expr: "self.domain.sample_goal_from_state"
    call_sites: [126]
  - target: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRW._make_instances"
    expr: "self._make_instances"
    call_sites: [129]
raises: []
reads_attrs:
  - "self.domain"
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_q.PathFindEdgeSupRW.make_instances_rw`

**File:** [deepxube/pathfinding/supervised_q.py:101](../../../../deepxube/pathfinding/supervised_q.py#L101)
**Class:** `PathFindEdgeSupRW`
**Visibility:** public
**Kind:** method

## Signature

```python
def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]
```

## Docstring

Sample start states, take one labelled action, walk to goal, derive goal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `steps_gen` | `List[int]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |

## Returns

`List[InstanceEdgeSup]`

## Calls

- `time.time` → `func:time.time` (lines: 104, 106, 109, 115, 118, 122, 125, 127)
- `np.where` → `func:numpy.where` (lines: 112)
- `np.array` → `func:numpy.array` (lines: 112, 119, 121)
- `np.maximum` → `func:numpy.maximum` (lines: 119)
- `self._make_instances` → `func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRW._make_instances` (lines: 129)

### Unresolved
- `self.domain.sample_start_states` (lines: 105)
- `len` (lines: 105)
- `self.times.record_time` (lines: 106, 115, 122, 127)
- `self.domain.sample_state_action` (lines: 110)
- `self.domain.next_state` (lines: 111)
- `np.maximum(np.array(steps_gen) - 1, 0).tolist` (lines: 119)
- `self.domain.random_walk` (lines: 120)
- `(np.array(path_costs_1step) + np.array(path_costs)).tolist` (lines: 121)
- `self.domain.sample_goal_from_state` (lines: 126)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.times`

## Source

```python
    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]:
        """ Sample start states, take one labelled action, walk to goal, derive goal. """
        # start states
        start_time = time.time()
        states_start: List[State] = self.domain.sample_start_states(len(steps_gen))
        self.times.record_time("get_start_states", time.time() - start_time)

        # first step
        start_time = time.time()
        acts_init: List[Action] = self.domain.sample_state_action(states_start)
        states_start_1step, path_costs_1step = self.domain.next_state(states_start, acts_init)
        for idx in np.where(np.array(steps_gen) == 0)[0]:
            states_start_1step[idx] = states_start[idx]
            path_costs_1step[idx] = 0.0
        self.times.record_time("first_step", time.time() - start_time)

        # random walk
        start_time = time.time()
        steps_gen_min_1: List[int] = np.maximum(np.array(steps_gen) - 1, 0).tolist()
        states_goal, path_costs = self.domain.random_walk(states_start_1step, steps_gen_min_1)
        path_costs = (np.array(path_costs_1step) + np.array(path_costs)).tolist()
        self.times.record_time("random_walk", time.time() - start_time)

        # state to goal
        start_time = time.time()
        goals: List[Goal] = self.domain.sample_goal_from_state(states_start, states_goal)
        self.times.record_time("sample_goal", time.time() - start_time)

        return self._make_instances(states_start, goals, acts_init, path_costs, inst_infos)
```
