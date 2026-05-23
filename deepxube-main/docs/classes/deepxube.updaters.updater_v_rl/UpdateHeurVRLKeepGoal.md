---
id: "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal"
kind: "class"
name: "UpdateHeurVRLKeepGoal"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 238
line_end: 248
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_v_rl')"
generic_parameters: []
bases:
  - name: "UpdateHeurVRLKeepGoalABC[FNsHeurV]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal.functions_type"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_v_rl"
docstring_source: "present"
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal`

**File:** [deepxube/updaters/updater_v_rl.py:238](../../../deepxube/updaters/updater_v_rl.py#L238)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_v_rl')`

## Docstring

Concrete keep-goal V RL updater with a V-only pathfinder. 

## Inheritance

**Direct bases:**
- `UpdateHeurVRLKeepGoalABC[FNsHeurV]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_v_rl`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurVRLKeepGoal(UpdateHeurVRLKeepGoalABC[FNsHeurV]):
    """ Concrete keep-goal V RL updater with a V-only pathfinder. """

    @staticmethod
    def functions_type() -> Type[FNsHeurV]:
        """ :return: ``FNsHeurV`` — V-only functions bundle. """
        return FNsHeurV

    def _get_pathfind_functions(self) -> FNsHeurV:
        """ Build the ``FNsHeurV`` bundle using this updater's heuristic fn. """
        return FNsHeurV(self.get_heur_fn())
```
