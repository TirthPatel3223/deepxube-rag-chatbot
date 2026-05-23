---
id: "func:deepxube.updaters.updater_v_rl._get_nodes_popped_data"
kind: "function"
name: "_get_nodes_popped_data"
qualified_name: "deepxube.updaters.updater_v_rl._get_nodes_popped_data"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 31
line_end: 44
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "nodes_popped"
    annotation: "List[Node]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "Tuple[List[State], List[Goal], List[bool]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [33, 42]
  - target: null
    expr: "is_solved_l.append"
    call_sites: [40]
  - target: null
    expr: "times.record_time"
    call_sites: [42]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl._get_nodes_popped_data`

**File:** [deepxube/updaters/updater_v_rl.py:31](../../../../deepxube/updaters/updater_v_rl.py#L31)
**Visibility:** private
**Kind:** function

## Signature

```python
def _get_nodes_popped_data(nodes_popped: List[Node], times: Times) -> Tuple[List[State], List[Goal], List[bool]]
```

## Docstring

Unpack popped nodes into parallel (states, goals, is_solved) lists. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `nodes_popped` | `List[Node]` | — |
| `times` | `Times` | — |

## Returns

`Tuple[List[State], List[Goal], List[bool]]`

## Calls

- `time.time` → `func:time.time` (lines: 33, 42)

### Unresolved
- `is_solved_l.append` (lines: 40)
- `times.record_time` (lines: 42)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _get_nodes_popped_data(nodes_popped: List[Node], times: Times) -> Tuple[List[State], List[Goal], List[bool]]:
    """ Unpack popped nodes into parallel (states, goals, is_solved) lists. """
    start_time = time.time()

    states: List[State] = [node.state for node in nodes_popped]
    goals: List[Goal] = [node.goal for node in nodes_popped]
    is_solved_l: List[bool] = []
    for node in nodes_popped:
        assert node.is_solved is not None
        is_solved_l.append(node.is_solved)

    times.record_time("nodes_popped", time.time() - start_time)

    return states, goals, is_solved_l
```
