---
id: "module:deepxube.trainers.train_policy"
kind: "module"
name: "train_policy"
qualified_name: "deepxube.trainers.train_policy"
file: "deepxube/trainers/train_policy.py"
line_count: 39
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "PolicyNNet", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpdatePolicy", "alias": null}]
  - kind: "from"
    module: "deepxube.base.trainer"
    names: [{"name": "Train", "alias": null}, {"name": "update_optimizer", "alias": null}]
  - kind: "from"
    module: "deepxube.trainers.utils.train_utils"
    names: [{"name": "train_policy_nnet_step", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.trainers.train_policy.TrainPolicy"
module_level_functions: []
module_level_constants: []
---

# Module `deepxube.trainers.train_policy`

**File:** [deepxube/trainers/train_policy.py](../../deepxube/trainers/train_policy.py)
**Lines:** 39

## Module docstring

Concrete policy trainer that implements one forward-backward pass using the policy network's built-in VAE loss. 

## Contents

### Classes
- `TrainPolicy` — see `../classes/deepxube.trainers.train_policy/TrainPolicy.md`

## Imports

- `from typing import List, Tuple`
- `from deepxube.base.heuristic import PolicyNNet`
- `from deepxube.base.updater import UpdatePolicy`
- `from deepxube.base.trainer import Train, update_optimizer`
- `from deepxube.trainers.utils.train_utils import train_policy_nnet_step`
- `from deepxube.utils.timing_utils import Times`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `import time`
