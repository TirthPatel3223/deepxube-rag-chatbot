---
id: "func:deepxube.base.pathfinding.PathFindSetHeurQ._set_node_vals"
kind: "method"
name: "_set_node_vals"
qualified_name: "deepxube.base.pathfinding.PathFindSetHeurQ._set_node_vals"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 769
line_end: 789
class: "PathFindSetHeurQ"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nodes"
    annotation: "List[Node]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [771, 776, 778, 789]
  - target: "func:deepxube.base.pathfinding.PathFindSetHeurQ.get_state_actions"
    expr: "self.get_state_actions"
    call_sites: [774]
  - target: null
    expr: "self.times.record_time"
    call_sites: [776, 789]
  - target: null
    expr: "self.functions.heur_fn_q"
    call_sites: [779]
  - target: null
    expr: "min"
    call_sites: [780]
  - target: null
    expr: "len"
    call_sites: [782, 783]
  - target: null
    expr: "zip"
    call_sites: [785]
raises: []
reads_attrs:
  - "self.functions"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindSetHeurQ._set_node_vals`

**File:** [deepxube/base/pathfinding.py:769](../../../../deepxube/base/pathfinding.py#L769)
**Class:** `PathFindSetHeurQ`
**Visibility:** private
**Kind:** method

## Signature

```python
def _set_node_vals(self, nodes: List[Node]) -> None
```

## Docstring

Evaluate Q on each node's (state, goal, applicable actions) and store min-Q as heuristic. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 771, 776, 778, 789)
- `self.get_state_actions` → `func:deepxube.base.pathfinding.PathFindSetHeurQ.get_state_actions` (lines: 774)

### Unresolved
- `self.times.record_time` (lines: 776, 789)
- `self.functions.heur_fn_q` (lines: 779)
- `min` (lines: 780)
- `len` (lines: 782, 783)
- `zip` (lines: 785)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.functions`
- `self.times`

## Source

```python
    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Evaluate Q on each node's (state, goal, applicable actions) and store min-Q as heuristic. """
        start_time = time.time()
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]
        actions_l: List[List[Action]] = self.get_state_actions(states, goals)

        self.times.record_time("actions", time.time() - start_time)

        start_time = time.time()
        qvals_l: List[List[float]] = self.functions.heur_fn_q(states, goals, actions_l)
        heuristics: List[float] = [min(x) for x in qvals_l]

        assert len(heuristics) == len(actions_l) == len(qvals_l) == len(states) == len(goals), \
            f"{len(heuristics)}, {len(actions_l)}, {len(qvals_l)}, {len(states)}, {len(goals)}"

        for node, heuristic, actions, qvals in zip(nodes, heuristics, actions_l, qvals_l, strict=True):
            node.heuristic = heuristic
            node.q_values = (actions, qvals)

        self.times.record_time("heur", time.time() - start_time)
```
