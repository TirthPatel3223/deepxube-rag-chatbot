---
id: "class:deepxube.pathfinding.supervised_v.PathFindNodeSup"
kind: "class"
name: "PathFindNodeSup"
qualified_name: "deepxube.pathfinding.supervised_v.PathFindNodeSup"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 45
line_end: 84
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFindNode[D, Any, InstanceNodeSup]"
    resolved_id: null
  - name: "PathFindSup[D, InstanceNodeSup]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSup.step"
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSup._compute_costs"
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSup._make_instances"
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSup.__repr__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_v.PathFindNodeSup`

**File:** [deepxube/pathfinding/supervised_v.py:45](../../../deepxube/pathfinding/supervised_v.py#L45)
**Abstract:** yes

## Docstring

Abstract supervised V pathfinder: ``step`` emits the root node and finishes. 

## Inheritance

**Direct bases:**
- `PathFindNode[D, Any, InstanceNodeSup]`
- `PathFindSup[D, InstanceNodeSup]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `step`
- `_compute_costs` *(trivial, skipped)*
- `_make_instances`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class PathFindNodeSup(PathFindNode[D, Any, InstanceNodeSup], PathFindSup[D, InstanceNodeSup], ABC):
    """ Abstract supervised V pathfinder: ``step`` emits the root node and finishes. """

    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Emit each instance's root node with its supervised path cost as heuristic. """
        nodes: List[Node] = []
        for instance in self.instances:
            node_root: Node = instance.root_node
            node_root.heuristic = instance.path_cost_sup
            node_root.backup_val = instance.path_cost_sup
            nodes.append(node_root)
            instance.add_nodes_popped([node_root])
            instance.itr += 1
        start_time = time.time()
        self.set_is_solved(nodes)
        self.times.record_time("is_solved", time.time() - start_time)

        return nodes, []

    def _compute_costs(self, instances: List[InstanceNodeSup], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ Not used: supervised pathfinders skip cost computation. """
        raise NotImplementedError

    def _make_instances(self, states_start: List[State], goals: List[Goal], path_costs: List[float], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Build one ``InstanceNodeSup`` per (state, goal, target path-cost) triple. """
        nodes_root: List[Node] = self._create_root_nodes(states_start, goals, False)

        start_time = time.time()
        if inst_infos is None:
            inst_infos = [None for _ in states_start]

        instances: List[InstanceNodeSup] = []
        for node_root, path_cost, inst_info in zip(nodes_root, path_costs, inst_infos):
            instances.append(InstanceNodeSup(node_root, path_cost, inst_info))
        self.times.record_time("instances", time.time() - start_time)

        return instances

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"
```
