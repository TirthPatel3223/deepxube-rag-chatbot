---
id: "class:deepxube.domains.sokoban.Sokoban"
kind: "class"
name: "Sokoban"
qualified_name: "deepxube.domains.sokoban.Sokoban"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 134
line_end: 344
is_abstract: false
is_dataclass: false
decorators:
  - "@domain_factory.register_class('sokoban')"
generic_parameters: []
bases:
  - name: "ActsEnumFixed[SkState, SkAction, SkGoal]"
    resolved_id: null
  - name: "StartGoalWalkable[SkState, SkAction, SkGoal]"
    resolved_id: null
  - name: "StateGoalVizable[SkState, SkAction, SkGoal]"
    resolved_id: null
  - name: "StringToAct[SkState, SkAction, SkGoal]"
    resolved_id: null
methods:
  - "func:deepxube.domains.sokoban.Sokoban.__init__"
  - "func:deepxube.domains.sokoban.Sokoban.next_state"
  - "func:deepxube.domains.sokoban.Sokoban.get_actions_fixed"
  - "func:deepxube.domains.sokoban.Sokoban.is_solved"
  - "func:deepxube.domains.sokoban.Sokoban.sample_start_states"
  - "func:deepxube.domains.sokoban.Sokoban.sample_goal_from_state"
  - "func:deepxube.domains.sokoban.Sokoban.string_to_action"
  - "func:deepxube.domains.sokoban.Sokoban.string_to_action_help"
  - "func:deepxube.domains.sokoban.Sokoban.visualize_state_goal"
  - "func:deepxube.domains.sokoban.Sokoban.to_img"
  - "func:deepxube.domains.sokoban.Sokoban._get_next_idx"
  - "func:deepxube.domains.sokoban.Sokoban.__getstate__"
  - "func:deepxube.domains.sokoban.Sokoban.__repr__"
attributes:
  - name: "self._surfaces"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.actions"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.dim"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_actions"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_boxes"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.states_train"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.domain_factory.domain_factory"
    key: "sokoban"
docstring_source: "present"
---

# `deepxube.domains.sokoban.Sokoban`

**File:** [deepxube/domains/sokoban.py:134](../../../deepxube/domains/sokoban.py#L134)
**Abstract:** no
**Decorators:** `@domain_factory.register_class('sokoban')`

## Docstring

Sokoban puzzle registered as ``sokoban``; agent pushes boxes to target positions on a 10×10 grid. 

## Inheritance

**Direct bases:**
- `ActsEnumFixed[SkState, SkAction, SkGoal]`
- `StartGoalWalkable[SkState, SkAction, SkGoal]`
- `StateGoalVizable[SkState, SkAction, SkGoal]`
- `StringToAct[SkState, SkAction, SkGoal]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.domain_factory.domain_factory` under key `sokoban`

## Methods

- `__init__`
- `next_state`
- `get_actions_fixed` *(trivial, skipped)* — *(no docstring)*
- `is_solved`
- `sample_start_states`
- `sample_goal_from_state`
- `string_to_action`
- `string_to_action_help` *(trivial, skipped)* — *(no docstring)*
- `visualize_state_goal`
- `to_img`
- `_get_next_idx`
- `__getstate__` *(trivial, skipped)* — *(no docstring)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self._surfaces` | — | __init__ |
| `self.actions` | — | __init__ |
| `self.dim` | — | __init__ |
| `self.num_actions` | — | __init__ |
| `self.num_boxes` | — | __init__ |
| `self.states_train` | — | __init__ |

## Source

```python
class Sokoban(ActsEnumFixed[SkState, SkAction, SkGoal], StartGoalWalkable[SkState, SkAction, SkGoal], StateGoalVizable[SkState, SkAction, SkGoal],
              StringToAct[SkState, SkAction, SkGoal]):
    """ Sokoban puzzle registered as ``sokoban``; agent pushes boxes to target positions on a 10×10 grid. """

    def __init__(self) -> None:
        """ Initialise grid dimensions and prompt the user to download training data if absent. """
        super().__init__()

        self.dim: int = 10
        self.num_boxes: int = 4

        self.num_actions: int = 4

        self.states_train: Optional[List[SkState]] = None
        self._surfaces: Optional[Dict[str, NDArray]] = None
        self.actions: List[SkAction] = [SkAction(x) for x in range(self.num_actions)]

        # check if data needs to be downloaded
        data_dir = get_data_dir()
        data_download_link: str = "https://github.com/forestagostinelli/DeepXubeData/raw/main/sokoban.tar.gz"
        if not os.path.exists(f"{data_dir}/sokoban/"):
            valid_user_in: bool = False
            while not valid_user_in:
                user_in: str = input(f"Sokoban data needs to be downloaded from {data_download_link}. "
                                     f"Download data (about 16MB)? (y/n):")
                if user_in.upper() == "Y":
                    valid_user_in = True
                    print("Downloading compressed data")
                    if not os.path.exists(data_dir):
                        os.makedirs(data_dir)

                    tar_gz_file_name = f"{data_dir}/sokoban.tar.gz"
                    wget.download(data_download_link, tar_gz_file_name, bar=None)
                    tar_gz_file = tarfile.open(tar_gz_file_name)
                    print("Uncompressing data")
                    tar_gz_file.extractall(data_dir)
                    print("Deleting compressed data")
                    os.remove(tar_gz_file_name)
                elif user_in.upper() == "N":
                    valid_user_in = True

    def next_state(self, states: List[SkState], actions: List[SkAction]) -> Tuple[List[SkState], List[float]]:
        """ :return: States after applying movement rules: agent→wall stays, agent→box→obstacle stays,
        agent→box→empty slides box, agent→empty moves freely. """
        agent = np.stack([state.agent for state in states], axis=0)
        boxes = np.stack([state.boxes for state in states], axis=0)
        walls_next = np.stack([state.walls for state in states], axis=0)

        idxs_arange = np.arange(0, len(states))
        agent_next_tmp = self._get_next_idx(agent, actions)
        agent_next = np.zeros(agent_next_tmp.shape, dtype=int)

        boxes_next = boxes.copy()

        # agent -> wall
        agent_wall = walls_next[idxs_arange, agent_next_tmp[:, 0], agent_next_tmp[:, 1]]
        agent_next[agent_wall] = agent[agent_wall]

        # agent -> box
        agent_box = boxes[idxs_arange, agent_next_tmp[:, 0], agent_next_tmp[:, 1]]
        boxes_next_tmp = self._get_next_idx(agent_next_tmp, actions)

        box_wall = walls_next[idxs_arange, boxes_next_tmp[:, 0], boxes_next_tmp[:, 1]]
        box_box = boxes[idxs_arange, boxes_next_tmp[:, 0], boxes_next_tmp[:, 1]]

        # agent -> box -> obstacle
        agent_box_obstacle = agent_box & (box_wall | box_box)
        agent_next[agent_box_obstacle] = agent[agent_box_obstacle]

        # agent -> box -> empty
        agent_box_empty = agent_box & np.logical_not(box_wall | box_box)
        agent_next[agent_box_empty] = agent_next_tmp[agent_box_empty]
        abe_idxs = np.where(agent_box_empty)[0]

        agent_next_idxs_abe = agent_next[agent_box_empty]
        boxes_next_idxs_abe = boxes_next_tmp[agent_box_empty]

        boxes_next[abe_idxs, agent_next_idxs_abe[:, 0], agent_next_idxs_abe[:, 1]] = False
        boxes_next[abe_idxs, boxes_next_idxs_abe[:, 0], boxes_next_idxs_abe[:, 1]] = True

        # agent -> empty
        agent_empty = np.logical_not(agent_wall | agent_box)
        agent_next[agent_empty] = agent_next_tmp[agent_empty]
        boxes_next[agent_empty] = boxes[agent_empty]

        states_next: List[SkState] = []
        for idx in range(len(states)):
            state_next: SkState = SkState(agent_next[idx], boxes_next[idx], walls_next[idx])
            states_next.append(state_next)

        transition_costs: List[float] = [1.0 for _ in range(len(states))]

        return states_next, transition_costs

    def get_actions_fixed(self) -> List[SkAction]:
        return self.actions.copy()

    def is_solved(self, states: List[SkState], goals: List[SkGoal]) -> List[bool]:
        """ :return: True for each state whose box map exactly matches the goal box map. """
        boxes_states: NDArray = np.stack([state.boxes for state in states], axis=0)
        targets: NDArray = np.stack([goal.boxes for goal in goals], axis=0)
        return cast(List[bool], np.all(boxes_states == targets, axis=(1, 2)).tolist())

    def sample_start_states(self, num_states: int) -> List[SkState]:
        """ :return: ``num_states`` training states each perturbed by a random walk of 0–100 steps. """
        # get states
        if self.states_train is None:
            self.states_train = _get_train_states()
        state_idxs = np.random.randint(0, len(self.states_train), size=num_states)
        states: List[SkState] = [self.states_train[idx] for idx in state_idxs]

        # random walk
        step_range: Tuple[int, int] = (0, 100)

        steps_range: List[int] = list(range(step_range[0], step_range[1] + 1))
        step_nums: List[int] = np.random.choice(steps_range, num_states).tolist()

        return self.random_walk(states, step_nums)[0]

    def sample_goal_from_state(self, states_start: Optional[List[SkState]], states_goal: List[SkState]) -> List[SkGoal]:
        """ :return: Goals derived from the box positions of each state in ``states_goal``. """
        goals: List[SkGoal] = []
        for state_goal in states_goal:
            goals.append(SkGoal(state_goal.boxes))

        return goals

    def string_to_action(self, act_str: str) -> Optional[SkAction]:
        """ :return: ``SkAction`` for ``'w'``/``'s'``/``'a'``/``'d'``, or ``None`` if unrecognised. """
        act_str_to_act: Dict[str, SkAction] = {"w": SkAction(0), "s": SkAction(1), "a": SkAction(2), "d": SkAction(3)}
        if act_str in act_str_to_act.keys():
            return act_str_to_act[act_str]
        else:
            return None

    def string_to_action_help(self) -> str:
        return "w, d, a, d: up, down, left, right"

    def visualize_state_goal(self, state: SkState, goal: SkGoal, fig: Figure) -> None:
        """ Render the board as an RGB image and display it on ``fig``. """
        room_rgb = self.to_img(state, goal)

        ax = fig.add_subplot(111)
        ax.imshow(room_rgb)

    def to_img(self, state: SkState, goal: SkGoal) -> NDArray:
        """ :return: Shape ``(dim*16, dim*16, 3)`` RGB array compositing surface tiles for each cell. """
        if self._surfaces is None:
            self._surfaces = _get_surfaces()

        room_rgb: NDArray[np.uint8] = np.zeros(shape=(self.dim * 16, self.dim * 16, 3), dtype=np.uint8)
        for i in range(self.dim):
            x_i = i * 16

            for j in range(self.dim):
                y_j = j * 16

                surface_str: str
                if state.walls[i, j]:
                    surface_str = "wall"
                elif (state.agent[0] == i) and (state.agent[1] == j):
                    if goal.boxes[i, j]:
                        surface_str = "player_on_target"
                    else:
                        surface_str = "player"
                elif state.boxes[i, j]:
                    if goal.boxes[i, j]:
                        surface_str = "box_on_target"
                    else:
                        surface_str = "box"
                elif goal.boxes[i, j]:
                    surface_str = "box_target"
                else:
                    surface_str = "floor"
                room_rgb[x_i:(x_i + 16), y_j:(y_j + 16), :] = self._surfaces[surface_str]

        # img = Image.fromarray(room_rgb, 'RGB')
        # img = img.resize((self.img_dim, self.img_dim))

        return room_rgb

    def _get_next_idx(self, curr_idxs: NDArray[np.int_], actions: List[SkAction]) -> NDArray[np.int_]:
        """ :return: Candidate next ``(row, col)`` positions after applying each action, clamped to grid bounds. """
        actions_np: NDArray[np.int_] = np.array([action.action for action in actions])
        next_idxs: NDArray[np.int_] = curr_idxs.copy()

        action_idxs: NDArray[np.int_] = np.where(actions_np == 0)[0]
        next_idxs[action_idxs, 0] = next_idxs[action_idxs, 0] - 1

        action_idxs = np.where(actions_np == 1)[0]
        next_idxs[action_idxs, 0] = next_idxs[action_idxs, 0] + 1

        action_idxs = np.where(actions_np == 2)[0]
        next_idxs[action_idxs, 1] = next_idxs[action_idxs, 1] - 1

        action_idxs = np.where(actions_np == 3)[0]
        next_idxs[action_idxs, 1] = next_idxs[action_idxs, 1] + 1

        next_idxs = np.maximum(next_idxs, 0)
        next_idxs = np.minimum(next_idxs, self.dim - 1)

        return next_idxs

    def __getstate__(self) -> Dict:
        self.states_train = None
        self._surfaces = None

        return self.__dict__

    def __repr__(self) -> str:
        return "Sokoban"
```
