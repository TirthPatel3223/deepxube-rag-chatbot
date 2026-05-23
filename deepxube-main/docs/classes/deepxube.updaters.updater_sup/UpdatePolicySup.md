---
id: "class:deepxube.updaters.updater_sup.UpdatePolicySup"
kind: "class"
name: "UpdatePolicySup"
qualified_name: "deepxube.updaters.updater_sup.UpdatePolicySup"
module: "deepxube.updaters.updater_sup"
file: "deepxube/updaters/updater_sup.py"
line_start: 25
line_end: 58
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_policy_sup')"
generic_parameters: []
bases:
  - name: "UpdatePolicy[Domain, Any, PathFindEdgeSup, InstanceEdge]"
    resolved_id: null
  - name: "UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_sup.UpdatePolicySup.domain_type"
  - "func:deepxube.updaters.updater_sup.UpdatePolicySup.pathfind_type"
  - "func:deepxube.updaters.updater_sup.UpdatePolicySup._get_instance_data_norb"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_policy_sup"
docstring_source: "present"
---

# `deepxube.updaters.updater_sup.UpdatePolicySup`

**File:** [deepxube/updaters/updater_sup.py:25](../../../deepxube/updaters/updater_sup.py#L25)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_policy_sup')`

## Docstring

Supervised policy updater: training targets are the actions taken along
each random-walk path produced by ``PathFindEdgeSup``.

## Inheritance

**Direct bases:**
- `UpdatePolicy[Domain, Any, PathFindEdgeSup, InstanceEdge]`
- `UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_policy_sup`

## Methods

- `domain_type` *(trivial, skipped)*
- `pathfind_type` *(trivial, skipped)*
- `_get_instance_data_norb`

## Source

```python
class UpdatePolicySup(UpdatePolicy[Domain, Any, PathFindEdgeSup, InstanceEdge], UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]):
    """ Supervised policy updater: training targets are the actions taken along
    each random-walk path produced by ``PathFindEdgeSup``.
    """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Accepts any ``Domain`` (no additional mixin required). """
        return Domain

    @staticmethod
    def pathfind_type() -> Type[PathFindEdgeSup]:
        """ :return: Requires an edge-based supervised pathfinder. """
        return PathFindEdgeSup

    def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Convert popped edges from finished instances into training numpy
        arrays (state, goal, action) for the policy network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here but part of the
            signature).
        :return: List of numpy arrays ready for policy training.
        """
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        states: List[State] = [edge.node.state for edge in edges_popped]
        goals: List[Goal] = [edge.node.goal for edge in edges_popped]
        actions: List[Action] = [edge.action for edge in edges_popped]

        inputs_np: List[NDArray] = self.get_policy_nnet_par().to_np_train(states, goals, actions)
        return inputs_np
```
