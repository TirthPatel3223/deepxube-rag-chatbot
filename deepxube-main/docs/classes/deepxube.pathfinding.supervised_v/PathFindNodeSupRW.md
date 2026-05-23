---
id: "class:deepxube.pathfinding.supervised_v.PathFindNodeSupRW"
kind: "class"
name: "PathFindNodeSupRW"
qualified_name: "deepxube.pathfinding.supervised_v.PathFindNodeSupRW"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 88
line_end: 111
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('sup_v_rw')"
generic_parameters: []
bases:
  - name: "PathFindNodeSup[StartGoalWalkable]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRW.domain_type"
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRW.make_instances_rw"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "sup_v_rw"
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_v.PathFindNodeSupRW`

**File:** [deepxube/pathfinding/supervised_v.py:88](../../../deepxube/pathfinding/supervised_v.py#L88)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('sup_v_rw')`

## Docstring

Supervised V pathfinder driven by forward random walks from sampled start states. 

## Inheritance

**Direct bases:**
- `PathFindNodeSup[StartGoalWalkable]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `sup_v_rw`

## Methods

- `domain_type` *(trivial, skipped)*
- `make_instances_rw`

## Source

```python
class PathFindNodeSupRW(PathFindNodeSup[StartGoalWalkable]):
    """ Supervised V pathfinder driven by forward random walks from sampled start states. """

    @staticmethod
    def domain_type() -> Type[StartGoalWalkable]:
        """ :return: Requires ``StartGoalWalkable``. """
        return StartGoalWalkable

    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Sample start states, walk forward, derive goals from the walked states. """
        start_time = time.time()
        states_start: List[State] = self.domain.sample_start_states(len(steps_gen))
        self.times.record_time("get_start_states", time.time() - start_time)

        start_time = time.time()
        states_goal, path_costs = self.domain.random_walk(states_start, steps_gen)
        self.times.record_time("random_walk", time.time() - start_time)

        # state to goal
        start_time = time.time()
        goals: List[Goal] = self.domain.sample_goal_from_state(states_start, states_goal)
        self.times.record_time("sample_goal", time.time() - start_time)

        return self._make_instances(states_start, goals, path_costs, inst_infos)
```
