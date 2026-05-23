---
id: "class:deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn"
kind: "class"
name: "HasTwoDSGActsEnumFixedIn"
qualified_name: "deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 306
line_end: 332
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HasTwoDSGIn[S, A, G]"
    resolved_id: null
  - name: "HasActsEnumFixedIn[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn.__init_subclass__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn`

**File:** [deepxube/base/nnet_input.py:306](../../../deepxube/base/nnet_input.py#L306)
**Abstract:** yes

## Docstring

``HasTwoDSGIn`` + ``HasActsEnumFixedIn`` for fixed-Q networks on 2-D inputs. 

## Inheritance

**Direct bases:**
- `HasTwoDSGIn[S, A, G]`
- `HasActsEnumFixedIn[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init_subclass__`

## Source

```python
class HasTwoDSGActsEnumFixedIn(HasTwoDSGIn[S, A, G], HasActsEnumFixedIn[S, A, G], ABC):
    """ ``HasTwoDSGIn`` + ``HasActsEnumFixedIn`` for fixed-Q networks on 2-D inputs. """

    class TwoDSGActFixConcrete(TwoDIn["HasTwoDSGActsEnumFixedIn"], StateGoalActFixIn["HasTwoDSGActsEnumFixedIn", State, Goal, Action]):
        """ Auto-generated 2-D ``NNetInput`` that appends per-state action indices. """

        def __init__(self, domain: "HasTwoDSGActsEnumFixedIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
            """ Delegate to the domain's ``get_input_info_2d_sg``. """
            return self.domain.get_input_info_2d_sg()

        def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
            """ Build the 2-D (state, goal) input then append an integer action-index array. """
            num_actions: int = len(actions_l[0])
            actions_np: NDArray = np.zeros((len(actions_l), num_actions)).astype(int)
            for i, actions in enumerate(actions_l):
                actions_np[i] = np.array(self.domain.actions_to_indices(actions))

            return self.domain.to_np_2d_sg(states, goals) + [actions_np]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``TwoDSGActFixConcrete`` under ``"2d_sg_actfix"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.TwoDSGActFixConcrete, "2d_sg_actfix")
```
