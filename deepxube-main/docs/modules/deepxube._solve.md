---
id: "module:deepxube._solve"
kind: "module"
name: "_solve"
qualified_name: "deepxube._solve"
file: "deepxube/_solve.py"
line_count: 226
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Any", "alias": null}, {"name": "Tuple", "alias": null}]
  - kind: "import"
    module: "argparse"
    alias: null
  - kind: "from"
    module: "argparse"
    names: [{"name": "ArgumentParser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNetPar", "alias": null}, {"name": "PolicyNNetPar", "alias": null}, {"name": "HeurFn", "alias": null}, {"name": "HeurFnV", "alias": null}, {"name": "HeurFnQ", "alias": null}, {"name": "PolicyFn", "alias": null}, {"name": "policy_fn_rand", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "Node", "alias": null}, {"name": "Instance", "alias": null}, {"name": "PathFind", "alias": null}, {"name": "get_path", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "get_pathfind_functions", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.command_line_utils"
    names: [{"name": "get_domain_from_arg", "alias": null}, {"name": "get_pathfind_name_kwargs", "alias": null}, {"name": "get_pathfind_from_arg", "alias": null}, {"name": "get_heur_nnet_par_from_arg", "alias": null}, {"name": "get_policy_nnet_par_from_arg", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "data_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet"
    names: [{"name": "nnet_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.pathfinding.utils.performance"
    names: [{"name": "is_valid_soln", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "torch"
    names: [{"name": "nn", "alias": null}]
  - kind: "import"
    module: "pickle"
    alias: null
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "time"
    alias: null
  - kind: "import"
    module: "sys"
    alias: null
classes: []
module_level_functions:
  - "func:deepxube._solve.parse_solve"
  - "func:deepxube._solve.get_heur_fn"
  - "func:deepxube._solve.get_policy_fn"
  - "func:deepxube._solve.solve_cli"
  - "func:deepxube._solve._get_mean"
module_level_constants: []
---

# Module `deepxube._solve`

**File:** [deepxube/_solve.py](../../deepxube/_solve.py)
**Lines:** 226

## Module docstring

CLI solve command: loads problem instances from a pickle file and runs a pathfinding algorithm, saving results. 

## Contents

### Module-level functions
- `parse_solve`
- `get_heur_fn`
- `get_policy_fn`
- `solve_cli`
- `_get_mean`

## Imports

- `from typing import List, Dict, Optional, Any, Tuple`
- `import argparse`
- `from argparse import ArgumentParser`
- `from deepxube.base.domain import Domain, State, Action, Goal`
- `from deepxube.base.heuristic import HeurNNetPar, PolicyNNetPar, HeurFn, HeurFnV, HeurFnQ, PolicyFn, policy_fn_rand`
- `from deepxube.base.pathfinding import Node, Instance, PathFind, get_path`
- `from deepxube.factories.pathfinding_factory import get_pathfind_functions`
- `from deepxube.utils.command_line_utils import get_domain_from_arg, get_pathfind_name_kwargs, get_pathfind_from_arg, get_heur_nnet_par_from_arg, get_policy_nnet_par_from_arg`
- `from deepxube.utils import data_utils`
- `from deepxube.nnet import nnet_utils`
- `from deepxube.pathfinding.utils.performance import is_valid_soln`
- `import numpy as np`
- `from torch import nn`
- `import pickle`
- `import os`
- `import time`
- `import sys`
