---
id: "func:deepxube.updaters.updater_policy_rl._get_edge_popped_data"
kind: "function"
name: "_get_edge_popped_data"
qualified_name: "deepxube.updaters.updater_policy_rl._get_edge_popped_data"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 30
line_end: 40
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "edges_popped"
    annotation: "List[EdgeQ]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "Tuple[List[State], List[Goal], List[Action]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [32, 38]
  - target: null
    expr: "times.record_time"
    call_sites: [38]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl._get_edge_popped_data`

**File:** [deepxube/updaters/updater_policy_rl.py:30](../../../../deepxube/updaters/updater_policy_rl.py#L30)
**Visibility:** private
**Kind:** function

## Signature

```python
def _get_edge_popped_data(edges_popped: List[EdgeQ], times: Times) -> Tuple[List[State], List[Goal], List[Action]]
```

## Docstring

Unpack popped edges into (states, goals, actions). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `edges_popped` | `List[EdgeQ]` | — |
| `times` | `Times` | — |

## Returns

`Tuple[List[State], List[Goal], List[Action]]`

## Calls

- `time.time` → `func:time.time` (lines: 32, 38)

### Unresolved
- `times.record_time` (lines: 38)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _get_edge_popped_data(edges_popped: List[EdgeQ], times: Times) -> Tuple[List[State], List[Goal], List[Action]]:
    """ Unpack popped edges into (states, goals, actions). """
    start_time = time.time()
    nodes: List[Node] = [edge.node for edge in edges_popped]
    states: List[State] = [node.state for node in nodes]
    goals: List[Goal] = [node.goal for node in nodes]
    actions: List[Action] = [edge.action for edge in edges_popped]

    times.record_time("edge_data", time.time() - start_time)

    return states, goals, actions
```
