---
id: "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalPolicy"
kind: "class"
name: "UpdateHeurVRLKeepGoalPolicy"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalPolicy"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 266
line_end: 276
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_v_p_rl')"
generic_parameters: []
bases:
  - name: "UpdateHeurVRLKeepGoalABC[FNsHeurVPolicy]"
    resolved_id: null
  - name: "UpdateHasPolicy[Domain, FNsHeurVPolicy, PathFindSetHeurV, InstanceNode]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalPolicy.functions_type"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalPolicy._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_v_p_rl"
docstring_source: "present"
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalPolicy`

**File:** [deepxube/updaters/updater_v_rl.py:266](../../../deepxube/updaters/updater_v_rl.py#L266)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_v_p_rl')`

## Docstring

Concrete keep-goal V RL updater that also trains a policy. 

## Inheritance

**Direct bases:**
- `UpdateHeurVRLKeepGoalABC[FNsHeurVPolicy]`
- `UpdateHasPolicy[Domain, FNsHeurVPolicy, PathFindSetHeurV, InstanceNode]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_v_p_rl`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurVRLKeepGoalPolicy(UpdateHeurVRLKeepGoalABC[FNsHeurVPolicy], UpdateHasPolicy[Domain, FNsHeurVPolicy, PathFindSetHeurV, InstanceNode]):
    """ Concrete keep-goal V RL updater that also trains a policy. """

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy`` — V + policy bundle. """
        return FNsHeurVPolicy

    def _get_pathfind_functions(self) -> FNsHeurVPolicy:
        """ Build the ``FNsHeurVPolicy`` bundle from this updater's V + policy fns. """
        return FNsHeurVPolicy(self.get_heur_fn(), self.get_policy_fn())
```
