---
id: "func:deepxube.base.pathfinding.PathFindNode.step"
kind: "method"
name: "step"
qualified_name: "deepxube.base.pathfinding.PathFindNode.step"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 439
line_end: 509
class: "PathFindNode"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "verbose"
    annotation: "bool"
    default: "False"
returns: "Tuple[List[Node], List[EdgeQ]]"
docstring_source: "present"
callees:
  - target: null
    expr: "instance.finished"
    call_sites: [441]
  - target: null
    expr: "len"
    call_sites: [442]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [447, 450, 456, 459, 468, 471, 477, 481, 484, 493, 495, 498]
  - target: null
    expr: "instance.get_nodes"
    call_sites: [448]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [449, 465]
  - target: null
    expr: "self.times.record_time"
    call_sites: [450, 459, 471, 481, 493, 498]
  - target: "func:deepxube.base.pathfinding.PathFindNode.set_is_solved"
    expr: "self.set_is_solved"
    call_sites: [453]
  - target: null
    expr: "zip"
    call_sites: [457, 479, 486, 496]
  - target: null
    expr: "instance.record_goal"
    call_sites: [458]
  - target: "func:deepxube.base.pathfinding.PathFindNode._expand"
    expr: "self._expand"
    call_sites: [462]
  - target: "func:deepxube.base.pathfinding.PathFindNode._set_node_vals"
    expr: "self._set_node_vals"
    call_sites: [465]
  - target: null
    expr: "enumerate"
    call_sites: [469]
  - target: null
    expr: "instance.filter_expanded_nodes"
    call_sites: [470]
  - target: "func:deepxube.base.pathfinding.PathFindNode._compute_costs"
    expr: "self._compute_costs"
    call_sites: [474]
  - target: null
    expr: "nodes_next_by_inst.append"
    call_sites: [480]
  - target: null
    expr: "instance.push_pop_nodes"
    call_sites: [480]
  - target: null
    expr: "edges_popped_inst.append"
    call_sites: [490]
  - target: "func:deepxube.base.pathfinding.EdgeQ"
    expr: "EdgeQ"
    call_sites: [490]
  - target: null
    expr: "instance.add_edges_popped"
    call_sites: [491]
  - target: null
    expr: "edges_next_flat.extend"
    call_sites: [492]
  - target: null
    expr: "instance.set_next_nodes"
    call_sites: [497]
  - target: "func:deepxube.base.pathfinding.PathFindNode._verbose"
    expr: "self._verbose"
    call_sites: [507]
raises: []
reads_attrs:
  - "self.instances"
  - "self.itr"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindNode.step`

**File:** [deepxube/base/pathfinding.py:439](../../../../deepxube/base/pathfinding.py#L439)
**Class:** `PathFindNode`
**Visibility:** public
**Kind:** method

## Signature

```python
def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]
```

## Docstring

Pop frontier nodes, mark goals, expand, score children, push back. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `verbose` | `bool` | `False` |

## Returns

`Tuple[List[Node], List[EdgeQ]]`

## Calls

- `time.time` → `func:time.time` (lines: 447, 450, 456, 459, 468, 471, 477, 481, 484, 493, 495, 498)
- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 449, 465)
- `self.set_is_solved` → `func:deepxube.base.pathfinding.PathFindNode.set_is_solved` (lines: 453)
- `self._expand` → `func:deepxube.base.pathfinding.PathFindNode._expand` (lines: 462)
- `self._set_node_vals` → `func:deepxube.base.pathfinding.PathFindNode._set_node_vals` (lines: 465)
- `self._compute_costs` → `func:deepxube.base.pathfinding.PathFindNode._compute_costs` (lines: 474)
- `EdgeQ` → `func:deepxube.base.pathfinding.EdgeQ` (lines: 490)
- `self._verbose` → `func:deepxube.base.pathfinding.PathFindNode._verbose` (lines: 507)

### Unresolved
- `instance.finished` (lines: 441)
- `len` (lines: 442)
- `instance.get_nodes` (lines: 448)
- `self.times.record_time` (lines: 450, 459, 471, 481, 493, 498)
- `zip` (lines: 457, 479, 486, 496)
- `instance.record_goal` (lines: 458)
- `enumerate` (lines: 469)
- `instance.filter_expanded_nodes` (lines: 470)
- `nodes_next_by_inst.append` (lines: 480)
- `instance.push_pop_nodes` (lines: 480)
- `edges_popped_inst.append` (lines: 490)
- `instance.add_edges_popped` (lines: 491)
- `edges_next_flat.extend` (lines: 492)
- `instance.set_next_nodes` (lines: 497)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.instances`
- `self.itr`
- `self.times`

## Source

```python
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
```
