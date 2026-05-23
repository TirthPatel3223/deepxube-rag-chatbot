---
id: "func:deepxube.base.pathfinding.PathFind.set_is_solved"
kind: "method"
name: "set_is_solved"
qualified_name: "deepxube.base.pathfinding.PathFind.set_is_solved"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 347
line_end: 360
class: "PathFind"
visibility: "public"
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
    call_sites: [349, 360]
  - target: null
    expr: "states.append"
    call_sites: [353]
  - target: null
    expr: "goals.append"
    call_sites: [354]
  - target: null
    expr: "self.domain.is_solved"
    call_sites: [356]
  - target: null
    expr: "zip"
    call_sites: [357]
  - target: null
    expr: "self.times.record_time"
    call_sites: [360]
raises: []
reads_attrs:
  - "self.domain"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFind.set_is_solved`

**File:** [deepxube/base/pathfinding.py:347](../../../../deepxube/base/pathfinding.py#L347)
**Class:** `PathFind`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_is_solved(self, nodes: List[Node]) -> None
```

## Docstring

Populate ``node.is_solved`` for each node by querying the domain. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 349, 360)

### Unresolved
- `states.append` (lines: 353)
- `goals.append` (lines: 354)
- `self.domain.is_solved` (lines: 356)
- `zip` (lines: 357)
- `self.times.record_time` (lines: 360)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.times`

## Source

```python
    def set_is_solved(self, nodes: List[Node]) -> None:
        """ Populate ``node.is_solved`` for each node by querying the domain. """
        start_time = time.time()
        states: List[State] = []
        goals: List[Goal] = []
        for node in nodes:
            states.append(node.state)
            goals.append(node.goal)

        is_solved_l: List[bool] = self.domain.is_solved(states, goals)
        for node, is_solved in zip(nodes, is_solved_l, strict=True):
            node.is_solved = is_solved

        self.times.record_time("is_solved", time.time() - start_time)
```
