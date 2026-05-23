---
id: "class:deepxube.base.updater.UpdateHER"
kind: "class"
name: "UpdateHER"
qualified_name: "deepxube.base.updater.UpdateHER"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 520
line_end: 582
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Update[GoalSampleableFromState, FNs, P, Inst]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateHER._step_sync_main"
  - "func:deepxube.base.updater.UpdateHER._get_instance_data_norb"
  - "func:deepxube.base.updater.UpdateHER._get_her_goals"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateHER`

**File:** [deepxube/base/updater.py:520](../../../deepxube/base/updater.py#L520)
**Abstract:** yes

## Docstring

Mixin for updaters that perform Hindsight Experience Replay: failed
instances have their goals relabelled to an actually-reached state. 

## Inheritance

**Direct bases:**
- `Update[GoalSampleableFromState, FNs, P, Inst]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_step_sync_main` *(trivial, skipped)*
- `_get_instance_data_norb` *(trivial, skipped)*
- `_get_her_goals`

## Source

```python
class UpdateHER(Update[GoalSampleableFromState, FNs, P, Inst], ABC):
    """ Mixin for updaters that perform Hindsight Experience Replay: failed
    instances have their goals relabelled to an actually-reached state. """

    def _step_sync_main(self, pathfind: P, times: Times) -> List[NDArray]:
        """ Not supported: HER requires post-search goal relabelling. """
        raise NotImplementedError("Cannot train with sync_main if also doing hindsight experience replay (HER) since goal relabeling is done after search is "
                                  "complete.")

    def _get_instance_data_norb(self, instances: List[Inst], times: Times) -> List[NDArray]:
        """ Not supported: HER requires a replay buffer. """
        raise NotImplementedError("Must use replay buffer if doing HER.")

    def _get_her_goals(self, instances: List[Inst], times: Times) -> Tuple[List[Inst], List[Goal]]:
        """ If instance is not finisheed and solved, get deepest states out all nodes that have children + root node for relabeled goal.
            :return: Instances and their corresponding goals (order of instances changes)
        """
        # get states/goals or mark for goal relabelling
        instances_goalkeep: List[Inst] = []
        instances_relabel: List[Inst] = []

        rand_keeps: List[float] = cast(List[float], np.random.uniform(0, 1, size=len(instances)).tolist())
        for instance, rand_keep in zip(instances, rand_keeps):
            if instance.finished() and instance.has_soln():
                instances_goalkeep.append(instance)
            else:
                instances_relabel.append(instance)

        # get goals goalkeep
        goals_goalkeep: List[Goal] = [instance.root_node.goal for instance in instances_goalkeep]

        # get relabeled goals
        goals_relabel: List[Goal] = []
        if len(instances_relabel) > 0:
            # get start states and deepest states
            start_time = time.time()
            states_start: List[State] = []
            states_deepest: List[State] = []
            for instance in instances_relabel:
                states_start.append(instance.root_node.state)

                # get all descendants that have children
                nodes_desc: List[Node] = instance.root_node.get_all_descendants()
                node_desc_w_children: List[Node] = [node_desc for node_desc in nodes_desc if len(node_desc.edge_dict) > 0]

                # get state of deepest node
                state_deepest: State = instance.root_node.state
                deepest_depth: int = 0
                for node in node_desc_w_children:
                    depth: int = len(get_path(node)[0])
                    if depth > deepest_depth:
                        deepest_depth = depth
                        state_deepest = node.state
                states_deepest.append(state_deepest)

            times.record_time("her_node_deepest", time.time() - start_time)

            # relabel
            start_time = time.time()
            goals_relabel = self.domain.sample_goal_from_state(states_start, states_deepest)
            times.record_time("her_relabel", time.time() - start_time)

        return instances_goalkeep + instances_relabel, goals_goalkeep + goals_relabel
```
