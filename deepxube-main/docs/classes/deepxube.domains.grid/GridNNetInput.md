---
id: "class:deepxube.domains.grid.GridNNetInput"
kind: "class"
name: "GridNNetInput"
qualified_name: "deepxube.domains.grid.GridNNetInput"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 164
line_end: 177
is_abstract: false
is_dataclass: false
decorators:
  - "@register_nnet_input('grid', 'grid_nnet_input')"
generic_parameters: []
bases:
  - name: "StateGoalIn[Grid, GridState, GridGoal]"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.GridNNetInput.get_input_info"
  - "func:deepxube.domains.grid.GridNNetInput.to_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.grid.GridNNetInput`

**File:** [deepxube/domains/grid.py:164](../../../deepxube/domains/grid.py#L164)
**Abstract:** no
**Decorators:** `@register_nnet_input('grid', 'grid_nnet_input')`

## Docstring

2-D spatial NNet input for Grid: two binary channel maps (robot position, goal position). 

## Inheritance

**Direct bases:**
- `StateGoalIn[Grid, GridState, GridGoal]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_input_info` *(trivial, skipped)* — *(no docstring)*
- `to_np`

## Source

```python
class GridNNetInput(StateGoalIn[Grid, GridState, GridGoal]):
    """ 2-D spatial NNet input for Grid: two binary channel maps (robot position, goal position). """

    def get_input_info(self) -> int:
        return self.domain.dim

    def to_np(self, states: List[GridState], goals: List[GridGoal]) -> List[NDArray]:
        """ :return: Shape ``(N, 2, dim, dim)`` array with binary robot and goal position maps. """
        np_rep: NDArray = np.zeros((len(states), 2, self.domain.dim, self.domain.dim))
        for idx, (state, goal) in enumerate(zip(states, goals)):
            np_rep[idx, 0, state.robot_x, state.robot_y] = 1
            np_rep[idx, 1, goal.robot_x, goal.robot_y] = 1

        return [np_rep]
```
