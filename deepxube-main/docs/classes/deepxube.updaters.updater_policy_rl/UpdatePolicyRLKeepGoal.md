---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoal"
kind: "class"
name: "UpdatePolicyRLKeepGoal"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoal"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 197
line_end: 207
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_p_rl')"
generic_parameters: []
bases:
  - name: "UpdatePolicyRLKeepGoalABC[FNsPolicy]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoal.functions_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoal._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_p_rl"
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoal`

**File:** [deepxube/updaters/updater_policy_rl.py:197](../../../deepxube/updaters/updater_policy_rl.py#L197)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_p_rl')`

## Docstring

Concrete keep-goal policy RL updater with a policy-only pathfinder. 

## Inheritance

**Direct bases:**
- `UpdatePolicyRLKeepGoalABC[FNsPolicy]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_p_rl`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdatePolicyRLKeepGoal(UpdatePolicyRLKeepGoalABC[FNsPolicy]):
    """ Concrete keep-goal policy RL updater with a policy-only pathfinder. """

    @staticmethod
    def functions_type() -> Type[FNsPolicy]:
        """ :return: ``FNsPolicy``. """
        return FNsPolicy

    def _get_pathfind_functions(self) -> FNsPolicy:
        """ Build the ``FNsPolicy`` bundle using this updater's policy fn. """
        return FNsPolicy(self.get_policy_fn())
```
