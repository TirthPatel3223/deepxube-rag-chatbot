# DeepXube: Concrete Examples & Training Recipes

---
**[RAG SYSTEM INSTRUCTION - DO NOT SHOW TO USER]**
This file provides concrete, real-world examples from the DeepXube codebase. Use it when users ask:
- "Show me what a domain looks like"
- "How does X puzzle represent its state?"
- "What training command should I use for my puzzle?"
- "Why would I pick A* over Beam Search?"

Cross-reference with `ADDING_NEW_DOMAIN.md` for templates and `TRAINING_GUIDE.md` for full CLI docs.
---

---

# PART 1: State Representation Examples

Each example below shows **how a real puzzle in the codebase represents its state** and feeds it to the neural network. Study the one closest to your puzzle.

---

## Example 1: Rubik's Cube — 1D Flat Array (Permutation Puzzle)

**Source:** `deepxube/domains/cube3.py`
**Registered as:** `cube3`
**Pattern:** Template A (1D Flat + Fixed Actions + Reversible)

### How the state is represented

The 3×3 Rubik's Cube has 6 faces × 9 stickers = **54 colour values**. Each sticker holds an integer 0–5 representing its colour. The state is stored as a flat `uint8` numpy array of length 54.

```python
class Cube3State(State):
    __slots__ = ['colors', 'hash']

    def __init__(self, colors: NDArray[np.uint8]):
        self.colors = colors          # shape: (54,), values 0-5
        self.hash: Optional[int] = None

    def __hash__(self):
        if self.hash is None:
            self.hash = hash(self.colors.tobytes())
        return self.hash

    def __eq__(self, other):
        if isinstance(other, Cube3State):
            return np.array_equal(self.colors, other.colors)
        return NotImplemented
```

**Solved state:** `[0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 2,2,..., 5,5,5,5,5,5,5,5,5]`
(Each face is one solid colour.)

### How it feeds into the neural network

The domain tells the network: "I have 54 integers, each with 6 possible values (one-hot depth = 6)."

```python
def get_input_info_flat_sg(self):
    return [54], [6]    # [num_elements], [one_hot_depth_per_element]

def to_np_flat_sg(self, states, goals):
    return [np.stack([x.colors for x in states], axis=0).astype(np.uint8)]
```

The `resnet_fc` network one-hot encodes each of the 54 positions into a 6-dim vector → 54×6 = **324-dimensional input**, then passes through FC residual blocks.

### How actions work

12 quarter-turn moves (6 faces × clockwise/counterclockwise). Each move is a precomputed permutation of sticker indices.

```python
atomic_actions = ['U-1','U1','D-1','D1','L-1','L1','R-1','R1','B-1','B1','F-1','F1']

def rev_action(self, states, actions):
    # Even index ↔ odd index: U-1 reverses U1, etc.
    return [Cube3Action(a.action + 1 if a.action % 2 == 0 else a.action - 1)
            for a in actions]
```

### Mixins used

```python
@domain_factory.register_class("cube3")
class Cube3(
    NextStateNPActsEnumFixed,        # Vectorized batch transitions via numpy
    GoalStartRevWalkableActsRev,     # Generate training data by walking backward from goal
    HasFlatSGActsEnumFixedIn,        # Register flat input for V and QFix networks
    HasFlatSGAIn,                    # Register flat+action input for QIn networks
    StateGoalVizable,                # Enable visualization
    StringToAct,                     # Interactive mode
):
```

### CLI usage
```bash
--domain cube3
--heur resnet_fc.5000H_4B_bn --heur_type V
--pathfind sup_v_rw_rev          # supervised init (reverse walk)
--pathfind graph_v.10B_1.0W      # RL refinement (A*)
```

---

## Example 2: 15-Puzzle (NPuzzle) — 1D Flat Array (Sliding Tile)

**Source:** `deepxube/domains/npuzzle.py`
**Registered as:** `npuzzle`
**Pattern:** Template A variant (1D Flat + Fixed Actions + Reversible, direct `next_state` override)

### How the state is represented

A 4×4 grid with tiles numbered 1–15 and one blank (0). Stored as a flat array of length 16.

```python
class NPState(State):
    def __init__(self, tiles: NDArray):
        self.tiles = tiles    # e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
```

**Solved state:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]`

### NNet input

```python
def get_input_info_flat_sg(self):
    return [16], [16]    # 16 positions, each can hold values 0-15 (one-hot depth = 16)

def to_np_flat_sg(self, states, goals):
    return [np.stack([x.tiles for x in states], axis=0)]
```

One-hot encoding: 16 positions × 16 values = **256-dimensional input**.

### Key difference from Cube3

NPuzzle overrides `next_state()` directly instead of using `_next_state_np()`. It precomputes a swap table for efficiency but doesn't route through the `NextStateNP` mixin:

```python
def next_state(self, states, actions):
    states_np = np.stack([x.tiles for x in states], axis=0)
    _, z_idxs = np.where(states_np == 0)   # find blank position
    # ... swap blank with adjacent tile based on action
    return [NPState(x) for x in states_next_np], transition_costs
```

### CLI usage
```bash
--domain npuzzle.4              # 4x4 = 15-puzzle
--heur resnet_fc.1000H_4B_bn --heur_type V
```

---

## Example 3: LightsOut — 2D Spatial Grid (Toggle Puzzle)

**Source:** `deepxube/domains/lightsout.py`
**Registered as:** `lightsout`
**Pattern:** Template B (2D Spatial + Fixed Actions + Reversible)

### How the state is represented

A dim×dim binary grid (0=off, 1=on). Stored as a flat `uint8` array but reshaped to 2D for the CNN.

```python
class LOState(State):
    def __init__(self, tiles: NDArray[np.uint8]):
        self.tiles = tiles     # shape: (49,) for a 7x7 grid, values 0 or 1
```

**Solved state:** All zeros (all lights off).

### NNet input — TWO representations registered

LightsOut registers **both flat AND 2D** inputs, making it compatible with both `resnet_fc` and `resnet_2d`:

```python
# Flat input (for resnet_fc)
def get_input_info_flat_sg(self):
    return [49], [1]        # 49 binary values, no one-hot needed

def to_np_flat_sg(self, states, goals):
    return [np.stack([x.tiles for x in states], axis=0).astype(np.uint8)]

# 2D input (for resnet_2d CNN)
def get_input_info_2d_sg(self):
    return [1], (7, 7), [1], 1   # 1 channel, 7x7 grid, one-hot depth 1

def to_np_2d_sg(self, states, goals):
    tiles_flat = np.stack([x.tiles for x in states], axis=0).astype(np.uint8)
    return [tiles_flat.reshape((-1, 1, 7, 7))]   # (batch, channels, H, W)
```

### Actions: self-inverse (toggling twice = no change)

```python
def rev_action(self, states, actions):
    return actions    # Every toggle is its own inverse!
```

49 actions for a 7×7 grid (one per cell). Each toggle flips the cell and its 4 cardinal neighbours.

### Mixins used

```python
@domain_factory.register_class("lightsout")
class LightsOut(
    NextStateNPActsEnumFixed,
    GoalStartRevWalkableActsRev,
    HasFlatSGActsEnumFixedIn,     # Flat input → works with resnet_fc
    HasFlatSGAIn,                 # Flat+action → works with QIn
    HasTwoDSGActsEnumFixedIn,     # 2D spatial → works with resnet_2d
):
```

### CLI usage
```bash
--domain lightsout.7
# CNN path:
--heur resnet_2d.64C_4B_bn --heur_type V
# OR flat path:
--heur resnet_fc.1000H_4B_bn --heur_type V
```

---

## Example 4: Grid Navigation — Forward-Walk (No Reversal Needed)

**Source:** `deepxube/domains/grid.py`
**Registered as:** `grid`
**Pattern:** Template C (Forward-Walk + Fixed Actions)

### How the state is represented

Just an (x, y) position on a dim×dim grid. No numpy array needed.

```python
class GridState(State):
    def __init__(self, robot_x: int, robot_y: int):
        self.robot_x = robot_x
        self.robot_y = robot_y
```

### NNet input

4 integers `[state_x, state_y, goal_x, goal_y]`, each one-hot encoded with depth=dim:

```python
def get_input_info_flat_sg(self):
    return [4], [self.dim]      # 4 values, one-hot depth = grid dimension

def to_np_flat_sg(self, states, goals):
    return [np.stack([
        np.array([s.robot_x for s in states]),
        np.array([s.robot_y for s in states]),
        np.array([g.robot_x for g in goals]),
        np.array([g.robot_y for g in goals]),
    ], axis=1)]
```

### Forward-walk pattern (StartGoalWalkable)

Grid doesn't need `rev_action` or `sample_goalstate_goal_pairs`. Instead:

```python
def sample_start_states(self, num_states):
    return [GridState(np.random.randint(self.dim), np.random.randint(self.dim))
            for _ in range(num_states)]

def sample_goal_from_state(self, states_start, states_goal):
    return [GridGoal(s.robot_x, s.robot_y) for s in states_goal]
```

Training generates data by: random start → walk forward → the end state becomes the goal.

### Direct next_state override (no NextStateNP)

```python
def next_state(self, states, actions):
    states_next = []
    for state, action in zip(states, actions):
        if action.action == 0:    # up
            states_next.append(GridState(min(state.robot_x + 1, self.dim - 1), state.robot_y))
        elif action.action == 1:  # down
            states_next.append(GridState(max(state.robot_x - 1, 0), state.robot_y))
        # ... left, right
    return states_next, [1.0] * len(states)
```

### CLI usage
```bash
--domain grid.7
--heur resnet_fc.100H_2B_bn --heur_type V
--pathfind sup_v_rw        # NOTE: sup_v_rw (forward), NOT sup_v_rw_rev
```

---

## Example 5: Sokoban — Custom NNetInput (Multi-Channel Board)

**Source:** `deepxube/domains/sokoban.py`
**Registered as:** `sokoban`
**Pattern:** Template D (Custom NNetInput + Forward-Walk)

### How the state is represented

A Sokoban board has multiple layers that can't be collapsed into a single tile array:

```python
class SkState(State):
    def __init__(self, agent: NDArray, boxes: NDArray, walls: NDArray):
        self.agent = agent       # shape: (2,) — row, col position
        self.boxes = boxes       # shape: (10, 10) — binary box map
        self.walls = walls       # shape: (10, 10) — binary wall map
```

### Custom NNetInput (NOT using Has*In mixins)

Sokoban defines its own `NNetInput` class and registers it separately:

```python
from deepxube.factories.nnet_input_factory import register_nnet_input

@register_nnet_input("sokoban", "sokoban_nnet_input")
class SkNNetInput(FlatIn[Sokoban], StateGoalIn[Sokoban, SkState, SkGoal]):

    def get_input_info(self):
        return [400], [1]    # 4 channels × 10×10 = 400, binary (no one-hot)

    def to_np(self, states, goals):
        walls = np.stack([s.walls for s in states], axis=0)
        boxes = np.stack([s.boxes for s in states], axis=0)
        targets = np.stack([g.boxes for g in goals], axis=0)
        agents = np.zeros((len(states), 10, 10))
        for i, s in enumerate(states):
            agents[i, s.agent[0], s.agent[1]] = 1

        rep = np.stack([walls, boxes, agents, targets], axis=1)   # (N, 4, 10, 10)
        return [rep.reshape((rep.shape[0], -1)).astype(np.uint8)]  # flatten to (N, 400)
```

**Key insight:** The 4 channels (walls, boxes, agent position, target positions) are stacked and flattened into a single 400-element vector. The `@register_nnet_input` decorator handles registration — the domain class itself has NO `Has*In` mixins.

### CLI usage
```bash
--domain sokoban
--heur resnet_fc.5000H_4B_bn --heur_type V
--pathfind sup_v_rw          # Forward-walk (Sokoban uses StartGoalWalkable)
```

---

# PART 2: Training Approach Examples & Decision Guide

## When to Use Each Training Approach

| Approach | Pathfinder | When to use | Analogy |
|---|---|---|---|
| **Supervised** | `sup_v_rw_rev` | **Always first.** Gives the network a rough distance estimate. | Teaching by showing flash cards |
| **A* (Graph Search)** | `graph_v` | When branching factor is small enough for A* to find solutions. | Learning by practicing real problem-solving |
| **Beam Search** | `beam_v` | When A* runs out of memory due to huge state spaces. | Focused practice — only keep top K attempts |
| **Policy Only** | `beam_p` | When you want a fast action-selector without any search at inference. | Memorizing the best move for each state |

---

## Recipe 1: The Standard DeepCubeA Pipeline (Rubik's Cube Style)

**Best for:** Permutation puzzles with small branching factor (6–20 actions), reversible moves, and moderate solution depth (≤30 moves).

**Why this works:** A* can explore enough of the tree to find solutions when guided by even a mediocre heuristic. The reverse-walk supervised init gives a strong enough starting point.

```bash
# Step 1: Supervised initialization
python -m deepxube train \
  --domain cube3 \
  --heur resnet_fc.5000H_4B_bn --heur_type V \
  --pathfind sup_v_rw_rev \
  --dir ./cube3_sup \
  --batch_size 10000 --max_itrs 100000 --step_max 30

# Step 2: RL with A*
python -m deepxube train \
  --domain cube3 \
  --heur resnet_fc.5000H_4B_bn --heur_type V \
  --pathfind graph_v.100B_1.0W \
  --dir ./cube3_rl \
  --batch_size 10000 --max_itrs 1000000 --step_max 30 \
  --search_itrs 5000

# Step 3: Solve
python -m deepxube problem_inst --domain cube3 --step_min 1 --step_max 30 --num 100 --file cube3_test.pkl
python -m deepxube solve \
  --domain cube3 \
  --heur resnet_fc.5000H_4B_bn --heur_file ./cube3_rl/heur_nnet.pt --heur_type V \
  --pathfind graph_v.1000B_1.0W \
  --file cube3_test.pkl --results ./cube3_results/
```

---

## Recipe 2: Beam Search Pipeline (Large State Space)

**Best for:** Puzzles with massive branching factor OR very deep solutions where A* exhausts memory. Examples: Sokoban (solutions can be 100+ moves), large tile puzzles.

**Why beam over A*:** A* keeps ALL expanded nodes in memory. For a puzzle with 49 actions (LightsOut 7×7) and solutions 20 moves deep, A* would need to store ~49^20 nodes. Beam search caps memory at beam_size × depth.

```bash
# Step 1: Supervised initialization
python -m deepxube train \
  --domain lightsout.7 \
  --heur resnet_2d.64C_4B_bn --heur_type V \
  --pathfind sup_v_rw_rev \
  --dir ./lo_sup \
  --batch_size 1000 --max_itrs 50000 --step_max 30

# Step 2: RL with Beam Search
python -m deepxube train \
  --domain lightsout.7 \
  --heur resnet_2d.64C_4B_bn --heur_type V \
  --pathfind beam_v.100B_1.0T_0.1E \
  --dir ./lo_beam \
  --batch_size 1000 --max_itrs 100000 --step_max 30 \
  --search_itrs 200

# Step 3: Solve
python -m deepxube problem_inst --domain lightsout.7 --step_min 1 --step_max 30 --num 100 --file lo_test.pkl
python -m deepxube solve \
  --domain lightsout.7 \
  --heur resnet_2d.64C_4B_bn --heur_file ./lo_beam/heur_nnet.pt --heur_type V \
  --pathfind beam_v.1000B \
  --file lo_test.pkl --results ./lo_results/
```

---

## Recipe 3: Q-Network Pipeline (Act Without Simulation)

**Best for:** When `next_state()` is expensive to compute and you want to pick actions directly from Q-values without simulating children.

**Why QFix over V:** With a V-network, search must call `next_state()` for every child to evaluate V(child). With QFix, the network outputs Q-values for ALL actions in a single forward pass — no `next_state()` calls needed during greedy action selection.

```bash
# Step 1: Supervised Q initialization
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn --heur_type QFix \
  --pathfind sup_q_rw_rev \
  --dir ./q_sup \
  --batch_size 1000 --max_itrs 50000 --step_max 30

# Step 2: RL with A* using Q-values
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn --heur_type QFix \
  --pathfind graph_q.10B_1.0W_0.1E \
  --dir ./q_rl \
  --batch_size 1000 --max_itrs 100000 --step_max 30

# Step 3: Solve using Q-guided A*
python -m deepxube solve \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn --heur_file ./q_rl/heur_nnet.pt --heur_type QFix \
  --pathfind graph_q.100B_1.0W \
  --file test.pkl --results ./q_results/
```

---

## Recipe 4: V + Policy Combination

**Best for:** Domains where the action space is too large to enumerate, or where you want to prune the search tree. The policy proposes which actions to try, and the V-network evaluates them.

**Why add a policy:** In a puzzle with 1000 possible moves per state, A* would expand all 1000 children. A policy narrows this to the 10 most promising moves, dramatically speeding up search.

```bash
# Step 1: Supervised V initialization (same as Recipe 1)
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn --heur_type V \
  --pathfind sup_v_rw_rev \
  --dir ./vp_sup \
  --batch_size 1000 --max_itrs 50000 --step_max 30

# Step 2: Joint V + Policy training with A*
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn --heur_type V \
  --policy resnet_fc.1000H_4B_10E_bn \
  --pathfind graph_v_p.10B_1.0W_0.1E \
  --dir ./vp_rl \
  --batch_size 1000 --max_itrs 100000 --step_max 30

# Step 3: Solve with policy-guided A*
python -m deepxube solve \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn --heur_file ./vp_rl/heur_nnet.pt --heur_type V \
  --policy resnet_fc.1000H_4B_10E_bn --policy_file ./vp_rl/policy_nnet.pt \
  --pathfind graph_v_p.100B_1.0W \
  --file test.pkl --results ./vp_results/
```

---

## Recipe 5: Forward-Walk Domain (Sokoban / Grid Style)

**Best for:** Puzzles where moves can't be reversed. Training instances are generated by starting from a known-good state and walking forward.

**Key difference:** Uses `sup_v_rw` (NOT `sup_v_rw_rev`) because there's no reverse walk.

```bash
# Step 1: Supervised init with FORWARD walks
python -m deepxube train \
  --domain grid.10 \
  --heur resnet_fc.100H_2B_bn --heur_type V \
  --pathfind sup_v_rw \
  --dir ./grid_sup \
  --batch_size 1000 --max_itrs 50000 --step_max 30

# Step 2: RL refinement
python -m deepxube train \
  --domain grid.10 \
  --heur resnet_fc.100H_2B_bn --heur_type V \
  --pathfind graph_v.10B_1.0W_0.1E \
  --dir ./grid_rl \
  --batch_size 1000 --max_itrs 50000 --step_max 30
```

---

## Recipe 6: Hard Puzzles with HER + LHBL

**Best for:** Extremely difficult puzzles where the initial heuristic is poor and A* rarely finds solutions early in training.

**Why HER:** If search fails to reach the goal, HER relabels the deepest-reached state AS the goal. This way every search attempt produces useful training data.

**Why LHBL (`--backup -1`):** Standard Bellman backup can get trapped in dead-end regions. LHBL uses tree backup from root — it looks ahead a limited number of steps and trusts the network's value estimate at the frontier.

**Domain requirement:** HER needs `sample_goal_from_state()` — your domain must support deriving a goal from an arbitrary state.

```bash
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn --heur_type V \
  --pathfind graph_v.10B_1.0W_0.1E \
  --dir ./hard_rl \
  --batch_size 1000 --max_itrs 200000 --step_max 50 \
  --search_itrs 500 \
  --her \
  --backup -1 \
  --rb 5
```

---

# PART 3: Decision Flowchart

```
START: "I have a new puzzle to solve"
  │
  ├─ Can you represent the state as a flat array of tokens?
  │   ├─ YES → Is it naturally a 2D grid?
  │   │   ├─ YES → Use Template B (2D) + resnet_2d
  │   │   └─ NO  → Use Template A (1D) + resnet_fc
  │   └─ NO → Do you need multiple channels/layers?
  │       ├─ YES → Use Template D (Custom NNetInput) + resnet_fc
  │       └─ NO  → Use Template E (Logic/ASP)
  │
  ├─ Are all moves available in every state?
  │   ├─ YES → Use ActsEnumFixed
  │   └─ NO  → Override get_state_actions() or use ActsEnum
  │
  ├─ Can every move be reversed?
  │   ├─ YES → Use GoalStartRevWalkableActsRev
  │   │         Supervised: sup_v_rw_rev / sup_q_rw_rev
  │   └─ NO  → Use StartGoalWalkable
  │             Supervised: sup_v_rw / sup_q_rw
  │
  ├─ How big is the branching factor?
  │   ├─ Small (≤20 actions) → RL with A*: graph_v
  │   └─ Large (>20 actions) → RL with Beam: beam_v
  │       OR add a Policy to prune: graph_v_p / beam_v_p
  │
  └─ How hard is the puzzle?
      ├─ Moderate (solutions ≤30 steps) → Standard pipeline (Recipe 1)
      └─ Very hard (solutions >30 steps, rarely finds goal) → Add HER + LHBL (Recipe 6)
```

---

# PART 4: Training Hyperparameter Quick Reference

| Puzzle Difficulty | `--step_max` | `--search_itrs` | `--batch_size` | Network Size |
|---|---|---|---|---|
| Easy (Grid, small puzzles) | 10–20 | 50–100 | 1000 | `100H_2B` |
| Medium (15-Puzzle, LightsOut) | 20–50 | 100–500 | 1000–5000 | `1000H_4B` |
| Hard (Rubik's Cube) | 30 | 1000–5000 | 10000 | `5000H_4B` |
| Very Hard (Sokoban) | 50–100 | 500–2000 | 1000 | `5000H_4B` + HER |

> **Note:** These are starting-point estimates. The professor will add validated benchmarks with exact numbers for each existing domain in a future update. <!-- TODO: Add empirical training results here -->
