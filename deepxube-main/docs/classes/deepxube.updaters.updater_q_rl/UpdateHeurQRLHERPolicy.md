---
id: "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy"
kind: "class"
name: "UpdateHeurQRLHERPolicy"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 291
line_end: 301
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_q_p_rl_her')"
generic_parameters: []
bases:
  - name: "UpdateHeurQRLHERABC[FNsHeurQPolicy]"
    resolved_id: null
  - name: "UpdateHasPolicy[Domain, FNsHeurQPolicy, PathFindSetHeurQ, InstanceEdge]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy.functions_type"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_q_p_rl_her"
docstring_source: "present"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy`

**File:** [deepxube/updaters/updater_q_rl.py:291](../../../deepxube/updaters/updater_q_rl.py#L291)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_q_p_rl_her')`

## Docstring

Concrete HER Q RL updater that also trains a policy. 

## Inheritance

**Direct bases:**
- `UpdateHeurQRLHERABC[FNsHeurQPolicy]`
- `UpdateHasPolicy[Domain, FNsHeurQPolicy, PathFindSetHeurQ, InstanceEdge]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_q_p_rl_her`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurQRLHERPolicy(UpdateHeurQRLHERABC[FNsHeurQPolicy], UpdateHasPolicy[Domain, FNsHeurQPolicy, PathFindSetHeurQ, InstanceEdge]):
    """ Concrete HER Q RL updater that also trains a policy. """

    @staticmethod
    def functions_type() -> Type[FNsHeurQPolicy]:
        """ :return: ``FNsHeurQPolicy``. """
        return FNsHeurQPolicy

    def _get_pathfind_functions(self) -> FNsHeurQPolicy:
        """ Build the ``FNsHeurQPolicy`` bundle from this updater's Q + policy fns. """
        return FNsHeurQPolicy(self.get_heur_fn(), self.get_policy_fn())
```
