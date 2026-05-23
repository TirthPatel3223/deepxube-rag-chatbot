---
id: "module:deepxube.nnet.nnet_utils"
kind: "module"
name: "nnet_utils"
qualified_name: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_count: 270
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Any", "alias": null}, {"name": "Callable", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Generic", "alias": null}]
  - kind: "from"
    module: "dataclasses"
    names: [{"name": "dataclass", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.data_utils"
    names: [{"name": "SharedNDArray", "alias": null}, {"name": "np_to_shnd", "alias": null}, {"name": "combine_l_l", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "torch"
    names: [{"name": "nn", "alias": null}]
  - kind: "from"
    module: "collections"
    names: [{"name": "OrderedDict", "alias": null}]
  - kind: "import"
    module: "re"
    alias: null
  - kind: "from"
    module: "torch"
    names: [{"name": "Tensor", "alias": null}]
  - kind: "from"
    module: "torch.multiprocessing"
    names: [{"name": "Queue", "alias": null}, {"name": "get_context", "alias": null}]
  - kind: "from"
    module: "multiprocessing.process"
    names: [{"name": "BaseProcess", "alias": null}]
classes:
  - "class:deepxube.nnet.nnet_utils.NNetParInfo"
  - "class:deepxube.nnet.nnet_utils.NNetPar"
module_level_functions:
  - "func:deepxube.nnet.nnet_utils.to_pytorch_input"
  - "func:deepxube.nnet.nnet_utils.get_device"
  - "func:deepxube.nnet.nnet_utils.load_nnet"
  - "func:deepxube.nnet.nnet_utils.get_available_gpu_nums"
  - "func:deepxube.nnet.nnet_utils.nnet_batched"
  - "func:deepxube.nnet.nnet_utils.nnet_in_out_shared_q"
  - "func:deepxube.nnet.nnet_utils.nnet_fn_runner"
  - "func:deepxube.nnet.nnet_utils.get_nnet_par_infos"
  - "func:deepxube.nnet.nnet_utils.start_nnet_fn_runners"
  - "func:deepxube.nnet.nnet_utils.stop_nnet_runners"
  - "func:deepxube.nnet.nnet_utils.get_nnet_par_out"
module_level_constants:
  - name: "NNetCallable"
    annotation: null
    value_expr: "Callable[..., Any]"
  - name: "NNetFn"
    annotation: null
    value_expr: "TypeVar('NNetFn', bound=NNetCallable)"
---

# Module `deepxube.nnet.nnet_utils`

**File:** [deepxube/nnet/nnet_utils.py](../../deepxube/nnet/nnet_utils.py)
**Lines:** 270

## Module docstring

Neural network utility functions and parallel inference workers for DeepXube. Handles device selection, model
loading, batched forward passes, and IPC-based parallel nnet runners using shared memory. 

## Contents

### Classes
- `NNetParInfo` — see `../classes/deepxube.nnet.nnet_utils/NNetParInfo.md`
- `NNetPar` — see `../classes/deepxube.nnet.nnet_utils/NNetPar.md`

### Module-level functions
- `to_pytorch_input`
- `get_device`
- `load_nnet`
- `get_available_gpu_nums`
- `nnet_batched`
- `nnet_in_out_shared_q`
- `nnet_fn_runner`
- `get_nnet_par_infos`
- `start_nnet_fn_runners`
- `stop_nnet_runners`
- `get_nnet_par_out`

### Module-level constants / TypeVars
- `NNetCallable` = `Callable[..., Any]`
- `NNetFn` = `TypeVar('NNetFn', bound=NNetCallable)`

## Imports

- `from abc import ABC, abstractmethod`
- `from typing import List, Tuple, Optional, Any, Callable, TypeVar, Generic`
- `from dataclasses import dataclass`
- `from deepxube.utils.data_utils import SharedNDArray, np_to_shnd, combine_l_l`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `import os`
- `import torch`
- `from torch import nn`
- `from collections import OrderedDict`
- `import re`
- `from torch import Tensor`
- `from torch.multiprocessing import Queue, get_context`
- `from multiprocessing.process import BaseProcess`
