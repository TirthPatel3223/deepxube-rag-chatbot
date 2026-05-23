---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._get_instance_data_rb"
kind: "method"
name: "_get_instance_data_rb"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._get_instance_data_rb"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 207
line_end: 245
class: "UpdateHeurQRLHERABC"
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
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._get_her_goals"
    expr: "self._get_her_goals"
    call_sites: [210]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [213, 231, 234, 236]
  - target: null
    expr: "zip"
    call_sites: [219, 226]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [220, 224, 226]
  - target: null
    expr: "states_her.extend"
    call_sites: [222]
  - target: null
    expr: "goals_her.extend"
    call_sites: [223]
  - target: null
    expr: "len"
    call_sites: [223, 242]
  - target: null
    expr: "actions_her.extend"
    call_sites: [224]
  - target: null
    expr: "tcs_her.append"
    call_sites: [228]
  - target: null
    expr: "states_next_her.append"
    call_sites: [229]
  - target: null
    expr: "times.record_time"
    call_sites: [231, 236]
  - target: null
    expr: "self.domain.is_solved"
    call_sites: [235]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._rb_add"
    expr: "self._rb_add"
    call_sites: [239]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._sample_rb_qlearn_target"
    expr: "self._sample_rb_qlearn_target"
    call_sites: [242]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [245]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._get_instance_data_rb`

**File:** [deepxube/updaters/updater_q_rl.py:207](../../../../deepxube/updaters/updater_q_rl.py#L207)
**Class:** `UpdateHeurQRLHERABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_rb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]
```

## Docstring

Relabel goals via HER, push the relabeled batch, then sample and Q-target. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceEdge]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `self._get_her_goals` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._get_her_goals` (lines: 210)
- `time.time` → `func:time.time` (lines: 213, 231, 234, 236)
- `self._rb_add` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._rb_add` (lines: 239)
- `self._sample_rb_qlearn_target` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._sample_rb_qlearn_target` (lines: 242)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._inputs_ctgs_to_np` (lines: 245)

### Unresolved
- `zip` (lines: 219, 226)
- `instance.get_edges_popped` (lines: 220, 224, 226)
- `states_her.extend` (lines: 222)
- `goals_her.extend` (lines: 223)
- `len` (lines: 223, 242)
- `actions_her.extend` (lines: 224)
- `tcs_her.append` (lines: 228)
- `states_next_her.append` (lines: 229)
- `times.record_time` (lines: 231, 236)
- `self.domain.is_solved` (lines: 235)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def _get_instance_data_rb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Relabel goals via HER, push the relabeled batch, then sample and Q-target. """
        # get goals according to HER
        instances, goals_inst_her = self._get_her_goals(instances, times)

        # get states and goals
        start_time = time.time()
        states_her: List[State] = []
        goals_her: List[Goal] = []
        actions_her: List[Action] = []
        tcs_her: List[float] = []
        states_next_her: List[State] = []
        for instance, goal_her in zip(instances, goals_inst_her, strict=True):
            nodes: List[Node] = [edge.node for edge in instance.get_edges_popped()]
            states_inst: List[State] = [node.state for node in nodes]
            states_her.extend(states_inst)
            goals_her.extend([goal_her] * len(states_inst))
            actions_her.extend([edge.action for edge in instance.get_edges_popped()])

            for edge, node in zip(instance.get_edges_popped(), nodes, strict=True):
                tc, node_next = node.edge_dict[edge.action]
                tcs_her.append(tc)
                states_next_her.append(node_next.state)

        times.record_time("data_her", time.time() - start_time)

        # is solved
        start_time = time.time()
        is_solved_l_her: List[bool] = self.domain.is_solved(states_her, goals_her)
        times.record_time("is_solved_her", time.time() - start_time)

        # add to replay buffer
        self._rb_add(states_her, goals_her, is_solved_l_her, actions_her, tcs_her, states_next_her, times)

        # rb q-learning update
        states, goals, actions, ctgs_backup = self._sample_rb_qlearn_target(len(states_her), times)

        # to_np
        return self._inputs_ctgs_to_np(states, goals, actions, ctgs_backup, times)
```
