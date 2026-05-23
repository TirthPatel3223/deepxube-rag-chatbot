---
id: "module:deepxube.domains.grid"
kind: "module"
name: "grid"
qualified_name: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_count: 230
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Any", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Type", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "matplotlib.figure"
    names: [{"name": "Figure", "alias": null}]
  - kind: "from"
    module: "torch"
    names: [{"name": "nn", "alias": null}, {"name": "Tensor", "alias": null}]
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Parser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "ActsEnumFixed", "alias": null}, {"name": "StartGoalWalkable", "alias": null}, {"name": "StateGoalVizable", "alias": null}, {"name": "StringToAct", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "StateGoalIn", "alias": null}, {"name": "HasFlatSGActsEnumFixedIn", "alias": null}, {"name": "HasFlatSGAIn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNet", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.pytorch_models"
    names: [{"name": "Conv2dModel", "alias": null}, {"name": "FullyConnectedModel", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.heuristic_factory"
    names: [{"name": "heuristic_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.nnet_input_factory"
    names: [{"name": "register_nnet_input", "alias": null}]
  - kind: "from"
    module: "matplotlib.colors"
    names: [{"name": "ListedColormap", "alias": null}]
  - kind: "import"
    module: "matplotlib.pyplot"
    alias: "plt"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "import"
    module: "re"
    alias: null
classes:
  - "class:deepxube.domains.grid.GridState"
  - "class:deepxube.domains.grid.GridGoal"
  - "class:deepxube.domains.grid.GridAction"
  - "class:deepxube.domains.grid.Grid"
  - "class:deepxube.domains.grid.GridParser"
  - "class:deepxube.domains.grid.GridNNetInput"
  - "class:deepxube.domains.grid.GridNet"
  - "class:deepxube.domains.grid.GridNetParser"
module_level_functions: []
module_level_constants: []
---

# Module `deepxube.domains.grid`

**File:** [deepxube/domains/grid.py](../../deepxube/domains/grid.py)
**Lines:** 230

## Module docstring

Grid navigation domain: a robot moves 4-directionally in a 2-D grid; the goal is to reach a target cell. 

## Contents

### Classes
- `GridState` — see `../classes/deepxube.domains.grid/GridState.md`
- `GridGoal` — see `../classes/deepxube.domains.grid/GridGoal.md`
- `GridAction` — see `../classes/deepxube.domains.grid/GridAction.md`
- `Grid` — see `../classes/deepxube.domains.grid/Grid.md`
- `GridParser` — see `../classes/deepxube.domains.grid/GridParser.md`
- `GridNNetInput` — see `../classes/deepxube.domains.grid/GridNNetInput.md`
- `GridNet` — see `../classes/deepxube.domains.grid/GridNet.md`
- `GridNetParser` — see `../classes/deepxube.domains.grid/GridNetParser.md`

## Imports

- `from typing import List, Tuple, Dict, Any, Optional, Type`
- `import numpy as np`
- `from matplotlib.figure import Figure`
- `from torch import nn, Tensor`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.domain import State, Action, Goal, ActsEnumFixed, StartGoalWalkable, StateGoalVizable, StringToAct`
- `from deepxube.base.nnet_input import StateGoalIn, HasFlatSGActsEnumFixedIn, HasFlatSGAIn`
- `from deepxube.base.heuristic import HeurNNet`
- `from deepxube.nnet.pytorch_models import Conv2dModel, FullyConnectedModel`
- `from deepxube.factories.heuristic_factory import heuristic_factory`
- `from deepxube.factories.domain_factory import domain_factory`
- `from deepxube.factories.nnet_input_factory import register_nnet_input`
- `from matplotlib.colors import ListedColormap`
- `import matplotlib.pyplot as plt`
- `from numpy.typing import NDArray`
- `import re`
