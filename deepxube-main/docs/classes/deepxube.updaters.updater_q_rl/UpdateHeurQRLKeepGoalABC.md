---
id: "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC"
kind: "class"
name: "UpdateHeurQRLKeepGoalABC"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 119
line_end: 196
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeurQRL[Domain, FNsHQ]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC.domain_type"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._step_sync_main"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_norb"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC._get_instance_data_rb"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC`

**File:** [deepxube/updaters/updater_q_rl.py:119](../../../deepxube/updaters/updater_q_rl.py#L119)
**Abstract:** yes

## Docstring

Keep-goal (non-HER) Q RL updater: goals are preserved as sampled. 

## Inheritance

**Direct bases:**
- `UpdateHeurQRL[Domain, FNsHQ]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `_step_sync_main`
- `_get_instance_data_norb`
- `_get_instance_data_rb`

## Source

```python
class UpdateHeurQRLKeepGoalABC(UpdateHeurQRL[Domain, FNsHQ], ABC):
    """ Keep-goal (non-HER) Q RL updater: goals are preserved as sampled. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    def _step_sync_main(self, pathfind: PathFindSetHeurQ, times: Times) -> List[NDArray]:
        """ Take a step, push popped edges, and return a Q-targeted sample batch. """
        # take a step
        edges_popped: List[EdgeQ] = _pathfind_q_step(pathfind)

        # get sync states/goals/is_solved
        states_sync, goals_sync, is_solved_l_sync, actions_sync, tcs_sync, states_next_sync = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_sync, goals_sync, is_solved_l_sync, actions_sync, tcs_sync, states_next_sync, times)

        # rb q-learning update
        states, goals, actions, ctgs_backup = self._sample_rb_qlearn_target(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, ctgs_backup, times)

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

    def _get_instance_data_rb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Replay-buffer path: push popped edges, then sample and Q-target. """
        # get popped edge data
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())
        states_p, goals_p, is_solved_l_p, actions_p, tcs_p, states_next_p = _get_edge_popped_data(edges_popped, times)

        # add to replay buffer
        self._rb_add(states_p, goals_p, is_solved_l_p, actions_p, tcs_p, states_next_p, times)

        # rb q-learning update
        states, goals, actions, ctgs_backup = self._sample_rb_qlearn_target(len(edges_popped), times)

        return self._inputs_ctgs_to_np(states, goals, actions, ctgs_backup, times)
```
