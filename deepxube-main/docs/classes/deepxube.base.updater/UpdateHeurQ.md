---
id: "class:deepxube.base.updater.UpdateHeurQ"
kind: "class"
name: "UpdateHeurQ"
qualified_name: "deepxube.base.updater.UpdateHeurQ"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 757
line_end: 771
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHeur[D, FNsHQ, P, InstanceEdge, HeurNNetParQ, HeurFnQ]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateHeurQ.get_heur_train_shapes_dtypes"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateHeurQ`

**File:** [deepxube/base/updater.py:757](../../../deepxube/base/updater.py#L757)
**Abstract:** yes

## Docstring

Heuristic updater for Q-type networks (per-action cost-to-go). 

## Inheritance

**Direct bases:**
- `UpdateHeur[D, FNsHQ, P, InstanceEdge, HeurNNetParQ, HeurFnQ]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_heur_train_shapes_dtypes`

## Source

```python
class UpdateHeurQ(UpdateHeur[D, FNsHQ, P, InstanceEdge, HeurNNetParQ, HeurFnQ], ABC):
    """ Heuristic updater for Q-type networks (per-action cost-to-go). """

    def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Input shapes/dtypes plus a scalar float64 target slot. """
        states, goals = self.domain.sample_problem_instances([0])
        actions: List[Action] = self.domain.sample_state_action(states)
        inputs_nnet: List[NDArray[Any]] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))
        shapes_dtypes.append((tuple(), np.dtype(np.float64)))

        return shapes_dtypes
```
