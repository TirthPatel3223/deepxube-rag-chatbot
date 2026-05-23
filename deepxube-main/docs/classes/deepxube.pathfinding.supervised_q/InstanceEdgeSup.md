---
id: "class:deepxube.pathfinding.supervised_q.InstanceEdgeSup"
kind: "class"
name: "InstanceEdgeSup"
qualified_name: "deepxube.pathfinding.supervised_q.InstanceEdgeSup"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 14
line_end: 41
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "InstanceEdge"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_q.InstanceEdgeSup.filter_popped_nodes"
  - "func:deepxube.pathfinding.supervised_q.InstanceEdgeSup.push_pop_edges"
  - "func:deepxube.pathfinding.supervised_q.InstanceEdgeSup.frontier_size"
  - "func:deepxube.pathfinding.supervised_q.InstanceEdgeSup.record_goal"
  - "func:deepxube.pathfinding.supervised_q.InstanceEdgeSup.__init__"
  - "func:deepxube.pathfinding.supervised_q.InstanceEdgeSup.finished"
attributes:
  - name: "self.action"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.path_cost_sup"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_q.InstanceEdgeSup`

**File:** [deepxube/pathfinding/supervised_q.py:14](../../../deepxube/pathfinding/supervised_q.py#L14)
**Abstract:** no

## Docstring

Supervised one-shot edge instance: carries the initial action + target Q-value. 

## Inheritance

**Direct bases:**
- `InstanceEdge`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `filter_popped_nodes` *(trivial, skipped)*
- `push_pop_edges` *(trivial, skipped)*
- `frontier_size` *(trivial, skipped)*
- `record_goal` *(trivial, skipped)*
- `__init__` *(trivial, skipped)*
- `finished` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.action` | — | __init__ |
| `self.path_cost_sup` | — | __init__ |

## Source

```python
class InstanceEdgeSup(InstanceEdge):
    """ Supervised one-shot edge instance: carries the initial action + target Q-value. """

    def filter_popped_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Not used. """
        raise NotImplementedError

    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Not used. """
        raise NotImplementedError

    def frontier_size(self) -> int:
        """ Not used. """
        raise NotImplementedError

    def record_goal(self, nodes: List[Node]) -> None:
        """ Not used. """
        raise NotImplementedError

    def __init__(self, root_node: Node, action: Action, path_cost_sup: float, inst_info: Any):
        """ Initialise with the initial action and the random-walk path cost as the Q target. """
        super().__init__(root_node, inst_info)
        self.action: Action = action
        self.path_cost_sup: float = path_cost_sup

    def finished(self) -> bool:
        """ :return: True after one iteration. """
        return self.itr > 0
```
