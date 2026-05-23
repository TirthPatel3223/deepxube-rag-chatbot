---
id: "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC"
kind: "class"
name: "UpdateHeurVRLKeepGoalABC"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 124
line_end: 196
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeurVRL[Domain, FNsHV]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC.domain_type"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._step_sync_main"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_norb"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC._get_instance_data_rb"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC`

**File:** [deepxube/updaters/updater_v_rl.py:124](../../../deepxube/updaters/updater_v_rl.py#L124)
**Abstract:** yes

## Docstring

Keep-goal (non-HER) V RL updater: goals are preserved as sampled. 

## Inheritance

**Direct bases:**
- `UpdateHeurVRL[Domain, FNsHV]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `_step_sync_main`
- `_get_instance_data_norb`
- `_get_instance_data_rb`

## Source

```python
class UpdateHeurVRLKeepGoalABC(UpdateHeurVRL[Domain, FNsHV], ABC):
    """ Keep-goal (non-HER) V RL updater: goals are preserved as sampled. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain`` (no ``GoalSampleableFromState`` required). """
        return Domain

    def _step_sync_main(self, pathfind: PathFindSetHeurV, times: Times) -> List[NDArray]:
        """ Take a step, push popped nodes to the buffer, and return a VI-targeted sample batch. """
        # take a step
        nodes_popped: List[Node] = _pathfind_v_step(pathfind)

        # get sync states/goals/is_solved
        states_sync, goals_sync, is_solved_l_sync = _get_nodes_popped_data(nodes_popped, times)

        # add to replay buffer
        self._rb_add(states_sync, goals_sync, is_solved_l_sync, times)

        # rb value iteration update
        states, goals, ctgs_backup = self._sample_rb_vi_target(len(nodes_popped), times)

        return self._inputs_ctgs_to_np(states, goals, ctgs_backup, times)

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

    def _get_instance_data_rb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]:
        """ Replay-buffer path: push popped nodes, then sample and VI-target. """
        # get popped node data
        nodes_popped: List[Node] = []
        for instance in instances:
            nodes_popped.extend(instance.get_nodes_popped())
        states_popped, goals_popped, is_solved_l = _get_nodes_popped_data(nodes_popped, times)

        # add to replay buffer
        self._rb_add(states_popped, goals_popped, is_solved_l, times)

        # rb value iteration update
        states, goals, ctgs_backup = self._sample_rb_vi_target(len(nodes_popped), times)

        return self._inputs_ctgs_to_np(states, goals, ctgs_backup, times)
```
