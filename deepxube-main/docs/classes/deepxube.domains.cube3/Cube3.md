---
id: "class:deepxube.domains.cube3.Cube3"
kind: "class"
name: "Cube3"
qualified_name: "deepxube.domains.cube3.Cube3"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 511
line_end: 712
is_abstract: false
is_dataclass: false
decorators:
  - "@domain_factory.register_class('cube3')"
generic_parameters: []
bases:
  - name: "NextStateNPActsEnumFixed[Cube3State, Cube3Action, Cube3Goal]"
    resolved_id: null
  - name: "GoalStartRevWalkableActsRev[Cube3State, Cube3Action, Cube3Goal]"
    resolved_id: null
  - name: "HasFlatSGActsEnumFixedIn[Cube3State, Cube3Action, Cube3Goal]"
    resolved_id: null
  - name: "HasFlatSGAIn[Cube3State, Cube3Action, Cube3Goal]"
    resolved_id: null
  - name: "StateGoalVizable[Cube3State, Cube3Action, Cube3Goal]"
    resolved_id: null
  - name: "StringToAct[Cube3State, Cube3Action, Cube3Goal]"
    resolved_id: null
methods:
  - "func:deepxube.domains.cube3.Cube3.__init__"
  - "func:deepxube.domains.cube3.Cube3.is_solved"
  - "func:deepxube.domains.cube3.Cube3.get_goal_states"
  - "func:deepxube.domains.cube3.Cube3.sample_goalstate_goal_pairs"
  - "func:deepxube.domains.cube3.Cube3.get_input_info_flat_sg"
  - "func:deepxube.domains.cube3.Cube3.get_input_info_flat_sga"
  - "func:deepxube.domains.cube3.Cube3.to_np_flat_sg"
  - "func:deepxube.domains.cube3.Cube3.to_np_flat_sga"
  - "func:deepxube.domains.cube3.Cube3.actions_to_indices"
  - "func:deepxube.domains.cube3.Cube3.visualize_state_goal"
  - "func:deepxube.domains.cube3.Cube3.string_to_action"
  - "func:deepxube.domains.cube3.Cube3.string_to_action_help"
  - "func:deepxube.domains.cube3.Cube3.get_actions_fixed"
  - "func:deepxube.domains.cube3.Cube3.rev_action"
  - "func:deepxube.domains.cube3.Cube3._states_to_np"
  - "func:deepxube.domains.cube3.Cube3._np_to_states"
  - "func:deepxube.domains.cube3.Cube3._next_state_np"
  - "func:deepxube.domains.cube3.Cube3._compute_rotation_idxs"
  - "func:deepxube.domains.cube3.Cube3.__repr__"
attributes:
  - name: "atomic_actions"
    annotation: "List[str]"
    default: "['%s%i' % (f, n) for f in ['U', 'D', 'L', 'R', 'B', 'F'] for n in [-1, 1]]"
    from: "class_body"
  - name: "self.actions"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.adj_faces"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.cube_len"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.goal_colors"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_actions"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_colors"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_stickers"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.rotate_idxs_new"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.rotate_idxs_old"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.domain_factory.domain_factory"
    key: "cube3"
docstring_source: "present"
---

# `deepxube.domains.cube3.Cube3`

**File:** [deepxube/domains/cube3.py:511](../../../deepxube/domains/cube3.py#L511)
**Abstract:** no
**Decorators:** `@domain_factory.register_class('cube3')`

## Docstring

Rubik's Cube (3×3×3) domain registered as ``cube3``; 12 quarter-turn moves on 6 faces. 

## Inheritance

**Direct bases:**
- `NextStateNPActsEnumFixed[Cube3State, Cube3Action, Cube3Goal]`
- `GoalStartRevWalkableActsRev[Cube3State, Cube3Action, Cube3Goal]`
- `HasFlatSGActsEnumFixedIn[Cube3State, Cube3Action, Cube3Goal]`
- `HasFlatSGAIn[Cube3State, Cube3Action, Cube3Goal]`
- `StateGoalVizable[Cube3State, Cube3Action, Cube3Goal]`
- `StringToAct[Cube3State, Cube3Action, Cube3Goal]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.domain_factory.domain_factory` under key `cube3`

## Methods

- `__init__`
- `is_solved`
- `get_goal_states`
- `sample_goalstate_goal_pairs`
- `get_input_info_flat_sg` *(trivial, skipped)*
- `get_input_info_flat_sga`
- `to_np_flat_sg`
- `to_np_flat_sga`
- `actions_to_indices` *(trivial, skipped)*
- `visualize_state_goal`
- `string_to_action`
- `string_to_action_help` *(trivial, skipped)* — *(no docstring)*
- `get_actions_fixed` *(trivial, skipped)* — *(no docstring)*
- `rev_action`
- `_states_to_np`
- `_np_to_states`
- `_next_state_np`
- `_compute_rotation_idxs`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `atomic_actions` | `List[str]` | class_body |
| `self.actions` | — | __init__ |
| `self.adj_faces` | — | __init__ |
| `self.cube_len` | — | __init__ |
| `self.goal_colors` | — | __init__ |
| `self.num_actions` | — | __init__ |
| `self.num_colors` | — | __init__ |
| `self.num_stickers` | — | __init__ |
| `self.rotate_idxs_new` | — | __init__ |
| `self.rotate_idxs_old` | — | __init__ |

## Source

```python
class Cube3(NextStateNPActsEnumFixed[Cube3State, Cube3Action, Cube3Goal],
            GoalStartRevWalkableActsRev[Cube3State, Cube3Action, Cube3Goal],
            HasFlatSGActsEnumFixedIn[Cube3State, Cube3Action, Cube3Goal], HasFlatSGAIn[Cube3State, Cube3Action, Cube3Goal],
            StateGoalVizable[Cube3State, Cube3Action, Cube3Goal], StringToAct[Cube3State, Cube3Action, Cube3Goal]):
    """ Rubik's Cube (3×3×3) domain registered as ``cube3``; 12 quarter-turn moves on 6 faces. """

    atomic_actions: List[str] = ["%s%i" % (f, n) for f in ['U', 'D', 'L', 'R', 'B', 'F'] for n in [-1, 1]]

    def __init__(self) -> None:
        """ Precompute the solved colour array and per-move sticker-index permutation tables. """
        super().__init__()
        self.cube_len: int = 3
        self.num_colors: int = 6
        self.num_actions = len(self.atomic_actions)
        self.num_stickers: int = self.num_colors * (self.cube_len ** 2)

        # solved state
        self.goal_colors: NDArray[np.uint8] = (np.arange(0, self.num_stickers, 1,
                                                         dtype=np.uint8) // (self.cube_len ** 2)).astype(np.uint8)

        # get idxs changed for moves
        self.rotate_idxs_new: Dict[str, NDArray[np.int_]]
        self.rotate_idxs_old: Dict[str, NDArray[np.int_]]

        self.adj_faces: Dict[int, NDArray[np.int_]] = _get_adj()

        self.rotate_idxs_new, self.rotate_idxs_old = self._compute_rotation_idxs(self.cube_len, self.atomic_actions)
        self.actions: List[Cube3Action] = [Cube3Action(x) for x in range(self.num_actions)]

    def is_solved(self, states: List[Cube3State], goals: List[Cube3Goal]) -> List[bool]:
        """ :return: True for each state whose colour array exactly matches the goal. """
        states_np: NDArray = np.stack([x.colors for x in states], axis=0)
        goals_np: NDArray = np.stack([x.colors for x in goals], axis=0)
        return cast(List[bool], np.all(states_np == goals_np, axis=1).tolist())

    def get_goal_states(self, num_states: int) -> List[Cube3State]:
        """ :return: ``num_states`` copies of the solved cube state. """
        return [Cube3State(self.goal_colors.copy()) for _ in range(num_states)]

    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[Cube3State], List[Cube3Goal]]:
        """ :return: ``num`` pairs of the solved state and matching goal. """
        states_goal: List[Cube3State] = [Cube3State(self.goal_colors.copy())] * num
        goals: List[Cube3Goal] = [Cube3Goal(self.goal_colors.copy())] * num

        return states_goal, goals

    def get_input_info_flat_sg(self) -> Tuple[List[int], List[int]]:
        """ :return: Flat (state+goal) input descriptor: 54 stickers × 6 colours. """
        return [self.num_stickers], [self.num_colors]

    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Flat (state+goal+action) input descriptor. """
        return [self.num_stickers, 1], [self.num_colors, self.get_num_acts()]

    def to_np_flat_sg(self, states: List[Cube3State], goals: List[Cube3Goal]) -> List[NDArray]:
        """ :return: Stacked uint8 colour arrays (state only; goal is always solved). """
        return [np.stack([x.colors for x in states], axis=0).astype(np.uint8)]

    def to_np_flat_sga(self, states: List[Cube3State], goals: List[Cube3Goal],
                       actions: List[Cube3Action]) -> List[NDArray]:
        """ :return: Flat state arrays extended with action indices. """
        return self.to_np_flat_sg(states, goals) + [np.expand_dims(np.array(self.actions_to_indices(actions)), 1)]

    def actions_to_indices(self, actions: List[Cube3Action]) -> List[int]:
        """ :return: Integer indices of each action. """
        return [action_cube3.action for action_cube3 in actions]

    def visualize_state_goal(self, state: Cube3State, goal: Cube3Goal, fig: Figure) -> None:
        """ Render the cube state as an ``InteractiveCube`` on ``fig``. """
        interactive_cube: InteractiveCube = InteractiveCube(3, state.colors)
        fig.add_axes(interactive_cube)

    def string_to_action(self, act_str: str) -> Optional[Cube3Action]:
        """ :return: ``Cube3Action`` for strings like ``'U1'`` or ``'F-1'``, or ``None`` if unrecognised. """
        if act_str in self.atomic_actions:
            return Cube3Action(self.atomic_actions.index(act_str))
        else:
            return None

    def string_to_action_help(self) -> str:
        return "<face><dir>. i.e. U1, U-1, faces are U, D, L, R, B, F and dirs are 1 and -1"

    def get_actions_fixed(self) -> List[Cube3Action]:
        return self.actions.copy()

    def rev_action(self, states: List[Cube3State], actions: List[Cube3Action]) -> List[Cube3Action]:
        """ :return: Reverse of each action (even index ↔ odd index neighbour). """
        actions_rev: List[Cube3Action] = []
        for action in actions:
            action_val: int = action.action
            action_val_rev: int
            if action_val % 2 == 0:
                action_val_rev = action_val + 1
            else:
                action_val_rev = action_val - 1
            actions_rev.append(Cube3Action(action_val_rev))

        return actions_rev

    def _states_to_np(self, states: List[Cube3State]) -> List[NDArray[np.uint8]]:
        """ :return: Stacked colour numpy arrays. """
        return [np.stack([x.colors for x in states], axis=0)]

    def _np_to_states(self, states_np: List[NDArray]) -> List[Cube3State]:
        """ :return: List of ``Cube3State`` reconstructed from a stacked numpy array. """
        assert len(states_np) == 1
        return [Cube3State(x) for x in states_np[0]]

    def _next_state_np(self, states_np_l: List[NDArray[np.uint8]],
                       actions: List[Cube3Action]) -> Tuple[List[NDArray], List[float]]:
        """ :return: States after applying each action's sticker permutation. """
        assert len(states_np_l) == 1
        colors_next_np: NDArray[np.uint8] = states_np_l[0].copy()
        assert colors_next_np.shape[0] == len(actions), f"#states {colors_next_np.shape[0]} != #actions {len(actions)}"

        state_idxs: NDArray = np.arange(0, colors_next_np.shape[0])
        state_idxs = np.expand_dims(state_idxs, 1)

        rotate_idxs_new: NDArray = np.stack([self.rotate_idxs_new[self.atomic_actions[action.action]] for action in actions])
        rotate_idxs_old: NDArray = np.stack([self.rotate_idxs_old[self.atomic_actions[action.action]] for action in actions])
        colors_next_np[state_idxs, rotate_idxs_new] = colors_next_np[state_idxs, rotate_idxs_old]

        return [colors_next_np], [1.0] * len(actions)

    def _compute_rotation_idxs(self, cube_len: int,
                               moves: List[str]) -> Tuple[Dict[str, NDArray[np.int_]], Dict[str, NDArray[np.int_]]]:
        """ :return: ``(rotate_idxs_new, rotate_idxs_old)`` flat-index permutation tables for every move string. """
        rotate_idxs_new: Dict[str, NDArray[np.int_]] = dict()
        rotate_idxs_old: Dict[str, NDArray[np.int_]] = dict()

        for move in moves:
            f: str = move[0]
            sign: int = int(move[1:])

            rotate_idxs_new[move] = np.array([], dtype=int)
            rotate_idxs_old[move] = np.array([], dtype=int)

            colors: NDArray = np.zeros((6, cube_len, cube_len), dtype=np.int64)
            colors_new = np.copy(colors)

            # WHITE:0, YELLOW:1, BLUE:2, GREEN:3, ORANGE: 4, RED: 5

            adj_idxs = {0: {2: [range(0, cube_len), cube_len - 1], 3: [range(0, cube_len), cube_len - 1],
                            4: [range(0, cube_len), cube_len - 1], 5: [range(0, cube_len), cube_len - 1]},
                        1: {2: [range(0, cube_len), 0], 3: [range(0, cube_len), 0], 4: [range(0, cube_len), 0],
                            5: [range(0, cube_len), 0]},
                        2: {0: [0, range(0, cube_len)], 1: [0, range(0, cube_len)],
                            4: [cube_len - 1, range(cube_len - 1, -1, -1)], 5: [0, range(0, cube_len)]},
                        3: {0: [cube_len - 1, range(0, cube_len)], 1: [cube_len - 1, range(0, cube_len)],
                            4: [0, range(cube_len - 1, -1, -1)], 5: [cube_len - 1, range(0, cube_len)]},
                        4: {0: [range(0, cube_len), cube_len - 1], 1: [range(cube_len - 1, -1, -1), 0],
                            2: [0, range(0, cube_len)], 3: [cube_len - 1, range(cube_len - 1, -1, -1)]},
                        5: {0: [range(0, cube_len), 0], 1: [range(cube_len - 1, -1, -1), cube_len - 1],
                            2: [cube_len - 1, range(0, cube_len)], 3: [0, range(cube_len - 1, -1, -1)]}
                        }
            face_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'B': 4, 'F': 5}
            face = face_dict[f]

            faces_to = self.adj_faces[face]
            if sign == 1:
                faces_from = faces_to[(np.arange(0, len(faces_to)) + 1) % len(faces_to)]
            else:
                faces_from = faces_to[(np.arange(len(faces_to) - 1, len(faces_to) - 1 + len(faces_to))) % len(faces_to)]

            cubes_idxs = [[0, range(0, cube_len)], [range(0, cube_len), cube_len - 1],
                          [cube_len - 1, range(cube_len - 1, -1, -1)], [range(cube_len - 1, -1, -1), 0]]
            cubes_to = np.array([0, 1, 2, 3])
            if sign == 1:
                cubes_from = cubes_to[(np.arange(len(cubes_to) - 1, len(cubes_to) - 1 + len(cubes_to))) % len(cubes_to)]
            else:
                cubes_from = cubes_to[(np.arange(0, len(cubes_to)) + 1) % len(cubes_to)]

            for i in range(4):
                idxs_new = [[idx1, idx2] for idx1 in np.array([cubes_idxs[cubes_to[i]][0]]).flatten() for idx2 in
                            np.array([cubes_idxs[cubes_to[i]][1]]).flatten()]
                idxs_old = [[idx1, idx2] for idx1 in np.array([cubes_idxs[cubes_from[i]][0]]).flatten() for idx2 in
                            np.array([cubes_idxs[cubes_from[i]][1]]).flatten()]
                for idxNew, idxOld in zip(idxs_new, idxs_old):
                    flat_idx_new: int = int(np.ravel_multi_index((face, idxNew[0], idxNew[1]), colors_new.shape))
                    flat_idx_old: int = int(np.ravel_multi_index((face, idxOld[0], idxOld[1]), colors.shape))
                    rotate_idxs_new[move] = np.concatenate((rotate_idxs_new[move], [flat_idx_new]))
                    rotate_idxs_old[move] = np.concatenate((rotate_idxs_old[move], [flat_idx_old]))

            # Rotate adjacent faces
            face_idxs = adj_idxs[face]
            for i in range(0, len(faces_to)):
                face_to: int = int(faces_to[i])
                face_from: int = int(faces_from[i])
                idxs_new = [[idx1, idx2] for idx1 in np.array([face_idxs[face_to][0]]).flatten() for idx2 in
                            np.array([face_idxs[face_to][1]]).flatten()]
                idxs_old = [[idx1, idx2] for idx1 in np.array([face_idxs[face_from][0]]).flatten() for idx2 in
                            np.array([face_idxs[face_from][1]]).flatten()]
                for idxNew, idxOld in zip(idxs_new, idxs_old):
                    flat_idx_new = int(np.ravel_multi_index((face_to, idxNew[0], idxNew[1]), colors_new.shape))
                    flat_idx_old = int(np.ravel_multi_index((face_from, idxOld[0], idxOld[1]), colors.shape))
                    rotate_idxs_new[move] = np.concatenate((rotate_idxs_new[move], [flat_idx_new]))
                    rotate_idxs_old[move] = np.concatenate((rotate_idxs_old[move], [flat_idx_old]))

        return rotate_idxs_new, rotate_idxs_old

    def __repr__(self) -> str:
        return "Cube3()"
```
