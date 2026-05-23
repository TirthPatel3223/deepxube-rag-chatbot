---
id: "class:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete"
kind: "class"
name: "HeurNNetParQActInConcrete"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 294
line_end: 328
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HeurNNetParQIn"
    resolved_id: null
  - name: "HeurNNetParFacClass"
    resolved_id: null
methods:
  - "func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete.__init__"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._to_np_one_act"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._get_nnet_input"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete`

**File:** [deepxube/factories/heuristic_factory.py:294](../../../deepxube/factories/heuristic_factory.py#L294)
**Abstract:** no

## Docstring

Q-network wrapper with action-as-input (scalar Q output); input
satisfies ``StateGoalActIn``. Used when the action space is not fixed.

## Inheritance

**Direct bases:**
- `HeurNNetParQIn`
- `HeurNNetParFacClass`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `_to_np_one_act`
- `_get_nnet_input` *(trivial, skipped)*

## Source

```python
class HeurNNetParQActInConcrete(HeurNNetParQIn, HeurNNetParFacClass):
    """ Q-network wrapper with action-as-input (scalar Q output); input
    satisfies ``StateGoalActIn``. Used when the action space is not fixed.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str],
                 nnet_name: str, nnet_kwargs: Dict[str, Any]):
        """ Initialise a Q-in wrapper with Q-fix off and output dim 1.

        :param domain: The domain the input operates on.
        :param nnet_input_name: Input registry key.
        :param nnet_name: Heuristic network registration key.
        :param nnet_kwargs: Network constructor kwargs.
        """
        HeurNNetParFacClass.__init__(self, domain, nnet_input_name, nnet_name, nnet_kwargs, False, 1)

    def _to_np_one_act(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray]:
        """ Convert state/goal plus one action per (state, goal) to numpy
        inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions: One action per (state, goal).
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions)

    def _get_nnet_input(self) -> StateGoalActIn:
        """ Return the cached input, asserting it satisfies ``StateGoalActIn``.

        :return: The ``StateGoalActIn`` instance.
        """
        nnet_input: NNetInput = super()._get_nnet_input()
        assert isinstance(nnet_input, StateGoalActIn)
        return nnet_input
```
