---
id: "class:deepxube.pathfinding.supervised_q.PathFindEdgeSup"
kind: "class"
name: "PathFindEdgeSup"
qualified_name: "deepxube.pathfinding.supervised_q.PathFindEdgeSup"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 47
line_end: 89
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFindEdge[D, Any, InstanceEdgeSup]"
    resolved_id: null
  - name: "PathFindSup[D, InstanceEdgeSup]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup.step"
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup._compute_costs"
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup._make_instances"
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSup.__repr__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_q.PathFindEdgeSup`

**File:** [deepxube/pathfinding/supervised_q.py:47](../../../deepxube/pathfinding/supervised_q.py#L47)
**Abstract:** yes

## Docstring

Abstract supervised Q pathfinder: ``step`` emits a single (root, action, q_target) edge per instance. 

## Inheritance

**Direct bases:**
- `PathFindEdge[D, Any, InstanceEdgeSup]`
- `PathFindSup[D, InstanceEdgeSup]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `step`
- `_compute_costs` *(trivial, skipped)*
- `_make_instances`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class PathFindEdgeSup(PathFindEdge[D, Any, InstanceEdgeSup], PathFindSup[D, InstanceEdgeSup], ABC):
    """ Abstract supervised Q pathfinder: ``step`` emits a single (root, action, q_target) edge per instance. """

    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Emit each instance's initial edge with its supervised path cost as Q-value. """
        edges: List[EdgeQ] = []
        for instance in self.instances:
            node_root: Node = instance.root_node
            edge: EdgeQ = EdgeQ(node_root, instance.action, instance.path_cost_sup)
            edges.append(edge)
            node_root.backup_val = instance.path_cost_sup
            instance.itr += 1
            instance.add_edges_popped([edge])
        start_time = time.time()
        self.set_is_solved([edge.node for edge in edges])
        self.times.record_time("is_solved", time.time() - start_time)

        return [], edges

    def _compute_costs(self, instances: List[InstanceEdgeSup], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ Not used: supervised pathfinders skip cost computation. """
        raise NotImplementedError

    def _make_instances(self, states_start: List[State], goals: List[Goal], acts_init: List[Action], path_costs: List[float],
                        inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]:
        """ Build one ``InstanceEdgeSup`` per (state, goal, action, target path-cost) tuple. """
        # make root nodes
        nodes_root: List[Node] = self._create_root_nodes(states_start, goals, False)

        # make instances
        start_time = time.time()
        if inst_infos is None:
            inst_infos = [None for _ in states_start]

        instances: List[InstanceEdgeSup] = []
        for node_root, act_init, path_cost, inst_info in zip(nodes_root, acts_init, path_costs, inst_infos):
            instances.append(InstanceEdgeSup(node_root, act_init, path_cost, inst_info))
        self.times.record_time("instances", time.time() - start_time)

        return instances

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"
```
