---
id: "module:deepxube.trainers.utils.train_utils"
kind: "module"
name: "train_utils"
qualified_name: "deepxube.trainers.utils.train_utils"
file: "deepxube/trainers/utils/train_utils.py"
line_count: 96
docstring_source: "present"
imports:
  - kind: "import"
    module: "time"
    alias: null
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "PolicyNNet", "alias": null}]
  - kind: "from"
    module: "deepxube.base.trainer"
    names: [{"name": "TrainArgs", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet"
    names: [{"name": "nnet_utils", "alias": null}]
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "torch"
    names: [{"name": "Tensor", "alias": null}]
  - kind: "from"
    module: "torch.optim.optimizer"
    names: [{"name": "Optimizer", "alias": null}]
  - kind: "import"
    module: "torch.nn"
    alias: "nn"
classes: []
module_level_functions:
  - "func:deepxube.trainers.utils.train_utils.ctgs_summary"
  - "func:deepxube.trainers.utils.train_utils.train_heur_nnet_step"
  - "func:deepxube.trainers.utils.train_utils.train_policy_nnet_step"
module_level_constants: []
---

# Module `deepxube.trainers.utils.train_utils`

**File:** [deepxube/trainers/utils/train_utils.py](../../deepxube/trainers/utils/train_utils.py)
**Lines:** 96

## Module docstring

Low-level SGD step utilities shared by heuristic and policy trainers. 

## Contents

### Module-level functions
- `ctgs_summary`
- `train_heur_nnet_step`
- `train_policy_nnet_step`

## Imports

- `import time`
- `from typing import List, Tuple`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `from deepxube.base.heuristic import PolicyNNet`
- `from deepxube.base.trainer import TrainArgs`
- `from deepxube.nnet import nnet_utils`
- `import torch`
- `from torch import Tensor`
- `from torch.optim.optimizer import Optimizer`
- `import torch.nn as nn`
