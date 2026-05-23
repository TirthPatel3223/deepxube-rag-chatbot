---
id: "module:deepxube._train_cli"
kind: "module"
name: "_train_cli"
qualified_name: "deepxube._train_cli"
file: "deepxube/_train_cli.py"
line_count: 128
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Optional", "alias": null}, {"name": "List", "alias": null}]
  - kind: "import"
    module: "argparse"
    alias: null
  - kind: "from"
    module: "argparse"
    names: [{"name": "ArgumentParser", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.updater_factory"
    names: [{"name": "get_updater", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNetPar", "alias": null}, {"name": "PolicyNNetPar", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpArgs", "alias": null}, {"name": "Update", "alias": null}, {"name": "UpdateHeur", "alias": null}, {"name": "UpdatePolicy", "alias": null}]
  - kind: "from"
    module: "deepxube.base.trainer"
    names: [{"name": "TrainArgs", "alias": null}]
  - kind: "from"
    module: "deepxube.trainers.utils.train_loop"
    names: [{"name": "TestArgs", "alias": null}, {"name": "train", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.command_line_utils"
    names: [{"name": "get_domain_from_arg", "alias": null}, {"name": "get_heur_nnet_par_from_arg", "alias": null}, {"name": "get_policy_nnet_par_from_arg", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "pickle"
    alias: null
classes: []
module_level_functions:
  - "func:deepxube._train_cli.parser_train"
  - "func:deepxube._train_cli.train_cli"
module_level_constants: []
---

# Module `deepxube._train_cli`

**File:** [deepxube/_train_cli.py](../../deepxube/_train_cli.py)
**Lines:** 128

## Module docstring

CLI train command: parses training hyperparameters and launches the main training loop. 

## Contents

### Module-level functions
- `parser_train`
- `train_cli`

## Imports

- `from typing import Optional, List`
- `import argparse`
- `from argparse import ArgumentParser`
- `from deepxube.factories.updater_factory import get_updater`
- `from deepxube.base.domain import State, Goal`
- `from deepxube.base.heuristic import HeurNNetPar, PolicyNNetPar`
- `from deepxube.base.updater import UpArgs, Update, UpdateHeur, UpdatePolicy`
- `from deepxube.base.trainer import TrainArgs`
- `from deepxube.trainers.utils.train_loop import TestArgs, train`
- `from deepxube.utils.command_line_utils import get_domain_from_arg, get_heur_nnet_par_from_arg, get_policy_nnet_par_from_arg`
- `import numpy as np`
- `import pickle`
