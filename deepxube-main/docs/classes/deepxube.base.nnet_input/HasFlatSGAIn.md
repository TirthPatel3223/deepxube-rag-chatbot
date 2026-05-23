---
id: "class:deepxube.base.nnet_input.HasFlatSGAIn"
kind: "class"
name: "HasFlatSGAIn"
qualified_name: "deepxube.base.nnet_input.HasFlatSGAIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 228
line_end: 259
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "DynamicNNetInput[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.HasFlatSGAIn.__init_subclass__"
  - "func:deepxube.base.nnet_input.HasFlatSGAIn.get_input_info_flat_sga"
  - "func:deepxube.base.nnet_input.HasFlatSGAIn.to_np_flat_sga"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.HasFlatSGAIn`

**File:** [deepxube/base/nnet_input.py:228](../../../deepxube/base/nnet_input.py#L228)
**Abstract:** yes

## Docstring

Domain mixin: provides a flat (state, goal, single action) network input. 

## Inheritance

**Direct bases:**
- `DynamicNNetInput[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init_subclass__`
- `get_input_info_flat_sga` *(trivial, skipped)*
- `to_np_flat_sga` *(trivial, skipped)*

## Source

```python
class HasFlatSGAIn(DynamicNNetInput[S, A, G]):
    """ Domain mixin: provides a flat (state, goal, single action) network input. """

    class FlatSGAConcrete(FlatIn["HasFlatSGAIn"], StateGoalActIn["HasFlatSGAIn", State, Goal, Action]):
        """ Auto-generated ``NNetInput`` delegating to the domain's ``to_np_flat_sga``. """

        def __init__(self, domain: "HasFlatSGAIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], List[int]]:
            """ Delegate to the domain's ``get_input_info_flat_sga``. """
            return self.domain.get_input_info_flat_sga()

        def to_np(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray]:
            """ Delegate to the domain's ``to_np_flat_sga``. """
            return self.domain.to_np_flat_sga(states, goals, actions)

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``FlatSGAConcrete`` under ``"flat_sga"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.FlatSGAConcrete, "flat_sga")

    @abstractmethod
    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Same shape as ``get_input_info_flat_sg`` but for the (state, goal, action) input. """
        pass

    @abstractmethod
    def to_np_flat_sga(self, states: List[S], goals: List[G], actions: List[A]) -> List[NDArray]:
        """ Convert (states, goals, actions) to numpy network input. """
        pass
```
