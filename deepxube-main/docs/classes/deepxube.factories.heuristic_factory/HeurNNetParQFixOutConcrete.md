---
id: "class:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete"
kind: "class"
name: "HeurNNetParQFixOutConcrete"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 256
line_end: 291
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HeurNNetParQFixOut"
    resolved_id: null
  - name: "HeurNNetParFacClass"
    resolved_id: null
methods:
  - "func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete.__init__"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._to_np_fixed_acts"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._get_nnet_input"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete`

**File:** [deepxube/factories/heuristic_factory.py:256](../../../deepxube/factories/heuristic_factory.py#L256)
**Abstract:** no

## Docstring

Q-network wrapper with a fixed output per action
(output dim = ``num_acts``); input satisfies ``StateGoalActFixIn``.

## Inheritance

**Direct bases:**
- `HeurNNetParQFixOut`
- `HeurNNetParFacClass`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `_to_np_fixed_acts`
- `_get_nnet_input` *(trivial, skipped)*

## Source

```python
class HeurNNetParQFixOutConcrete(HeurNNetParQFixOut, HeurNNetParFacClass):
    """ Q-network wrapper with a fixed output per action
    (output dim = ``num_acts``); input satisfies ``StateGoalActFixIn``.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], out_dim: int):
        """ Initialise a Q-fix wrapper with Q-fix on and output dim = ``out_dim``.

        :param domain: The domain the input operates on.
        :param nnet_input_name: Input registry key.
        :param nnet_name: Heuristic network registration key.
        :param nnet_kwargs: Network constructor kwargs.
        :param out_dim: Number of outputs, one per fixed action.
        """
        HeurNNetParFacClass.__init__(self, domain, nnet_input_name, nnet_name, nnet_kwargs, True, out_dim)

    def _to_np_fixed_acts(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
        """ Convert state/goal plus per-state action lists to numpy inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions_l: One list of actions per (state, goal), all drawn
            from the fixed-action set.
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions_l)

    def _get_nnet_input(self) -> StateGoalActFixIn:
        """ Return the cached input, asserting it satisfies
        ``StateGoalActFixIn``.

        :return: The ``StateGoalActFixIn`` instance.
        """
        nnet_input: NNetInput = super()._get_nnet_input()
        assert isinstance(nnet_input, StateGoalActFixIn)
        return nnet_input
```
