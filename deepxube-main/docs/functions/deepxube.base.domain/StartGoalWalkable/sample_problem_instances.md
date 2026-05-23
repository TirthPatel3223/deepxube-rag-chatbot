---
id: "func:deepxube.base.domain.StartGoalWalkable.sample_problem_instances"
kind: "method"
name: "sample_problem_instances"
qualified_name: "deepxube.base.domain.StartGoalWalkable.sample_problem_instances"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 415
line_end: 436
class: "StartGoalWalkable"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num_steps_l"
    annotation: "List[int]"
    default: null
  - name: "times"
    annotation: "Optional[Times]"
    default: "None"
returns: "Tuple[List[S], List[G]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [419]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [422, 424, 427, 429, 432, 434]
  - target: "func:deepxube.base.domain.StartGoalWalkable.sample_start_states"
    expr: "self.sample_start_states"
    call_sites: [423]
  - target: null
    expr: "len"
    call_sites: [423]
  - target: null
    expr: "times.record_time"
    call_sites: [424, 429, 434]
  - target: "func:deepxube.base.domain.StartGoalWalkable.random_walk"
    expr: "self.random_walk"
    call_sites: [428]
  - target: "func:deepxube.base.domain.StartGoalWalkable.sample_goal_from_state"
    expr: "self.sample_goal_from_state"
    call_sites: [433]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.StartGoalWalkable.sample_problem_instances`

**File:** [deepxube/base/domain.py:415](../../../../deepxube/base/domain.py#L415)
**Class:** `StartGoalWalkable`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_problem_instances(self, num_steps_l: List[int], times: Optional[Times] = None) -> Tuple[List[S], List[G]]
```

## Docstring

Sample start states, walk forward ``num_steps_l`` steps, then sample a goal containing the walked state. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_steps_l` | `List[int]` | — |
| `times` | `Optional[Times]` | `None` |

## Returns

`Tuple[List[S], List[G]]`

## Calls

- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 419)
- `time.time` → `func:time.time` (lines: 422, 424, 427, 429, 432, 434)
- `self.sample_start_states` → `func:deepxube.base.domain.StartGoalWalkable.sample_start_states` (lines: 423)
- `self.random_walk` → `func:deepxube.base.domain.StartGoalWalkable.random_walk` (lines: 428)
- `self.sample_goal_from_state` → `func:deepxube.base.domain.StartGoalWalkable.sample_goal_from_state` (lines: 433)

### Unresolved
- `len` (lines: 423)
- `times.record_time` (lines: 424, 429, 434)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_problem_instances(self, num_steps_l: List[int], times: Optional[Times] = None) -> Tuple[List[S], List[G]]:
        """ Sample start states, walk forward ``num_steps_l`` steps, then sample a goal containing the walked state. """
        # Initialize
        if times is None:
            times = Times()

        # Start states
        start_time = time.time()
        states_start: List[S] = self.sample_start_states(len(num_steps_l))
        times.record_time("sample_start_states", time.time() - start_time)

        # random walk
        start_time = time.time()
        states_goal: List[S] = self.random_walk(states_start, num_steps_l)[0]
        times.record_time("random_walk", time.time() - start_time)

        # state to goal
        start_time = time.time()
        goals: List[G] = self.sample_goal_from_state(states_start, states_goal)
        times.record_time("sample_goal", time.time() - start_time)

        return states_start, goals
```
