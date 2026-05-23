---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_norb"
kind: "method"
name: "_get_instance_data_norb"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_norb"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 148
line_end: 180
class: "UpdateHeurVRLKeepGoalABC"
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
    annotation: "List[InstanceNode]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "nodes_popped.extend"
    call_sites: [153]
  - target: null
    expr: "instance.get_nodes_popped"
    call_sites: [153]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [156, 171, 173, 178]
  - target: null
    expr: "node.bellman_backup"
    call_sites: [159]
  - target: null
    expr: "node.upper_bound_parent_path"
    call_sites: [164]
  - target: null
    expr: "instance.root_node.tree_backup"
    call_sites: [167]
  - target: null
    expr: "ValueError"
    call_sites: [169]
  - target: null
    expr: "times.record_time"
    call_sites: [171, 178]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [180]
raises:
  - exception: "ValueError"
    call_sites: [169]
reads_attrs:
  - "self.up_args"
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_norb`

**File:** [deepxube/updaters/updater_v_rl.py:148](../../../../deepxube/updaters/updater_v_rl.py#L148)
**Class:** `UpdateHeurVRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_norb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]
```

## Docstring

No-replay-buffer path: run backup (Bellman or tree), then emit training arrays. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceNode]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `time.time` → `func:time.time` (lines: 156, 171, 173, 178)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._inputs_ctgs_to_np` (lines: 180)

### Unresolved
- `nodes_popped.extend` (lines: 153)
- `instance.get_nodes_popped` (lines: 153)
- `node.bellman_backup` (lines: 159)
- `node.upper_bound_parent_path` (lines: 164)
- `instance.root_node.tree_backup` (lines: 167)
- `ValueError` (lines: 169)
- `times.record_time` (lines: 171, 178)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 169)

## Attribute access

**Reads:**
- `self.up_args`

## Source

```python
    def _get_instance_data_norb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]:
        """ No-replay-buffer path: run backup (Bellman or tree), then emit training arrays. """
        # get popped node data
        nodes_popped: List[Node] = []
        for instance in instances:
            nodes_popped.extend(instance.get_nodes_popped())

        # get backup
        start_time = time.time()
        if self.up_args.backup == 1:
            for node in nodes_popped:
                node.bellman_backup()
            if self.up_args.ub_heur_solns:
                for node in nodes_popped:
                    assert node.is_solved is not None
                    if node.is_solved:
                        node.upper_bound_parent_path(0.0)
        elif self.up_args.backup == -1:
            for instance in instances:
                instance.root_node.tree_backup()
        else:
            raise ValueError(f"Unknown backup {self.up_args.backup}")

        times.record_time("backup", time.time() - start_time)

        start_time = time.time()
        states: List[State] = [node.state for node in nodes_popped]
        goals: List[Goal] = [node.goal for node in nodes_popped]
        ctgs_backup: List[float] = [node.backup_val for node in nodes_popped]

        times.record_time("get_tr_data", time.time() - start_time)

        return self._inputs_ctgs_to_np(states, goals, ctgs_backup, times)
```
