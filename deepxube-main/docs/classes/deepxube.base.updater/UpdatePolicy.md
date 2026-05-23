---
id: "class:deepxube.base.updater.UpdatePolicy"
kind: "class"
name: "UpdatePolicy"
qualified_name: "deepxube.base.updater.UpdatePolicy"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 718
line_end: 738
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "UpdateHasPolicy[D, FNsP, P, Inst]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdatePolicy.get_policy_train_shapes_dtypes"
  - "func:deepxube.base.updater.UpdatePolicy.get_policy_fn"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdatePolicy`

**File:** [deepxube/base/updater.py:718](../../../deepxube/base/updater.py#L718)
**Abstract:** yes

## Docstring

Updater specialised on training a policy network. 

## Inheritance

**Direct bases:**
- `UpdateHasPolicy[D, FNsP, P, Inst]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_policy_train_shapes_dtypes`
- `get_policy_fn`

## Source

```python
class UpdatePolicy(UpdateHasPolicy[D, FNsP, P, Inst], ABC):
    """ Updater specialised on training a policy network. """

    def get_policy_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Shape/dtype of each training-array slot for the policy. """
        states, goals = self.domain.sample_problem_instances([0])
        actions: List[Action] = self.domain.sample_state_action(states)
        inputs_nnet: List[NDArray[Any]] = self.get_policy_nnet_par().to_np_train(states, goals, actions)

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))

        return shapes_dtypes

    def get_policy_fn(self) -> PolicyFn:
        """ :return: Policy function. ``sync_main`` is not yet supported. """
        if not self.up_args.sync_main:
            return super().get_policy_fn()
        else:
            raise NotImplementedError("sync_main not yet implemented for policy_fn")
```
