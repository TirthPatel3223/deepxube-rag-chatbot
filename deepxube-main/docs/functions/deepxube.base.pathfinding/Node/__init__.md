---
id: "func:deepxube.base.pathfinding.Node.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.pathfinding.Node.__init__"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 34
line_end: 48
class: "Node"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "state"
    annotation: "State"
    default: null
  - name: "goal"
    annotation: "Goal"
    default: null
  - name: "path_cost"
    annotation: "float"
    default: null
  - name: "heuristic"
    annotation: "float"
    default: null
  - name: "q_values"
    annotation: "Optional[Tuple[List[Action], List[float]]]"
    default: null
  - name: "is_solved"
    annotation: "Optional[bool]"
    default: null
  - name: "parent_action"
    annotation: "Optional[Action]"
    default: null
  - name: "parent_t_cost"
    annotation: "Optional[float]"
    default: null
  - name: "parent"
    annotation: "Optional['Node']"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "dict"
    call_sites: [47]
raises: []
reads_attrs:
  - "self.act_probs"
  - "self.backup_val"
  - "self.edge_dict"
  - "self.goal"
  - "self.heuristic"
  - "self.is_solved"
  - "self.parent"
  - "self.parent_action"
  - "self.parent_t_cost"
  - "self.path_cost"
  - "self.q_values"
  - "self.state"
writes_attrs:
  - "self.act_probs"
  - "self.backup_val"
  - "self.edge_dict"
  - "self.goal"
  - "self.heuristic"
  - "self.is_solved"
  - "self.parent"
  - "self.parent_action"
  - "self.parent_t_cost"
  - "self.path_cost"
  - "self.q_values"
  - "self.state"
---

# `deepxube.base.pathfinding.Node.__init__`

**File:** [deepxube/base/pathfinding.py:34](../../../../deepxube/base/pathfinding.py#L34)
**Class:** `Node`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, state: State, goal: Goal, path_cost: float, heuristic: float, q_values: Optional[Tuple[List[Action], List[float]]], is_solved: Optional[bool], parent_action: Optional[Action], parent_t_cost: Optional[float], parent: Optional['Node'])
```

## Docstring

Snapshot one node at construction; child edges are populated later via ``add_edge``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `state` | `State` | — |
| `goal` | `Goal` | — |
| `path_cost` | `float` | — |
| `heuristic` | `float` | — |
| `q_values` | `Optional[Tuple[List[Action], List[float]]]` | — |
| `is_solved` | `Optional[bool]` | — |
| `parent_action` | `Optional[Action]` | — |
| `parent_t_cost` | `Optional[float]` | — |
| `parent` | `Optional['Node']` | — |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

### Unresolved
- `dict` (lines: 47)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.act_probs`
- `self.backup_val`
- `self.edge_dict`
- `self.goal`
- `self.heuristic`
- `self.is_solved`
- `self.parent`
- `self.parent_action`
- `self.parent_t_cost`
- `self.path_cost`
- `self.q_values`
- `self.state`

**Reads:**
- `self.act_probs`
- `self.backup_val`
- `self.edge_dict`
- `self.goal`
- `self.heuristic`
- `self.is_solved`
- `self.parent`
- `self.parent_action`
- `self.parent_t_cost`
- `self.path_cost`
- `self.q_values`
- `self.state`

## Source

```python
    def __init__(self, state: State, goal: Goal, path_cost: float, heuristic: float, q_values: Optional[Tuple[List[Action], List[float]]],
                 is_solved: Optional[bool], parent_action: Optional[Action], parent_t_cost: Optional[float], parent: Optional['Node']):
        """ Snapshot one node at construction; child edges are populated later via ``add_edge``. """
        self.state: State = state
        self.goal: Goal = goal
        self.path_cost: float = path_cost
        self.heuristic: float = heuristic
        self.q_values: Optional[Tuple[List[Action], List[float]]] = q_values
        self.act_probs: Optional[Tuple[List[Action], List[float]]] = None
        self.is_solved: Optional[bool] = is_solved
        self.parent_action: Optional[Action] = parent_action
        self.parent_t_cost: Optional[float] = parent_t_cost
        self.parent: Optional[Node] = parent
        self.edge_dict: Dict[Action, Tuple[float, Node]] = dict()
        self.backup_val: float = np.inf
```
