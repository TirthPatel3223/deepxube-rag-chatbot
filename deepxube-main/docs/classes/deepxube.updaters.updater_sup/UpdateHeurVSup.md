---
id: "class:deepxube.updaters.updater_sup.UpdateHeurVSup"
kind: "class"
name: "UpdateHeurVSup"
qualified_name: "deepxube.updaters.updater_sup.UpdateHeurVSup"
module: "deepxube.updaters.updater_sup"
file: "deepxube/updaters/updater_sup.py"
line_start: 62
line_end: 94
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_heurv_sup')"
generic_parameters: []
bases:
  - name: "UpdateHeurV[Domain, Any, PathFindNodeSup]"
    resolved_id: null
  - name: "UpdateSup[Domain, PathFindNodeSup, InstanceNode]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_sup.UpdateHeurVSup.domain_type"
  - "func:deepxube.updaters.updater_sup.UpdateHeurVSup.pathfind_type"
  - "func:deepxube.updaters.updater_sup.UpdateHeurVSup._get_instance_data_norb"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_heurv_sup"
docstring_source: "present"
---

# `deepxube.updaters.updater_sup.UpdateHeurVSup`

**File:** [deepxube/updaters/updater_sup.py:62](../../../deepxube/updaters/updater_sup.py#L62)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_heurv_sup')`

## Docstring

Supervised V-heuristic updater: training target is the node's
``heuristic`` cost-to-go computed by ``PathFindNodeSup``.

## Inheritance

**Direct bases:**
- `UpdateHeurV[Domain, Any, PathFindNodeSup]`
- `UpdateSup[Domain, PathFindNodeSup, InstanceNode]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_heurv_sup`

## Methods

- `domain_type` *(trivial, skipped)*
- `pathfind_type` *(trivial, skipped)*
- `_get_instance_data_norb`

## Source

```python
class UpdateHeurVSup(UpdateHeurV[Domain, Any, PathFindNodeSup], UpdateSup[Domain, PathFindNodeSup, InstanceNode]):
    """ Supervised V-heuristic updater: training target is the node's
    ``heuristic`` cost-to-go computed by ``PathFindNodeSup``.
    """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Accepts any ``Domain``. """
        return Domain

    @staticmethod
    def pathfind_type() -> Type[PathFindNodeSup]:
        """ :return: Requires a node-based supervised pathfinder. """
        return PathFindNodeSup

    def _get_instance_data_norb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]:
        """ Convert popped nodes from finished instances into training numpy
        arrays (state, goal, ctg) for the V-heuristic network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here).
        :return: List of numpy arrays, last element is the cost-to-go target.
        """
        nodes_popped: List[Node] = []
        for instance in instances:
            nodes_popped.extend(instance.get_nodes_popped())

        states: List[State] = [node.state for node in nodes_popped]
        goals: List[Goal] = [node.goal for node in nodes_popped]

        ctgs_backup: List[float] = [node.heuristic for node in nodes_popped]
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals)
        return inputs_np + [np.array(ctgs_backup)]
```
