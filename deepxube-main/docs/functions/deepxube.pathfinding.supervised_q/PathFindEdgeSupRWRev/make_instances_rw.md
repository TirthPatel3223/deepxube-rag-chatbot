---
id: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev.make_instances_rw"
kind: "method"
name: "make_instances_rw"
qualified_name: "deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev.make_instances_rw"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 141
line_end: 163
class: "PathFindEdgeSupRWRev"
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
    call_sites: [143, 145, 147, 150, 152, 161]
  - target: null
    expr: "self.domain.sample_goalstate_goal_pairs"
    call_sites: [144]
  - target: null
    expr: "len"
    call_sites: [144]
  - target: null
    expr: "self.times.record_time"
    call_sites: [145, 150, 161]
  - target: null
    expr: "np.maximum(np.array(steps_gen) - 1, 0).tolist"
    call_sites: [148]
  - target: "func:numpy.maximum"
    expr: "np.maximum"
    call_sites: [148]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [148, 156, 160]
  - target: null
    expr: "self.domain.random_walk"
    call_sites: [149]
  - target: null
    expr: "self.domain.sample_state_action"
    call_sites: [153]
  - target: null
    expr: "self.domain.next_state"
    call_sites: [154]
  - target: null
    expr: "self.domain.rev_action"
    call_sites: [155]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [156]
  - target: null
    expr: "(np.array(path_costs_1step) + np.array(path_costs)).tolist"
    call_sites: [160]
  - target: "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev._make_instances"
    expr: "self._make_instances"
    call_sites: [163]
raises: []
reads_attrs:
  - "self.domain"
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev.make_instances_rw`

**File:** [deepxube/pathfinding/supervised_q.py:141](../../../../deepxube/pathfinding/supervised_q.py#L141)
**Class:** `PathFindEdgeSupRWRev`
**Visibility:** public
**Kind:** method

## Signature

```python
def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]
```

## Docstring

Reverse walk to a state one step from the goal, then derive the forward initial action via reversal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `steps_gen` | `List[int]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |

## Returns

`List[InstanceEdgeSup]`

## Calls

- `time.time` → `func:time.time` (lines: 143, 145, 147, 150, 152, 161)
- `np.maximum` → `func:numpy.maximum` (lines: 148)
- `np.array` → `func:numpy.array` (lines: 148, 156, 160)
- `np.where` → `func:numpy.where` (lines: 156)
- `self._make_instances` → `func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev._make_instances` (lines: 163)

### Unresolved
- `self.domain.sample_goalstate_goal_pairs` (lines: 144)
- `len` (lines: 144)
- `self.times.record_time` (lines: 145, 150, 161)
- `np.maximum(np.array(steps_gen) - 1, 0).tolist` (lines: 148)
- `self.domain.random_walk` (lines: 149)
- `self.domain.sample_state_action` (lines: 153)
- `self.domain.next_state` (lines: 154)
- `self.domain.rev_action` (lines: 155)
- `(np.array(path_costs_1step) + np.array(path_costs)).tolist` (lines: 160)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.times`

## Source

```python
    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]:
        """ Reverse walk to a state one step from the goal, then derive the forward initial action via reversal. """
        start_time = time.time()
        states_goal, goals = self.domain.sample_goalstate_goal_pairs(len(steps_gen))
        self.times.record_time("samp_goal_state_goal", time.time() - start_time)

        start_time = time.time()
        steps_gen_min_1: List[int] = np.maximum(np.array(steps_gen) - 1, 0).tolist()
        states_start_1step, path_costs = self.domain.random_walk(states_goal, steps_gen_min_1)
        self.times.record_time("random_walk", time.time() - start_time)

        start_time = time.time()
        acts_init_rev: List[Action] = self.domain.sample_state_action(states_start_1step)
        states_start, path_costs_1step = self.domain.next_state(states_start_1step, acts_init_rev)
        acts_init: List[Action] = self.domain.rev_action(states_start, acts_init_rev)
        for idx in np.where(np.array(steps_gen) == 0)[0]:
            states_start[idx] = states_start_1step[idx]
            path_costs_1step[idx] = 0.0

        path_costs = (np.array(path_costs_1step) + np.array(path_costs)).tolist()
        self.times.record_time("first_step", time.time() - start_time)

        return self._make_instances(states_start, goals, acts_init, path_costs, inst_infos)
```
