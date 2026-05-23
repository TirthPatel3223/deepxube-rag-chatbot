---
id: "module:deepxube.trainers.utils.train_loop"
kind: "module"
name: "train_loop"
qualified_name: "deepxube.trainers.utils.train_loop"
file: "deepxube/trainers/utils/train_loop.py"
line_count: 254
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Optional", "alias": null}, {"name": "List", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "from"
    module: "dataclasses"
    names: [{"name": "dataclass", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNet", "alias": null}, {"name": "PolicyNNet", "alias": null}, {"name": "HeurNNetPar", "alias": null}, {"name": "PolicyNNetPar", "alias": null}, {"name": "HeurFn", "alias": null}, {"name": "PolicyFn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "PathFind", "alias": null}, {"name": "Instance", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpdateHasHeur", "alias": null}, {"name": "UpdateHasPolicy", "alias": null}, {"name": "UpdateHeur", "alias": null}, {"name": "UpdatePolicy", "alias": null}]
  - kind: "from"
    module: "deepxube.base.trainer"
    names: [{"name": "TrainArgs", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "get_pathfind_functions", "alias": null}]
  - kind: "from"
    module: "deepxube.pathfinding.utils.performance"
    names: [{"name": "PathFindPerf", "alias": null}]
  - kind: "from"
    module: "deepxube.trainers.train_heur"
    names: [{"name": "TrainHeur", "alias": null}]
  - kind: "from"
    module: "deepxube.trainers.train_policy"
    names: [{"name": "TrainPolicy", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.command_line_utils"
    names: [{"name": "get_pathfind_from_arg", "alias": null}, {"name": "get_pathfind_name_kwargs", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet"
    names: [{"name": "nnet_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "data_utils", "alias": null}]
  - kind: "from"
    module: "torch.utils.tensorboard"
    names: [{"name": "SummaryWriter", "alias": null}]
  - kind: "import"
    module: "sys"
    alias: null
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.trainers.utils.train_loop.TestArgs"
module_level_functions:
  - "func:deepxube.trainers.utils.train_loop.get_curr_itr"
  - "func:deepxube.trainers.utils.train_loop.get_curr_update_num"
  - "func:deepxube.trainers.utils.train_loop.get_pathfind"
  - "func:deepxube.trainers.utils.train_loop.train"
  - "func:deepxube.trainers.utils.train_loop.get_pathfind_w_instances"
  - "func:deepxube.trainers.utils.train_loop.test"
module_level_constants: []
---

# Module `deepxube.trainers.utils.train_loop`

**File:** [deepxube/trainers/utils/train_loop.py](../../deepxube/trainers/utils/train_loop.py)
**Lines:** 254

## Module docstring

High-level training loop for DeepXube: wires together heuristic and policy trainers, manages checkpoints, and
runs periodic test evaluations via pathfinding benchmarks. 

## Contents

### Classes
- `TestArgs` — see `../classes/deepxube.trainers.utils.train_loop/TestArgs.md`

### Module-level functions
- `get_curr_itr`
- `get_curr_update_num`
- `get_pathfind`
- `train`
- `get_pathfind_w_instances`
- `test`

## Imports

- `from typing import Optional, List, Any`
- `from dataclasses import dataclass`
- `from deepxube.base.domain import Domain, State, Goal`
- `from deepxube.base.heuristic import HeurNNet, PolicyNNet, HeurNNetPar, PolicyNNetPar, HeurFn, PolicyFn`
- `from deepxube.base.pathfinding import PathFind, Instance`
- `from deepxube.base.updater import UpdateHasHeur, UpdateHasPolicy, UpdateHeur, UpdatePolicy`
- `from deepxube.base.trainer import TrainArgs`
- `from deepxube.factories.pathfinding_factory import get_pathfind_functions`
- `from deepxube.pathfinding.utils.performance import PathFindPerf`
- `from deepxube.trainers.train_heur import TrainHeur`
- `from deepxube.trainers.train_policy import TrainPolicy`
- `from deepxube.utils.command_line_utils import get_pathfind_from_arg, get_pathfind_name_kwargs`
- `from deepxube.nnet import nnet_utils`
- `from deepxube.utils import data_utils`
- `from torch.utils.tensorboard import SummaryWriter`
- `import sys`
- `import os`
- `import torch`
- `import time`
