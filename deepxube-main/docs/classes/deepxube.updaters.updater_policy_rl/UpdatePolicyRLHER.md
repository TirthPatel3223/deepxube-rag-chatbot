---
id: "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER"
kind: "class"
name: "UpdatePolicyRLHER"
qualified_name: "deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 211
line_end: 221
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_p_rl_her')"
generic_parameters: []
bases:
  - name: "UpdatePolicyRLHERABC[FNsPolicy]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER.functions_type"
  - "func:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_p_rl_her"
docstring_source: "present"
---

# `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER`

**File:** [deepxube/updaters/updater_policy_rl.py:211](../../../deepxube/updaters/updater_policy_rl.py#L211)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_p_rl_her')`

## Docstring

Concrete HER policy RL updater with a policy-only pathfinder. 

## Inheritance

**Direct bases:**
- `UpdatePolicyRLHERABC[FNsPolicy]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_p_rl_her`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdatePolicyRLHER(UpdatePolicyRLHERABC[FNsPolicy]):
    """ Concrete HER policy RL updater with a policy-only pathfinder. """

    @staticmethod
    def functions_type() -> Type[FNsPolicy]:
        """ :return: ``FNsPolicy``. """
        return FNsPolicy

    def _get_pathfind_functions(self) -> FNsPolicy:
        """ Build the ``FNsPolicy`` bundle using this updater's policy fn. """
        return FNsPolicy(self.get_policy_fn())
```
