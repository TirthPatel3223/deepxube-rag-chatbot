---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC"
kind: "class"
name: "UpdatePolicyRLKeepGoalABC"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 100
line_end: 156
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdatePolicyRL[Domain, FNsP]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC.domain_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._step_sync_main"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_norb"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC._get_instance_data_rb"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC`

**File:** [deepxube/updaters/updater_policy_rl.py:100](../../../deepxube/updaters/updater_policy_rl.py#L100)
**Abstract:** yes

## Docstring

Keep-goal (non-HER) policy RL updater: goals are preserved as sampled. 

## Inheritance

**Direct bases:**
- `UpdatePolicyRL[Domain, FNsP]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `_step_sync_main`
- `_get_instance_data_norb`
- `_get_instance_data_rb`

## Source

```python
class UpdatePolicyRLKeepGoalABC(UpdatePolicyRL[Domain, FNsP], ABC):
    """ Keep-goal (non-HER) policy RL updater: goals are preserved as sampled. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    def _step_sync_main(self, pathfind: PathFindActsPolicy, times: Times) -> List[NDArray]:
        """ Take a step, push popped edges, and return a sampled training batch. """
        # take a step
        edges_popped: List[EdgeQ] = _pathfind_step(pathfind)

        # get sync states/goals/is_solved
        states_sync, goals_sync, actions_sync = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_sync, goals_sync, actions_sync, times)

        # rb q-learning update
        states, goals, actions = self._sample_rb(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, times)

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

    def _get_instance_data_rb(self, instances: List[Instance], times: Times) -> List[NDArray]:
        """ Replay-buffer path: push popped edges, then sample a training batch. """
        # get popped edge data
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())
        states_p, goals_p, actions_p = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_p, goals_p, actions_p, times)

        # rb q-learning update
        states, goals, actions = self._sample_rb(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, times)
```
