---
id: "class:deepxube.base.domain.GoalGrndAtoms"
kind: "class"
name: "GoalGrndAtoms"
qualified_name: "deepxube.base.domain.GoalGrndAtoms"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 632
line_end: 719
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GoalSampleableFromState[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalGrndAtoms.state_to_model"
  - "func:deepxube.base.domain.GoalGrndAtoms.model_to_state"
  - "func:deepxube.base.domain.GoalGrndAtoms.goal_to_model"
  - "func:deepxube.base.domain.GoalGrndAtoms.model_to_goal"
  - "func:deepxube.base.domain.GoalGrndAtoms.is_solved"
  - "func:deepxube.base.domain.GoalGrndAtoms.sample_goal_from_state"
  - "func:deepxube.base.domain.GoalGrndAtoms.get_bk"
  - "func:deepxube.base.domain.GoalGrndAtoms.get_ground_atoms"
  - "func:deepxube.base.domain.GoalGrndAtoms.on_model"
  - "func:deepxube.base.domain.GoalGrndAtoms.start_state_fixed"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalGrndAtoms`

**File:** [deepxube/base/domain.py:632](../../../deepxube/base/domain.py#L632)
**Abstract:** yes

## Docstring

Mixin for domains whose states and goals can be represented as sets of ground atoms (Answer Set Programming). 

## Inheritance

**Direct bases:**
- `GoalSampleableFromState[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `state_to_model` *(trivial, skipped)*
- `model_to_state` *(trivial, skipped)*
- `goal_to_model` *(trivial, skipped)*
- `model_to_goal` *(trivial, skipped)*
- `is_solved`
- `sample_goal_from_state`
- `get_bk` *(trivial, skipped)*
- `get_ground_atoms` *(trivial, skipped)*
- `on_model` *(trivial, skipped)*
- `start_state_fixed` *(trivial, skipped)*

## Source

```python
class GoalGrndAtoms(GoalSampleableFromState[S, A, G]):
    """ Mixin for domains whose states and goals can be represented as sets of ground atoms (Answer Set Programming). """

    @abstractmethod
    def state_to_model(self, states: List[S]) -> List[Model]:
        """ Convert states to ASP models (sets of ground atoms). """
        pass

    @abstractmethod
    def model_to_state(self, models: List[Model]) -> List[S]:
        """ Assumes model is a fully specified state

        :param models:
        :return:
        """
        pass

    @abstractmethod
    def goal_to_model(self, goals: List[G]) -> List[Model]:
        """ Convert goals to ASP models. """
        pass

    @abstractmethod
    def model_to_goal(self, models: List[Model]) -> List[G]:
        """ Inverse of ``goal_to_model``. """
        pass

    def is_solved(self, states: List[S], goals: List[G]) -> List[bool]:
        """ Returns whether or not state is solved

        :param states: List of states
        :param goals: List of goals
        :return: Boolean numpy array where the element at index i corresponds to whether or not the
        state at index i is solved
        """
        models_g: List[Model] = self.goal_to_model(goals)
        is_solved_l: List[bool] = []
        models_s: List[Model] = self.state_to_model(states)
        for model_state, model_goal in zip(models_s, models_g):
            is_solved_l.append(model_goal.issubset(model_state))

        return is_solved_l

    def sample_goal_from_state(self, states_start: Optional[List[S]], states_goal: List[S]) -> List[G]:
        """ Build a goal by randomly subsetting the state's ground-atom model (HER-style relabelling). """
        models_g: List[Model] = []

        models_s: List[Model] = self.state_to_model(states_goal)
        keep_probs: NDArray[np.float64] = np.random.rand(len(states_goal))
        for model_s, keep_prob in zip(models_s, keep_probs):
            rand_subset: Set[Atom] = misc_utils.random_subset(model_s, keep_prob)
            models_g.append(frozenset(rand_subset))

        return self.model_to_goal(models_g)

    @abstractmethod
    def get_bk(self) -> List[str]:
        """ get background, each element in list is a line

        :return:
        """
        pass

    @abstractmethod
    def get_ground_atoms(self) -> List[Atom]:
        """ Get all possible ground atoms that can be used to make a state

        :return:
        """
        pass

    @abstractmethod
    def on_model(self, m: ModelCl) -> Model:
        """ Process results from clingo

        :param m:
        :return:
        """
        pass

    @abstractmethod
    def start_state_fixed(self, states: List[S]) -> List[Model]:
        """ Given the start state, what must also be true for the goal state (i.e. immovable walls)

        :param states:
        :return:
        """
        pass
```
