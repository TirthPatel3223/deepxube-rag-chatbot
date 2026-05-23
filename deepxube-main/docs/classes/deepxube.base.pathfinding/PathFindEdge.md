---
id: "class:deepxube.base.pathfinding.PathFindEdge"
kind: "class"
name: "PathFindEdge"
qualified_name: "deepxube.base.pathfinding.PathFindEdge"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 581
line_end: 716
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNs, IEdge]"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindEdge.step"
  - "func:deepxube.base.pathfinding.PathFindEdge.get_next_nodes"
  - "func:deepxube.base.pathfinding.PathFindEdge._get_edges"
  - "func:deepxube.base.pathfinding.PathFindEdge._compute_costs"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindEdge`

**File:** [deepxube/base/pathfinding.py:581](../../../deepxube/base/pathfinding.py#L581)
**Abstract:** yes

## Docstring

``PathFind`` skeleton for edge-based open sets (Q*-style). 

## Inheritance

**Direct bases:**
- `PathFind[D, FNs, IEdge]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `step`
- `get_next_nodes`
- `_get_edges`
- `_compute_costs` *(trivial, skipped)*

## Source

```python
class PathFindEdge(PathFind[D, FNs, IEdge]):  # TODO add nodes popped
    """ ``PathFind`` skeleton for edge-based open sets (Q*-style). """

    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Pop frontier edges, materialise their child nodes, score, push back. """
        instances: List[IEdge] = [instance for instance in self.instances if not instance.finished()]
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

        # filter popped nodes
        start_time = time.time()
        for inst_idx, instance in enumerate(instances):
            nodes_popped_by_inst[inst_idx] = instance.filter_popped_nodes(nodes_popped_by_inst[inst_idx])
        self.times.record_time("filt", time.time() - start_time)

        # expand
        edges_exp_by_inst: List[List[EdgeQ]] = self._get_edges(nodes_popped_by_inst)

        # get costs
        costs_by_inst: List[List[float]] = self._compute_costs(instances, edges_exp_by_inst)

        # push
        start_time = time.time()
        edges_next_by_inst: List[List[EdgeQ]] = []
        for instance, edges_exp, costs in zip(instances, edges_exp_by_inst, costs_by_inst, strict=True):
            edges_next_by_inst.append(instance.push_pop_edges(edges_exp, costs))
        self.times.record_time("pushpop", time.time() - start_time)

        # get next nodes
        nodes_next_by_inst: List[List[Node]] = self.get_next_nodes(instances, edges_next_by_inst)

        # eval nodes
        self._set_node_vals(misc_utils.flatten(nodes_next_by_inst)[0])

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

        return nodes_popped_flat, misc_utils.flatten(edges_next_by_inst)[0]

    def get_next_nodes(self, instances: List[IEdge], edges_by_inst: List[List[EdgeQ]]) -> List[List[Node]]:
        """ Materialise the child nodes implied by ``edges_by_inst`` (creating new nodes when not in the parent's edge_dict). """
        if len(instances) == 0:
            return []
        start_time = time.time()
        # flatten
        edges, split_idxs = misc_utils.flatten(edges_by_inst)
        nodes: List[Node] = [edge.node for edge in edges]

        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]
        path_costs: List[float] = [node.path_cost for node in nodes]
        actions: List[Action] = [edge.action for edge in edges]

        # next states
        states_next, tcs = self.domain.next_state(states, actions)
        path_costs_next: List[float] = (np.array(path_costs) + np.array(tcs)).tolist()
        self.times.record_time("next_state", time.time() - start_time)

        # next nodes
        start_time = time.time()
        nodes_next: List[Node] = []
        for idx in range(len(edges)):
            edge_dict_val: Optional[Tuple[float, Node]] = nodes[idx].edge_dict.get(actions[idx])
            node_next: Node
            if edge_dict_val is not None:
                node_next = edge_dict_val[1]
            else:
                node_next = Node(states_next[idx], goals[idx], path_costs_next[idx], 0.0, None, None, actions[idx], tcs[idx], nodes[idx])
                nodes[idx].add_edge(actions[idx], tcs[idx], node_next)
            nodes_next.append(node_next)
        self.times.record_time("nodes", time.time() - start_time)

        # update instances
        start_time = time.time()
        nodes_next_by_inst: List[List[Node]] = misc_utils.unflatten(nodes_next, split_idxs)
        for instance, edges_by_inst_i, nodes_next_by_inst_i in zip(instances, edges_by_inst, nodes_next_by_inst, strict=True):
            instance.add_edges_popped(edges_by_inst_i)
            instance.num_nodes_generated += len(nodes_next_by_inst_i)
        self.times.record_time("up_inst", time.time() - start_time)

        return nodes_next_by_inst

    def _get_edges(self, nodes_by_inst: List[List[Node]]) -> List[List[EdgeQ]]:
        """ Build per-instance edge lists from each popped node's q_values or act_probs. """
        # make edges
        start_time = time.time()
        edges_by_inst: List[List[EdgeQ]] = []

        for nodes in nodes_by_inst:
            edges: List[EdgeQ] = []
            for node in nodes:
                action_vals: Optional[Tuple[List[Action], List[float]]] = None
                if node.q_values is not None:
                    action_vals = node.q_values
                elif node.act_probs is not None:
                    action_vals = node.act_probs

                assert action_vals is not None
                for action, act_val in zip(action_vals[0], action_vals[1], strict=True):
                    edges.append(EdgeQ(node, action, act_val))
            edges_by_inst.append(edges)
        self.times.record_time("edges", time.time() - start_time)

        return edges_by_inst

    @abstractmethod
    def _compute_costs(self, instances: List[IEdge], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ Subclass hook: compute open-set priority cost for each edge. """
        pass
```
