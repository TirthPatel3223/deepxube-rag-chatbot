---
id: "func:deepxube.pathfinding.beam_search.InstanceBeam.record_goal"
kind: "method"
name: "record_goal"
qualified_name: "deepxube.pathfinding.beam_search.InstanceBeam.record_goal"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 50
line_end: 56
class: "InstanceBeam"
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
callees: []
raises: []
reads_attrs:
  - "self.goal_node"
writes_attrs:
  - "self.goal_node"
---

# `deepxube.pathfinding.beam_search.InstanceBeam.record_goal`

**File:** [deepxube/pathfinding/beam_search.py:50](../../../../deepxube/pathfinding/beam_search.py#L50)
**Class:** `InstanceBeam`
**Visibility:** public
**Kind:** method

## Signature

```python
def record_goal(self, nodes: List[Node]) -> None
```

## Docstring

Record the best (lowest-cost) solved node seen so far. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.goal_node`

**Reads:**
- `self.goal_node`

## Source

```python
    def record_goal(self, nodes: List[Node]) -> None:
        """ Record the best (lowest-cost) solved node seen so far. """
        for node in nodes:
            assert node.is_solved is not None
            if node.is_solved:
                if (self.goal_node is None) or (self.goal_node.path_cost > node.path_cost):
                    self.goal_node = node
```
