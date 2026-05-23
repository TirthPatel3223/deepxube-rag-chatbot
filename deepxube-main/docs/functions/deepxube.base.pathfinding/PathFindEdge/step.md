---
id: "func:deepxube.base.pathfinding.PathFindEdge.step"
kind: "method"
name: "step"
qualified_name: "deepxube.base.pathfinding.PathFindEdge.step"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 584
line_end: 645
class: "PathFindEdge"
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
    call_sites: [586]
  - target: null
    expr: "len"
    call_sites: [587]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [592, 595, 601, 604, 607, 610, 619, 623, 631, 634]
  - target: null
    expr: "instance.get_nodes"
    call_sites: [593]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [594, 629, 645]
  - target: null
    expr: "self.times.record_time"
    call_sites: [595, 604, 610, 623, 634]
  - target: "func:deepxube.base.pathfinding.PathFindEdge.set_is_solved"
    expr: "self.set_is_solved"
    call_sites: [598]
  - target: null
    expr: "zip"
    call_sites: [602, 621, 632]
  - target: null
    expr: "instance.record_goal"
    call_sites: [603]
  - target: null
    expr: "enumerate"
    call_sites: [608]
  - target: null
    expr: "instance.filter_popped_nodes"
    call_sites: [609]
  - target: "func:deepxube.base.pathfinding.PathFindEdge._get_edges"
    expr: "self._get_edges"
    call_sites: [613]
  - target: "func:deepxube.base.pathfinding.PathFindEdge._compute_costs"
    expr: "self._compute_costs"
    call_sites: [616]
  - target: null
    expr: "edges_next_by_inst.append"
    call_sites: [622]
  - target: null
    expr: "instance.push_pop_edges"
    call_sites: [622]
  - target: "func:deepxube.base.pathfinding.PathFindEdge.get_next_nodes"
    expr: "self.get_next_nodes"
    call_sites: [626]
  - target: "func:deepxube.base.pathfinding.PathFindEdge._set_node_vals"
    expr: "self._set_node_vals"
    call_sites: [629]
  - target: null
    expr: "instance.set_next_nodes"
    call_sites: [633]
  - target: "func:deepxube.base.pathfinding.PathFindEdge._verbose"
    expr: "self._verbose"
    call_sites: [643]
raises: []
reads_attrs:
  - "self.instances"
  - "self.itr"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindEdge.step`

**File:** [deepxube/base/pathfinding.py:584](../../../../deepxube/base/pathfinding.py#L584)
**Class:** `PathFindEdge`
**Visibility:** public
**Kind:** method

## Signature

```python
def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]
```

## Docstring

Pop frontier edges, materialise their child nodes, score, push back. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `verbose` | `bool` | `False` |

## Returns

`Tuple[List[Node], List[EdgeQ]]`

## Calls

- `time.time` → `func:time.time` (lines: 592, 595, 601, 604, 607, 610, 619, 623, 631, 634)
- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 594, 629, 645)
- `self.set_is_solved` → `func:deepxube.base.pathfinding.PathFindEdge.set_is_solved` (lines: 598)
- `self._get_edges` → `func:deepxube.base.pathfinding.PathFindEdge._get_edges` (lines: 613)
- `self._compute_costs` → `func:deepxube.base.pathfinding.PathFindEdge._compute_costs` (lines: 616)
- `self.get_next_nodes` → `func:deepxube.base.pathfinding.PathFindEdge.get_next_nodes` (lines: 626)
- `self._set_node_vals` → `func:deepxube.base.pathfinding.PathFindEdge._set_node_vals` (lines: 629)
- `self._verbose` → `func:deepxube.base.pathfinding.PathFindEdge._verbose` (lines: 643)

### Unresolved
- `instance.finished` (lines: 586)
- `len` (lines: 587)
- `instance.get_nodes` (lines: 593)
- `self.times.record_time` (lines: 595, 604, 610, 623, 634)
- `zip` (lines: 602, 621, 632)
- `instance.record_goal` (lines: 603)
- `enumerate` (lines: 608)
- `instance.filter_popped_nodes` (lines: 609)
- `edges_next_by_inst.append` (lines: 622)
- `instance.push_pop_edges` (lines: 622)
- `instance.set_next_nodes` (lines: 633)

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
```
