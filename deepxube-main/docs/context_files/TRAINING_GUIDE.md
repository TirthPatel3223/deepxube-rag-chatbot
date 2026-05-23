# DeepXube: Comprehensive Training, Solving & Evaluation Guide

---
**[RAG SYSTEM INSTRUCTION - DO NOT SHOW TO USER]**
When a user asks how to train a heuristic in DeepXube, guide them through these decisions:

**DECISION 1 — Network Output Type:**
*"What should your network predict?"*
- Distance to goal → `V` (recommended for most puzzles)
- Value of each action → `QFix` (for fixed action sets, no simulation needed at inference)
- Value of one specific action → `QIn` (for variable action spaces)

**DECISION 2 — Have you trained before?**
- No → Start with **Supervised Random Walks** (Section 3)
- Yes, I have a pretrained model → Go to **RL refinement** (Section 4 or 5)

**DECISION 3 — Search budget:**
- My puzzle has manageable branching → **A* Graph Search** (Section 4)
- My puzzle has huge branching or needs deep solutions → **Beam Search** (Section 5)

**IMPORTANT:** After the user finishes creating their domain using `ADDING_NEW_DOMAIN.md`, reassure them that **NO further code changes are required** for training. DeepXube's factories handle it automatically — they only need to run the right CLI command.
---

## 1. The Full Pipeline (Overview)

Training a heuristic in DeepXube follows this pipeline:

```
┌─────────────────────┐
│  1. Create Domain    │  ← ADDING_NEW_DOMAIN.md
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  2. Verify Domain    │  domain_info, time, viz
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  3. Supervised Init  │  sup_v_rw_rev / sup_v_rw  (gives the network a basic sense of distance)
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  4. RL Refinement    │  graph_v / beam_v  (searches for real solutions, trains on what it finds)
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  5. Generate Tests   │  problem_inst  (create puzzle instances to solve)
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  6. Solve & Evaluate │  solve  (use the trained network to find solutions)
└────────┬────────────┘
         ▼
┌─────────────────────┐
│  7. Visualize        │  train_summary, viz --soln
└─────────────────────┘
```

---

## 2. Choosing the Network Output Type (`--heur_type`)

### A. Value Functions (`--heur_type V`)
**What:** Network takes (State, Goal) → scalar estimated cost-to-go.
**When to use:** Most puzzles. Works with A* search (`graph_v`) where the search expands nodes and evaluates V(child).
**Recommended as default.**

### B. Q-Functions — Fixed Actions (`--heur_type QFix`)
**What:** Network takes (State, Goal) → vector of Q-values, one per action.
**When to use:** Fixed action spaces where you want to act greedily without simulating next states (no `next_state()` call at inference). Only works if the domain inherits `ActsEnumFixed`.

### C. Q-Functions — Action as Input (`--heur_type QIn`)
**What:** Network takes (State, Goal, Action) → scalar Q-value.
**When to use:** Variable action spaces where actions differ per state. Domain must provide `HasFlatSGAIn` or equivalent.

### Network Architecture Options

| Architecture | CLI flag | Input type | Best for |
|---|---|---|---|
| FC-ResNet | `resnet_fc` | `FlatIn` | 1D flat states (Template A, C) |
| Conv-ResNet | `resnet_2d` | `TwoDIn` | 2D spatial states (Template B) |
| Custom | user-defined | user-defined | Special cases (Template D) |

**`resnet_fc` argument format:**
```
resnet_fc.<int>H_<int>B_bn
```
- `<int>H` — hidden dimension (width of residual layers). E.g. `1000H`
- `<int>B` — number of residual blocks (depth). E.g. `4B`
- `bn` — enable batch normalization (optional, recommended)
- `wn` — enable weight normalization (optional, alternative to bn)

Examples: `resnet_fc.1000H_4B_bn`, `resnet_fc.500H_2B_wn`, `resnet_fc.100H_2B_bn`

**`resnet_2d` argument format:**
```
resnet_2d.<int>C_<int>B_bn
```
- `<int>C` — number of channels. E.g. `64C`
- `<int>B` — number of residual blocks. E.g. `4B`
- `bn` / `wn` — batch/weight normalization

Examples: `resnet_2d.64C_4B_bn`, `resnet_2d.32C_2B_bn`

---

## 3. Step 1: Supervised Random Walks (Network Initialization)

**What it does:** Starts at the Goal State, randomly walks backward (or forward), and trains the network to predict how many steps it took. This gives the network a rough sense of distance.

**Why you MUST do this first:** An untrained network outputs random values. If you drop it directly into A* search, the search will expand nodes in random order, run out of memory, and learn nothing. Supervised initialization gives it a basic distance estimate so that RL search can actually find solutions.

### Available Pathfinders

| Pathfinder | Network type | Domain requirement |
|---|---|---|
| `sup_v_rw` | V-network | `StartGoalWalkable` (Template C) |
| `sup_v_rw_rev` | V-network | `GoalStartRevWalkable` (Template A, B) |
| `sup_q_rw` | Q-network | `StartGoalWalkable` (Template C) |
| `sup_q_rw_rev` | Q-network | `GoalStartRevWalkableActsRev` (Template A, B) |

**If your domain uses Template A or B** (reverse-walkable), use `sup_v_rw_rev` or `sup_q_rw_rev`.
**If your domain uses Template C** (forward-walkable), use `sup_v_rw` or `sup_q_rw`.

### CLI Example — Supervised V-Network (Reverse-Walkable Domain)
```bash
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.100H_2B_bn \
  --heur_type V \
  --pathfind sup_v_rw_rev \
  --dir ./saved_models_sup \
  --batch_size 1000 \
  --max_itrs 50000 \
  --step_max 30
```

### CLI Example — Supervised V-Network (Forward-Walkable Domain)
```bash
python -m deepxube train \
  --domain myfwpuzzle.10 \
  --heur resnet_fc.100H_2B_bn \
  --heur_type V \
  --pathfind sup_v_rw \
  --dir ./saved_models_sup \
  --batch_size 1000 \
  --max_itrs 50000 \
  --step_max 30
```

### CLI Example — Supervised V-Network (2D Domain with CNN)
```bash
python -m deepxube train \
  --domain mygridpuzzle.7 \
  --heur resnet_2d.64C_4B_bn \
  --heur_type V \
  --pathfind sup_v_rw_rev \
  --dir ./saved_models_sup_2d \
  --batch_size 1000 \
  --max_itrs 50000 \
  --step_max 30
```

---

## 4. Step 2a: RL Refinement via A* Graph Search

**What it does:** Uses the pretrained network as a heuristic to guide A* search. When A* finds a solution (or a better path), the actual discovered cost becomes the new training target. This is the classic DeepCubeA approach (Approximate Value Iteration).

**When to use:** After supervised initialization. Best when the branching factor is manageable (e.g., Rubik's Cube with 18 moves, 15-Puzzle with 2-4 moves).

**Domain requirement:** Must implement `ActsEnum` (so states can be expanded). All templates except the Logic template satisfy this.

### Available Pathfinders

| Pathfinder | Functions | Domain type |
|---|---|---|
| `graph_v` | V heuristic only | `ActsEnum` |
| `graph_q` | Q heuristic only | `ActsEnum` |
| `graph_v_p` | V heuristic + Policy | Any `Domain` |
| `graph_q_p` | Q heuristic + Policy | Any `Domain` |

### CLI Argument Format for Graph Search
```
graph_v.<int>B_<float>W_<float>E
```
- `<int>B` — batch size: how many nodes to pop from the open set per iteration. E.g. `10B`
- `<float>W` — weight in [0, 1]: 0 = greedy best-first, 1 = pure A*. E.g. `1.0W`
- `<float>E` — epsilon in [0, 1]: probability of popping a random node instead of the best. E.g. `0.1E`

All three are optional and can appear in any order. Defaults: batch_size=1, weight=1.0, eps=0.0.

Examples: `graph_v.10B_1.0W_0.1E`, `graph_v.1B_0.5W`, `graph_q.10B`

### CLI Example — A* with V-Network
```bash
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.100H_2B_bn \
  --heur_type V \
  --pathfind graph_v.10B_1.0W_0.1E \
  --dir ./saved_models_rl \
  --batch_size 1000 \
  --max_itrs 100000 \
  --step_max 30 \
  --search_itrs 100
```

---

## 5. Step 2b: RL Refinement via Beam Search

**What it does:** Like A*, but instead of keeping the entire search frontier, it only keeps the top K (the "beam width") best states at each depth. Trades optimality for memory efficiency.

**When to use:** When A* runs out of RAM (huge branching factor), or when solutions are very deep.

### Available Pathfinders

| Pathfinder | Functions | Domain type |
|---|---|---|
| `beam_v` | V heuristic only | `ActsEnum` |
| `beam_q` | Q heuristic only | `ActsEnum` |
| `beam_p` | Policy only | Any `Domain` |
| `beam_v_p` | V heuristic + Policy | Any `Domain` |
| `beam_q_p` | Q heuristic + Policy | Any `Domain` |

### CLI Argument Format for Beam Search
```
beam_v.<int>B_<float>T_<float>E
```
- `<int>B` — beam size: how many states to keep per depth level. E.g. `100B`
- `<float>T` — temperature for Boltzmann selection: 0 = pure argmax top-k, >0 = stochastic. E.g. `1.0T`
- `<float>E` — epsilon: probability of replacing a selected state with a random one. E.g. `0.1E`

All three are optional. Defaults: beam_size=1, temp=0.0, eps=0.0.

Examples: `beam_v.100B_1.0T_0.1E`, `beam_v.50B`, `beam_q.100B_0.0T`

### CLI Example — Beam Search with V-Network
```bash
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.100H_2B_bn \
  --heur_type V \
  --pathfind beam_v.100B_1.0T_0.1E \
  --dir ./saved_models_beam \
  --batch_size 1000 \
  --max_itrs 100000 \
  --step_max 30 \
  --search_itrs 100
```

---

## 6. Training a Policy Network

A policy network outputs a probability distribution over actions — "which move is most likely to lead toward the goal?" It can be used alone or alongside a V/Q network to prune the search tree.

### CLI Flags for Policy
```
--policy resnet_fc.100H_2B_10E_bn   # policy architecture (10E = encoding dim for VAE)
--policy_samp 10                     # number of actions to sample from policy
--policy_rand 5                      # number of random actions (prevents mode collapse)
```

### Example: Training V-Network + Policy Together (A* with policy pruning)
```bash
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.100H_2B_bn \
  --heur_type V \
  --policy resnet_fc.100H_2B_10E_bn \
  --pathfind graph_v_p.10B_1.0W_0.1E \
  --dir ./saved_models_vp \
  --batch_size 1000 \
  --max_itrs 100000 \
  --step_max 30
```

### Example: Training Policy Alone (Beam Search)
```bash
python -m deepxube train \
  --domain mypuzzle \
  --policy resnet_fc.100H_2B_10E_bn \
  --pathfind beam_p.100B_1.0T \
  --dir ./saved_models_policy \
  --batch_size 1000 \
  --max_itrs 100000 \
  --step_max 30
```

Use `--skip_heur` to skip heuristic training or `--skip_policy` to skip policy training if training both but want to freeze one.

---

## 7. Advanced Training Modifiers

### Bellman Backup (`--backup`)
Controls how the target value is calculated during RL training.
- **`--backup 1` (Default):** Standard Bellman backup. Target = cost of path found during search.
- **`--backup -1`:** Limited Horizon Bellman Lookahead (LHBL). Uses tree backup from the root — looks a limited number of steps ahead and trusts the network's evaluation of frontier states. Useful when dead-ends trap standard Bellman backups.

### Hindsight Experience Replay (`--her`)
**What:** If the RL search fails to reach the actual goal, it treats the deepest state it *did* reach as a "fake goal" and trains on that data instead of discarding it.

**When to use:** Extremely hard puzzles where the search rarely reaches the real goal early in training. Ensures the network always learns something from every search.

**Domain requirement:** The domain MUST implement `GoalSampleableFromState` (i.e., it needs a `sample_goal_from_state()` method). Domains using the `GoalGrndAtoms` mixin get this for free. For Template A/B domains, you would need to add this mixin and implement the method.

**Not compatible with supervised pathfinders** (`sup_*`).

### Replay Buffer (`--rb`)
- `--rb 0` (default): No replay buffer. Training waits for each update to finish, then samples from that update's data only. Faster updates but more susceptible to distribution shift.
- `--rb N`: Keep the last N updates' worth of data. Samples from the full buffer. More stable but slightly slower.

### Example: A* with LHBL and HER
```bash
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.100H_2B_bn \
  --heur_type V \
  --pathfind graph_v.10B_1.0W_0.1E \
  --dir ./saved_models_advanced \
  --batch_size 1000 \
  --max_itrs 100000 \
  --step_max 30 \
  --backup -1 \
  --her \
  --rb 5
```

---

## 8. Complete CLI Reference for `train`

### Required Arguments
| Flag | Description |
|---|---|
| `--domain` | Domain name and optional args. E.g. `mypuzzle` or `lightsout.7` |
| `--pathfind` | Pathfinding algorithm and args. E.g. `sup_v_rw_rev` or `graph_v.10B_1.0W` |
| `--dir` | Directory to save neural network checkpoints |
| `--step_max` | Max number of steps when generating problem instances |

### Heuristic Arguments
| Flag | Description |
|---|---|
| `--heur` | Heuristic network architecture. E.g. `resnet_fc.100H_2B_bn` |
| `--heur_type` | Output type: `V`, `QFix`, or `QIn` |
| `--skip_heur` | Skip heuristic training (only train policy) |

### Policy Arguments
| Flag | Description |
|---|---|
| `--policy` | Policy network architecture. E.g. `resnet_fc.100H_2B_10E_bn` |
| `--policy_samp` | Actions sampled from policy per state (default: 10) |
| `--policy_rand` | Random actions mixed in (default: 5) |
| `--skip_policy` | Skip policy training (only train heuristic) |

### Training Hyperparameters
| Flag | Default | Description |
|---|---|---|
| `--batch_size` | 1000 | Training batch size |
| `--max_itrs` | 100000 | Maximum training iterations |
| `--display` | 0 | Display frequency (0 = minimal output) |
| `--bal` | off | Balance step distribution by solve rate |
| `--rb` | 0 | Replay buffer size (0 = disabled) |
| `--up_lt` | inf | Loss threshold for update |

### Update / Search Arguments
| Flag | Default | Description |
|---|---|---|
| `--procs` | 1 | Parallel processes for data generation |
| `--up_itrs` | 100 | Iterations per update check |
| `--up_gen_itrs` | 100 | Iterations for generating data per update |
| `--search_itrs` | 1000 | Search iterations per problem instance |
| `--up_batch_size` | 100 | Problem instances generated per batch (lower if OOM) |
| `--up_nnet_batch_size` | 20000 | NNet batch size during update (lower if GPU OOM) |
| `--backup` | 1 | 1 = Bellman, -1 = LHBL |
| `--her` | off | Enable Hindsight Experience Replay |
| `--sync_main` | off | Use main network for search during update |

### Testing During Training
| Flag | Default | Description |
|---|---|---|
| `--t_file` | None | Pickle file with test instances |
| `--t_search_itrs` | 100 | Search iterations when testing |
| `--t_up_freq` | 10 | Test every N updates |
| `--t_pathfinds` | bwas | Comma-separated pathfinders for testing |
| `--t_init` | off | Test before training begins |

---

## 9. Generating Test Instances

Before solving, generate problem instances (state/goal pairs):

```bash
python -m deepxube problem_inst \
  --domain mypuzzle \
  --step_min 0 \
  --step_max 30 \
  --num 100 \
  --file test_instances.pkl
```

This creates a pickle file containing `{'states': [...], 'goals': [...]}`.

You can also use `--redo` to overwrite an existing file.

---

## 10. Solving Problem Instances

Use a trained network to solve puzzle instances:

```bash
python -m deepxube solve \
  --domain mypuzzle \
  --heur resnet_fc.100H_2B_bn \
  --heur_file ./saved_models_rl/heur_nnet.pt \
  --heur_type V \
  --pathfind graph_v.10B_1.0W \
  --file test_instances.pkl \
  --results ./results/
```

### Solve Arguments
| Flag | Description |
|---|---|
| `--heur_file` | Path to trained heuristic network weights |
| `--policy_file` | Path to trained policy network weights (if using policy) |
| `--file` | Pickle file with problem instances |
| `--results` | Directory to save results |
| `--time_limit` | Per-instance time limit in seconds (-1 = infinite) |
| `--nnet_batch_size` | NNet batch size during search (lower if GPU OOM) |

### Solving with Policy
```bash
python -m deepxube solve \
  --domain mypuzzle \
  --heur resnet_fc.100H_2B_bn \
  --heur_file ./saved_models_vp/heur_nnet.pt \
  --heur_type V \
  --policy resnet_fc.100H_2B_10E_bn \
  --policy_file ./saved_models_vp/policy_nnet.pt \
  --pathfind graph_v_p.10B_1.0W \
  --file test_instances.pkl \
  --results ./results_vp/
```

### Solving without a Trained Network (Zero Heuristic)
```bash
python -m deepxube solve \
  --domain mypuzzle \
  --heur_type V \
  --pathfind graph_v.10B \
  --file test_instances.pkl \
  --results ./results_baseline/
```
This uses an all-zeros heuristic (equivalent to breadth-first search). Useful as a baseline.

---

## 11. Visualizing Results

### Training Progress
```bash
python -m deepxube train_summary --dir ./saved_models_rl
```
Shows an interactive 6-panel matplotlib figure: percent solved vs step, path costs, search iterations, cost-to-go targets, number of instances, and target vs prediction scatter.

Use `--type policy` to view policy training summary instead of heuristic.

### Visualize Solutions
```bash
python -m deepxube viz \
  --domain mypuzzle \
  --file ./results/results.pkl \
  --idx 0 \
  --soln
```
Step through a solved instance interactively (requires `StateGoalVizable` mixin).

---

## 12. End-to-End Example

Here's a complete workflow for a Rubik's-Cube-like puzzle using Template A:

```bash
# 1. Verify domain is registered
python -m deepxube domain_info --names mypuzzle

# 2. Test basic functionality
python -m deepxube time --domain mypuzzle --step_max 20

# 3. Supervised initialization (50k iterations)
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn \
  --heur_type V \
  --pathfind sup_v_rw_rev \
  --dir ./saved_models/sup \
  --batch_size 1000 \
  --max_itrs 50000 \
  --step_max 30

# 4. RL refinement with A* (100k iterations, loads pretrained weights automatically)
python -m deepxube train \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn \
  --heur_type V \
  --pathfind graph_v.10B_1.0W_0.1E \
  --dir ./saved_models/rl \
  --batch_size 1000 \
  --max_itrs 100000 \
  --step_max 30 \
  --search_itrs 500

# 5. Generate test instances
python -m deepxube problem_inst \
  --domain mypuzzle \
  --step_min 1 --step_max 30 \
  --num 100 --file test.pkl

# 6. Solve
python -m deepxube solve \
  --domain mypuzzle \
  --heur resnet_fc.1000H_4B_bn \
  --heur_file ./saved_models/rl/heur_nnet.pt \
  --heur_type V \
  --pathfind graph_v.100B_1.0W \
  --file test.pkl \
  --results ./results/

# 7. View training progress
python -m deepxube train_summary --dir ./saved_models/rl
```

---

## 13. Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| "Cannot build heur nnet for domain X, heur type Y" | Your domain's NNet input type doesn't match the heuristic network's expected input | Use `resnet_fc` for flat domains, `resnet_2d` for 2D domains. Run `domain_info` to see which inputs are registered |
| "No updaters for Domain X, PathFind Y, HER Z" | The pathfinder requires a domain mixin you don't have | Run `pathfinding_info` to see domain type requirements. Common: using `sup_v_rw` on a `GoalStartRevWalkable` domain (need `sup_v_rw_rev` instead) |
| "No hindsight experience replay for supervised" | `--her` used with `sup_*` pathfinder | HER only works with RL pathfinders (`graph_*`, `beam_*`) |
| OOM during training | Too many states in search or NNet batch too large | Lower `--up_batch_size` and `--up_nnet_batch_size` |
| Search never finds solutions | Supervised init not done, or `--search_itrs` too low | Always do supervised init first. Increase `--search_itrs` |
| Training loss doesn't decrease | Learning rate issue or network too small/large | Try different `H` (hidden dim) and `B` (blocks) |
| Domain not found at CLI | File not in `./domains/` or has import error | Check for Python errors by importing the file manually |

---

## 14. Pathfinder ↔ Domain Compatibility Matrix

This table shows which pathfinders work with which domain base classes:

| Pathfinder | Required Domain Type | Notes |
|---|---|---|
| `sup_v_rw` | `StartGoalWalkable` | Forward walk, V-network |
| `sup_v_rw_rev` | `GoalStartRevWalkable` | Reverse walk, V-network |
| `sup_q_rw` | `StartGoalWalkable` | Forward walk, Q-network |
| `sup_q_rw_rev` | `GoalStartRevWalkableActsRev` | Reverse walk + reversible actions, Q-network |
| `graph_v` | `ActsEnum` | A* with V heuristic |
| `graph_q` | `ActsEnum` | A* with Q heuristic |
| `graph_v_p` | Any `Domain` | A* with V + Policy |
| `graph_q_p` | Any `Domain` | A* with Q + Policy |
| `beam_v` | `ActsEnum` | Beam search with V |
| `beam_q` | `ActsEnum` | Beam search with Q |
| `beam_p` | Any `Domain` | Beam search with Policy only |
| `beam_v_p` | Any `Domain` | Beam search with V + Policy |
| `beam_q_p` | Any `Domain` | Beam search with Q + Policy |

**Template A & B** domains satisfy: `ActsEnumFixed` (which is a subclass of `ActsEnum`), `GoalStartRevWalkableActsRev` → **all pathfinders work**.

**Template C** domains satisfy: `ActsEnumFixed`, `StartGoalWalkable` → all **except** `sup_v_rw_rev` and `sup_q_rw_rev`.
