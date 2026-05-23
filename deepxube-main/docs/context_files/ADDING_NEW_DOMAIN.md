# DeepXube: How to Add a New Puzzle Domain

---
**[RAG SYSTEM INSTRUCTION - DO NOT SHOW TO USER]**
When a user asks how to add a new domain to DeepXube, guide them through THREE decisions in order:

**DECISION 1 — State Representation:**
*"How do you want to represent your puzzle state to the neural network?*
*1) As a flat 1D array (best for permutation puzzles like Rubik's Cube)*
*2) As a 2D spatial grid (best for spatial puzzles like LightsOut, 15-Puzzle)*
*3) As a custom multi-channel encoding (best for complex games like Sokoban)*
*4) As logical rules via ASP/PDDL (for planning tasks)"*

**DECISION 2 — Action Space:**
*"Are the available moves the same in every state, or do they change depending on the current state?"*
- Same everywhere → `ActsEnumFixed` (Rubik's Cube, LightsOut)
- Change per state → `ActsEnum` or direct override (Sokoban)

**DECISION 3 — Problem Instance Generation:**
*"Can your puzzle's moves be reversed? (i.e., can you undo any move?)"*
- Yes → `GoalStartRevWalkableActsRev` (start from goal, walk backwards)
- No / Not easily → `StartGoalWalkable` (start from random state, walk forwards)

Once they answer all three, serve them the matching template from the sections below.

**AFTER the user finishes their domain**, proactively guide them to verify it works, then transition to `TRAINING_GUIDE.md`.
---

## Overview

Adding a new puzzle to DeepXube requires creating **one Python file** containing:
1. A **State** class — what does one configuration of the puzzle look like?
2. A **Goal** class — what does a solved puzzle look like?
3. An **Action** class — what is one move?
4. A **Domain** class — how do moves change the state? How do you generate training instances?
5. A **Parser** class — how does the CLI parse arguments for your domain?

You register everything with decorators. DeepXube's factory system auto-discovers your domain at startup.

### Where to Put Your File

You have two options:

**Option A (Recommended): Local directory**
Create a `domains/` folder in your working directory and put your file there:
```
your_project/
├── domains/
│   └── mypuzzle.py      ← your domain
├── saved_models/         ← training output goes here
```
DeepXube auto-imports all `.py` files from `./domains/` at startup.

**Option B: Inside the package**
Place your file at `deepxube/domains/mypuzzle.py`. This works because the package auto-imports all submodules, but it modifies the library source.

---

## Quick Reference: Which Template Do I Need?

| My puzzle is like... | Actions | Reversible? | Template |
|---|---|---|---|
| Rubik's Cube, permutation puzzle | Fixed set, same in every state | Yes | **Template A** (1D Flat) |
| LightsOut, tile toggle puzzle | Fixed set, same in every state | Yes (self-inverse) | **Template B** (2D Spatial) |
| Grid navigation, simple board game | Fixed set, same in every state | No / doesn't matter | **Template C** (Forward-Walk) |
| Sokoban, complex board game | Change per state | No | **Template D** (Custom Input) |
| Planning task with logical rules | Defined by ASP/PDDL | Varies | **Template E** (Logic) |

---

## TEMPLATE A: 1D Flat Array + Fixed Actions + Reversible Moves

**Use when:** Your puzzle state is naturally a 1D array of integers/tokens, every state has the same set of moves, and every move can be undone.

**Real examples in codebase:** `Cube3` (Rubik's Cube), `NPuzzle` (15-Puzzle), `LightsOut`

Create `domains/mypuzzle.py`:

```python
import numpy as np
from typing import List, Tuple, Optional, Dict, Any
from deepxube.factories.domain_factory import domain_factory
from deepxube.base.factory import Parser
from deepxube.base.domain import (
    State, Action, Goal,
    NextStateNPActsEnumFixed,        # Vectorized transitions + fixed action set
    GoalStartRevWalkableActsRev,     # Generate instances by walking backwards from goal
)
from deepxube.base.nnet_input import (
    HasFlatSGActsEnumFixedIn,        # Enables V and QFix heuristics on flat input
    HasFlatSGAIn,                    # Enables QIn heuristic on flat input
)


# ─── State, Goal, Action ──────────────────────────────────────────

class MyState(State):
    __slots__ = ['data', 'hash']

    def __init__(self, data: np.ndarray):
        self.data = data
        self.hash: Optional[int] = None

    def __hash__(self) -> int:
        if self.hash is None:
            self.hash = hash(self.data.tobytes())
        return self.hash

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MyState):
            return np.array_equal(self.data, other.data)
        return NotImplemented


class MyGoal(Goal):
    def __init__(self, data: np.ndarray):
        self.data = data


class MyAction(Action):
    def __init__(self, action_id: int):
        self.action = action_id

    def __hash__(self) -> int:
        return self.action

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MyAction):
            return self.action == other.action
        return NotImplemented


# ─── Domain ────────────────────────────────────────────────────────

@domain_factory.register_class("mypuzzle")
class MyPuzzle(
    NextStateNPActsEnumFixed[MyState, MyAction, MyGoal],
    GoalStartRevWalkableActsRev[MyState, MyAction, MyGoal],
    HasFlatSGActsEnumFixedIn[MyState, MyAction, MyGoal],
    HasFlatSGAIn[MyState, MyAction, MyGoal],
):
    def __init__(self, **kwargs):
        super().__init__()

        ### YOUR CODE HERE ###
        # 1. Define the size of your state and the set of moves
        self.num_elements = 9          # e.g. 9 tiles for a 3x3 puzzle
        self.move_names = ['R', 'R_inv', 'U', 'U_inv']
        self.num_actions = len(self.move_names)
        self.actions = [MyAction(i) for i in range(self.num_actions)]

        # 2. Define the solved state as a 1D numpy array
        self.goal_data = np.arange(self.num_elements, dtype=np.uint8)

    # 3. Define how moves change the state (vectorized over a batch)
    def _next_state_np(self, states_np_l: List[np.ndarray],
                       actions: List[MyAction]) -> Tuple[List[np.ndarray], List[float]]:
        states_data = states_np_l[0].copy()  # shape: (batch, num_elements)

        ### YOUR CODE HERE ###
        for i, action in enumerate(actions):
            if action.action == 0:    # e.g. rotate right
                pass  # Modify states_data[i] in-place
            elif action.action == 1:  # e.g. rotate right inverse
                pass

        return [states_data], [1.0] * len(actions)  # transition cost = 1.0

    # 4. Define the reverse of each move
    def rev_action(self, states: List[MyState],
                   actions: List[MyAction]) -> List[MyAction]:
        ### YOUR CODE HERE ###
        # Example: action 0 <-> action 1, action 2 <-> action 3
        rev_map = {0: 1, 1: 0, 2: 3, 3: 2}
        return [MyAction(rev_map[a.action]) for a in actions]

    # ─── Boilerplate (copy as-is, just change class names) ─────────

    def is_solved(self, states: List[MyState], goals: List[MyGoal]) -> List[bool]:
        s = np.stack([x.data for x in states], axis=0)
        g = np.stack([x.data for x in goals], axis=0)
        return np.all(s == g, axis=1).tolist()

    def sample_goalstate_goal_pairs(self, num: int):
        return ([MyState(self.goal_data.copy())] * num,
                [MyGoal(self.goal_data.copy())] * num)

    def get_actions_fixed(self) -> List[MyAction]:
        return self.actions.copy()

    def actions_to_indices(self, actions: List[MyAction]) -> List[int]:
        return [a.action for a in actions]

    def get_input_info_flat_sg(self):
        return [self.num_elements], [1]  # [dims], [one_hot_depths]

    def get_input_info_flat_sga(self):
        return [self.num_elements, 1], [1, self.num_actions]

    def to_np_flat_sg(self, states: List[MyState], goals: List[MyGoal]):
        return [np.stack([x.data for x in states], axis=0).astype(np.uint8)]

    def to_np_flat_sga(self, states, goals, actions):
        return self.to_np_flat_sg(states, goals) + [
            np.expand_dims(np.array(self.actions_to_indices(actions)), 1)
        ]

    def _states_to_np(self, states: List[MyState]) -> List[np.ndarray]:
        return [np.stack([x.data for x in states], axis=0)]

    def _np_to_states(self, states_np: List[np.ndarray]) -> List[MyState]:
        return [MyState(x) for x in states_np[0]]


# ─── Parser ────────────────────────────────────────────────────────

@domain_factory.register_parser("mypuzzle")
class MyPuzzleParser(Parser):
    def parse(self, args_str: str) -> Dict[str, Any]:
        # If your puzzle has parameters (e.g. grid size), parse them here.
        # CLI usage: --domain mypuzzle.3  →  args_str = "3"
        # return {"dim": int(args_str)}
        return {}

    def help(self) -> str:
        return "No arguments needed. Usage: --domain mypuzzle"
```

**Compatible training commands:**
```bash
# Use resnet_fc for flat inputs
--heur resnet_fc.100H_2B_bn --heur_type V
--heur resnet_fc.100H_2B_bn --heur_type QFix
--heur resnet_fc.100H_2B_bn --heur_type QIn
```

---

## TEMPLATE B: 2D Spatial Grid + Fixed Actions + Reversible Moves

**Use when:** Your puzzle state is naturally a 2D grid and you want to use a CNN.

**Real example in codebase:** `LightsOut`

Create `domains/mygridpuzzle.py`:

```python
import numpy as np
from typing import List, Tuple, Optional, Dict, Any
from deepxube.factories.domain_factory import domain_factory
from deepxube.base.factory import Parser
from deepxube.base.domain import (
    State, Action, Goal,
    NextStateNPActsEnumFixed,
    GoalStartRevWalkableActsRev,
)
from deepxube.base.nnet_input import (
    HasFlatSGActsEnumFixedIn,         # Also register flat input (needed for QIn)
    HasFlatSGAIn,                     # Needed for QIn heuristic
    HasTwoDSGActsEnumFixedIn,         # 2D spatial input for CNN
)


class GridState(State):
    __slots__ = ['tiles', 'hash']
    def __init__(self, tiles: np.ndarray):
        self.tiles = tiles
        self.hash: Optional[int] = None
    def __hash__(self) -> int:
        if self.hash is None:
            self.hash = hash(self.tiles.tobytes())
        return self.hash
    def __eq__(self, other: object) -> bool:
        if isinstance(other, GridState):
            return np.array_equal(self.tiles, other.tiles)
        return NotImplemented

class GridGoal(Goal):
    def __init__(self, tiles: np.ndarray):
        self.tiles = tiles

class GridAction(Action):
    def __init__(self, action_id: int):
        self.action = action_id
    def __hash__(self) -> int:
        return self.action
    def __eq__(self, other: object) -> bool:
        if isinstance(other, GridAction):
            return self.action == other.action
        return NotImplemented


@domain_factory.register_class("mygridpuzzle")
class MyGridPuzzle(
    NextStateNPActsEnumFixed[GridState, GridAction, GridGoal],
    GoalStartRevWalkableActsRev[GridState, GridAction, GridGoal],
    HasFlatSGActsEnumFixedIn[GridState, GridAction, GridGoal],
    HasFlatSGAIn[GridState, GridAction, GridGoal],
    HasTwoDSGActsEnumFixedIn[GridState, GridAction, GridGoal],
):
    def __init__(self, dim: int = 5, **kwargs):
        super().__init__()

        ### YOUR CODE HERE ###
        self.dim = dim
        self.num_tiles = self.dim * self.dim
        self.num_actions = self.num_tiles  # e.g. one action per cell
        self.actions = [GridAction(i) for i in range(self.num_actions)]
        self.goal_tiles = np.zeros(self.num_tiles, dtype=np.uint8)

    def _next_state_np(self, states_np_l, actions):
        tiles = states_np_l[0].copy()  # shape: (batch, num_tiles)
        ### YOUR CODE HERE: modify tiles[i] based on actions[i] ###
        return [tiles], [1.0] * len(actions)

    def rev_action(self, states, actions):
        ### YOUR CODE HERE ###
        return actions  # If moves are self-inverse (like LightsOut toggles)

    # ─── Boilerplate ───────────────────────────────────────────────

    def is_solved(self, states, goals):
        s = np.stack([x.tiles for x in states], axis=0)
        g = np.stack([x.tiles for x in goals], axis=0)
        return np.all(s == g, axis=1).tolist()

    def sample_goalstate_goal_pairs(self, num):
        return ([GridState(self.goal_tiles.copy())] * num,
                [GridGoal(self.goal_tiles.copy())] * num)

    def get_actions_fixed(self):
        return self.actions.copy()

    def actions_to_indices(self, actions):
        return [a.action for a in actions]

    # Flat input methods (needed for QIn and as fallback)
    def get_input_info_flat_sg(self):
        return [self.num_tiles], [1]

    def get_input_info_flat_sga(self):
        return [self.num_tiles, 1], [1, self.num_actions]

    def to_np_flat_sg(self, states, goals):
        return [np.stack([x.tiles for x in states], axis=0).astype(np.uint8)]

    def to_np_flat_sga(self, states, goals, actions):
        return self.to_np_flat_sg(states, goals) + [
            np.expand_dims(np.array(self.actions_to_indices(actions)), 1)
        ]

    # 2D input methods (for CNN)
    def get_input_info_2d_sg(self):
        # [channels], (height, width), [one_hot_depths], optional_qfix_1x1
        return [1], (self.dim, self.dim), [1], 1

    def to_np_2d_sg(self, states, goals):
        tiles = np.stack([x.tiles for x in states], axis=0).astype(np.uint8)
        return [tiles.reshape((-1, 1, self.dim, self.dim))]

    # Numpy conversion
    def _states_to_np(self, states):
        return [np.stack([x.tiles for x in states], axis=0)]

    def _np_to_states(self, states_np):
        return [GridState(x) for x in states_np[0]]


@domain_factory.register_parser("mygridpuzzle")
class MyGridPuzzleParser(Parser):
    def parse(self, args_str: str) -> Dict[str, Any]:
        return {"dim": int(args_str)}   # Usage: --domain mygridpuzzle.7

    def help(self) -> str:
        return "An integer for the grid dimension. E.g. 'mygridpuzzle.7'"
```

**Compatible training commands:**
```bash
# Use resnet_2d for 2D spatial inputs (CNN)
--heur resnet_2d.64C_4B_bn --heur_type V
--heur resnet_2d.64C_4B_bn --heur_type QFix

# Or use resnet_fc for flat inputs (also works because we registered flat mixins)
--heur resnet_fc.100H_2B_bn --heur_type V
--heur resnet_fc.100H_2B_bn --heur_type QIn
```

---

## TEMPLATE C: Forward-Walk + Fixed Actions (No Reverse Required)

**Use when:** Your puzzle's moves can't easily be reversed, OR you want to generate diverse start states by sampling randomly instead of walking backwards from the goal. This uses `StartGoalWalkable` instead of `GoalStartRevWalkable`.

**Real examples in codebase:** `Grid`, `Sokoban`

```python
import numpy as np
from typing import List, Tuple, Optional, Dict, Any
from deepxube.factories.domain_factory import domain_factory
from deepxube.base.factory import Parser
from deepxube.base.domain import (
    State, Action, Goal,
    ActsEnumFixed,            # Fixed action set (no numpy vectorization)
    StartGoalWalkable,        # Generate instances by walking FORWARDS
)
from deepxube.base.nnet_input import HasFlatSGActsEnumFixedIn, HasFlatSGAIn


class FWState(State):
    __slots__ = ['pos', 'hash']
    def __init__(self, pos: np.ndarray):
        self.pos = pos
        self.hash: Optional[int] = None
    def __hash__(self):
        if self.hash is None:
            self.hash = hash(self.pos.tobytes())
        return self.hash
    def __eq__(self, other):
        if isinstance(other, FWState):
            return np.array_equal(self.pos, other.pos)
        return NotImplemented

class FWGoal(Goal):
    def __init__(self, pos: np.ndarray):
        self.pos = pos

class FWAction(Action):
    def __init__(self, action_id: int):
        self.action = action_id
    def __hash__(self):
        return self.action
    def __eq__(self, other):
        if isinstance(other, FWAction):
            return self.action == other.action
        return NotImplemented


@domain_factory.register_class("myfwpuzzle")
class MyFWPuzzle(
    ActsEnumFixed[FWState, FWAction, FWGoal],
    StartGoalWalkable[FWState, FWAction, FWGoal],
    HasFlatSGActsEnumFixedIn[FWState, FWAction, FWGoal],
    HasFlatSGAIn[FWState, FWAction, FWGoal],
):
    def __init__(self, dim: int = 7, **kwargs):
        super().__init__()
        self.dim = dim
        self.actions_list = [FWAction(i) for i in range(4)]  # up/down/left/right

    # REQUIRED: Direct next_state override (no numpy vectorization needed)
    def next_state(self, states: List[FWState],
                   actions: List[FWAction]) -> Tuple[List[FWState], List[float]]:
        ### YOUR CODE HERE ###
        next_states = []
        for state, action in zip(states, actions):
            pos = state.pos.copy()
            # Apply movement logic here
            next_states.append(FWState(pos))
        return next_states, [1.0] * len(states)

    def is_solved(self, states, goals):
        return [np.array_equal(s.pos, g.pos) for s, g in zip(states, goals)]

    def get_actions_fixed(self):
        return self.actions_list.copy()

    # REQUIRED for StartGoalWalkable: sample diverse start states
    def sample_start_states(self, num_states: int) -> List[FWState]:
        ### YOUR CODE HERE ###
        # Generate random starting configurations
        return [FWState(np.random.randint(0, self.dim, size=2))
                for _ in range(num_states)]

    # REQUIRED for StartGoalWalkable: derive a goal from a walked-to state
    def sample_goal_from_state(self, states_start, states_goal):
        ### YOUR CODE HERE ###
        return [FWGoal(s.pos.copy()) for s in states_goal]

    def actions_to_indices(self, actions):
        return [a.action for a in actions]

    # NNet input methods
    def get_input_info_flat_sg(self):
        return [4], [self.dim]  # [sx, sy, gx, gy], one-hot depth = dim

    def get_input_info_flat_sga(self):
        return [4, 1], [self.dim, len(self.actions_list)]

    def to_np_flat_sg(self, states, goals):
        data = np.stack([
            np.array([s.pos[0] for s in states]),
            np.array([s.pos[1] for s in states]),
            np.array([g.pos[0] for g in goals]),
            np.array([g.pos[1] for g in goals]),
        ], axis=1)
        return [data]

    def to_np_flat_sga(self, states, goals, actions):
        return self.to_np_flat_sg(states, goals) + [
            np.expand_dims(np.array(self.actions_to_indices(actions)), 1)
        ]


@domain_factory.register_parser("myfwpuzzle")
class MyFWPuzzleParser(Parser):
    def parse(self, args_str: str) -> Dict[str, Any]:
        return {"dim": int(args_str)}

    def help(self) -> str:
        return "An integer for the dimension. E.g. 'myfwpuzzle.10'"
```

**Key differences from Templates A/B:**
- Overrides `next_state()` directly instead of `_next_state_np()` — simpler, no numpy batch conversion needed
- Implements `sample_start_states()` and `sample_goal_from_state()` instead of `sample_goalstate_goal_pairs()` and `rev_action()`
- **Compatible supervised pathfinders:** `sup_v_rw` and `sup_q_rw` (NOT `sup_v_rw_rev` or `sup_q_rw_rev`)

---

## TEMPLATE D: Custom NNetInput Registration

**Use when:** Your puzzle's state doesn't fit neatly into "flat array of tiles" or "2D grid". For example, Sokoban has 4 separate channels (walls, boxes, agent, targets) that get stacked into a custom representation.

Instead of using `Has*In` mixins, you define a standalone `NNetInput` class:

```python
# Add this to your domain file, AFTER the domain class

from deepxube.base.nnet_input import FlatIn, StateGoalIn
from deepxube.factories.nnet_input_factory import register_nnet_input

@register_nnet_input("mypuzzle", "mypuzzle_custom_input")
class MyCustomInput(FlatIn["MyPuzzle"], StateGoalIn["MyPuzzle", MyState, MyGoal]):
    """Custom NNet input that combines multiple state channels."""

    def get_input_info(self):
        total_dim = 400  # your custom total input size
        return [total_dim], [1]  # [dims], [one_hot_depths]

    def to_np(self, states, goals):
        # Build a custom numpy representation
        # Example: stack multiple binary maps into a flat vector
        reps = []
        for state, goal in zip(states, goals):
            rep = np.concatenate([
                state.walls.flatten(),
                state.boxes.flatten(),
                state.agent_map.flatten(),
                goal.targets.flatten(),
            ])
            reps.append(rep)
        return [np.stack(reps, axis=0).astype(np.uint8)]
```

**Important:** When using custom `NNetInput`, your domain class does NOT inherit `HasFlatSGIn` or `HasTwoDSGIn`. Remove those mixins. The custom input is registered separately by the `@register_nnet_input` decorator.

---

## TEMPLATE E: Logic / ASP / PDDL Domain (Advanced)

**Use when:** Your puzzle is defined using logical rules (Answer Set Programming).

This pathway is advanced and requires understanding the `clingo` ASP solver. The key methods are:

```python
from deepxube.base.domain import GoalGrndAtoms, SupportsPDDL
from deepxube.logic.logic_objects import Atom, Model

@domain_factory.register_class("mylogicpuzzle")
class MyLogicPuzzle(
    GoalGrndAtoms[LogicState, LogicAction, LogicGoal],
    # ... other mixins
):
    def state_to_model(self, states: List[LogicState]) -> List[Model]:
        """Convert each state to a frozenset of ground atoms."""
        pass

    def model_to_state(self, models: List[Model]) -> List[LogicState]:
        """Reconstruct State objects from ground atom sets."""
        pass

    def goal_to_model(self, goals: List[LogicGoal]) -> List[Model]:
        """Convert goals to ground atom sets."""
        pass

    def model_to_goal(self, models: List[Model]) -> List[LogicGoal]:
        pass

    def get_bk(self) -> List[str]:
        """Return background knowledge (static ASP rules)."""
        pass

    def get_ground_atoms(self) -> List[Atom]:
        """Return all possible ground atoms for state construction."""
        pass

    def on_model(self, m) -> Model:
        """Process clingo solver results."""
        pass

    def start_state_fixed(self, states) -> List[Model]:
        """Given start state, return what must also be true in goal (e.g. walls)."""
        pass
```

This is the least-documented pathway. For a working reference, study the `Sokoban` domain which uses `GoalSampleableFromState`, or consult `deepxube/logic/asp.py` for the ASP integration.

---

## Verification: Testing Your Domain

After creating your domain file, verify it works before training:

### Step 1: Check Registration
```bash
python -m deepxube domain_info --names mypuzzle
```
This prints:
- Which mixins your domain has
- Which NNet inputs are registered
- Which pathfinders are compatible

If your domain doesn't appear, check that the file is in `./domains/` or `deepxube/domains/` and has no import errors.

### Step 2: Check Compatible Heuristics
```bash
python -m deepxube heuristic_info
```
Shows all registered heuristic networks and what input type they expect. Make sure at least one matches your domain's registered NNet inputs.

### Step 3: Check Compatible Pathfinders
```bash
python -m deepxube pathfinding_info
```
Shows all pathfinders and what domain type they require. Cross-reference with your domain's mixins from Step 1.

### Step 4: Test Timing
```bash
python -m deepxube time --domain mypuzzle --step_max 10
```
Tests basic operations: generating states, taking actions, checking if solved. If this crashes, your domain has a bug in its core methods.

### Step 5: Visualize (Optional)
If your domain implements `StateGoalVizable`:
```bash
python -m deepxube viz --domain mypuzzle --steps 10
```

---

## Optional Mixins

These are not required but enhance your domain's capabilities:

| Mixin | What it enables | Method to implement |
|---|---|---|
| `StateGoalVizable` | `python -m deepxube viz` command | `visualize_state_goal(state, goal, fig)` |
| `StringToAct` | Interactive stepping in viz mode | `string_to_action(str)`, `string_to_action_help()` |

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| Domain not found | File not auto-imported | Check file location and syntax errors |
| "Cannot build heur nnet" | NNet input type mismatch | Run `domain_info` and `heuristic_info` to check compatibility |
| "No updaters for Domain" | Pathfinder requires a mixin you don't have | Run `pathfinding_info` and check domain type requirements |
| Assertion in `expand` | `get_actions_fixed()` returns empty list | Make sure you return at least one action |
| Shape mismatch in training | `get_input_info_*` doesn't match `to_np_*` output | Verify array dimensions match |

---

## Next Step: Training

Once your domain passes verification, proceed to **TRAINING_GUIDE.md** for the full training pipeline:
1. Initialize the network with supervised random walks
2. Refine with RL (A* or Beam Search)
3. Generate test instances and solve them
