---
id: "class:deepxube.base.updater.UpdateHasHeur"
kind: "class"
name: "UpdateHasHeur"
qualified_name: "deepxube.base.updater.UpdateHasHeur"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 589
line_end: 615
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "D"
  - "FNsH"
  - "P"
  - "Inst"
  - "HNet"
  - "H"
bases:
  - name: "Update[D, FNsH, P, Inst]"
    resolved_id: null
  - name: "Generic[D, FNsH, P, Inst, HNet, H]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateHasHeur.heur_name"
  - "func:deepxube.base.updater.UpdateHasHeur.set_heur_nnet"
  - "func:deepxube.base.updater.UpdateHasHeur.set_heur_file"
  - "func:deepxube.base.updater.UpdateHasHeur.get_heur_nnet_par"
  - "func:deepxube.base.updater.UpdateHasHeur.get_heur_fn"
  - "func:deepxube.base.updater.UpdateHasHeur._get_heur_fn_from_dict"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateHasHeur`

**File:** [deepxube/base/updater.py:589](../../../deepxube/base/updater.py#L589)
**Abstract:** yes
**Generic parameters:** `D, FNsH, P, Inst, HNet, H`

## Docstring

Mixin for updaters that own a heuristic NNet under the ``"heur"`` key. 

## Inheritance

**Direct bases:**
- `Update[D, FNsH, P, Inst]`
- `Generic[D, FNsH, P, Inst, HNet, H]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `heur_name` *(trivial, skipped)*
- `set_heur_nnet`
- `set_heur_file`
- `get_heur_nnet_par`
- `get_heur_fn`
- `_get_heur_fn_from_dict`

## Source

```python
class UpdateHasHeur(Update[D, FNsH, P, Inst], Generic[D, FNsH, P, Inst, HNet, H], ABC):
    """ Mixin for updaters that own a heuristic NNet under the ``"heur"`` key. """

    @staticmethod
    def heur_name() -> str:
        """ :return: Fixed NNet key for the heuristic network. """
        return 'heur'

    def set_heur_nnet(self, heur_nnet: HNet) -> None:
        """ Register the heuristic NNet parameter object. """
        self.add_nnet_par(self.heur_name(), heur_nnet)

    def set_heur_file(self, heur_file: str) -> None:
        """ Record the heuristic network's checkpoint path. """
        self.set_nnet_file(self.heur_name(), heur_file)

    def get_heur_nnet_par(self) -> HNet:
        """ :return: Registered heuristic NNet parameter object. """
        return cast(HNet, self.nnet_par_dict[self.heur_name()])

    def get_heur_fn(self) -> H:
        """ :return: Current heuristic-function callable. """
        return self._get_heur_fn_from_dict()

    def _get_heur_fn_from_dict(self) -> H:
        """ Fetch the heuristic callable from the NNet-function dict. """
        return cast(H, self.nnet_fn_dict[self.heur_name()])
```
