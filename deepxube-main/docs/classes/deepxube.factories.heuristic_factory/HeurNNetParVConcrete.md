---
id: "class:deepxube.factories.heuristic_factory.HeurNNetParVConcrete"
kind: "class"
name: "HeurNNetParVConcrete"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParVConcrete"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 221
line_end: 253
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HeurNNetParV"
    resolved_id: null
  - name: "HeurNNetParFacClass"
    resolved_id: null
methods:
  - "func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete.__init__"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete.to_np"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete._get_nnet_input"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.factories.heuristic_factory.HeurNNetParVConcrete`

**File:** [deepxube/factories/heuristic_factory.py:221](../../../deepxube/factories/heuristic_factory.py#L221)
**Abstract:** no

## Docstring

V-type heuristic network wrapper: output is a scalar cost-to-go per
(state, goal) pair, input shape satisfies ``StateGoalIn``.

## Inheritance

**Direct bases:**
- `HeurNNetParV`
- `HeurNNetParFacClass`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `to_np`
- `_get_nnet_input` *(trivial, skipped)*

## Source

```python
class HeurNNetParVConcrete(HeurNNetParV, HeurNNetParFacClass):
    """ V-type heuristic network wrapper: output is a scalar cost-to-go per
    (state, goal) pair, input shape satisfies ``StateGoalIn``.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str,
                 nnet_kwargs: Dict[str, Any]):
        """ Initialise a V-type wrapper with Q-fix off and output dim 1.

        :param domain: The domain the input operates on.
        :param nnet_input_name: Input registry key.
        :param nnet_name: Heuristic network registration key.
        :param nnet_kwargs: Network constructor kwargs.
        """
        HeurNNetParFacClass.__init__(self, domain, nnet_input_name, nnet_name, nnet_kwargs, False, 1)

    def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]:
        """ Convert state/goal pairs to numpy network inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :return: List of numpy arrays, one per network input tensor.
        """
        return self._get_nnet_input().to_np(states, goals)

    def _get_nnet_input(self) -> StateGoalIn:
        """ Return the cached input, asserting it satisfies ``StateGoalIn``.

        :return: The ``StateGoalIn`` instance.
        """
        nnet_input: NNetInput = super()._get_nnet_input()
        assert isinstance(nnet_input, StateGoalIn)
        return nnet_input
```
