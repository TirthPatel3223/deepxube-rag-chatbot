---
id: "module:deepxube.nnet.pytorch_models"
kind: "module"
name: "pytorch_models"
qualified_name: "deepxube.nnet.pytorch_models"
file: "deepxube/nnet/pytorch_models.py"
line_count: 308
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Union", "alias": null}, {"name": "Callable", "alias": null}, {"name": "Tuple", "alias": null}]
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "torch.nn.parameter"
    names: [{"name": "Parameter", "alias": null}]
  - kind: "from"
    module: "torch"
    names: [{"name": "Tensor", "alias": null}, {"name": "nn", "alias": null}]
  - kind: "from"
    module: "torch.nn.utils"
    names: [{"name": "parametrizations", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
classes:
  - "class:deepxube.nnet.pytorch_models.OneHot"
  - "class:deepxube.nnet.pytorch_models.SPLASH"
  - "class:deepxube.nnet.pytorch_models.SPLASH1"
  - "class:deepxube.nnet.pytorch_models.LinearAct"
  - "class:deepxube.nnet.pytorch_models.ResnetModel"
  - "class:deepxube.nnet.pytorch_models.FullyConnectedModel"
  - "class:deepxube.nnet.pytorch_models.Conv2dModel"
module_level_functions:
  - "func:deepxube.nnet.pytorch_models.get_act_fn"
  - "func:deepxube.nnet.pytorch_models.make_onehots"
module_level_constants: []
---

# Module `deepxube.nnet.pytorch_models`

**File:** [deepxube/nnet/pytorch_models.py](../../deepxube/nnet/pytorch_models.py)
**Lines:** 308

## Module docstring

Core PyTorch building blocks used by DeepXube heuristics: activation functions (including learnable SPLASH),
one-hot encoding, and configurable ResNet, FC, and Conv2d model constructors. 

## Contents

### Classes
- `OneHot` — see `../classes/deepxube.nnet.pytorch_models/OneHot.md`
- `SPLASH` — see `../classes/deepxube.nnet.pytorch_models/SPLASH.md`
- `SPLASH1` — see `../classes/deepxube.nnet.pytorch_models/SPLASH1.md`
- `LinearAct` — see `../classes/deepxube.nnet.pytorch_models/LinearAct.md`
- `ResnetModel` — see `../classes/deepxube.nnet.pytorch_models/ResnetModel.md`
- `FullyConnectedModel` — see `../classes/deepxube.nnet.pytorch_models/FullyConnectedModel.md`
- `Conv2dModel` — see `../classes/deepxube.nnet.pytorch_models/Conv2dModel.md`

### Module-level functions
- `get_act_fn`
- `make_onehots`

## Imports

- `from typing import List, Optional, Union, Callable, Tuple`
- `import torch`
- `from torch.nn.parameter import Parameter`
- `from torch import Tensor, nn`
- `from torch.nn.utils import parametrizations`
- `import numpy as np`
