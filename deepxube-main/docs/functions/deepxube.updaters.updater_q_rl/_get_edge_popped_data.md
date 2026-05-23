---
id: "func:deepxube.updaters.updater_q_rl._get_edge_popped_data"
kind: "function"
name: "_get_edge_popped_data"
qualified_name: "deepxube.updaters.updater_q_rl._get_edge_popped_data"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 29
line_end: 50
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
returns: "Tuple[List[State], List[Goal], List[bool], List[Action], List[float], List[State]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [33, 48]
  - target: null
    expr: "zip"
    call_sites: [42]
  - target: null
    expr: "is_solved_l.append"
    call_sites: [44]
  - target: null
    expr: "tcs.append"
    call_sites: [46]
  - target: null
    expr: "states_next.append"
    call_sites: [47]
  - target: null
    expr: "times.record_time"
    call_sites: [48]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl._get_edge_popped_data`

**File:** [deepxube/updaters/updater_q_rl.py:29](../../../../deepxube/updaters/updater_q_rl.py#L29)
**Visibility:** private
**Kind:** function

## Signature

```python
def _get_edge_popped_data(edges_popped: List[EdgeQ], times: Times) -> Tuple[List[State], List[Goal], List[bool], List[Action], List[float], List[State]]
```

## Docstring

Unpack popped edges into (states, goals, is_solved, actions, tcs, next_states). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `edges_popped` | `List[EdgeQ]` | — |
| `times` | `Times` | — |

## Returns

`Tuple[List[State], List[Goal], List[bool], List[Action], List[float], List[State]]`

## Calls

- `time.time` → `func:time.time` (lines: 33, 48)

### Unresolved
- `zip` (lines: 42)
- `is_solved_l.append` (lines: 44)
- `tcs.append` (lines: 46)
- `states_next.append` (lines: 47)
- `times.record_time` (lines: 48)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _get_edge_popped_data(edges_popped: List[EdgeQ],
                          times: Times) -> Tuple[List[State], List[Goal], List[bool], List[Action], List[float], List[State]]:
    """ Unpack popped edges into (states, goals, is_solved, actions, tcs, next_states). """

    start_time = time.time()
    nodes: List[Node] = [edge.node for edge in edges_popped]
    states: List[State] = [node.state for node in nodes]
    goals: List[Goal] = [node.goal for node in nodes]
    actions: List[Action] = [edge.action for edge in edges_popped]

    is_solved_l: List[bool] = []
    tcs: List[float] = []
    states_next: List[State] = []
    for edge, node in zip(edges_popped, nodes, strict=True):
        assert node.is_solved is not None
        is_solved_l.append(node.is_solved)
        tc, node_next = node.edge_dict[edge.action]
        tcs.append(tc)
        states_next.append(node_next.state)
    times.record_time("edge_data", time.time() - start_time)

    return states, goals, is_solved_l, actions, tcs, states_next
```
