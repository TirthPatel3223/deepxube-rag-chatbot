---
id: "module:deepxube.updaters.updater_v_rl"
kind: "module"
name: "updater_v_rl"
qualified_name: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_count: 290
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "cast", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Type", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "GoalSampleableFromState", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "FNsHV", "alias": null}, {"name": "FNsHeurV", "alias": null}, {"name": "FNsHeurVPolicy", "alias": null}, {"name": "PathFindSetHeurV", "alias": null}, {"name": "Node", "alias": null}, {"name": "InstanceNode", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpdateHER", "alias": null}, {"name": "UpdateHasPolicy", "alias": null}, {"name": "UpdateHeurV", "alias": null}, {"name": "UpdateRL", "alias": null}, {"name": "UpArgs", "alias": null}, {"name": "D", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.updater_factory"
    names: [{"name": "updater_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.updaters.utils.replay_buffer_utils"
    names: [{"name": "ReplayBufferV", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "misc_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.updaters.updater_v_rl.UpdateHeurVRL"
  - "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC"
  - "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC"
  - "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal"
  - "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLHER"
  - "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalPolicy"
  - "class:deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy"
module_level_functions:
  - "func:deepxube.updaters.updater_v_rl._pathfind_v_step"
  - "func:deepxube.updaters.updater_v_rl._get_nodes_popped_data"
module_level_constants: []
---

# Module `deepxube.updaters.updater_v_rl`

**File:** [deepxube/updaters/updater_v_rl.py](../../deepxube/updaters/updater_v_rl.py)
**Lines:** 290

## Module docstring

V-function RL updaters (with and without HER variants). Each concrete class
registers a factory key and wires up value-iteration backups plus
replay-buffer sampling for training a V-heuristic network. 

## Contents

### Classes
- `UpdateHeurVRL` — see `../classes/deepxube.updaters.updater_v_rl/UpdateHeurVRL.md`
- `UpdateHeurVRLKeepGoalABC` — see `../classes/deepxube.updaters.updater_v_rl/UpdateHeurVRLKeepGoalABC.md`
- `UpdateHeurVRLHERABC` — see `../classes/deepxube.updaters.updater_v_rl/UpdateHeurVRLHERABC.md`
- `UpdateHeurVRLKeepGoal` — see `../classes/deepxube.updaters.updater_v_rl/UpdateHeurVRLKeepGoal.md`
- `UpdateHeurVRLHER` — see `../classes/deepxube.updaters.updater_v_rl/UpdateHeurVRLHER.md`
- `UpdateHeurVRLKeepGoalPolicy` — see `../classes/deepxube.updaters.updater_v_rl/UpdateHeurVRLKeepGoalPolicy.md`
- `UpdateHeurVRLHERPolicy` — see `../classes/deepxube.updaters.updater_v_rl/UpdateHeurVRLHERPolicy.md`

### Module-level functions
- `_pathfind_v_step` *(trivial, skipped)*
- `_get_nodes_popped_data`

## Imports

- `from abc import ABC`
- `from typing import List, cast, Tuple, Type`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `from deepxube.base.domain import Domain, GoalSampleableFromState, State, Goal`
- `from deepxube.base.pathfinding import FNsHV, FNsHeurV, FNsHeurVPolicy, PathFindSetHeurV, Node, InstanceNode`
- `from deepxube.base.updater import UpdateHER, UpdateHasPolicy, UpdateHeurV, UpdateRL, UpArgs, D`
- `from deepxube.factories.updater_factory import updater_factory`
- `from deepxube.updaters.utils.replay_buffer_utils import ReplayBufferV`
- `from deepxube.utils import misc_utils`
- `from deepxube.utils.timing_utils import Times`
- `import time`
