---
id: "func:deepxube.base.pathfinding.PathFindNode._expand"
kind: "method"
name: "_expand"
qualified_name: "deepxube.base.pathfinding.PathFindNode._expand"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 511
line_end: 573
class: "PathFindNode"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instances"
    annotation: "List[INode]"
    default: null
  - name: "nodes_by_inst"
    annotation: "List[List[Node]]"
    default: null
returns: "List[List[Node]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [513, 535, 538, 557, 560, 571]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [517, 533, 534, 565]
  - target: null
    expr: "len"
    call_sites: [519, 531, 543, 569]
  - target: "func:deepxube.base.pathfinding.PathFindNode.expand_states"
    expr: "self.expand_states"
    call_sites: [529]
  - target: null
    expr: "zip"
    call_sites: [531, 567]
  - target: null
    expr: "self.times.record_time"
    call_sites: [535, 557, 571]
  - target: null
    expr: "enumerate"
    call_sites: [540]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [541]
  - target: null
    expr: "range"
    call_sites: [543]
  - target: null
    expr: "node.edge_dict.get"
    call_sites: [546]
  - target: "func:deepxube.base.pathfinding.Node"
    expr: "Node"
    call_sites: [552]
  - target: null
    expr: "float"
    call_sites: [552]
  - target: null
    expr: "node.add_edge"
    call_sites: [553]
  - target: null
    expr: "nodes_c_i.append"
    call_sites: [555]
  - target: null
    expr: "nodes_c.extend"
    call_sites: [556]
  - target: "func:deepxube.utils.misc_utils.unflatten"
    expr: "misc_utils.unflatten"
    call_sites: [561, 562]
  - target: null
    expr: "nodes_c_by_inst.append"
    call_sites: [565]
  - target: null
    expr: "instance.add_nodes_popped"
    call_sites: [568]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFindNode._expand`

**File:** [deepxube/base/pathfinding.py:511](../../../../deepxube/base/pathfinding.py#L511)
**Class:** `PathFindNode`
**Visibility:** private
**Kind:** method

## Signature

```python
def _expand(self, instances: List[INode], nodes_by_inst: List[List[Node]]) -> List[List[Node]]
```

## Docstring

Expand each instance's popped nodes into child nodes (deduped via the parent's edge dict). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[INode]` | — |
| `nodes_by_inst` | `List[List[Node]]` | — |

## Returns

`List[List[Node]]`

## Calls

- `time.time` → `func:time.time` (lines: 513, 535, 538, 557, 560, 571)
- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 517, 533, 534, 565)
- `self.expand_states` → `func:deepxube.base.pathfinding.PathFindNode.expand_states` (lines: 529)
- `np.array` → `func:numpy.array` (lines: 541)
- `Node` → `func:deepxube.base.pathfinding.Node` (lines: 552)
- `misc_utils.unflatten` → `func:deepxube.utils.misc_utils.unflatten` (lines: 561, 562)

### Unresolved
- `len` (lines: 519, 531, 543, 569)
- `zip` (lines: 531, 567)
- `self.times.record_time` (lines: 535, 557, 571)
- `enumerate` (lines: 540)
- `range` (lines: 543)
- `node.edge_dict.get` (lines: 546)
- `float` (lines: 552)
- `node.add_edge` (lines: 553)
- `nodes_c_i.append` (lines: 555)
- `nodes_c.extend` (lines: 556)
- `nodes_c_by_inst.append` (lines: 565)
- `instance.add_nodes_popped` (lines: 568)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
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
```
