---
id: "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLHER"
kind: "class"
name: "UpdateHeurQRLHER"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLHER"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 263
line_end: 273
is_abstract: false
is_dataclass: false
decorators:
  - "@updater_factory.register_class('update_q_rl_her')"
generic_parameters: []
bases:
  - name: "UpdateHeurQRLHERABC[FNsHeurQ]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHER.functions_type"
  - "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHER._get_pathfind_functions"
attributes: []
factory_registrations:
  - factory: "deepxube.factories.updater_factory.updater_factory"
    key: "update_q_rl_her"
docstring_source: "present"
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLHER`

**File:** [deepxube/updaters/updater_q_rl.py:263](../../../deepxube/updaters/updater_q_rl.py#L263)
**Abstract:** no
**Decorators:** `@updater_factory.register_class('update_q_rl_her')`

## Docstring

Concrete HER Q RL updater with a Q-only pathfinder. 

## Inheritance

**Direct bases:**
- `UpdateHeurQRLHERABC[FNsHeurQ]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.updater_factory.updater_factory` under key `update_q_rl_her`

## Methods

- `functions_type` *(trivial, skipped)*
- `_get_pathfind_functions`

## Source

```python
class UpdateHeurQRLHER(UpdateHeurQRLHERABC[FNsHeurQ]):
    """ Concrete HER Q RL updater with a Q-only pathfinder. """

    @staticmethod
    def functions_type() -> Type[FNsHeurQ]:
        """ :return: ``FNsHeurQ``. """
        return FNsHeurQ

    def _get_pathfind_functions(self) -> FNsHeurQ:
        """ Build the ``FNsHeurQ`` bundle using this updater's heuristic fn. """
        return FNsHeurQ(self.get_heur_fn())
```
