---
id: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._get_instance_data_rb"
kind: "method"
name: "_get_instance_data_rb"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._get_instance_data_rb"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 207
line_end: 234
class: "UpdateHeurVRLHERABC"
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
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._get_her_goals"
    expr: "self._get_her_goals"
    call_sites: [210]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [213, 221, 224, 226]
  - target: null
    expr: "zip"
    call_sites: [216]
  - target: null
    expr: "instance.get_nodes_popped"
    call_sites: [217]
  - target: null
    expr: "states_her.extend"
    call_sites: [218]
  - target: null
    expr: "goals_her.extend"
    call_sites: [219]
  - target: null
    expr: "len"
    call_sites: [219, 232]
  - target: null
    expr: "times.record_time"
    call_sites: [221, 226]
  - target: null
    expr: "self.domain.is_solved"
    call_sites: [225]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._rb_add"
    expr: "self._rb_add"
    call_sites: [229]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._sample_rb_vi_target"
    expr: "self._sample_rb_vi_target"
    call_sites: [232]
  - target: "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._inputs_ctgs_to_np"
    expr: "self._inputs_ctgs_to_np"
    call_sites: [234]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._get_instance_data_rb`

**File:** [deepxube/updaters/updater_v_rl.py:207](../../../../deepxube/updaters/updater_v_rl.py#L207)
**Class:** `UpdateHeurVRLHERABC`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_rb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]
```

## Docstring

Relabel goals via HER, push the relabeled batch, then sample and VI-target. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceNode]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `self._get_her_goals` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._get_her_goals` (lines: 210)
- `time.time` → `func:time.time` (lines: 213, 221, 224, 226)
- `self._rb_add` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._rb_add` (lines: 229)
- `self._sample_rb_vi_target` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._sample_rb_vi_target` (lines: 232)
- `self._inputs_ctgs_to_np` → `func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._inputs_ctgs_to_np` (lines: 234)

### Unresolved
- `zip` (lines: 216)
- `instance.get_nodes_popped` (lines: 217)
- `states_her.extend` (lines: 218)
- `goals_her.extend` (lines: 219)
- `len` (lines: 219, 232)
- `times.record_time` (lines: 221, 226)
- `self.domain.is_solved` (lines: 225)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def _get_instance_data_rb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]:
        """ Relabel goals via HER, push the relabeled batch, then sample and VI-target. """
        # get goals according to HER
        instances, goals_inst_her = self._get_her_goals(instances, times)

        # get states and goals
        start_time = time.time()
        states_her: List[State] = []
        goals_her: List[Goal] = []
        for instance, goal_her in zip(instances, goals_inst_her, strict=True):
            states_inst: List[State] = [node.state for node in instance.get_nodes_popped()]
            states_her.extend(states_inst)
            goals_her.extend([goal_her] * len(states_inst))

        times.record_time("data_her", time.time() - start_time)

        # is solved
        start_time = time.time()
        is_solved_l_her: List[bool] = self.domain.is_solved(states_her, goals_her)
        times.record_time("is_solved_her", time.time() - start_time)

        # add to replay buffer
        self._rb_add(states_her, goals_her, is_solved_l_her, times)

        # rb value iteration update
        states, goals, ctgs_backup = self._sample_rb_vi_target(len(states_her), times)

        return self._inputs_ctgs_to_np(states, goals, ctgs_backup, times)
```
