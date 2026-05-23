---
id: "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC"
kind: "class"
name: "UpdateHeurQRLHERABC"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 199
line_end: 245
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeurQRL[GoalSampleableFromState, FNsHQ]"
    resolved_id: null
  - name: "UpdateHER[FNsHQ, PathFindSetHeurQ, InstanceEdge]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC.domain_type"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC._get_instance_data_rb"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC`

**File:** [deepxube/updaters/updater_q_rl.py:199](../../../deepxube/updaters/updater_q_rl.py#L199)
**Abstract:** yes

## Docstring

HER Q RL updater: failed instances get their goals relabelled. 

## Inheritance

**Direct bases:**
- `UpdateHeurQRL[GoalSampleableFromState, FNsHQ]`
- `UpdateHER[FNsHQ, PathFindSetHeurQ, InstanceEdge]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `_get_instance_data_rb`

## Source

```python
class UpdateHeurQRLHERABC(UpdateHeurQRL[GoalSampleableFromState, FNsHQ], UpdateHER[FNsHQ, PathFindSetHeurQ, InstanceEdge], ABC):
    """ HER Q RL updater: failed instances get their goals relabelled. """

    @staticmethod
    def domain_type() -> Type[GoalSampleableFromState]:
        """ :return: Requires ``GoalSampleableFromState`` for goal relabelling. """
        return GoalSampleableFromState

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
