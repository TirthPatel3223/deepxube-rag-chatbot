---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurV"
kind: "class"
name: "UpdatePolicyRLKeepGoalHeurV"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurV"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 225
line_end: 236
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_p_v_rl')"
generic_parameters: []
bases:
  - name: "UpdatePolicyRLKeepGoalABC[FNsHeurVPolicy]"
    resolved_id: null
  - name: "UpdateHasHeur[Domain, FNsHeurVPolicy, PathFindActsPolicy, Instance, HeurNNetParV, HeurFnV]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurV.functions_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurV._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_p_v_rl"
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurV`

**File:** [deepxube/updaters/updater_policy_rl.py:225](../../../deepxube/updaters/updater_policy_rl.py#L225)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_p_v_rl')`

## Docstring

Concrete keep-goal policy RL updater paired with a V-heuristic. 

## Inheritance

**Direct bases:**
- `UpdatePolicyRLKeepGoalABC[FNsHeurVPolicy]`
- `UpdateHasHeur[Domain, FNsHeurVPolicy, PathFindActsPolicy, Instance, HeurNNetParV, HeurFnV]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_p_v_rl`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdatePolicyRLKeepGoalHeurV(UpdatePolicyRLKeepGoalABC[FNsHeurVPolicy],
                                  UpdateHasHeur[Domain, FNsHeurVPolicy, PathFindActsPolicy, Instance, HeurNNetParV, HeurFnV]):
    """ Concrete keep-goal policy RL updater paired with a V-heuristic. """

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy``. """
        return FNsHeurVPolicy

    def _get_pathfind_functions(self) -> FNsHeurVPolicy:
        """ Build the ``FNsHeurVPolicy`` bundle from V + policy fns. """
        return FNsHeurVPolicy(self.get_heur_fn(), self.get_policy_fn())
```
