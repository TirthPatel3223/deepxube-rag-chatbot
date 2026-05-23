---
id: "class:deepxube.base.pathfinding.PathFindNode"
kind: "class"
name: "PathFindNode"
qualified_name: "deepxube.base.pathfinding.PathFindNode"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 436
line_end: 578
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNs, INode]"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindNode.step"
  - "func:deepxube.base.pathfinding.PathFindNode._expand"
  - "func:deepxube.base.pathfinding.PathFindNode._compute_costs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindNode`

**File:** [deepxube/base/pathfinding.py:436](../../../deepxube/base/pathfinding.py#L436)
**Abstract:** yes

## Docstring

``PathFind`` skeleton for node-based open sets (best-first style). 

## Inheritance

**Direct bases:**
- `PathFind[D, FNs, INode]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `step`
- `_expand`
- `_compute_costs` *(trivial, skipped)*

## Source

```python
class PathFindNode(PathFind[D, FNs, INode]):
    """ ``PathFind`` skeleton for node-based open sets (best-first style). """

    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Pop frontier nodes, mark goals, expand, score children, push back. """
        instances: List[INode] = [instance for instance in self.instances if not instance.finished()]
        if len(instances) == 0:
            self.itr += 1  # TODO make more elegant
            return [], []

        # pop from open
        start_time = time.time()
        nodes_popped_by_inst: List[List[Node]] = [instance.get_nodes() for instance in instances]
        nodes_popped_flat: List[Node] = misc_utils.flatten(nodes_popped_by_inst)[0]
        self.times.record_time("pop", time.time() - start_time)

        # is solved
        self.set_is_solved(nodes_popped_flat)

        # record goal
        start_time = time.time()
        for instance, nodes in zip(instances, nodes_popped_by_inst, strict=True):
            instance.record_goal(nodes)
        self.times.record_time("goal", time.time() - start_time)

        # expand
        nodes_exp_by_inst: List[List[Node]] = self._expand(instances, nodes_popped_by_inst)

        # eval nodes
        self._set_node_vals(misc_utils.flatten(nodes_exp_by_inst)[0])

        # filter expanded nodes
        start_time = time.time()
        for inst_idx, instance in enumerate(instances):
            nodes_exp_by_inst[inst_idx] = instance.filter_expanded_nodes(nodes_exp_by_inst[inst_idx])
        self.times.record_time("filt", time.time() - start_time)

        # get costs
        costs_by_inst: List[List[float]] = self._compute_costs(instances, nodes_exp_by_inst)

        # push
        start_time = time.time()
        nodes_next_by_inst: List[List[Node]] = []
        for instance, nodes_exp, costs in zip(instances, nodes_exp_by_inst, costs_by_inst, strict=True):
            nodes_next_by_inst.append(instance.push_pop_nodes(nodes_exp, costs))
        self.times.record_time("pushpop", time.time() - start_time)

        # get next edges
        start_time = time.time()
        edges_next_flat: List[EdgeQ] = []
        for instance, nodes_next in zip(instances, nodes_next_by_inst):
            edges_popped_inst: List[EdgeQ] = []
            for node in nodes_next:
                assert (node.parent is not None) and (node.parent_action is not None) and (node.parent_t_cost is not None)
                edges_popped_inst.append(EdgeQ(node.parent, node.parent_action, node.parent_t_cost + node.heuristic))
            instance.add_edges_popped(edges_popped_inst)
            edges_next_flat.extend(edges_popped_inst)
        self.times.record_time("edges_next", time.time() - start_time)

        start_time = time.time()
        for instance, nodes_next in zip(instances, nodes_next_by_inst):
            instance.set_next_nodes(nodes_next)
        self.times.record_time("set_next", time.time() - start_time)

        # update iterations
        self.itr += 1
        for instance in instances:
            instance.itr += 1

        # verbose
        if verbose:
            self._verbose(instances, nodes_popped_by_inst)

        return nodes_popped_flat, edges_next_flat

    def _expand(self, instances: List[INode], nodes_by_inst: List[List[Node]]) -> List[List[Node]]:
        """ Expand each instance's popped nodes into child nodes (deduped via the parent's edge dict). """
        start_time = time.time()
        # flatten (for speed)
        nodes: List[Node]
        split_idxs: List[int]
        nodes, split_idxs = misc_utils.flatten(nodes_by_inst)

        if len(nodes) == 0:
            return [[]]

        # Get children of nodes
        states: List[State] = [x.state for x in nodes]
        goals: List[Goal] = [x.goal for x in nodes]

        states_c_l: List[List[State]]
        actions: List[List[Action]]
        tcs: List[List[float]]
        states_c_l, actions, tcs = self.expand_states(states, goals)

        goals_c: List[List[Goal]] = [[node.goal] * len(state_c) for node, state_c in zip(nodes, states_c_l, strict=True)]
        states_c_flat: List[State]
        states_c_flat, split_idxs_c = misc_utils.flatten(states_c_l)
        goals_c_flat, _ = misc_utils.flatten(goals_c)
        self.times.record_time("expand", time.time() - start_time)

        # get children nodes
        start_time = time.time()
        nodes_c: List[Node] = []
        for node_idx, node in enumerate(nodes):
            path_costs_c_i: NDArray = node.path_cost + np.array(tcs[node_idx])
            nodes_c_i: List[Node] = []
            for c_idx in range(len(states_c_l[node_idx])):
                action: Action = actions[node_idx][c_idx]

                edge_dict_val: Optional[Tuple[float, Node]] = node.edge_dict.get(action)
                node_c: Node
                if edge_dict_val is not None:
                    node_c = edge_dict_val[1]
                else:
                    t_cost: float = tcs[node_idx][c_idx]
                    node_c = Node(states_c_l[node_idx][c_idx], goals_c[node_idx][c_idx], float(path_costs_c_i[c_idx]), 0.0, None, None, action, t_cost, node)
                    node.add_edge(action, t_cost, node_c)

                nodes_c_i.append(node_c)
            nodes_c.extend(nodes_c_i)
        self.times.record_time("nodes", time.time() - start_time)

        # get child nodes by instance
        start_time = time.time()
        nodes_c_by_state: List[List[Node]] = misc_utils.unflatten(nodes_c, split_idxs_c)
        nodes_c_by_inst_state: List[List[List[Node]]] = misc_utils.unflatten(nodes_c_by_state, split_idxs)
        nodes_c_by_inst: List[List[Node]] = []
        for nodes_c_by_inst_state_i in nodes_c_by_inst_state:
            nodes_c_by_inst.append(misc_utils.flatten(nodes_c_by_inst_state_i)[0])

        for instance, nodes_by_inst_i, nodes_c_by_inst_i in zip(instances, nodes_by_inst, nodes_c_by_inst, strict=True):
            instance.add_nodes_popped(nodes_by_inst_i)
            instance.num_nodes_generated += len(nodes_c_by_inst_i)

        self.times.record_time("up_inst", time.time() - start_time)

        return nodes_c_by_inst

    @abstractmethod
    def _compute_costs(self, instances: List[INode], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ Subclass hook: compute open-set priority cost for each child node. """
        pass
```
