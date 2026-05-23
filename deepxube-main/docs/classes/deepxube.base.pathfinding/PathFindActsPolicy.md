---
id: "class:deepxube.base.pathfinding.PathFindActsPolicy"
kind: "class"
name: "PathFindActsPolicy"
qualified_name: "deepxube.base.pathfinding.PathFindActsPolicy"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 809
line_end: 836
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNsP, I]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindActsPolicy.expand_states"
  - "func:deepxube.base.pathfinding.PathFindActsPolicy.get_state_actions"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindActsPolicy`

**File:** [deepxube/base/pathfinding.py:809](../../../deepxube/base/pathfinding.py#L809)
**Abstract:** yes

## Docstring

Action-source mixin: actions come from the policy function rather than the domain. 

## Inheritance

**Direct bases:**
- `PathFind[D, FNsP, I]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `expand_states`
- `get_state_actions` *(trivial, skipped)*

## Source

```python
class PathFindActsPolicy(PathFind[D, FNsP, I], ABC):
    """ Action-source mixin: actions come from the policy function rather than the domain. """

    def expand_states(self, states: List[State], goals: List[Goal]) -> Tuple[List[List[State]], List[List[Action]], List[List[float]]]:
        """ Sample actions from the policy and apply them via ``Domain.next_state``. """
        actions_l: List[List[Action]] = self.functions.policy_fn(self.domain, states, goals)[0]

        # repeat states according to actions
        actions_flat, split_idxs = misc_utils.flatten(actions_l)

        states_flat: List[State] = []
        for state, actions in zip(states, actions_l, strict=True):
            states_flat.extend([state] * len(actions))

        assert len(states_flat) == len(actions_flat), f"{len(states_flat)}, {len(actions_flat)}"

        # get next states
        states_exp_flat, tcs_flat = self.domain.next_state(states_flat, actions_flat)

        # unflatten
        states_exp: List[List[State]] = misc_utils.unflatten(states_exp_flat, split_idxs)
        tcs_l: List[List[float]] = misc_utils.unflatten(tcs_flat, split_idxs)

        return states_exp, actions_l, tcs_l

    def get_state_actions(self, states: List[State], goals: List[Goal]) -> List[List[Action]]:
        """ :return: Per-state action lists drawn from the policy. """
        return self.functions.policy_fn(self.domain, states, goals)[0]
```
