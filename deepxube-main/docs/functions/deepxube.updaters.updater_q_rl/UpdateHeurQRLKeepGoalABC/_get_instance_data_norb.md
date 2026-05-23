---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_norb"
kind: "method"
name: "_get_instance_data_norb"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_norb"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 143
line_end: 180
class: "UpdateHeurQRLKeepGoalABC"
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
    annotation: "List[InstanceEdge]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "edges_popped.extend"
    call_sites: [148]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [148]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [151, 163, 165, 177]
  - target: null
    expr: "edge.node.upper_bound_parent_path"
    call_sites: [157]
  - target: null
    expr: "instance.root_node.tree_backup"
    call_sites: [160]
  - target: null
    expr: "ValueError"
    call_sites: [162]
  - target: null
    expr: "times.record_time"
    call_sites: [163, 177]
  - target: null
    expr: "zip"
    call_sites: [172]
  - target: null
    expr: "node.backup_act"
    call_sites: [173]
  - target: null
    expr: "ctgs_backup.append"
    call_sites: [175]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [180]
raises:
  - exception: "ValueError"
    call_sites: [162]
reads_attrs:
  - "self.up_args"
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_norb`

**File:** [deepxube/updaters/updater_q_rl.py:143](../../../../deepxube/updaters/updater_q_rl.py#L143)
**Class:** `UpdateHeurQRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]
```

## Docstring

No-replay-buffer path: run backup, then emit training arrays from per-edge ctgs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceEdge]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `time.time` → `func:time.time` (lines: 151, 163, 165, 177)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._inputs_ctgs_to_np` (lines: 180)

### Unresolved
- `edges_popped.extend` (lines: 148)
- `instance.get_edges_popped` (lines: 148)
- `edge.node.upper_bound_parent_path` (lines: 157)
- `instance.root_node.tree_backup` (lines: 160)
- `ValueError` (lines: 162)
- `times.record_time` (lines: 163, 177)
- `zip` (lines: 172)
- `node.backup_act` (lines: 173)
- `ctgs_backup.append` (lines: 175)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 162)

## Attribute access

**Reads:**
- `self.up_args`

## Source

```python
    def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ No-replay-buffer path: run backup, then emit training arrays from per-edge ctgs. """
        # get popped edge data
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        # backup
        start_time = time.time()
        if self.up_args.backup == 1:
            if self.up_args.ub_heur_solns:
                for edge in edges_popped:
                    assert edge.node.is_solved is not None
                    if edge.node.is_solved:
                        edge.node.upper_bound_parent_path(0.0)
        elif self.up_args.backup == -1:
            for instance in instances:
                instance.root_node.tree_backup()
        else:
            raise ValueError(f"Unknown backup {self.up_args.backup}")
        times.record_time("backup", time.time() - start_time)

        start_time = time.time()
        nodes: List[Node] = [edge.node for edge in edges_popped]
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]
        actions: List[Action] = [edge.action for edge in edges_popped]

        ctgs_backup: List[float] = []
        for edge, node in zip(edges_popped, nodes):
            ctg_backup = node.backup_act(edge.action)
            node.backup_val = ctg_backup
            ctgs_backup.append(ctg_backup)

        times.record_time("get_tr_data", time.time() - start_time)

        # to_np
        return self._inputs_ctgs_to_np(states, goals, actions, ctgs_backup, times)
```
