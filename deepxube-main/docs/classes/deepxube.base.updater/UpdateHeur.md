---
id: "class:deepxube.base.updater.UpdateHeur"
kind: "class"
name: "UpdateHeur"
qualified_name: "deepxube.base.updater.UpdateHeur"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 697
line_end: 715
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHasHeur[D, FNsH, P, Inst, HNet, H]"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateHeur.get_heur_train_shapes_dtypes"
  - "func:deepxube.base.updater.UpdateHeur.get_heur_fn"
  - "func:deepxube.base.updater.UpdateHeur._get_targ_heur_fn"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateHeur`

**File:** [deepxube/base/updater.py:697](../../../deepxube/base/updater.py#L697)
**Abstract:** yes

## Docstring

Updater specialised on training a heuristic network. 

## Inheritance

**Direct bases:**
- `UpdateHasHeur[D, FNsH, P, Inst, HNet, H]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_heur_train_shapes_dtypes` *(trivial, skipped)*
- `get_heur_fn`
- `_get_targ_heur_fn`

## Source

```python
class UpdateHeur(UpdateHasHeur[D, FNsH, P, Inst, HNet, H]):
    """ Updater specialised on training a heuristic network. """

    @abstractmethod
    def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Shape/dtype of each training-array slot for this heuristic. """
        pass

    def get_heur_fn(self) -> H:
        """ :return: Heuristic function; routed through the main process when ``sync_main``. """
        if not self.up_args.sync_main:
            return super().get_heur_fn()
        else:
            assert self.nnet_par_info_main is not None
            return cast(H, self.get_heur_nnet_par().get_nnet_par_fn(self.nnet_par_info_main, None))

    def _get_targ_heur_fn(self) -> H:
        """ :return: The target-network heuristic function (from the NNet-fn dict). """
        return self._get_heur_fn_from_dict()
```
