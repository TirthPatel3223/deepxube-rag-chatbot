---
id: "func:deepxube.tests.time_tests.test_env"
kind: "function"
name: "test_env"
qualified_name: "deepxube.tests.time_tests.test_env"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 32
line_end: 102
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "env"
    annotation: "Domain"
    default: null
  - name: "num_states"
    annotation: "int"
    default: null
  - name: "step_max"
    annotation: "int"
    default: null
returns: "Tuple[List[State], List[Goal], List[Action]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [35, 40, 46, 49, 54, 57, 62, 65, 71, 74, 80, 87, 89, 91, 93, 95, 97, 100]
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [36]
  - target: null
    expr: "env.sample_problem_instances"
    call_sites: [37]
  - target: null
    expr: "list"
    call_sites: [37]
  - target: null
    expr: "np.random.randint"
    call_sites: [37]
  - target: null
    expr: "len"
    call_sites: [38, 41, 43, 50, 51, 58, 59, 66, 67, 75, 76]
  - target: null
    expr: "print"
    call_sites: [42, 43, 51, 59, 67, 76, 79, 87, 91, 95, 100]
  - target: null
    expr: "sg_times.get_time_str"
    call_sites: [42]
  - target: null
    expr: "env.sample_state_action"
    call_sites: [47]
  - target: null
    expr: "env.next_state"
    call_sites: [55]
  - target: null
    expr: "env.is_solved"
    call_sites: [63]
  - target: null
    expr: "float"
    call_sites: [64]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [64]
  - target: null
    expr: "env.sample_next_state"
    call_sites: [72]
  - target: "func:torch.multiprocessing.get_context"
    expr: "get_context"
    call_sites: [81]
  - target: null
    expr: "ctx.Queue"
    call_sites: [82, 83]
  - target: null
    expr: "ctx.Process"
    call_sites: [84]
  - target: null
    expr: "proc.start"
    call_sites: [86]
  - target: null
    expr: "queue1.put"
    call_sites: [90, 98]
  - target: null
    expr: "queue2.get"
    call_sites: [94]
  - target: null
    expr: "proc.join"
    call_sites: [99]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.test_env`

**File:** [deepxube/tests/time_tests.py:32](../../../../deepxube/tests/time_tests.py#L32)
**Visibility:** public
**Kind:** function

## Signature

```python
def test_env(env: Domain, num_states: int, step_max: int) -> Tuple[List[State], List[Goal], List[Action]]
```

## Docstring

Time problem-instance generation, action sampling, next-state, is_solved, and IPC round-trip for ``env``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `env` | `Domain` | — |
| `num_states` | `int` | — |
| `step_max` | `int` | — |

## Returns

`Tuple[List[State], List[Goal], List[Action]]`

## Calls

- `time.time` → `func:time.time` (lines: 35, 40, 46, 49, 54, 57, 62, 65, 71, 74, 80, 87, 89, 91, 93, 95, 97, 100)
- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 36)
- `np.mean` → `func:numpy.mean` (lines: 64)
- `get_context` → `func:torch.multiprocessing.get_context` (lines: 81)

### Unresolved
- `env.sample_problem_instances` (lines: 37)
- `list` (lines: 37)
- `np.random.randint` (lines: 37)
- `len` (lines: 38, 41, 43, 50, 51, 58, 59, 66, 67, 75, 76)
- `print` (lines: 42, 43, 51, 59, 67, 76, 79, 87, 91, 95, 100)
- `sg_times.get_time_str` (lines: 42)
- `env.sample_state_action` (lines: 47)
- `env.next_state` (lines: 55)
- `env.is_solved` (lines: 63)
- `float` (lines: 64)
- `env.sample_next_state` (lines: 72)
- `ctx.Queue` (lines: 82, 83)
- `ctx.Process` (lines: 84)
- `proc.start` (lines: 86)
- `queue1.put` (lines: 90, 98)
- `queue2.get` (lines: 94)
- `proc.join` (lines: 99)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def test_env(env: Domain, num_states: int, step_max: int) -> Tuple[List[State], List[Goal], List[Action]]:
    """ Time problem-instance generation, action sampling, next-state, is_solved, and IPC round-trip for ``env``. """
    # get data
    start_time = time.time()
    sg_times: Times = Times()
    states, goals = env.sample_problem_instances(list(np.random.randint(step_max + 1, size=num_states)), times=sg_times)
    assert len(states) == len(goals), f"state({len(states)}) and goal({len(goals)}) pairs not same length"

    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print(sg_times.get_time_str(decplace=16))
    print("Generated %i start/goal states in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # get state action
    start_time = time.time()
    actions: List[Action] = env.sample_state_action(states)

    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Got %i random actions in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # next state
    start_time = time.time()
    env.next_state(states, actions)

    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Got %i next states in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # is_solved
    start_time = time.time()
    is_solved_l: List[bool] = env.is_solved(states, goals)
    per_solved: float = 100.0 * float(np.mean(is_solved_l))
    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print(f"Computed is_solved for {len(states)} states ({per_solved:.2f}% solved) in {elapsed_time} seconds "
          f"({states_per_sec:.2f}/second)")

    # next state
    start_time = time.time()
    states_next: List[State] = env.sample_next_state(states)[0]

    elapsed_time = time.time() - start_time
    states_per_sec = len(states_next) / elapsed_time
    print("Got %i random next states in %s seconds (%.2f/second)" % (len(states_next), elapsed_time, states_per_sec))

    # multiprocessing
    print("")
    start_time = time.time()
    ctx = get_context("spawn")
    queue1: Queue = ctx.Queue()
    queue2: Queue = ctx.Queue()
    proc = ctx.Process(target=data_runner, args=(queue1, queue2))
    proc.daemon = True
    proc.start()
    print("Process start time: %.2f" % (time.time() - start_time))

    start_time = time.time()
    queue1.put(env)
    print("Environment send time: %s" % (time.time() - start_time))

    start_time = time.time()
    queue2.get()
    print("Environment get time: %s" % (time.time() - start_time))

    start_time = time.time()
    queue1.put(None)
    proc.join()
    print("Process join time: %.2f" % (time.time() - start_time))

    return states, goals, actions
```
