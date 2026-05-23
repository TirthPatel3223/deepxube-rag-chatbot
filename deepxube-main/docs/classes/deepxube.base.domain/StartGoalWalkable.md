---
id: "class:deepxube.base.domain.StartGoalWalkable"
kind: "class"
name: "StartGoalWalkable"
qualified_name: "deepxube.base.domain.StartGoalWalkable"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 403
line_end: 436
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GoalSampleableFromState[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.StartGoalWalkable.sample_start_states"
  - "func:deepxube.base.domain.StartGoalWalkable.sample_problem_instances"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.StartGoalWalkable`

**File:** [deepxube/base/domain.py:403](../../../deepxube/base/domain.py#L403)
**Abstract:** yes

## Docstring

Can sample start states, take actions to obtain another state, and sample a goal from that state

## Inheritance

**Direct bases:**
- `GoalSampleableFromState[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_start_states` *(trivial, skipped)*
- `sample_problem_instances`

## Source

```python
class StartGoalWalkable(GoalSampleableFromState[S, A, G]):
    """ Can sample start states, take actions to obtain another state, and sample a goal from that state"""
    @abstractmethod
    def sample_start_states(self, num_states: int) -> List[S]:
        """ A method for generating start states. Should try to make this generate states that are as diverse as
        possible so that the trained heuristic function generalizes well.

        :param num_states: Number of states to get
        :return: Generated states
        """
        pass

    def sample_problem_instances(self, num_steps_l: List[int], times: Optional[Times] = None) -> Tuple[List[S], List[G]]:
        """ Sample start states, walk forward ``num_steps_l`` steps, then sample a goal containing the walked state. """
        # Initialize
        if times is None:
            times = Times()

        # Start states
        start_time = time.time()
        states_start: List[S] = self.sample_start_states(len(num_steps_l))
        times.record_time("sample_start_states", time.time() - start_time)

        # random walk
        start_time = time.time()
        states_goal: List[S] = self.random_walk(states_start, num_steps_l)[0]
        times.record_time("random_walk", time.time() - start_time)

        # state to goal
        start_time = time.time()
        goals: List[G] = self.sample_goal_from_state(states_start, states_goal)
        times.record_time("sample_goal", time.time() - start_time)

        return states_start, goals
```
