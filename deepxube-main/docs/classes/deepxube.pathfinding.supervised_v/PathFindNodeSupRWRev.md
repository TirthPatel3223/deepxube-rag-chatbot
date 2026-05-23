---
id: "class:deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev"
kind: "class"
name: "PathFindNodeSupRWRev"
qualified_name: "deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev"
module: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_start: 115
line_end: 133
is_abstract: false
is_dataclass: false
decorators:
  - "@pathfinding_factory.register_class('sup_v_rw_rev')"
generic_parameters: []
bases:
  - name: "PathFindNodeSup[GoalStartRevWalkable]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev.domain_type"
  - "func:deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev.make_instances_rw"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.pathfinding_factory.pathfinding_factory"
    key: "sup_v_rw_rev"
docstring_source: "present"
---

# `deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev`

**File:** [deepxube/pathfinding/supervised_v.py:115](../../../deepxube/pathfinding/supervised_v.py#L115)
**Abstract:** no
**Decorators:** `@pathfinding_factory.register_class('sup_v_rw_rev')`

## Docstring

Supervised V pathfinder driven by reverse random walks from sampled (state, goal) pairs. 

## Inheritance

**Direct bases:**
- `PathFindNodeSup[GoalStartRevWalkable]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.pathfinding_factory.pathfinding_factory` under key `sup_v_rw_rev`

## Methods

- `domain_type` *(trivial, skipped)*
- `make_instances_rw`

## Source

```python
class PathFindNodeSupRWRev(PathFindNodeSup[GoalStartRevWalkable]):
    """ Supervised V pathfinder driven by reverse random walks from sampled (state, goal) pairs. """

    @staticmethod
    def domain_type() -> Type[GoalStartRevWalkable]:
        """ :return: Requires ``GoalStartRevWalkable``. """
        return GoalStartRevWalkable

    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Sample (goal-state, goal) pairs, walk backwards to derive starts. """
        start_time = time.time()
        states_goal, goals = self.domain.sample_goalstate_goal_pairs(len(steps_gen))
        self.times.record_time("samp_goal_state_goal", time.time() - start_time)

        start_time = time.time()
        states_start, path_costs = self.domain.random_walk(states_goal, steps_gen)
        self.times.record_time("random_walk", time.time() - start_time)

        return self._make_instances(states_start, goals, path_costs, inst_infos)
```
