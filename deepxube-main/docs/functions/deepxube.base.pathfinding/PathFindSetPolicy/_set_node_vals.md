---
id: "func:deepxube.base.pathfinding.PathFindSetPolicy._set_node_vals"
kind: "method"
name: "_set_node_vals"
qualified_name: "deepxube.base.pathfinding.PathFindSetPolicy._set_node_vals"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 729
line_end: 743
class: "PathFindSetPolicy"
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
    call_sites: [731, 743]
  - target: null
    expr: "self.functions.policy_fn"
    call_sites: [734]
  - target: null
    expr: "len"
    call_sites: [736, 737, 740]
  - target: null
    expr: "zip"
    call_sites: [739]
  - target: null
    expr: "self.times.record_time"
    call_sites: [743]
raises: []
reads_attrs:
  - "self.domain"
  - "self.functions"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindSetPolicy._set_node_vals`

**File:** [deepxube/base/pathfinding.py:729](../../../../deepxube/base/pathfinding.py#L729)
**Class:** `PathFindSetPolicy`
**Visibility:** private
**Kind:** method

## Signature

```python
def _set_node_vals(self, nodes: List[Node]) -> None
```

## Docstring

Run the policy on (state, goal) pairs and stash the (actions, pdfs) on each node. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 731, 743)

### Unresolved
- `self.functions.policy_fn` (lines: 734)
- `len` (lines: 736, 737, 740)
- `zip` (lines: 739)
- `self.times.record_time` (lines: 743)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.functions`
- `self.times`

## Source

```python
    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Run the policy on (state, goal) pairs and stash the (actions, pdfs) on each node. """
        start_time = time.time()
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]
        actions_l, probs_l = self.functions.policy_fn(self.domain, states, goals)

        assert len(actions_l) == len(probs_l) == len(states) == len(goals), \
            f"{len(actions_l)}, {len(probs_l)}, {len(states)}, {len(goals)}"

        for node, actions, probs in zip(nodes, actions_l, probs_l, strict=True):
            assert len(actions) == len(probs), f"{len(actions)}, {len(probs)}"
            node.act_probs = (actions, probs)

        self.times.record_time("policy", time.time() - start_time)
```
