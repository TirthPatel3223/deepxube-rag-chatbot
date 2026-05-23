---
id: "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalPolicy"
kind: "class"
name: "UpdateHeurQRLKeepGoalPolicy"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalPolicy"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 277
line_end: 287
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_q_p_rl')"
generic_parameters: []
bases:
  - name: "UpdateHeurQRLKeepGoalABC[FNsHeurQPolicy]"
    resolved_id: null
  - name: "UpdateHasPolicy[Domain, FNsHeurQPolicy, PathFindSetHeurQ, InstanceEdge]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalPolicy.functions_type"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalPolicy._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_q_p_rl"
docstring_source: "present"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalPolicy`

**File:** [deepxube/updaters/updater_q_rl.py:277](../../../deepxube/updaters/updater_q_rl.py#L277)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_q_p_rl')`

## Docstring

Concrete keep-goal Q RL updater that also trains a policy. 

## Inheritance

**Direct bases:**
- `UpdateHeurQRLKeepGoalABC[FNsHeurQPolicy]`
- `UpdateHasPolicy[Domain, FNsHeurQPolicy, PathFindSetHeurQ, InstanceEdge]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_q_p_rl`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurQRLKeepGoalPolicy(UpdateHeurQRLKeepGoalABC[FNsHeurQPolicy], UpdateHasPolicy[Domain, FNsHeurQPolicy, PathFindSetHeurQ, InstanceEdge]):
    """ Concrete keep-goal Q RL updater that also trains a policy. """

    @staticmethod
    def functions_type() -> Type[FNsHeurQPolicy]:
        """ :return: ``FNsHeurQPolicy``. """
        return FNsHeurQPolicy

    def _get_pathfind_functions(self) -> FNsHeurQPolicy:
        """ Build the ``FNsHeurQPolicy`` bundle from this updater's Q + policy fns. """
        return FNsHeurQPolicy(self.get_heur_fn(), self.get_policy_fn())
```
