---
id: "class:deepxube.base.pathfinding.Node"
kind: "class"
name: "Node"
qualified_name: "deepxube.base.pathfinding.Node"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 26
line_end: 110
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.base.pathfinding.Node.__init__"
  - "func:deepxube.base.pathfinding.Node.add_edge"
  - "func:deepxube.base.pathfinding.Node.bellman_backup"
  - "func:deepxube.base.pathfinding.Node.upper_bound_parent_path"
  - "func:deepxube.base.pathfinding.Node.tree_backup"
  - "func:deepxube.base.pathfinding.Node.backup_act"
  - "func:deepxube.base.pathfinding.Node.get_all_descendants"
attributes:
  - name: "self.act_probs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.backup_val"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.edge_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.goal"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.heuristic"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.is_solved"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.parent"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.parent_action"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.parent_t_cost"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.path_cost"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.q_values"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.state"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.Node`

**File:** [deepxube/base/pathfinding.py:26](../../../deepxube/base/pathfinding.py#L26)
**Abstract:** no

## Docstring

Node in a per-instance search tree. Carries the (state, goal) pair, its
accumulated path cost, the heuristic / Q-values / policy probabilities, and
pointers to its parent edge and child edge map. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `add_edge` *(trivial, skipped)*
- `bellman_backup`
- `upper_bound_parent_path`
- `tree_backup`
- `backup_act`
- `get_all_descendants`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.act_probs` | — | __init__ |
| `self.backup_val` | — | __init__ |
| `self.edge_dict` | — | __init__ |
| `self.goal` | — | __init__ |
| `self.heuristic` | — | __init__ |
| `self.is_solved` | — | __init__ |
| `self.parent` | — | __init__ |
| `self.parent_action` | — | __init__ |
| `self.parent_t_cost` | — | __init__ |
| `self.path_cost` | — | __init__ |
| `self.q_values` | — | __init__ |
| `self.state` | — | __init__ |

## Source

```python
class Node:
    """ Node in a per-instance search tree. Carries the (state, goal) pair, its
    accumulated path cost, the heuristic / Q-values / policy probabilities, and
    pointers to its parent edge and child edge map. """

    __slots__ = ['state', 'goal', 'path_cost', 'heuristic', 'q_values', 'act_probs', 'is_solved', 'parent_action', 'parent_t_cost', 'parent',
                 'edge_dict', 'backup_val']

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

    def add_edge(self, action: Action, t_cost: float, node_next: "Node") -> None:
        """ Record a child node reached by ``action`` with transition cost ``t_cost``. """
        assert action not in self.edge_dict.keys()
        self.edge_dict[action] = (t_cost, node_next)

    def bellman_backup(self) -> float:
        """ Update ``backup_val`` to ``min_a (tc(a) + child.heuristic)`` (or 0 if solved). """
        assert self.is_solved is not None

        if self.is_solved:
            self.backup_val = 0.0
        else:
            if len(self.edge_dict) > 0:
                self.backup_val = min(tc + node_c.heuristic for tc, node_c in self.edge_dict.values())
        return self.backup_val

    def upper_bound_parent_path(self, ctg_ub: float) -> None:
        """ Recursively tighten ``backup_val`` to ``min(backup_val, ctg_ub + parent_tc + ...)`` up the parent chain. """
        self.backup_val = min(self.backup_val, ctg_ub)
        if self.parent is not None:
            assert self.parent_t_cost is not None
            self.parent.upper_bound_parent_path(ctg_ub + self.parent_t_cost)

    def tree_backup(self) -> float:
        """ Recursive tree backup: ``min`` over child sub-trees, leaf = ``max(heuristic, 0)``; for Limited-Horizon Bellman learning. """
        if (self.is_solved is not None) and self.is_solved:
            self.backup_val = 0.0
        else:
            if len(self.edge_dict) == 0:
                self.backup_val = max(self.heuristic, 0.0)
            else:
                self.backup_val = min(tc + node_c.tree_backup() for tc, node_c in self.edge_dict.values())

        return self.backup_val

    def backup_act(self, action: Action) -> float:
        """ :return: One-step backup target for the Q-value of ``action`` from this node. """
        assert self.is_solved is not None
        if self.is_solved:
            return 0.0
        else:
            tc, node_next = self.edge_dict[action]
            # assert node_next.q_values is not None
            if node_next.backup_val < np.inf:
                return tc + node_next.backup_val
            else:
                return tc + node_next.heuristic

    def get_all_descendants(self) -> List['Node']:
        """ Get all descendants of node (excluding self)

        :return: List of nodes that are descendants
        """
        fifo: List[Node] = [x[1] for x in self.edge_dict.values()]
        descendants: List[Node] = []
        while len(fifo) > 0:
            descendant: Node = fifo.pop(0)
            for _, descendant_c in descendant.edge_dict.values():
                fifo.append(descendant_c)
            descendants.append(descendant)
        return descendants
```
