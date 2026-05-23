---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC"
kind: "class"
name: "UpdatePolicyRLHERABC"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 159
line_end: 193
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdatePolicyRL[GoalSampleableFromState, FNsP]"
    resolved_id: null
  - name: "UpdateHER[FNsP, PathFindActsPolicy, Instance]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC.domain_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC._get_instance_data_rb"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC`

**File:** [deepxube/updaters/updater_policy_rl.py:159](../../../deepxube/updaters/updater_policy_rl.py#L159)
**Abstract:** yes

## Docstring

HER policy RL updater: failed instances get their goals relabelled. 

## Inheritance

**Direct bases:**
- `UpdatePolicyRL[GoalSampleableFromState, FNsP]`
- `UpdateHER[FNsP, PathFindActsPolicy, Instance]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `_get_instance_data_rb`

## Source

```python
class UpdatePolicyRLHERABC(UpdatePolicyRL[GoalSampleableFromState, FNsP], UpdateHER[FNsP, PathFindActsPolicy, Instance], ABC):
    """ HER policy RL updater: failed instances get their goals relabelled. """

    @staticmethod
    def domain_type() -> Type[GoalSampleableFromState]:
        """ :return: Requires ``GoalSampleableFromState`` for goal relabelling. """
        return GoalSampleableFromState

    def _get_instance_data_rb(self, instances: List[Instance], times: Times) -> List[NDArray]:
        """ Relabel goals via HER, push the relabeled batch, then sample for training. """
        # get goals according to HER
        instances, goals_inst_her = self._get_her_goals(instances, times)

        # get states and goals
        start_time = time.time()
        states_her: List[State] = []
        goals_her: List[Goal] = []
        actions_her: List[Action] = []
        for instance, goal_her in zip(instances, goals_inst_her, strict=True):
            nodes: List[Node] = [edge.node for edge in instance.get_edges_popped()]
            states_inst: List[State] = [node.state for node in nodes]
            states_her.extend(states_inst)
            goals_her.extend([goal_her] * len(states_inst))
            actions_her.extend([edge.action for edge in instance.get_edges_popped()])

        times.record_time("data_her", time.time() - start_time)

        # add to replay buffer
        self._rb_add(states_her, goals_her, actions_her, times)

        # rb q-learning update
        states, goals, actions = self._sample_rb(len(states_her), times)

        # to_np
        return self._inputs_ctgs_to_np(states, goals, actions, times)
```
