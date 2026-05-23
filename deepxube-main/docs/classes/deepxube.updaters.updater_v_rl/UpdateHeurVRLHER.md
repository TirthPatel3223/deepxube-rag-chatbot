---
id: "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLHER"
kind: "class"
name: "UpdateHeurVRLHER"
qualified_name: "deepxube.updaters.updater_v_rl.UpdateHeurVRLHER"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 252
line_end: 262
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_v_rl_her')"
generic_parameters: []
bases:
  - name: "UpdateHeurVRLHERABC[FNsHeurV]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHER.functions_type"
  - "func:deepxube.updaters.updater_v_rl.UpdateHeurVRLHER._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_v_rl_her"
docstring_source: "present"
---

# `deepxube.updaters.updater_v_rl.UpdateHeurVRLHER`

**File:** [deepxube/updaters/updater_v_rl.py:252](../../../deepxube/updaters/updater_v_rl.py#L252)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_v_rl_her')`

## Docstring

Concrete HER V RL updater with a V-only pathfinder. 

## Inheritance

**Direct bases:**
- `UpdateHeurVRLHERABC[FNsHeurV]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_v_rl_her`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurVRLHER(UpdateHeurVRLHERABC[FNsHeurV]):
    """ Concrete HER V RL updater with a V-only pathfinder. """

    @staticmethod
    def functions_type() -> Type[FNsHeurV]:
        """ :return: ``FNsHeurV``. """
        return FNsHeurV

    def _get_pathfind_functions(self) -> FNsHeurV:
        """ Build the ``FNsHeurV`` bundle using this updater's heuristic fn. """
        return FNsHeurV(self.get_heur_fn())
```
