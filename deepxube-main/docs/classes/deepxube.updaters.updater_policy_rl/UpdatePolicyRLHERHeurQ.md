---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ"
kind: "class"
name: "UpdatePolicyRLHERHeurQ"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 269
line_end: 279
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_p_q_rl_her')"
generic_parameters: []
bases:
  - name: "UpdatePolicyRLHERABC[FNsHeurQPolicy]"
    resolved_id: null
  - name: "UpdateHasHeur[Domain, FNsHeurQPolicy, PathFindActsPolicy, Instance, HeurNNetParQ, HeurFnQ]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ.functions_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_p_q_rl_her"
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ`

**File:** [deepxube/updaters/updater_policy_rl.py:269](../../../deepxube/updaters/updater_policy_rl.py#L269)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_p_q_rl_her')`

## Docstring

Concrete HER policy RL updater paired with a Q-heuristic. 

## Inheritance

**Direct bases:**
- `UpdatePolicyRLHERABC[FNsHeurQPolicy]`
- `UpdateHasHeur[Domain, FNsHeurQPolicy, PathFindActsPolicy, Instance, HeurNNetParQ, HeurFnQ]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_p_q_rl_her`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdatePolicyRLHERHeurQ(UpdatePolicyRLHERABC[FNsHeurQPolicy], UpdateHasHeur[Domain, FNsHeurQPolicy, PathFindActsPolicy, Instance, HeurNNetParQ, HeurFnQ]):
    """ Concrete HER policy RL updater paired with a Q-heuristic. """

    @staticmethod
    def functions_type() -> Type[FNsHeurQPolicy]:
        """ :return: ``FNsHeurQPolicy``. """
        return FNsHeurQPolicy

    def _get_pathfind_functions(self) -> FNsHeurQPolicy:
        """ Build the ``FNsHeurQPolicy`` bundle from Q + policy fns. """
        return FNsHeurQPolicy(self.get_heur_fn(), self.get_policy_fn())
```
