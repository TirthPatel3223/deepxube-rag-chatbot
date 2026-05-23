---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurV"
kind: "class"
name: "UpdatePolicyRLHERHeurV"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurV"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 240
line_end: 250
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_p_v_rl_her')"
generic_parameters: []
bases:
  - name: "UpdatePolicyRLHERABC[FNsHeurVPolicy]"
    resolved_id: null
  - name: "UpdateHasHeur[Domain, FNsHeurVPolicy, PathFindActsPolicy, Instance, HeurNNetParV, HeurFnV]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurV.functions_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurV._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_p_v_rl_her"
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurV`

**File:** [deepxube/updaters/updater_policy_rl.py:240](../../../deepxube/updaters/updater_policy_rl.py#L240)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_p_v_rl_her')`

## Docstring

Concrete HER policy RL updater paired with a V-heuristic. 

## Inheritance

**Direct bases:**
- `UpdatePolicyRLHERABC[FNsHeurVPolicy]`
- `UpdateHasHeur[Domain, FNsHeurVPolicy, PathFindActsPolicy, Instance, HeurNNetParV, HeurFnV]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_p_v_rl_her`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdatePolicyRLHERHeurV(UpdatePolicyRLHERABC[FNsHeurVPolicy], UpdateHasHeur[Domain, FNsHeurVPolicy, PathFindActsPolicy, Instance, HeurNNetParV, HeurFnV]):
    """ Concrete HER policy RL updater paired with a V-heuristic. """

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy``. """
        return FNsHeurVPolicy

    def _get_pathfind_functions(self) -> FNsHeurVPolicy:
        """ Build the ``FNsHeurVPolicy`` bundle from V + policy fns. """
        return FNsHeurVPolicy(self.get_heur_fn(), self.get_policy_fn())
```
