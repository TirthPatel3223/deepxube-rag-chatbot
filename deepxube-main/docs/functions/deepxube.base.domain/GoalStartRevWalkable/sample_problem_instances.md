---
id: "func:deepxube.base.domain.GoalStartRevWalkable.sample_problem_instances"
kind: "method"
name: "sample_problem_instances"
qualified_name: "deepxube.base.domain.GoalStartRevWalkable.sample_problem_instances"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 443
line_end: 459
class: "GoalStartRevWalkable"
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
    call_sites: [447]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [450, 452, 455, 457]
  - target: "func:deepxube.base.domain.GoalStartRevWalkable.sample_goalstate_goal_pairs"
    expr: "self.sample_goalstate_goal_pairs"
    call_sites: [451]
  - target: null
    expr: "len"
    call_sites: [451]
  - target: null
    expr: "times.record_time"
    call_sites: [452, 457]
  - target: "func:deepxube.base.domain.GoalStartRevWalkable.random_walk_rev"
    expr: "self.random_walk_rev"
    call_sites: [456]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.GoalStartRevWalkable.sample_problem_instances`

**File:** [deepxube/base/domain.py:443](../../../../deepxube/base/domain.py#L443)
**Class:** `GoalStartRevWalkable`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_problem_instances(self, num_steps_l: List[int], times: Optional[Times] = None) -> Tuple[List[S], List[G]]
```

## Docstring

Sample (goal-state, goal) pairs, then reverse-walk to derive starts. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_steps_l` | `List[int]` | — |
| `times` | `Optional[Times]` | `None` |

## Returns

`Tuple[List[S], List[G]]`

## Calls

- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 447)
- `time.time` → `func:time.time` (lines: 450, 452, 455, 457)
- `self.sample_goalstate_goal_pairs` → `func:deepxube.base.domain.GoalStartRevWalkable.sample_goalstate_goal_pairs` (lines: 451)
- `self.random_walk_rev` → `func:deepxube.base.domain.GoalStartRevWalkable.random_walk_rev` (lines: 456)

### Unresolved
- `len` (lines: 451)
- `times.record_time` (lines: 452, 457)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_problem_instances(self, num_steps_l: List[int], times: Optional[Times] = None) -> Tuple[List[S], List[G]]:
        """ Sample (goal-state, goal) pairs, then reverse-walk to derive starts. """
        # Initialize
        if times is None:
            times = Times()

        # goals
        start_time = time.time()
        states_goal, goals = self.sample_goalstate_goal_pairs(len(num_steps_l))
        times.record_time("sample_goalstate_goal_pairs", time.time() - start_time)

        # random walk to get start states
        start_time = time.time()
        states_start: List[S] = self.random_walk_rev(states_goal, num_steps_l)
        times.record_time("random_walk", time.time() - start_time)

        return states_start, goals
```
