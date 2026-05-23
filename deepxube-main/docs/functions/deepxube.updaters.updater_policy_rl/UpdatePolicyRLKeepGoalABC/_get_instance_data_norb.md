---
id: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_norb"
kind: "method"
name: "_get_instance_data_norb"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_norb"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 124
line_end: 140
class: "UpdatePolicyRLKeepGoalABC"
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
    annotation: "List[Instance]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "edges_popped.extend"
    call_sites: [129]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [129]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [131, 137]
  - target: null
    expr: "times.record_time"
    call_sites: [137]
  - target: "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [140]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_norb`

**File:** [deepxube/updaters/updater_policy_rl.py:124](../../../../deepxube/updaters/updater_policy_rl.py#L124)
**Class:** `UpdatePolicyRLKeepGoalABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_norb(self, instances: List[Instance], times: Times) -> List[NDArray]
```

## Docstring

No-replay-buffer path: pack popped edges straight into training arrays. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[Instance]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `time.time` → `func:time.time` (lines: 131, 137)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._inputs_ctgs_to_np` (lines: 140)

### Unresolved
- `edges_popped.extend` (lines: 129)
- `instance.get_edges_popped` (lines: 129)
- `times.record_time` (lines: 137)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_norb(self, instances: List[Instance], times: Times) -> List[NDArray]:
        """ No-replay-buffer path: pack popped edges straight into training arrays. """
        # get popped edge data
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        start_time = time.time()
        nodes: List[Node] = [edge.node for edge in edges_popped]
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]
        actions: List[Action] = [edge.action for edge in edges_popped]

        times.record_time("get_tr_data", time.time() - start_time)

        # to_np
        return self._inputs_ctgs_to_np(states, goals, actions, times)
```
