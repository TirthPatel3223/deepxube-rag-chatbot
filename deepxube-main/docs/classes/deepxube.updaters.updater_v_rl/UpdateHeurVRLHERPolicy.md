---
id: "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy"
kind: "class"
name: "UpdateHeurVRLHERPolicy"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 280
line_end: 290
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_v_p_rl_her')"
generic_parameters: []
bases:
  - name: "UpdateHeurVRLHERABC[FNsHeurVPolicy]"
    resolved_id: null
  - name: "UpdateHasPolicy[Domain, FNsHeurVPolicy, PathFindSetHeurV, InstanceNode]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy.functions_type"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_v_p_rl_her"
docstring_source: "present"
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy`

**File:** [deepxube/updaters/updater_v_rl.py:280](../../../deepxube/updaters/updater_v_rl.py#L280)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_v_p_rl_her')`

## Docstring

Concrete HER V RL updater that also trains a policy. 

## Inheritance

**Direct bases:**
- `UpdateHeurVRLHERABC[FNsHeurVPolicy]`
- `UpdateHasPolicy[Domain, FNsHeurVPolicy, PathFindSetHeurV, InstanceNode]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_v_p_rl_her`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurVRLHERPolicy(UpdateHeurVRLHERABC[FNsHeurVPolicy], UpdateHasPolicy[Domain, FNsHeurVPolicy, PathFindSetHeurV, InstanceNode]):
    """ Concrete HER V RL updater that also trains a policy. """

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy``. """
        return FNsHeurVPolicy

    def _get_pathfind_functions(self) -> FNsHeurVPolicy:
        """ Build the ``FNsHeurVPolicy`` bundle from this updater's V + policy fns. """
        return FNsHeurVPolicy(self.get_heur_fn(), self.get_policy_fn())
```
