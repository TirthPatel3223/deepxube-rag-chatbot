---
id: "class:deepxube.pathfinding.supervised_v.InstanceNodeSup"
kind: "class"
name: "InstanceNodeSup"
qualified_name: "deepxube.pathfinding.supervised_v.InstanceNodeSup"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 13
line_end: 39
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "InstanceNode"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_v.InstanceNodeSup.filter_expanded_nodes"
  - "func:deepxube.pathfinding.supervised_v.InstanceNodeSup.frontier_size"
  - "func:deepxube.pathfinding.supervised_v.InstanceNodeSup.record_goal"
  - "func:deepxube.pathfinding.supervised_v.InstanceNodeSup.push_pop_nodes"
  - "func:deepxube.pathfinding.supervised_v.InstanceNodeSup.__init__"
  - "func:deepxube.pathfinding.supervised_v.InstanceNodeSup.finished"
attributes:
  - name: "self.path_cost_sup"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_v.InstanceNodeSup`

**File:** [deepxube/pathfinding/supervised_v.py:13](../../../deepxube/pathfinding/supervised_v.py#L13)
**Abstract:** no

## Docstring

Supervised one-shot instance: just carries the random-walk target path cost. 

## Inheritance

**Direct bases:**
- `InstanceNode`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `filter_expanded_nodes` *(trivial, skipped)*
- `frontier_size` *(trivial, skipped)*
- `record_goal` *(trivial, skipped)*
- `push_pop_nodes` *(trivial, skipped)*
- `__init__` *(trivial, skipped)*
- `finished` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.path_cost_sup` | — | __init__ |

## Source

```python
class InstanceNodeSup(InstanceNode):
    """ Supervised one-shot instance: just carries the random-walk target path cost. """

    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def frontier_size(self) -> int:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def record_goal(self, nodes: List[Node]) -> None:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def __init__(self, root_node: Node, path_cost_sup: float, inst_info: Any):
        """ Initialise with the random-walk path cost as the heuristic target. """
        super().__init__(root_node, inst_info)
        self.path_cost_sup: float = path_cost_sup

    def finished(self) -> bool:
        """ :return: True after one iteration (single emission per instance). """
        return self.itr > 0
```
