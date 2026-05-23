---
id: "module:deepxube.updaters.updater_policy_rl"
kind: "module"
name: "updater_policy_rl"
qualified_name: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_count: 279
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Type", "alias": null}]
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "GoalSampleableFromState", "alias": null}, {"name": "Action", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNetParV", "alias": null}, {"name": "HeurNNetParQ", "alias": null}, {"name": "HeurFnV", "alias": null}, {"name": "HeurFnQ", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "FNsP", "alias": null}, {"name": "FNsPolicy", "alias": null}, {"name": "FNsHeurVPolicy", "alias": null}, {"name": "FNsHeurQPolicy", "alias": null}, {"name": "PathFind", "alias": null}, {"name": "PathFindActsPolicy", "alias": null}, {"name": "EdgeQ", "alias": null}, {"name": "Node", "alias": null}, {"name": "Instance", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpdateHER", "alias": null}, {"name": "UpdatePolicy", "alias": null}, {"name": "UpdateHasHeur", "alias": null}, {"name": "UpdateRL", "alias": null}, {"name": "D", "alias": null}, {"name": "UpArgs", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.updater_factory"
    names: [{"name": "updater_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.updaters.utils.replay_buffer_utils"
    names: [{"name": "ReplayBufferP", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRL"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoal"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurV"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurV"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurQ"
  - "class:deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ"
module_level_functions:
  - "func:deepxube.updaters.updater_policy_rl._pathfind_step"
  - "func:deepxube.updaters.updater_policy_rl._get_edge_popped_data"
module_level_constants: []
---

# Module `deepxube.updaters.updater_policy_rl`

**File:** [deepxube/updaters/updater_policy_rl.py](../../deepxube/updaters/updater_policy_rl.py)
**Lines:** 279

## Module docstring

Policy RL updaters (with and without HER variants). Each concrete class
registers a factory key and wires up action-sampling and replay-buffer
plumbing for training a policy network, optionally alongside a heuristic. 

## Contents

### Classes
- `UpdatePolicyRL` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRL.md`
- `UpdatePolicyRLKeepGoalABC` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLKeepGoalABC.md`
- `UpdatePolicyRLHERABC` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLHERABC.md`
- `UpdatePolicyRLKeepGoal` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLKeepGoal.md`
- `UpdatePolicyRLHER` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLHER.md`
- `UpdatePolicyRLKeepGoalHeurV` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLKeepGoalHeurV.md`
- `UpdatePolicyRLHERHeurV` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLHERHeurV.md`
- `UpdatePolicyRLKeepGoalHeurQ` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLKeepGoalHeurQ.md`
- `UpdatePolicyRLHERHeurQ` — see `../classes/deepxube.updaters.updater_policy_rl/UpdatePolicyRLHERHeurQ.md`

### Module-level functions
- `_pathfind_step` *(trivial, skipped)*
- `_get_edge_popped_data`

## Imports

- `from abc import ABC`
- `from typing import List, Tuple, Type`
- `from numpy.typing import NDArray`
- `from deepxube.base.domain import Domain, GoalSampleableFromState, Action, State, Goal`
- `from deepxube.base.heuristic import HeurNNetParV, HeurNNetParQ, HeurFnV, HeurFnQ`
- `from deepxube.base.pathfinding import FNsP, FNsPolicy, FNsHeurVPolicy, FNsHeurQPolicy, PathFind, PathFindActsPolicy, EdgeQ, Node, Instance`
- `from deepxube.base.updater import UpdateHER, UpdatePolicy, UpdateHasHeur, UpdateRL, D, UpArgs`
- `from deepxube.factories.updater_factory import updater_factory`
- `from deepxube.updaters.utils.replay_buffer_utils import ReplayBufferP`
- `from deepxube.utils.timing_utils import Times`
- `import numpy as np`
- `import time`
