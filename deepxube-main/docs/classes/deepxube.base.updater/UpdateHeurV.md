---
id: "class:deepxube.base.updater.UpdateHeurV"
kind: "class"
name: "UpdateHeurV"
qualified_name: "deepxube.base.updater.UpdateHeurV"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 741
line_end: 754
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeur[D, FNsHV, P, InstanceNode, HeurNNetParV, HeurFnV]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateHeurV.get_heur_train_shapes_dtypes"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateHeurV`

**File:** [deepxube/base/updater.py:741](../../../deepxube/base/updater.py#L741)
**Abstract:** yes

## Docstring

Heuristic updater for V-type networks (scalar cost-to-go output). 

## Inheritance

**Direct bases:**
- `UpdateHeur[D, FNsHV, P, InstanceNode, HeurNNetParV, HeurFnV]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_heur_train_shapes_dtypes`

## Source

```python
class UpdateHeurV(UpdateHeur[D, FNsHV, P, InstanceNode, HeurNNetParV, HeurFnV], ABC):
    """ Heuristic updater for V-type networks (scalar cost-to-go output). """

    def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Input shapes/dtypes plus a scalar float64 target slot. """
        states, goals = self.domain.sample_problem_instances([0])
        inputs_nnet: List[NDArray[Any]] = self.get_heur_nnet_par().to_np(states, goals)

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))
        shapes_dtypes.append((tuple(), np.dtype(np.float64)))

        return shapes_dtypes
```
