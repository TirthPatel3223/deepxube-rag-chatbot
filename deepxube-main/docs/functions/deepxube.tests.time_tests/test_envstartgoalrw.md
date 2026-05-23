---
id: "func:deepxube.tests.time_tests.test_envstartgoalrw"
kind: "function"
name: "test_envstartgoalrw"
qualified_name: "deepxube.tests.time_tests.test_envstartgoalrw"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 105
line_end: 113
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "env"
    annotation: "StartGoalWalkable"
    default: null
  - name: "num_states"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [108, 111]
  - target: null
    expr: "env.sample_start_states"
    call_sites: [109]
  - target: null
    expr: "len"
    call_sites: [112, 113]
  - target: null
    expr: "print"
    call_sites: [113]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.test_envstartgoalrw`

**File:** [deepxube/tests/time_tests.py:105](../../../../deepxube/tests/time_tests.py#L105)
**Visibility:** public
**Kind:** function

## Signature

```python
def test_envstartgoalrw(env: StartGoalWalkable, num_states: int) -> None
```

## Docstring

Time start-state sampling for domains that support random walks. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `env` | `StartGoalWalkable` | — |
| `num_states` | `int` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 108, 111)

### Unresolved
- `env.sample_start_states` (lines: 109)
- `len` (lines: 112, 113)
- `print` (lines: 113)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def test_envstartgoalrw(env: StartGoalWalkable, num_states: int) -> None:
    """ Time start-state sampling for domains that support random walks. """
    # generate start/goal states
    start_time = time.time()
    states: List[State] = env.sample_start_states(num_states)

    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Generated %i start states in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))
```
