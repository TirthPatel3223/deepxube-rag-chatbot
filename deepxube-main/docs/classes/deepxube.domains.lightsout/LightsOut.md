---
id: "class:deepxube.domains.lightsout.LightsOut"
kind: "class"
name: "LightsOut"
qualified_name: "deepxube.domains.lightsout.LightsOut"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 58
line_end: 154
is_abstract: false
is_dataclass: false
decorators:
  - "@domain_factory.register_class('lightsout')"
generic_parameters: []
bases:
  - name: "NextStateNPActsEnumFixed[LOState, LOAction, LOGoal]"
    resolved_id: null
  - name: "GoalStartRevWalkableActsRev[LOState, LOAction, LOGoal]"
    resolved_id: null
  - name: "HasFlatSGActsEnumFixedIn[LOState, LOAction, LOGoal]"
    resolved_id: null
  - name: "HasFlatSGAIn[LOState, LOAction, LOGoal]"
    resolved_id: null
  - name: "HasTwoDSGActsEnumFixedIn[LOState, LOAction, LOGoal]"
    resolved_id: null
methods:
  - "func:deepxube.domains.lightsout.LightsOut.__init__"
  - "func:deepxube.domains.lightsout.LightsOut.is_solved"
  - "func:deepxube.domains.lightsout.LightsOut.sample_goalstate_goal_pairs"
  - "func:deepxube.domains.lightsout.LightsOut.rev_action"
  - "func:deepxube.domains.lightsout.LightsOut.get_input_info_flat_sg"
  - "func:deepxube.domains.lightsout.LightsOut.get_input_info_flat_sga"
  - "func:deepxube.domains.lightsout.LightsOut.to_np_flat_sg"
  - "func:deepxube.domains.lightsout.LightsOut.to_np_flat_sga"
  - "func:deepxube.domains.lightsout.LightsOut.get_input_info_2d_sg"
  - "func:deepxube.domains.lightsout.LightsOut.to_np_2d_sg"
  - "func:deepxube.domains.lightsout.LightsOut.actions_to_indices"
  - "func:deepxube.domains.lightsout.LightsOut.get_actions_fixed"
  - "func:deepxube.domains.lightsout.LightsOut._states_to_np"
  - "func:deepxube.domains.lightsout.LightsOut._np_to_states"
  - "func:deepxube.domains.lightsout.LightsOut._next_state_np"
  - "func:deepxube.domains.lightsout.LightsOut.__repr__"
attributes:
  - name: "self.actions_fixed"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.dim"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.goal_np"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.move_matrix"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_tiles"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.domain_factory.domain_factory"
    key: "lightsout"
docstring_source: "present"
---

# `deepxube.domains.lightsout.LightsOut`

**File:** [deepxube/domains/lightsout.py:58](../../../deepxube/domains/lightsout.py#L58)
**Abstract:** no
**Decorators:** `@domain_factory.register_class('lightsout')`

## Docstring

Lights Out puzzle registered as ``lightsout``; toggling tile i flips it and its up/down/left/right neighbours. 

## Inheritance

**Direct bases:**
- `NextStateNPActsEnumFixed[LOState, LOAction, LOGoal]`
- `GoalStartRevWalkableActsRev[LOState, LOAction, LOGoal]`
- `HasFlatSGActsEnumFixedIn[LOState, LOAction, LOGoal]`
- `HasFlatSGAIn[LOState, LOAction, LOGoal]`
- `HasTwoDSGActsEnumFixedIn[LOState, LOAction, LOGoal]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.domain_factory.domain_factory` under key `lightsout`

## Methods

- `__init__`
- `is_solved`
- `sample_goalstate_goal_pairs`
- `rev_action` *(trivial, skipped)* — *(no docstring)*
- `get_input_info_flat_sg` *(trivial, skipped)* — *(no docstring)*
- `get_input_info_flat_sga`
- `to_np_flat_sg`
- `to_np_flat_sga`
- `get_input_info_2d_sg` *(trivial, skipped)* — *(no docstring)*
- `to_np_2d_sg`
- `actions_to_indices` *(trivial, skipped)* — *(no docstring)*
- `get_actions_fixed` *(trivial, skipped)* — *(no docstring)*
- `_states_to_np`
- `_np_to_states`
- `_next_state_np`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.actions_fixed` | — | __init__ |
| `self.dim` | — | __init__ |
| `self.goal_np` | — | __init__ |
| `self.move_matrix` | — | __init__ |
| `self.num_tiles` | — | __init__ |

## Source

```python
class LightsOut(NextStateNPActsEnumFixed[LOState, LOAction, LOGoal], GoalStartRevWalkableActsRev[LOState, LOAction, LOGoal],
                HasFlatSGActsEnumFixedIn[LOState, LOAction, LOGoal], HasFlatSGAIn[LOState, LOAction, LOGoal],
                HasTwoDSGActsEnumFixedIn[LOState, LOAction, LOGoal]):
    """ Lights Out puzzle registered as ``lightsout``; toggling tile i flips it and its up/down/left/right neighbours. """

    def __init__(self, dim: int = 7):
        """ Build the move matrix mapping each tile to the 5 indices it affects (itself + up to 4 neighbours). """
        super().__init__()
        self.dim: int = dim
        self.num_tiles: int = self.dim ** 2

        self.move_matrix: NDArray = np.zeros((self.num_tiles, 5), dtype=np.int64)
        for move in range(self.num_tiles):
            x_pos = int(np.floor(move / self.dim))
            y_pos = move % self.dim

            right = move + self.dim if x_pos < (self.dim-1) else move
            left = move - self.dim if x_pos > 0 else move
            up = move + 1 if y_pos < (self.dim - 1) else move
            down = move - 1 if y_pos > 0 else move

            self.move_matrix[move] = [move, right, left, up, down]

        self.actions_fixed: List[LOAction] = [LOAction(x) for x in range(self.num_tiles)]
        self.goal_np: NDArray = np.zeros(self.num_tiles, dtype=np.uint8)

    def is_solved(self, states: List[LOState], goals: List[LOGoal]) -> List[bool]:
        """ :return: True for each state whose tile array exactly matches the goal tile array. """
        states_np = np.stack([state.tiles for state in states], axis=0)
        goals_np = np.stack([goal.tiles for goal in goals], axis=0)

        return cast(List[bool], np.all(states_np == goals_np, axis=1).tolist())

    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[LOState], List[LOGoal]]:
        """ :return: ``num`` pairs of all-zeros goal states and matching goals. """
        states_goal: List[LOState] = [LOState(self.goal_np.copy())] * num
        goals: List[LOGoal] = [LOGoal(self.goal_np.copy())] * num

        return states_goal, goals

    def rev_action(self, states: List[LOState], actions: List[LOAction]) -> List[LOAction]:
        return actions

    def get_input_info_flat_sg(self) -> Tuple[List[int], List[int]]:
        return [self.num_tiles], [1]

    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Flat (state+goal+action) input descriptor for the NNet. """
        return [self.num_tiles, 1], [1, self.get_num_acts()]

    def to_np_flat_sg(self, states: List[LOState], goals: List[LOGoal]) -> List[NDArray]:
        """ :return: Stacked uint8 tile arrays (state only; goal is always all-zeros). """
        return [np.stack([x.tiles for x in states], axis=0).astype(np.uint8)]

    def to_np_flat_sga(self, states: List[LOState], goals: List[LOGoal], actions: List[LOAction]) -> List[NDArray]:
        """ :return: Flat state arrays extended with action indices. """
        return self.to_np_flat_sg(states, goals) + [np.expand_dims(np.array(self.actions_to_indices(actions)), 1)]

    def get_input_info_2d_sg(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
        return [1], (self.dim, self.dim), [1], 1

    def to_np_2d_sg(self, states: List[LOState], goals: List[LOGoal]) -> List[NDArray]:
        """ :return: Shape ``(N, 1, dim, dim)`` tile arrays for 2-D NNet inputs. """
        tiles_flat: NDArray[np.uint8] = np.stack([x.tiles for x in states], axis=0).astype(np.uint8)
        return [tiles_flat.reshape((-1, 1, self.dim, self.dim))]

    def actions_to_indices(self, actions: List[LOAction]) -> List[int]:
        return [action_lo.action for action_lo in actions]

    def get_actions_fixed(self) -> List[LOAction]:
        return self.actions_fixed.copy()

    def _states_to_np(self, states: List[LOState]) -> List[NDArray[np.uint8]]:
        """ :return: Stacked tile numpy arrays. """
        return [np.stack([x.tiles for x in states], axis=0)]

    def _np_to_states(self, states_np: List[NDArray]) -> List[LOState]:
        """ :return: List of ``LOState`` reconstructed from a stacked numpy array. """
        assert len(states_np) == 1
        return [LOState(x) for x in states_np[0]]

    def _next_state_np(self, states_np_l: List[NDArray], actions: List[LOAction]) -> Tuple[List[NDArray], List[float]]:
        """ :return: States after toggling each action's tile and its neighbours. """
        assert len(states_np_l) == 1
        tiles_next_np: NDArray = states_np_l[0].copy()

        state_idxs: NDArray = np.arange(0, tiles_next_np.shape[0])
        state_idxs = np.expand_dims(state_idxs, 1)

        actions_np: NDArray = np.array([action.action for action in actions])
        move_matrix = self.move_matrix[actions_np]
        tiles_next_np[state_idxs, move_matrix] = (tiles_next_np[state_idxs, move_matrix] + 1) % 2

        return [tiles_next_np], [1.0] * len(actions)

    def __repr__(self) -> str:
        return f"LightsOut(dim={self.dim})"
```
