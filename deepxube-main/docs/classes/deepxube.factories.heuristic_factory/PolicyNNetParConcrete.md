---
id: "class:deepxube.factories.heuristic_factory.PolicyNNetParConcrete"
kind: "class"
name: "PolicyNNetParConcrete"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParConcrete"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 331
line_end: 363
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PolicyNNetParFacClass"
    resolved_id: null
methods:
  - "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_fn"
  - "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete.to_np_train"
  - "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._nnet_out_to_actions"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.factories.heuristic_factory.PolicyNNetParConcrete`

**File:** [deepxube/factories/heuristic_factory.py:331](../../../deepxube/factories/heuristic_factory.py#L331)
**Abstract:** no

## Docstring

Factory-built concrete ``PolicyNNetPar`` delegating input conversion
and output decoding to a ``PolicyNNetIn``.

## Inheritance

**Direct bases:**
- `PolicyNNetParFacClass`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `to_np_fn`
- `to_np_train`
- `_nnet_out_to_actions`

## Source

```python
class PolicyNNetParConcrete(PolicyNNetParFacClass):
    """ Factory-built concrete ``PolicyNNetPar`` delegating input conversion
    and output decoding to a ``PolicyNNetIn``.
    """

    def to_np_fn(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]:
        """ Convert state/goal pairs to numpy inputs for policy inference
        (no actions supplied).

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np_fn(states, goals)

    def to_np_train(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]:
        """ Convert state/goal/action triples to numpy inputs for policy
        training (target-action labels included).

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions: One target action per (state, goal).
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions)

    def _nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[Action]:
        """ Decode raw network outputs into one ``Action`` per input state.

        :param nnet_out: Per-state output arrays from the policy network.
        :return: One sampled/argmaxed ``Action`` per state.
        """
        return self._get_nnet_input().nnet_out_to_actions(nnet_out)
```
