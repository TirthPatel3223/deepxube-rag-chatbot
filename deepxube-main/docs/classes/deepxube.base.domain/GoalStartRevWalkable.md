---
id: "class:deepxube.base.domain.GoalStartRevWalkable"
kind: "class"
name: "GoalStartRevWalkable"
qualified_name: "deepxube.base.domain.GoalStartRevWalkable"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 439
line_end: 469
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GoalStateGoalPairSampleable[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalStartRevWalkable.sample_problem_instances"
  - "func:deepxube.base.domain.GoalStartRevWalkable.random_walk_rev"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalStartRevWalkable`

**File:** [deepxube/base/domain.py:439](../../../deepxube/base/domain.py#L439)
**Abstract:** yes

## Docstring

Problem-instance generator that samples (state, goal) pairs and walks
backwards from the goal state to obtain a start state. 

## Inheritance

**Direct bases:**
- `GoalStateGoalPairSampleable[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_problem_instances`
- `random_walk_rev` *(trivial, skipped)*

## Source

```python
class GoalStartRevWalkable(GoalStateGoalPairSampleable[S, A, G]):
    """ Problem-instance generator that samples (state, goal) pairs and walks
    backwards from the goal state to obtain a start state. """

    def sample_problem_instances(self, num_steps_l: List[int], times: Optional[Times] = None) -> Tuple[List[S], List[G]]:
        """ Sample (goal-state, goal) pairs, then reverse-walk to derive starts. """
        # Initialize
        if times is None:
            times = Times()

        # goals
        start_time = time.time()
        states_goal, goals = self.sample_goalstate_goal_pairs(len(num_steps_l))
        times.record_time("sample_goalstate_goal_pairs", time.time() - start_time)

        # random walk to get start states
        start_time = time.time()
        states_start: List[S] = self.random_walk_rev(states_goal, num_steps_l)
        times.record_time("random_walk", time.time() - start_time)

        return states_start, goals

    @abstractmethod
    def random_walk_rev(self, states: List[S], num_steps_l: List[int]) -> List[S]:
        """ Domain need not be reversible as the distance of a path obtained by a number reverse steps can be roughly correlated with the number of steps

        :param states: List of states
        :param num_steps_l: List of integers
        :return: states resulting from reverse random walk
        """
        pass
```
