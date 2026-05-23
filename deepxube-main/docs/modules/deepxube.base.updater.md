---
id: "module:deepxube.base.updater"
kind: "module"
name: "updater"
qualified_name: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_count: 771
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Any", "alias": null}, {"name": "Generic", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Optional", "alias": null}, {"name": "cast", "alias": null}, {"name": "Type", "alias": null}]
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "import"
    module: "time"
    alias: null
  - kind: "from"
    module: "dataclasses"
    names: [{"name": "dataclass", "alias": null}]
  - kind: "from"
    module: "multiprocessing"
    names: [{"name": "Queue", "alias": null}]
  - kind: "from"
    module: "multiprocessing.process"
    names: [{"name": "BaseProcess", "alias": null}]
  - kind: "from"
    module: "multiprocessing.context"
    names: [{"name": "SpawnContext", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.nnet_utils"
    names: [{"name": "NNetParInfo", "alias": null}, {"name": "NNetCallable", "alias": null}, {"name": "NNetPar", "alias": null}, {"name": "get_nnet_par_infos", "alias": null}, {"name": "start_nnet_fn_runners", "alias": null}, {"name": "stop_nnet_runners", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "GoalSampleableFromState", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNetPar", "alias": null}, {"name": "HeurNNetParV", "alias": null}, {"name": "HeurNNetParQ", "alias": null}, {"name": "HeurFn", "alias": null}, {"name": "HeurFnV", "alias": null}, {"name": "HeurFnQ", "alias": null}, {"name": "PolicyNNetPar", "alias": null}, {"name": "PolicyFn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "FNs", "alias": null}, {"name": "FNsP", "alias": null}, {"name": "FNsHV", "alias": null}, {"name": "FNsHQ", "alias": null}, {"name": "FNsHeur", "alias": null}, {"name": "PathFind", "alias": null}, {"name": "PathFindSup", "alias": null}, {"name": "Instance", "alias": null}, {"name": "InstanceNode", "alias": null}, {"name": "InstanceEdge", "alias": null}, {"name": "get_path", "alias": null}, {"name": "Node", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.pathfinding.utils.performance"
    names: [{"name": "PathFindPerf", "alias": null}, {"name": "print_pathfindperf", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.command_line_utils"
    names: [{"name": "get_pathfind_name_kwargs", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.data_utils"
    names: [{"name": "SharedNDArray", "alias": null}, {"name": "np_to_shnd", "alias": null}, {"name": "get_nowait_noerr", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.misc_utils"
    names: [{"name": "split_evenly", "alias": null}, {"name": "split_evenly_w_max", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "import"
    module: "gc"
    alias: null
  - kind: "import"
    module: "copy"
    alias: null
  - kind: "from"
    module: "torch.multiprocessing"
    names: [{"name": "get_context", "alias": null}]
classes:
  - "class:deepxube.base.updater.UpArgs"
  - "class:deepxube.base.updater.Update"
  - "class:deepxube.base.updater.UpdateHER"
  - "class:deepxube.base.updater.UpdateHasHeur"
  - "class:deepxube.base.updater.UpdateHasPolicy"
  - "class:deepxube.base.updater.UpdateSup"
  - "class:deepxube.base.updater.UpdateRL"
  - "class:deepxube.base.updater.UpdateHeur"
  - "class:deepxube.base.updater.UpdatePolicy"
  - "class:deepxube.base.updater.UpdateHeurV"
  - "class:deepxube.base.updater.UpdateHeurQ"
module_level_functions:
  - "func:deepxube.base.updater._put_from_q"
module_level_constants:
  - name: "FNsH"
    annotation: null
    value_expr: "TypeVar('FNsH', bound=FNsHeur)"
  - name: "Inst"
    annotation: null
    value_expr: "TypeVar('Inst', bound=Instance)"
  - name: "D"
    annotation: null
    value_expr: "TypeVar('D', bound=Domain)"
  - name: "P"
    annotation: null
    value_expr: "TypeVar('P', bound=PathFind)"
  - name: "HNet"
    annotation: null
    value_expr: "TypeVar('HNet', bound=HeurNNetPar)"
  - name: "H"
    annotation: null
    value_expr: "TypeVar('H', bound=HeurFn)"
  - name: "PS"
    annotation: null
    value_expr: "TypeVar('PS', bound=PathFindSup)"
---

# Module `deepxube.base.updater`

**File:** [deepxube/base/updater.py](../../deepxube/base/updater.py)
**Lines:** 771

## Module docstring

Abstract base classes for training-data updaters.

An ``Update`` runs the pathfinder for a configured number of iterations,
collects the states/edges expanded along the way, and emits per-iteration
numpy arrays ready to be fed to the heuristic or policy network's training
step. Concrete subclasses in ``deepxube/updaters/`` specialise for supervised
vs. RL, V vs. Q, and with/without Hindsight Experience Replay (HER), and
register themselves with ``updater_factory``.

## Contents

### Classes
- `UpArgs` — see `../classes/deepxube.base.updater/UpArgs.md`
- `Update` — see `../classes/deepxube.base.updater/Update.md`
- `UpdateHER` — see `../classes/deepxube.base.updater/UpdateHER.md`
- `UpdateHasHeur` — see `../classes/deepxube.base.updater/UpdateHasHeur.md`
- `UpdateHasPolicy` — see `../classes/deepxube.base.updater/UpdateHasPolicy.md`
- `UpdateSup` — see `../classes/deepxube.base.updater/UpdateSup.md`
- `UpdateRL` — see `../classes/deepxube.base.updater/UpdateRL.md`
- `UpdateHeur` — see `../classes/deepxube.base.updater/UpdateHeur.md`
- `UpdatePolicy` — see `../classes/deepxube.base.updater/UpdatePolicy.md`
- `UpdateHeurV` — see `../classes/deepxube.base.updater/UpdateHeurV.md`
- `UpdateHeurQ` — see `../classes/deepxube.base.updater/UpdateHeurQ.md`

### Module-level functions
- `_put_from_q`

### Module-level constants / TypeVars
- `FNsH` = `TypeVar('FNsH', bound=FNsHeur)`
- `Inst` = `TypeVar('Inst', bound=Instance)`
- `D` = `TypeVar('D', bound=Domain)`
- `P` = `TypeVar('P', bound=PathFind)`
- `HNet` = `TypeVar('HNet', bound=HeurNNetPar)`
- `H` = `TypeVar('H', bound=HeurFn)`
- `PS` = `TypeVar('PS', bound=PathFindSup)`

## Imports

- `from typing import List, Dict, Tuple, Any, Generic, TypeVar, Optional, cast, Type`
- `from abc import ABC, abstractmethod`
- `import time`
- `from dataclasses import dataclass`
- `from multiprocessing import Queue`
- `from multiprocessing.process import BaseProcess`
- `from multiprocessing.context import SpawnContext`
- `import numpy as np`
- `import torch`
- `from numpy.typing import NDArray`
- `from deepxube.nnet.nnet_utils import NNetParInfo, NNetCallable, NNetPar, get_nnet_par_infos, start_nnet_fn_runners, stop_nnet_runners`
- `from deepxube.base.domain import Domain, State, Action, Goal, GoalSampleableFromState`
- `from deepxube.base.heuristic import HeurNNetPar, HeurNNetParV, HeurNNetParQ, HeurFn, HeurFnV, HeurFnQ, PolicyNNetPar, PolicyFn`
- `from deepxube.base.pathfinding import FNs, FNsP, FNsHV, FNsHQ, FNsHeur, PathFind, PathFindSup, Instance, InstanceNode, InstanceEdge, get_path, Node`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory`
- `from deepxube.pathfinding.utils.performance import PathFindPerf, print_pathfindperf`
- `from deepxube.utils.command_line_utils import get_pathfind_name_kwargs`
- `from deepxube.utils.data_utils import SharedNDArray, np_to_shnd, get_nowait_noerr`
- `from deepxube.utils.misc_utils import split_evenly, split_evenly_w_max`
- `from deepxube.utils.timing_utils import Times`
- `import gc`
- `import copy`
- `from torch.multiprocessing import get_context`
