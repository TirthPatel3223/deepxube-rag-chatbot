---
id: "module:deepxube.updaters.updater_q_rl"
kind: "module"
name: "updater_q_rl"
qualified_name: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_count: 301
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "cast", "alias": null}, {"name": "Type", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "GoalSampleableFromState", "alias": null}, {"name": "Action", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "FNsHQ", "alias": null}, {"name": "FNsHeurQ", "alias": null}, {"name": "FNsHeurQPolicy", "alias": null}, {"name": "PathFindSetHeurQ", "alias": null}, {"name": "EdgeQ", "alias": null}, {"name": "InstanceEdge", "alias": null}, {"name": "Node", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpdateHER", "alias": null}, {"name": "UpdateHasPolicy", "alias": null}, {"name": "UpdateHeurQ", "alias": null}, {"name": "UpdateRL", "alias": null}, {"name": "D", "alias": null}, {"name": "UpArgs", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.updater_factory"
    names: [{"name": "updater_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.updaters.utils.replay_buffer_utils"
    names: [{"name": "ReplayBufferQ", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.updaters.updater_q_rl.UpdateHeurQRL"
  - "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC"
  - "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC"
  - "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoal"
  - "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLHER"
  - "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalPolicy"
  - "class:deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy"
module_level_functions:
  - "func:deepxube.updaters.updater_q_rl._pathfind_q_step"
  - "func:deepxube.updaters.updater_q_rl._get_edge_popped_data"
module_level_constants: []
---

# Module `deepxube.updaters.updater_q_rl`

**File:** [deepxube/updaters/updater_q_rl.py](../../deepxube/updaters/updater_q_rl.py)
**Lines:** 301

## Module docstring

Q-function RL updaters (with and without HER variants). Each concrete class
registers a factory key and wires up one-step Q-learning targets plus
replay-buffer sampling for training a Q-heuristic network. 

## Contents

### Classes
- `UpdateHeurQRL` — see `../classes/deepxube.updaters.updater_q_rl/UpdateHeurQRL.md`
- `UpdateHeurQRLKeepGoalABC` — see `../classes/deepxube.updaters.updater_q_rl/UpdateHeurQRLKeepGoalABC.md`
- `UpdateHeurQRLHERABC` — see `../classes/deepxube.updaters.updater_q_rl/UpdateHeurQRLHERABC.md`
- `UpdateHeurQRLKeepGoal` — see `../classes/deepxube.updaters.updater_q_rl/UpdateHeurQRLKeepGoal.md`
- `UpdateHeurQRLHER` — see `../classes/deepxube.updaters.updater_q_rl/UpdateHeurQRLHER.md`
- `UpdateHeurQRLKeepGoalPolicy` — see `../classes/deepxube.updaters.updater_q_rl/UpdateHeurQRLKeepGoalPolicy.md`
- `UpdateHeurQRLHERPolicy` — see `../classes/deepxube.updaters.updater_q_rl/UpdateHeurQRLHERPolicy.md`

### Module-level functions
- `_pathfind_q_step` *(trivial, skipped)*
- `_get_edge_popped_data`

## Imports

- `from abc import ABC`
- `from typing import List, Tuple, cast, Type`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `from deepxube.base.domain import Domain, GoalSampleableFromState, Action, State, Goal`
- `from deepxube.base.pathfinding import FNsHQ, FNsHeurQ, FNsHeurQPolicy, PathFindSetHeurQ, EdgeQ, InstanceEdge, Node`
- `from deepxube.base.updater import UpdateHER, UpdateHasPolicy, UpdateHeurQ, UpdateRL, D, UpArgs`
- `from deepxube.factories.updater_factory import updater_factory`
- `from deepxube.updaters.utils.replay_buffer_utils import ReplayBufferQ`
- `from deepxube.utils.timing_utils import Times`
- `import time`
