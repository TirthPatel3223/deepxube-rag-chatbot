---
id: "class:deepxube.base.nnet_input.HasFlatSGIn"
kind: "class"
name: "HasFlatSGIn"
qualified_name: "deepxube.base.nnet_input.HasFlatSGIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 150
line_end: 187
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "DynamicNNetInput[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.HasFlatSGIn.__init_subclass__"
  - "func:deepxube.base.nnet_input.HasFlatSGIn.get_input_info_flat_sg"
  - "func:deepxube.base.nnet_input.HasFlatSGIn.to_np_flat_sg"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.HasFlatSGIn`

**File:** [deepxube/base/nnet_input.py:150](../../../deepxube/base/nnet_input.py#L150)
**Abstract:** yes

## Docstring

Has a flat representation for state/goal inputs

    

## Inheritance

**Direct bases:**
- `DynamicNNetInput[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init_subclass__`
- `get_input_info_flat_sg` *(trivial, skipped)*
- `to_np_flat_sg` *(trivial, skipped)*

## Source

```python
class HasFlatSGIn(DynamicNNetInput[S, A, G]):
    """ Has a flat representation for state/goal inputs

    """

    class FlatSGConcrete(FlatIn["HasFlatSGIn"], StateGoalIn["HasFlatSGIn", State, Goal]):
        """ Auto-generated ``NNetInput`` for ``HasFlatSGIn`` domains; delegates to the domain's ``to_np_flat_sg``. """

        def __init__(self, domain: "HasFlatSGIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], List[int]]:
            """ Delegate to the domain's ``get_input_info_flat_sg``. """
            return self.domain.get_input_info_flat_sg()

        def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]:
            """ Delegate to the domain's ``to_np_flat_sg``. """
            return self.domain.to_np_flat_sg(states, goals)

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``FlatSGConcrete`` under the ``"flat_sg"`` key for every subclass. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.FlatSGConcrete, "flat_sg")

    @abstractmethod
    def get_input_info_flat_sg(self) -> Tuple[List[int], List[int]]:
        """
        :return: A list of dimensions of the arrays given to the neural network (pre one_hot), A list of depths for performing a one_hot representation on
        that corresponding input.
        If 1, then no one_hot is performed.
        """
        pass

    @abstractmethod
    def to_np_flat_sg(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """ Domain-specific conversion of (states, goals) into the flat numpy input. """
        pass
```
