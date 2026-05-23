---
id: "class:deepxube.updaters.updater_sup.UpdateHeurQSup"
kind: "class"
name: "UpdateHeurQSup"
qualified_name: "deepxube.updaters.updater_sup.UpdateHeurQSup"
module: "deepxube.updaters.updater_sup"
file: "deepxube/updaters/updater_sup.py"
line_start: 98
line_end: 131
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_heurq_sup')"
generic_parameters: []
bases:
  - name: "UpdateHeurQ[Domain, Any, PathFindEdgeSup]"
    resolved_id: null
  - name: "UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_sup.UpdateHeurQSup.domain_type"
  - "func:deepxube.updaters.updater_sup.UpdateHeurQSup.pathfind_type"
  - "func:deepxube.updaters.updater_sup.UpdateHeurQSup._get_instance_data_norb"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_heurq_sup"
docstring_source: "present"
---

# `deepxube.updaters.updater_sup.UpdateHeurQSup`

**File:** [deepxube/updaters/updater_sup.py:98](../../../deepxube/updaters/updater_sup.py#L98)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_heurq_sup')`

## Docstring

Supervised Q-heuristic updater: training target is the edge's
``q_val`` computed by ``PathFindEdgeSup``.

## Inheritance

**Direct bases:**
- `UpdateHeurQ[Domain, Any, PathFindEdgeSup]`
- `UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_heurq_sup`

## Methods

- `domain_type` *(trivial, skipped)*
- `pathfind_type` *(trivial, skipped)*
- `_get_instance_data_norb`

## Source

```python
class UpdateHeurQSup(UpdateHeurQ[Domain, Any, PathFindEdgeSup], UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]):
    """ Supervised Q-heuristic updater: training target is the edge's
    ``q_val`` computed by ``PathFindEdgeSup``.
    """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Accepts any ``Domain``. """
        return Domain

    @staticmethod
    def pathfind_type() -> Type[PathFindEdgeSup]:
        """ :return: Requires an edge-based supervised pathfinder. """
        return PathFindEdgeSup

    def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Convert popped edges from finished instances into training numpy
        arrays (state, goal, action, q_val) for the Q-heuristic network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here).
        :return: List of numpy arrays, last element is the Q-value target.
        """
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        states: List[State] = [edge.node.state for edge in edges_popped]
        goals: List[Goal] = [edge.node.goal for edge in edges_popped]
        actions: List[Action] = [edge.action for edge in edges_popped]

        ctgs_backup: List[float] = [edge.q_val for edge in edges_popped]
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])
        return inputs_np + [np.array(ctgs_backup)]
```
