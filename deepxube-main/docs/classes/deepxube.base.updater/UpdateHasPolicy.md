---
id: "class:deepxube.base.updater.UpdateHasPolicy"
kind: "class"
name: "UpdateHasPolicy"
qualified_name: "deepxube.base.updater.UpdateHasPolicy"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 618
line_end: 644
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Update[D, FNsP, P, Inst]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateHasPolicy.policy_name"
  - "func:deepxube.base.updater.UpdateHasPolicy.set_policy_nnet"
  - "func:deepxube.base.updater.UpdateHasPolicy.set_policy_file"
  - "func:deepxube.base.updater.UpdateHasPolicy.get_policy_nnet_par"
  - "func:deepxube.base.updater.UpdateHasPolicy.get_policy_fn"
  - "func:deepxube.base.updater.UpdateHasPolicy._get_policy_fn_from_dict"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateHasPolicy`

**File:** [deepxube/base/updater.py:618](../../../deepxube/base/updater.py#L618)
**Abstract:** yes

## Docstring

Mixin for updaters that own a policy NNet under the ``"policy"`` key. 

## Inheritance

**Direct bases:**
- `Update[D, FNsP, P, Inst]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `policy_name` *(trivial, skipped)*
- `set_policy_nnet`
- `set_policy_file`
- `get_policy_nnet_par`
- `get_policy_fn`
- `_get_policy_fn_from_dict`

## Source

```python
class UpdateHasPolicy(Update[D, FNsP, P, Inst], ABC):
    """ Mixin for updaters that own a policy NNet under the ``"policy"`` key. """

    @staticmethod
    def policy_name() -> str:
        """ :return: Fixed NNet key for the policy network. """
        return 'policy'

    def set_policy_nnet(self, policy_nnet: PolicyNNetPar) -> None:
        """ Register the policy NNet parameter object. """
        self.add_nnet_par(self.policy_name(), policy_nnet)

    def set_policy_file(self, policy_file: str) -> None:
        """ Record the policy network's checkpoint path. """
        self.set_nnet_file(self.policy_name(), policy_file)

    def get_policy_nnet_par(self) -> PolicyNNetPar:
        """ :return: Registered policy NNet parameter object. """
        return cast(PolicyNNetPar, self.nnet_par_dict[self.policy_name()])

    def get_policy_fn(self) -> PolicyFn:
        """ :return: Current policy-function callable. """
        return self._get_policy_fn_from_dict()

    def _get_policy_fn_from_dict(self) -> PolicyFn:
        """ Fetch the policy callable from the NNet-function dict. """
        return cast(PolicyFn, self.nnet_fn_dict[self.policy_name()])
```
