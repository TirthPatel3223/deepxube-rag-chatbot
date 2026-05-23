---
id: "func:deepxube.base.pathfinding.PathFindEdge.get_next_nodes"
kind: "method"
name: "get_next_nodes"
qualified_name: "deepxube.base.pathfinding.PathFindEdge.get_next_nodes"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 647
line_end: 688
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
  - name: "instances"
    annotation: "List[IEdge]"
    default: null
  - name: "edges_by_inst"
    annotation: "List[List[EdgeQ]]"
    default: null
returns: "List[List[Node]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [649, 669, 685]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [651, 664, 667, 678, 681, 686]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [653]
  - target: null
    expr: "self.domain.next_state"
    call_sites: [662]
  - target: null
    expr: "(np.array(path_costs) + np.array(tcs)).tolist"
    call_sites: [663]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [663]
  - target: null
    expr: "self.times.record_time"
    call_sites: [664, 678, 686]
  - target: null
    expr: "range"
    call_sites: [669]
  - target: null
    expr: "nodes[idx].edge_dict.get"
    call_sites: [670]
  - target: "func:deepxube.base.pathfinding.Node"
    expr: "Node"
    call_sites: [675]
  - target: null
    expr: "nodes[idx].add_edge"
    call_sites: [676]
  - target: null
    expr: "nodes_next.append"
    call_sites: [677]
  - target: "func:deepxube.utils.misc_utils.unflatten"
    expr: "misc_utils.unflatten"
    call_sites: [682]
  - target: null
    expr: "zip"
    call_sites: [683]
  - target: null
    expr: "instance.add_edges_popped"
    call_sites: [684]
raises: []
reads_attrs:
  - "self.domain"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindEdge.get_next_nodes`

**File:** [deepxube/base/pathfinding.py:647](../../../../deepxube/base/pathfinding.py#L647)
**Class:** `PathFindEdge`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_next_nodes(self, instances: List[IEdge], edges_by_inst: List[List[EdgeQ]]) -> List[List[Node]]
```

## Docstring

Materialise the child nodes implied by ``edges_by_inst`` (creating new nodes when not in the parent's edge_dict). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[IEdge]` | — |
| `edges_by_inst` | `List[List[EdgeQ]]` | — |

## Returns

`List[List[Node]]`

## Calls

- `time.time` → `func:time.time` (lines: 651, 664, 667, 678, 681, 686)
- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 653)
- `np.array` → `func:numpy.array` (lines: 663)
- `Node` → `func:deepxube.base.pathfinding.Node` (lines: 675)
- `misc_utils.unflatten` → `func:deepxube.utils.misc_utils.unflatten` (lines: 682)

### Unresolved
- `len` (lines: 649, 669, 685)
- `self.domain.next_state` (lines: 662)
- `(np.array(path_costs) + np.array(tcs)).tolist` (lines: 663)
- `self.times.record_time` (lines: 664, 678, 686)
- `range` (lines: 669)
- `nodes[idx].edge_dict.get` (lines: 670)
- `nodes[idx].add_edge` (lines: 676)
- `nodes_next.append` (lines: 677)
- `zip` (lines: 683)
- `instance.add_edges_popped` (lines: 684)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.times`

## Source

```python
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
```
