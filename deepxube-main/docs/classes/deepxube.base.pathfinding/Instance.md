---
id: "class:deepxube.base.pathfinding.Instance"
kind: "class"
name: "Instance"
qualified_name: "deepxube.base.pathfinding.Instance"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 150
line_end: 217
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.Instance.__init__"
  - "func:deepxube.base.pathfinding.Instance.frontier_size"
  - "func:deepxube.base.pathfinding.Instance.get_nodes"
  - "func:deepxube.base.pathfinding.Instance.set_next_nodes"
  - "func:deepxube.base.pathfinding.Instance.record_goal"
  - "func:deepxube.base.pathfinding.Instance.add_nodes_popped"
  - "func:deepxube.base.pathfinding.Instance.get_nodes_popped"
  - "func:deepxube.base.pathfinding.Instance.add_edges_popped"
  - "func:deepxube.base.pathfinding.Instance.get_edges_popped"
  - "func:deepxube.base.pathfinding.Instance.has_soln"
  - "func:deepxube.base.pathfinding.Instance.path_cost"
  - "func:deepxube.base.pathfinding.Instance.finished"
attributes:
  - name: "self._edges_popped"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._nodes_curr"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._nodes_popped"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.goal_node"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.inst_info"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.itr"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_nodes_generated"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.root_node"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.Instance`

**File:** [deepxube/base/pathfinding.py:150](../../../deepxube/base/pathfinding.py#L150)
**Abstract:** yes

## Docstring

Per-problem search state shared across pathfinding iterations: root node,
current frontier, popped history, and goal pointer if found. 

## Inheritance

**Direct bases:**
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `frontier_size` *(trivial, skipped)*
- `get_nodes` *(trivial, skipped)*
- `set_next_nodes` *(trivial, skipped)*
- `record_goal` *(trivial, skipped)*
- `add_nodes_popped` *(trivial, skipped)*
- `get_nodes_popped` *(trivial, skipped)*
- `add_edges_popped` *(trivial, skipped)*
- `get_edges_popped` *(trivial, skipped)*
- `has_soln`
- `path_cost`
- `finished` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self._edges_popped` | — | __init__ |
| `self._nodes_curr` | — | __init__ |
| `self._nodes_popped` | — | __init__ |
| `self.goal_node` | — | __init__ |
| `self.inst_info` | — | __init__ |
| `self.itr` | — | __init__ |
| `self.num_nodes_generated` | — | __init__ |
| `self.root_node` | — | __init__ |

## Source

```python
class Instance(ABC):
    """ Per-problem search state shared across pathfinding iterations: root node,
    current frontier, popped history, and goal pointer if found. """

    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise an instance with a single-node frontier (the root). """
        self.root_node: Node = root_node
        self.itr: int = 0  # updater with every pathfinding iteration
        self.num_nodes_generated: int = 0
        self.inst_info: Any = inst_info
        self.goal_node: Optional[Node] = None
        self._nodes_curr: List[Node] = [self.root_node]
        self._nodes_popped: List[Node] = []
        self._edges_popped: List[EdgeQ] = []

    @abstractmethod
    def frontier_size(self) -> int:
        """ :return: Number of nodes / edges currently in the open set. """
        pass

    def get_nodes(self) -> List[Node]:
        """ :return: A copy of the current frontier nodes. """
        return self._nodes_curr.copy()

    def set_next_nodes(self, nodes_next: List[Node]) -> None:
        """ Replace the frontier with the given list. """
        self._nodes_curr = nodes_next.copy()

    @abstractmethod
    def record_goal(self, nodes: List[Node]) -> None:
        """ Subclass hook: scan ``nodes`` for one matching the goal and update ``self.goal_node``. """
        pass

    def add_nodes_popped(self, nodes_popped: List[Node]) -> None:
        """ Append nodes to the popped-history list. """
        self._nodes_popped.extend(nodes_popped)

    def get_nodes_popped(self) -> List[Node]:
        """ :return: A copy of all nodes popped during this instance's lifetime. """
        return self._nodes_popped.copy()

    def add_edges_popped(self, edges_popped: List[EdgeQ]) -> None:
        """ Append edges to the popped-history list. """
        self._edges_popped.extend(edges_popped)

    def get_edges_popped(self) -> List[EdgeQ]:
        """ :return: A copy of all edges popped during this instance's lifetime. """
        return self._edges_popped.copy()

    def has_soln(self) -> bool:
        """ :return: True if a goal-matching node has been recorded. """
        if self.goal_node is None:
            return False
        else:
            return True

    def path_cost(self) -> float:
        """ :return: Path cost of the recorded goal, or ``inf`` if none. """
        if not self.has_soln():
            return np.inf
        else:
            assert self.goal_node is not None
            return self.goal_node.path_cost

    @abstractmethod
    def finished(self) -> bool:
        """ :return: True if the instance is done (solved or otherwise terminated). """
        pass
```
