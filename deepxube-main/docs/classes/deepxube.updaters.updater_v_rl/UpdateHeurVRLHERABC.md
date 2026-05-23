---
id: "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC"
kind: "class"
name: "UpdateHeurVRLHERABC"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 199
line_end: 234
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeurVRL[GoalSampleableFromState, FNsHV]"
    resolved_id: null
  - name: "UpdateHER[FNsHV, PathFindSetHeurV, InstanceNode]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC.domain_type"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC._get_instance_data_rb"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC`

**File:** [deepxube/updaters/updater_v_rl.py:199](../../../deepxube/updaters/updater_v_rl.py#L199)
**Abstract:** yes

## Docstring

HER V RL updater: failed instances get their goals relabelled to a deepest reached state. 

## Inheritance

**Direct bases:**
- `UpdateHeurVRL[GoalSampleableFromState, FNsHV]`
- `UpdateHER[FNsHV, PathFindSetHeurV, InstanceNode]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `_get_instance_data_rb`

## Source

```python
class UpdateHeurVRLHERABC(UpdateHeurVRL[GoalSampleableFromState, FNsHV], UpdateHER[FNsHV, PathFindSetHeurV, InstanceNode], ABC):
    """ HER V RL updater: failed instances get their goals relabelled to a deepest reached state. """

    @staticmethod
    def domain_type() -> Type[GoalSampleableFromState]:
        """ :return: Requires a domain that supports ``sample_goal_from_state``. """
        return GoalSampleableFromState

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
