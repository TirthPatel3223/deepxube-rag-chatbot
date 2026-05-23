---
id: "class:deepxube.domains.grid.Grid"
kind: "class"
name: "Grid"
qualified_name: "deepxube.domains.grid.Grid"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 69
line_end: 149
is_abstract: false
is_dataclass: false
decorators:
  - "@domain_factory.register_class('grid')"
generic_parameters: []
bases:
  - name: "ActsEnumFixed[GridState, GridAction, GridGoal]"
    resolved_id: null
  - name: "StartGoalWalkable[GridState, GridAction, GridGoal]"
    resolved_id: null
  - name: "StateGoalVizable[GridState, GridAction, GridGoal]"
    resolved_id: null
  - name: "StringToAct[GridState, GridAction, GridGoal]"
    resolved_id: null
  - name: "HasFlatSGActsEnumFixedIn[GridState, GridAction, GridGoal]"
    resolved_id: null
  - name: "HasFlatSGAIn[GridState, GridAction, GridGoal]"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.Grid.__init__"
  - "func:deepxube.domains.grid.Grid.is_solved"
  - "func:deepxube.domains.grid.Grid.sample_start_states"
  - "func:deepxube.domains.grid.Grid.next_state"
  - "func:deepxube.domains.grid.Grid.sample_goal_from_state"
  - "func:deepxube.domains.grid.Grid.get_input_info_flat_sg"
  - "func:deepxube.domains.grid.Grid.get_input_info_flat_sga"
  - "func:deepxube.domains.grid.Grid.to_np_flat_sg"
  - "func:deepxube.domains.grid.Grid.to_np_flat_sga"
  - "func:deepxube.domains.grid.Grid.actions_to_indices"
  - "func:deepxube.domains.grid.Grid.visualize_state_goal"
  - "func:deepxube.domains.grid.Grid.string_to_action"
  - "func:deepxube.domains.grid.Grid.string_to_action_help"
  - "func:deepxube.domains.grid.Grid.get_actions_fixed"
  - "func:deepxube.domains.grid.Grid.__repr__"
attributes:
  - name: "self.actions_fixed"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.dim"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.domain_factory.domain_factory"
    key: "grid"
docstring_source: "present"
---

# `deepxube.domains.grid.Grid`

**File:** [deepxube/domains/grid.py:69](../../../deepxube/domains/grid.py#L69)
**Abstract:** no
**Decorators:** `@domain_factory.register_class('grid')`

## Docstring

2-D grid navigation domain registered as ``grid``; robot moves 4-directionally and movement is clamped at
boundaries. 

## Inheritance

**Direct bases:**
- `ActsEnumFixed[GridState, GridAction, GridGoal]`
- `StartGoalWalkable[GridState, GridAction, GridGoal]`
- `StateGoalVizable[GridState, GridAction, GridGoal]`
- `StringToAct[GridState, GridAction, GridGoal]`
- `HasFlatSGActsEnumFixedIn[GridState, GridAction, GridGoal]`
- `HasFlatSGAIn[GridState, GridAction, GridGoal]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.domain_factory.domain_factory` under key `grid`

## Methods

- `__init__`
- `is_solved` *(trivial, skipped)* — *(no docstring)*
- `sample_start_states`
- `next_state`
- `sample_goal_from_state`
- `get_input_info_flat_sg` *(trivial, skipped)* — *(no docstring)*
- `get_input_info_flat_sga`
- `to_np_flat_sg`
- `to_np_flat_sga`
- `actions_to_indices` *(trivial, skipped)* — *(no docstring)*
- `visualize_state_goal`
- `string_to_action`
- `string_to_action_help` *(trivial, skipped)* — *(no docstring)*
- `get_actions_fixed` *(trivial, skipped)* — *(no docstring)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.actions_fixed` | — | __init__ |
| `self.dim` | — | __init__ |

## Source

```python
class Grid(ActsEnumFixed[GridState, GridAction, GridGoal], StartGoalWalkable[GridState, GridAction, GridGoal],
           StateGoalVizable[GridState, GridAction, GridGoal], StringToAct[GridState, GridAction, GridGoal],
           HasFlatSGActsEnumFixedIn[GridState, GridAction, GridGoal], HasFlatSGAIn[GridState, GridAction, GridGoal]):
    """ 2-D grid navigation domain registered as ``grid``; robot moves 4-directionally and movement is clamped at
    boundaries. """

    def __init__(self, dim: int = 7):
        """ Set grid dimension and precompute the 4 fixed actions. """
        super().__init__()
        self.dim: int = dim
        self.actions_fixed: List[GridAction] = [GridAction(x) for x in [0, 1, 2, 3]]

    def is_solved(self, states: List[GridState], goals: List[GridGoal]) -> List[bool]:
        return [(state.robot_x == goal.robot_x) and (state.robot_y == goal.robot_y) for state, goal in zip(states, goals)]

    def sample_start_states(self, num_states: int) -> List[GridState]:
        """ :return: ``num_states`` random positions on the grid. """
        return [GridState(np.random.randint(self.dim), np.random.randint(self.dim)) for _ in range(num_states)]

    def next_state(self, states: List[GridState], actions: List[GridAction]) -> Tuple[List[GridState], List[float]]:
        """ :return: States after applying ``actions``; movement is clamped to grid boundaries. """
        states_next: List[GridState] = []
        for state, action in zip(states, actions):
            if action.action == 0:  # up
                states_next.append(GridState(min(state.robot_x + 1, self.dim - 1), state.robot_y))
            elif action.action == 1:  # down
                states_next.append(GridState(max(state.robot_x - 1, 0), state.robot_y))
            elif action.action == 2:  # left
                states_next.append(GridState(state.robot_x, min(state.robot_y + 1, self.dim - 1)))
            elif action.action == 3:  # right
                states_next.append(GridState(state.robot_x, max(state.robot_y - 1, 0)))

        return states_next, [1.0] * len(states_next)

    def sample_goal_from_state(self, states_start: Optional[List[GridState]], states_goal: List[GridState]) -> List[GridGoal]:
        """ :return: Goals matching the ``(x, y)`` position of each state in ``states_goal``. """
        return [GridGoal(state_goal.robot_x, state_goal.robot_y) for state_goal in states_goal]

    def get_input_info_flat_sg(self) -> Tuple[List[int], List[int]]:
        return [4], [self.dim]

    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Flat (state+goal+action) input descriptor used by the NNet. """
        return [4, 1], [self.dim, self.get_num_acts()]

    def to_np_flat_sg(self, states: List[GridState], goals: List[GridGoal]) -> List[NDArray]:
        """ :return: Stacked ``[sx, sy, gx, gy]`` arrays for each state/goal pair. """
        return [np.stack([np.stack([state.robot_x for state in states]), np.stack([state.robot_y for state in states]),
                          np.stack([goal.robot_x for goal in goals]), np.stack([goal.robot_y for goal in goals])], axis=1)]

    def to_np_flat_sga(self, states: List[GridState], goals: List[GridGoal], actions: List[GridAction]) -> List[NDArray]:
        """ :return: Flat state+goal arrays extended with action indices. """
        return self.to_np_flat_sg(states, goals) + [np.expand_dims(np.array(self.actions_to_indices(actions)), 1)]

    def actions_to_indices(self, actions: List[GridAction]) -> List[int]:
        return [action_i.action for action_i in actions]

    def visualize_state_goal(self, state: GridState, goal: GridGoal, fig: Figure) -> None:
        """ Draw the grid with robot (1=black) and goal (2=green) on ``fig``. """
        ax = plt.axes()
        grid: NDArray = np.zeros((self.dim, self.dim))
        grid[goal.robot_x, goal.robot_y] = 2
        grid[state.robot_x, state.robot_y] = 1
        ax.imshow(grid, cmap=ListedColormap(["white", "black", "green"]), origin="upper")
        fig.add_axes(ax)

    def string_to_action(self, act_str: str) -> Optional[GridAction]:
        """ :return: ``GridAction`` for ``'0'``–``'3'``, or ``None`` if unrecognised. """
        if act_str in {"0", "1", "2", "3"}:
            return GridAction(int(act_str))
        else:
            return None

    def string_to_action_help(self) -> str:
        return "0, 1, 2, or 3 for down, up, right, and left, respectively."

    def get_actions_fixed(self) -> List[GridAction]:
        return self.actions_fixed.copy()

    def __repr__(self) -> str:
        return f"Grid(dim={self.dim})"
```
