---
id: "func:deepxube.pathfinding.graph_search.InstanceGraph.record_goal"
kind: "method"
name: "record_goal"
qualified_name: "deepxube.pathfinding.graph_search.InstanceGraph.record_goal"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 58
line_end: 65
class: "InstanceGraph"
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
  - "self.ub"
writes_attrs:
  - "self.goal_node"
  - "self.ub"
---

# `deepxube.pathfinding.graph_search.InstanceGraph.record_goal`

**File:** [deepxube/pathfinding/graph_search.py:58](../../../../deepxube/pathfinding/graph_search.py#L58)
**Class:** `InstanceGraph`
**Visibility:** public
**Kind:** method

## Signature

```python
def record_goal(self, nodes: List[Node]) -> None
```

## Docstring

Record the cheapest solved node found so far and update the upper bound. 

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
- `self.ub`

**Reads:**
- `self.goal_node`
- `self.ub`

## Source

```python
    def record_goal(self, nodes: List[Node]) -> None:
        """ Record the cheapest solved node found so far and update the upper bound. """
        # keep solved nodes for training
        for node in nodes:
            assert node.is_solved is not None
            if node.is_solved and (self.ub > node.path_cost):
                self.goal_node = node
                self.ub = node.path_cost
```
