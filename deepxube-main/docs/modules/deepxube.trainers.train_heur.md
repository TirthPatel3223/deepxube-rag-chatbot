---
id: "module:deepxube.trainers.train_heur"
kind: "module"
name: "train_heur"
qualified_name: "deepxube.trainers.train_heur"
file: "deepxube/trainers/train_heur.py"
line_count: 52
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNet", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpdateHeur", "alias": null}]
  - kind: "from"
    module: "deepxube.base.trainer"
    names: [{"name": "Train", "alias": null}, {"name": "update_optimizer", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "from"
    module: "deepxube.trainers.utils.train_utils"
    names: [{"name": "train_heur_nnet_step", "alias": null}, {"name": "ctgs_summary", "alias": null}]
  - kind: "import"
    module: "torch.nn"
    alias: "nn"
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
  - "class:deepxube.trainers.train_heur.TrainHeur"
module_level_functions: []
module_level_constants: []
---

# Module `deepxube.trainers.train_heur`

**File:** [deepxube/trainers/train_heur.py](../../deepxube/trainers/train_heur.py)
**Lines:** 52

## Module docstring

Concrete heuristic (V/Q) trainer that implements one SGD update step using MSE loss on cost-to-go targets. 

## Contents

### Classes
- `TrainHeur` — see `../classes/deepxube.trainers.train_heur/TrainHeur.md`

## Imports

- `from typing import List, Tuple`
- `from deepxube.base.heuristic import HeurNNet`
- `from deepxube.base.updater import UpdateHeur`
- `from deepxube.base.trainer import Train, update_optimizer`
- `from deepxube.utils.timing_utils import Times`
- `from deepxube.trainers.utils.train_utils import train_heur_nnet_step, ctgs_summary`
- `import torch.nn as nn`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `import time`
