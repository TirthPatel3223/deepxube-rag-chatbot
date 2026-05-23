---
id: "module:deepxube.base.heuristic"
kind: "module"
name: "heuristic"
qualified_name: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_count: 566
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "abstractmethod", "alias": null}, {"name": "ABC", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Any", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Generic", "alias": null}, {"name": "cast", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Type", "alias": null}, {"name": "Protocol", "alias": null}, {"name": "runtime_checkable", "alias": null}, {"name": "Union", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}, {"name": "Action", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "NNetInput", "alias": null}, {"name": "PolicyNNetIn", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.nnet_utils"
    names: [{"name": "NNetParInfo", "alias": null}, {"name": "nnet_batched", "alias": null}, {"name": "NNetPar", "alias": null}, {"name": "get_nnet_par_out", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "misc_utils", "alias": null}]
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "torch"
    names: [{"name": "nn", "alias": null}, {"name": "Tensor", "alias": null}]
  - kind: "import"
    module: "torch.optim"
    alias: "optim"
  - kind: "from"
    module: "torch.optim.optimizer"
    names: [{"name": "Optimizer", "alias": null}]
  - kind: "import"
    module: "random"
    alias: null
classes:
  - "class:deepxube.base.heuristic.DeepXubeNNet"
  - "class:deepxube.base.heuristic.HeurNNet"
  - "class:deepxube.base.heuristic.PolicyNNet"
  - "class:deepxube.base.heuristic.PolicyVAE"
  - "class:deepxube.base.heuristic.HeurFnV"
  - "class:deepxube.base.heuristic.HeurFnQ"
  - "class:deepxube.base.heuristic.PolicyFn"
  - "class:deepxube.base.heuristic.HeurNNetPar"
  - "class:deepxube.base.heuristic.HeurNNetParV"
  - "class:deepxube.base.heuristic.HeurNNetParQ"
  - "class:deepxube.base.heuristic.HeurNNetParQFixOut"
  - "class:deepxube.base.heuristic.HeurNNetParQIn"
  - "class:deepxube.base.heuristic.PolicyNNetPar"
module_level_functions:
  - "func:deepxube.base.heuristic._flatten_list"
  - "func:deepxube.base.heuristic.policy_fn_rand"
  - "func:deepxube.base.heuristic._combine_nnet_with_rand"
module_level_constants:
  - name: "In"
    annotation: null
    value_expr: "TypeVar('In', bound=NNetInput)"
  - name: "PNNetIn"
    annotation: null
    value_expr: "TypeVar('PNNetIn', bound=PolicyNNetIn)"
  - name: "HeurFn"
    annotation: null
    value_expr: "Union[HeurFnV, HeurFnQ]"
  - name: "H"
    annotation: null
    value_expr: "TypeVar('H', bound=HeurFn)"
---

# Module `deepxube.base.heuristic`

**File:** [deepxube/base/heuristic.py](../../deepxube/base/heuristic.py)
**Lines:** 566

## Module docstring

Abstract heuristic and policy network base classes plus their parallelisable
``*Par`` wrappers.

A ``HeurNNet`` (V- or Q-type) outputs cost-to-go scalars; a ``PolicyNNet``
outputs sampled action distributions. The ``*Par`` classes pair an NNet
parameter object with the per-state numpy conversion (``to_np``) and produce
either an in-process callable or one routed through a worker queue. 

## Contents

### Classes
- `DeepXubeNNet` — see `../classes/deepxube.base.heuristic/DeepXubeNNet.md`
- `HeurNNet` — see `../classes/deepxube.base.heuristic/HeurNNet.md`
- `PolicyNNet` — see `../classes/deepxube.base.heuristic/PolicyNNet.md`
- `PolicyVAE` — see `../classes/deepxube.base.heuristic/PolicyVAE.md`
- `HeurFnV` — see `../classes/deepxube.base.heuristic/HeurFnV.md`
- `HeurFnQ` — see `../classes/deepxube.base.heuristic/HeurFnQ.md`
- `PolicyFn` — see `../classes/deepxube.base.heuristic/PolicyFn.md`
- `HeurNNetPar` — see `../classes/deepxube.base.heuristic/HeurNNetPar.md`
- `HeurNNetParV` — see `../classes/deepxube.base.heuristic/HeurNNetParV.md`
- `HeurNNetParQ` — see `../classes/deepxube.base.heuristic/HeurNNetParQ.md`
- `HeurNNetParQFixOut` — see `../classes/deepxube.base.heuristic/HeurNNetParQFixOut.md`
- `HeurNNetParQIn` — see `../classes/deepxube.base.heuristic/HeurNNetParQIn.md`
- `PolicyNNetPar` — see `../classes/deepxube.base.heuristic/PolicyNNetPar.md`

### Module-level functions
- `_flatten_list`
- `policy_fn_rand`
- `_combine_nnet_with_rand`

### Module-level constants / TypeVars
- `In` = `TypeVar('In', bound=NNetInput)`
- `PNNetIn` = `TypeVar('PNNetIn', bound=PolicyNNetIn)`
- `HeurFn` = `Union[HeurFnV, HeurFnQ]`
- `H` = `TypeVar('H', bound=HeurFn)`

## Imports

- `from abc import abstractmethod, ABC`
- `from typing import List, Any, TypeVar, Generic, cast, Tuple, Optional, Type, Protocol, runtime_checkable, Union`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `from deepxube.base.domain import Domain, State, Goal, Action`
- `from deepxube.base.nnet_input import NNetInput, PolicyNNetIn`
- `from deepxube.nnet.nnet_utils import NNetParInfo, nnet_batched, NNetPar, get_nnet_par_out`
- `from deepxube.utils import misc_utils`
- `import torch`
- `from torch import nn, Tensor`
- `import torch.optim as optim`
- `from torch.optim.optimizer import Optimizer`
- `import random`
