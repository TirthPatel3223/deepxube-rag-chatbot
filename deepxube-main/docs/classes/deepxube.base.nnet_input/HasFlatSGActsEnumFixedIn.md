---
id: "class:deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn"
kind: "class"
name: "HasFlatSGActsEnumFixedIn"
qualified_name: "deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 199
line_end: 225
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HasFlatSGIn[S, A, G]"
    resolved_id: null
  - name: "HasActsEnumFixedIn[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn.__init_subclass__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn`

**File:** [deepxube/base/nnet_input.py:199](../../../deepxube/base/nnet_input.py#L199)
**Abstract:** yes

## Docstring

Combines ``HasFlatSGIn`` with ``HasActsEnumFixedIn`` for fixed-Q networks on flat inputs. 

## Inheritance

**Direct bases:**
- `HasFlatSGIn[S, A, G]`
- `HasActsEnumFixedIn[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init_subclass__`

## Source

```python
class HasFlatSGActsEnumFixedIn(HasFlatSGIn[S, A, G], HasActsEnumFixedIn[S, A, G], ABC):
    """ Combines ``HasFlatSGIn`` with ``HasActsEnumFixedIn`` for fixed-Q networks on flat inputs. """

    class FlatSGActFixConcrete(FlatIn["HasFlatSGActsEnumFixedIn"], StateGoalActFixIn["HasFlatSGActsEnumFixedIn", State, Goal, Action]):
        """ Auto-generated ``NNetInput`` that appends per-state action-index arrays to the flat state/goal input. """

        def __init__(self, domain: "HasFlatSGActsEnumFixedIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], List[int]]:
            """ Delegate to the domain's ``get_input_info_flat_sg``. """
            return self.domain.get_input_info_flat_sg()

        def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
            """ Build the flat (state, goal) input then append an integer action-index array. """
            num_actions: int = len(actions_l[0])
            actions_np: NDArray = np.zeros((len(actions_l), num_actions)).astype(int)
            for i, actions in enumerate(actions_l):
                actions_np[i] = np.array(self.domain.actions_to_indices(actions))

            return self.domain.to_np_flat_sg(states, goals) + [actions_np]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``FlatSGActFixConcrete`` under ``"flat_sg_actfix"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.FlatSGActFixConcrete, "flat_sg_actfix")
```
