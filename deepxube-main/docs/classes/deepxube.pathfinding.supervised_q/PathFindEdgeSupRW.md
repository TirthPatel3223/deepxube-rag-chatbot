---
id: "class:deepxube.pathfinding.supervised_q.PathFindEdgeSupRW"
kind: "class"
name: "PathFindEdgeSupRW"
qualified_name: "deepxube.pathfinding.supervised_q.PathFindEdgeSupRW"
module: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_start: 93
line_end: 129
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('sup_q_rw')"
generic_parameters: []
bases:
  - name: "PathFindEdgeSup[StartGoalWalkable]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRW.domain_type"
  - "func:deepxube.pathfinding.supervised_q.PathFindEdgeSupRW.make_instances_rw"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "sup_q_rw"
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_q.PathFindEdgeSupRW`

**File:** [deepxube/pathfinding/supervised_q.py:93](../../../deepxube/pathfinding/supervised_q.py#L93)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('sup_q_rw')`

## Docstring

Supervised Q pathfinder driven by forward random walks. 

## Inheritance

**Direct bases:**
- `PathFindEdgeSup[StartGoalWalkable]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `sup_q_rw`

## Methods

- `domain_type` *(trivial, skipped)*
- `make_instances_rw`

## Source

```python
class PathFindEdgeSupRW(PathFindEdgeSup[StartGoalWalkable]):
    """ Supervised Q pathfinder driven by forward random walks. """

    @staticmethod
    def domain_type() -> Type[StartGoalWalkable]:
        """ :return: Requires ``StartGoalWalkable``. """
        return StartGoalWalkable

    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceEdgeSup]:
        """ Sample start states, take one labelled action, walk to goal, derive goal. """
        # start states
        start_time = time.time()
        states_start: List[State] = self.domain.sample_start_states(len(steps_gen))
        self.times.record_time("get_start_states", time.time() - start_time)

        # first step
        start_time = time.time()
        acts_init: List[Action] = self.domain.sample_state_action(states_start)
        states_start_1step, path_costs_1step = self.domain.next_state(states_start, acts_init)
        for idx in np.where(np.array(steps_gen) == 0)[0]:
            states_start_1step[idx] = states_start[idx]
            path_costs_1step[idx] = 0.0
        self.times.record_time("first_step", time.time() - start_time)

        # random walk
        start_time = time.time()
        steps_gen_min_1: List[int] = np.maximum(np.array(steps_gen) - 1, 0).tolist()
        states_goal, path_costs = self.domain.random_walk(states_start_1step, steps_gen_min_1)
        path_costs = (np.array(path_costs_1step) + np.array(path_costs)).tolist()
        self.times.record_time("random_walk", time.time() - start_time)

        # state to goal
        start_time = time.time()
        goals: List[Goal] = self.domain.sample_goal_from_state(states_start, states_goal)
        self.times.record_time("sample_goal", time.time() - start_time)

        return self._make_instances(states_start, goals, acts_init, path_costs, inst_infos)
```
