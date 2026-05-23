---
id: "class:deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev"
kind: "class"
name: "PathFindEdgeSupRWRev"
qualified_name: "deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 133
line_end: 163
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('sup_q_rw_rev')"
generic_parameters: []
bases:
  - name: "PathFindEdgeSup[GoalStartRevWalkableActsRev]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev.domain_type"
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev.make_instances_rw"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "sup_q_rw_rev"
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev`

**File:** [deepxube/pathfinding/supervised_q.py:133](../../../deepxube/pathfinding/supervised_q.py#L133)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('sup_q_rw_rev')`

## Docstring

Supervised Q pathfinder driven by reverse random walks; requires reversible actions for the initial-action label. 

## Inheritance

**Direct bases:**
- `PathFindEdgeSup[GoalStartRevWalkableActsRev]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `sup_q_rw_rev`

## Methods

- `domain_type` *(trivial, skipped)*
- `make_instances_rw`

## Source

```python
class PathFindEdgeSupRWRev(PathFindEdgeSup[GoalStartRevWalkableActsRev]):
    """ Supervised Q pathfinder driven by reverse random walks; requires reversible actions for the initial-action label. """

    @staticmethod
    def domain_type() -> Type[GoalStartRevWalkableActsRev]:
        """ :return: Requires ``GoalStartRevWalkableActsRev``. """
        return GoalStartRevWalkableActsRev

    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]:
        """ Reverse walk to a state one step from the goal, then derive the forward initial action via reversal. """
        start_time = time.time()
        states_goal, goals = self.domain.sample_goalstate_goal_pairs(len(steps_gen))
        self.times.record_time("samp_goal_state_goal", time.time() - start_time)

        start_time = time.time()
        steps_gen_min_1: List[int] = np.maximum(np.array(steps_gen) - 1, 0).tolist()
        states_start_1step, path_costs = self.domain.random_walk(states_goal, steps_gen_min_1)
        self.times.record_time("random_walk", time.time() - start_time)

        start_time = time.time()
        acts_init_rev: List[Action] = self.domain.sample_state_action(states_start_1step)
        states_start, path_costs_1step = self.domain.next_state(states_start_1step, acts_init_rev)
        acts_init: List[Action] = self.domain.rev_action(states_start, acts_init_rev)
        for idx in np.where(np.array(steps_gen) == 0)[0]:
            states_start[idx] = states_start_1step[idx]
            path_costs_1step[idx] = 0.0

        path_costs = (np.array(path_costs_1step) + np.array(path_costs)).tolist()
        self.times.record_time("first_step", time.time() - start_time)

        return self._make_instances(states_start, goals, acts_init, path_costs, inst_infos)
```
