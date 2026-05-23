---
id: "class:deepxube.base.nnet_input.HasTwoDSGIn"
kind: "class"
name: "HasTwoDSGIn"
qualified_name: "deepxube.base.nnet_input.HasTwoDSGIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 262
line_end: 303
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "DynamicNNetInput[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.HasTwoDSGIn.__init_subclass__"
  - "func:deepxube.base.nnet_input.HasTwoDSGIn.get_input_info_2d_sg"
  - "func:deepxube.base.nnet_input.HasTwoDSGIn.to_np_2d_sg"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.HasTwoDSGIn`

**File:** [deepxube/base/nnet_input.py:262](../../../deepxube/base/nnet_input.py#L262)
**Abstract:** yes

## Docstring

Has a 2d representation for state/goal inputs

    

## Inheritance

**Direct bases:**
- `DynamicNNetInput[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init_subclass__`
- `get_input_info_2d_sg` *(trivial, skipped)*
- `to_np_2d_sg` *(trivial, skipped)*

## Source

```python
class HasTwoDSGIn(DynamicNNetInput[S, A, G]):
    """ Has a 2d representation for state/goal inputs

    """

    class TwoDSGConcrete(TwoDIn["HasTwoDSGIn"], StateGoalIn["HasTwoDSGIn", State, Goal]):
        """ Auto-generated 2-D ``NNetInput`` for ``HasTwoDSGIn`` domains. """

        def __init__(self, domain: "HasTwoDSGIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
            """ Delegate to the domain's ``get_input_info_2d_sg``. """
            return self.domain.get_input_info_2d_sg()

        def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]:
            """ Delegate to the domain's ``to_np_2d_sg``. """
            return self.domain.to_np_2d_sg(states, goals)

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``TwoDSGConcrete`` under ``"2d_sg"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.TwoDSGConcrete, "2d_sg")

    @abstractmethod
    def get_input_info_2d_sg(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
        """
        :return: A list of channels of the arrays given to the neural network (pre one_hot), (height, width),
        a list of depths for performing a one_hot representation on that corresponding input, optional 1x1 conv channel out for qfix.
        The one_hot is applied to the channel dimension. If 1, then no one_hot is performed.
        """
        pass

    @abstractmethod
    def to_np_2d_sg(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """
        :param states: List of states
        :param goals: List of goals

        :return: list of arrays representing states and goals in (chan, height, width) format
        """
```
