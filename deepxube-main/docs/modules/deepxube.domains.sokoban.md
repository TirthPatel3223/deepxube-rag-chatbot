---
id: "module:deepxube.domains.sokoban"
kind: "module"
name: "sokoban"
qualified_name: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_count: 365
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Tuple", "alias": null}, {"name": "List", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Dict", "alias": null}, {"name": "cast", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "FlatIn", "alias": null}, {"name": "StateGoalIn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "ActsEnumFixed", "alias": null}, {"name": "StartGoalWalkable", "alias": null}, {"name": "StateGoalVizable", "alias": null}, {"name": "StringToAct", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.nnet_input_factory"
    names: [{"name": "register_nnet_input", "alias": null}]
  - kind: "from"
    module: "matplotlib.figure"
    names: [{"name": "Figure", "alias": null}]
  - kind: "import"
    module: "pickle"
    alias: null
  - kind: "import"
    module: "pathlib"
    alias: null
  - kind: "import"
    module: "tarfile"
    alias: null
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "wget"
    alias: null
  - kind: "from"
    module: "filelock"
    names: [{"name": "FileLock", "alias": null}]
classes:
  - "class:deepxube.domains.sokoban.SkState"
  - "class:deepxube.domains.sokoban.SkGoal"
  - "class:deepxube.domains.sokoban.SkAction"
  - "class:deepxube.domains.sokoban.Sokoban"
  - "class:deepxube.domains.sokoban.SkNNetInput"
module_level_functions:
  - "func:deepxube.domains.sokoban.load_states"
  - "func:deepxube.domains.sokoban._get_surfaces"
  - "func:deepxube.domains.sokoban._get_train_states"
  - "func:deepxube.domains.sokoban.get_data_dir"
module_level_constants: []
---

# Module `deepxube.domains.sokoban`

**File:** [deepxube/domains/sokoban.py](../../deepxube/domains/sokoban.py)
**Lines:** 365

## Module docstring

Sokoban domain: agent pushes boxes to target positions on a 10×10 grid; data loaded from a pre-built training set. 

## Contents

### Classes
- `SkState` — see `../classes/deepxube.domains.sokoban/SkState.md`
- `SkGoal` — see `../classes/deepxube.domains.sokoban/SkGoal.md`
- `SkAction` — see `../classes/deepxube.domains.sokoban/SkAction.md`
- `Sokoban` — see `../classes/deepxube.domains.sokoban/Sokoban.md`
- `SkNNetInput` — see `../classes/deepxube.domains.sokoban/SkNNetInput.md`

### Module-level functions
- `load_states`
- `_get_surfaces`
- `_get_train_states`
- `get_data_dir`

## Imports

- `from typing import Tuple, List, Optional, Dict, cast`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `from deepxube.base.nnet_input import FlatIn, StateGoalIn`
- `from deepxube.base.domain import State, Action, Goal, ActsEnumFixed, StartGoalWalkable, StateGoalVizable, StringToAct`
- `from deepxube.factories.domain_factory import domain_factory`
- `from deepxube.factories.nnet_input_factory import register_nnet_input`
- `from matplotlib.figure import Figure`
- `import pickle`
- `import pathlib`
- `import tarfile`
- `import os`
- `import wget`
- `from filelock import FileLock`
