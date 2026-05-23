---
id: "module:deepxube.tests.time_tests"
kind: "module"
name: "time_tests"
qualified_name: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_count: 247
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "cast", "alias": null}]
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "torch"
    names: [{"name": "Tensor", "alias": null}]
  - kind: "import"
    module: "torch.nn"
    alias: "nn"
  - kind: "from"
    module: "torch.multiprocessing"
    names: [{"name": "Queue", "alias": null}, {"name": "get_context", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "ActsEnum", "alias": null}, {"name": "StartGoalWalkable", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}, {"name": "Action", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.nnet_utils"
    names: [{"name": "NNetPar", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNetPar", "alias": null}, {"name": "PolicyNNet", "alias": null}, {"name": "PolicyNNetPar", "alias": null}, {"name": "PolicyFn", "alias": null}, {"name": "HeurNNetParV", "alias": null}, {"name": "HeurNNetParQ", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.nnet_utils"
    names: [{"name": "NNetCallable", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet"
    names: [{"name": "nnet_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.misc_utils"
    names: [{"name": "flatten", "alias": null}]
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
classes: []
module_level_functions:
  - "func:deepxube.tests.time_tests.data_runner"
  - "func:deepxube.tests.time_tests.test_env"
  - "func:deepxube.tests.time_tests.test_envstartgoalrw"
  - "func:deepxube.tests.time_tests.test_envenumerableacts"
  - "func:deepxube.tests.time_tests.init_nnet"
  - "func:deepxube.tests.time_tests.heur_fn_out"
  - "func:deepxube.tests.time_tests.test_heur_nnet_par"
  - "func:deepxube.tests.time_tests.test_policy_nnet_par"
  - "func:deepxube.tests.time_tests.time_test"
module_level_constants: []
---

# Module `deepxube.tests.time_tests`

**File:** [deepxube/tests/time_tests.py](../../deepxube/tests/time_tests.py)
**Lines:** 247

## Module docstring

Timing benchmarks for domain state generation, action sampling, expansion, and nnet inference. 

## Contents

### Module-level functions
- `data_runner`
- `test_env`
- `test_envstartgoalrw`
- `test_envenumerableacts`
- `init_nnet`
- `heur_fn_out`
- `test_heur_nnet_par`
- `test_policy_nnet_par`
- `time_test`

## Imports

- `from typing import List, Tuple, Optional, cast`
- `import torch`
- `from torch import Tensor`
- `import torch.nn as nn`
- `from torch.multiprocessing import Queue, get_context`
- `from deepxube.base.domain import Domain, ActsEnum, StartGoalWalkable, State, Goal, Action`
- `from deepxube.nnet.nnet_utils import NNetPar`
- `from deepxube.base.heuristic import HeurNNetPar, PolicyNNet, PolicyNNetPar, PolicyFn, HeurNNetParV, HeurNNetParQ`
- `from deepxube.nnet.nnet_utils import NNetCallable`
- `from deepxube.nnet import nnet_utils`
- `from deepxube.utils.misc_utils import flatten`
- `from deepxube.utils.timing_utils import Times`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `import time`
