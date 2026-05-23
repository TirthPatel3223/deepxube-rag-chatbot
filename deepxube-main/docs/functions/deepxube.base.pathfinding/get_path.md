---
id: "func:deepxube.base.pathfinding.get_path"
kind: "function"
name: "get_path"
qualified_name: "deepxube.base.pathfinding.get_path"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 113
line_end: 135
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "node"
    annotation: "Node"
    default: null
returns: "Tuple[List[State], List[Action], float]"
docstring_source: "present"
callees:
  - target: null
    expr: "path.append"
    call_sites: [124, 130]
  - target: null
    expr: "actions.append"
    call_sites: [127]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.pathfinding.get_path`

**File:** [deepxube/base/pathfinding.py:113](../../../../deepxube/base/pathfinding.py#L113)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_path(node: Node) -> Tuple[List[State], List[Action], float]
```

## Docstring

Gets path from the start state to the goal state associated with the input node

:param node: goal node
:return: List of states along path, List of actions in path, path cost

## Parameters

| Name | Type | Default |
|------|------|---------|
| `node` | `Node` | — |

## Returns

`Tuple[List[State], List[Action], float]`

## Calls

*(No resolved calls.)*

### Unresolved
- `path.append` (lines: 124, 130)
- `actions.append` (lines: 127)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_path(node: Node) -> Tuple[List[State], List[Action], float]:
    """ Gets path from the start state to the goal state associated with the input node

    :param node: goal node
    :return: List of states along path, List of actions in path, path cost
    """
    path: List[State] = []
    actions: List[Action] = []

    parent_node: Node = node
    while parent_node.parent is not None:
        path.append(parent_node.state)

        assert parent_node.parent_action is not None, "parent_action should not be None"
        actions.append(parent_node.parent_action)
        parent_node = parent_node.parent

    path.append(parent_node.state)

    path = path[::-1]
    actions = actions[::-1]

    return path, actions, node.path_cost
```
