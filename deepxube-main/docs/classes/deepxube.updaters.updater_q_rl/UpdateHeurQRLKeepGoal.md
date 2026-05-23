---
id: "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoal"
kind: "class"
name: "UpdateHeurQRLKeepGoal"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoal"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 249
line_end: 259
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_q_rl')"
generic_parameters: []
bases:
  - name: "UpdateHeurQRLKeepGoalABC[FNsHeurQ]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoal.functions_type"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoal._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_q_rl"
docstring_source: "present"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoal`

**File:** [deepxube/updaters/updater_q_rl.py:249](../../../deepxube/updaters/updater_q_rl.py#L249)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_q_rl')`

## Docstring

Concrete keep-goal Q RL updater with a Q-only pathfinder. 

## Inheritance

**Direct bases:**
- `UpdateHeurQRLKeepGoalABC[FNsHeurQ]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_q_rl`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurQRLKeepGoal(UpdateHeurQRLKeepGoalABC[FNsHeurQ]):
    """ Concrete keep-goal Q RL updater with a Q-only pathfinder. """

    @staticmethod
    def functions_type() -> Type[FNsHeurQ]:
        """ :return: ``FNsHeurQ``. """
        return FNsHeurQ

    def _get_pathfind_functions(self) -> FNsHeurQ:
        """ Build the ``FNsHeurQ`` bundle using this updater's heuristic fn. """
        return FNsHeurQ(self.get_heur_fn())
```
