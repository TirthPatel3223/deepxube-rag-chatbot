---
id: "module:deepxube.base.trainer"
kind: "module"
name: "trainer"
qualified_name: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_count: 421
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "from"
    module: "dataclasses"
    names: [{"name": "dataclass", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "Generic", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "cast", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Union", "alias": null}]
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "torch.utils.tensorboard"
    names: [{"name": "SummaryWriter", "alias": null}]
  - kind: "import"
    module: "torch.nn"
    alias: "nn"
  - kind: "from"
    module: "torch.nn"
    names: [{"name": "DataParallel", "alias": null}]
  - kind: "from"
    module: "torch.optim"
    names: [{"name": "Optimizer", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "DeepXubeNNet", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "Update", "alias": null}]
  - kind: "from"
    module: "deepxube.pathfinding.utils.performance"
    names: [{"name": "PathFindPerf", "alias": null}, {"name": "get_eq_weighted_perf", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.data_utils"
    names: [{"name": "sel_l", "alias": null}, {"name": "SharedNDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.nnet_utils"
    names: [{"name": "nnet_in_out_shared_q", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.data_utils"
    names: [{"name": "get_nowait_noerr", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet"
    names: [{"name": "nnet_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "from"
    module: "multiprocessing"
    names: [{"name": "Queue", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "import"
    module: "pickle"
    alias: null
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "shutil"
    alias: null
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.base.trainer.TrainArgs"
  - "class:deepxube.base.trainer.DataBuffer"
  - "class:deepxube.base.trainer.Status"
  - "class:deepxube.base.trainer.TrainSummary"
  - "class:deepxube.base.trainer.Train"
module_level_functions:
  - "func:deepxube.base.trainer.update_optimizer"
module_level_constants:
  - name: "NNet"
    annotation: null
    value_expr: "TypeVar('NNet', bound=DeepXubeNNet)"
  - name: "Up"
    annotation: null
    value_expr: "TypeVar('Up', bound=Update)"
---

# Module `deepxube.base.trainer`

**File:** [deepxube/base/trainer.py](../../deepxube/base/trainer.py)
**Lines:** 421

## Module docstring

Abstract trainer that drives the update -> train -> save loop.

The ``Train`` base owns the optimiser, network checkpoint files, replay-style
data buffer, and TensorBoard writer. Concrete trainers in ``deepxube/trainers/``
subclass it and provide the loss computation per iteration. 

## Contents

### Classes
- `TrainArgs` — see `../classes/deepxube.base.trainer/TrainArgs.md`
- `DataBuffer` — see `../classes/deepxube.base.trainer/DataBuffer.md`
- `Status` — see `../classes/deepxube.base.trainer/Status.md`
- `TrainSummary` — see `../classes/deepxube.base.trainer/TrainSummary.md`
- `Train` — see `../classes/deepxube.base.trainer/Train.md`

### Module-level functions
- `update_optimizer`

### Module-level constants / TypeVars
- `NNet` = `TypeVar('NNet', bound=DeepXubeNNet)`
- `Up` = `TypeVar('Up', bound=Update)`

## Imports

- `from abc import ABC, abstractmethod`
- `from dataclasses import dataclass`
- `from typing import Generic, TypeVar, List, Dict, Tuple, cast, Optional, Union`
- `import torch`
- `from torch.utils.tensorboard import SummaryWriter`
- `import torch.nn as nn`
- `from torch.nn import DataParallel`
- `from torch.optim import Optimizer`
- `from deepxube.base.heuristic import DeepXubeNNet`
- `from deepxube.base.updater import Update`
- `from deepxube.pathfinding.utils.performance import PathFindPerf, get_eq_weighted_perf`
- `from deepxube.utils.data_utils import sel_l, SharedNDArray`
- `from deepxube.nnet.nnet_utils import nnet_in_out_shared_q`
- `from deepxube.utils.data_utils import get_nowait_noerr`
- `from deepxube.nnet import nnet_utils`
- `from deepxube.utils.timing_utils import Times`
- `from multiprocessing import Queue`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `import pickle`
- `import os`
- `import shutil`
- `import time`
