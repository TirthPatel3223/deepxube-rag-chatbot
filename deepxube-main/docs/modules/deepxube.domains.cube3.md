---
id: "module:deepxube.domains.cube3"
kind: "module"
name: "cube3"
qualified_name: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_count: 712
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "cast", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "GoalStartRevWalkableActsRev", "alias": null}, {"name": "NextStateNPActsEnumFixed", "alias": null}, {"name": "StateGoalVizable", "alias": null}, {"name": "StringToAct", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "HasFlatSGActsEnumFixedIn", "alias": null}, {"name": "HasFlatSGAIn", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "matplotlib"
    names: [{"name": "pyplot", "alias": "plt"}]
  - kind: "from"
    module: "matplotlib.figure"
    names: [{"name": "Figure", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
classes:
  - "class:deepxube.domains.cube3.Cube3State"
  - "class:deepxube.domains.cube3.Cube3Goal"
  - "class:deepxube.domains.cube3.Cube3Action"
  - "class:deepxube.domains.cube3.Quaternion"
  - "class:deepxube.domains.cube3.InteractiveCube"
  - "class:deepxube.domains.cube3.Cube3"
module_level_functions:
  - "func:deepxube.domains.cube3._get_adj"
  - "func:deepxube.domains.cube3.project_points"
module_level_constants: []
---

# Module `deepxube.domains.cube3`

**File:** [deepxube/domains/cube3.py](../../deepxube/domains/cube3.py)
**Lines:** 712

## Module docstring

Rubik's Cube (3×3×3) domain: 12 quarter-turn moves (6 faces × ±1); goal is a solved colour configuration. 

## Contents

### Classes
- `Cube3State` — see `../classes/deepxube.domains.cube3/Cube3State.md`
- `Cube3Goal` — see `../classes/deepxube.domains.cube3/Cube3Goal.md`
- `Cube3Action` — see `../classes/deepxube.domains.cube3/Cube3Action.md`
- `Quaternion` — see `../classes/deepxube.domains.cube3/Quaternion.md`
- `InteractiveCube` — see `../classes/deepxube.domains.cube3/InteractiveCube.md`
- `Cube3` — see `../classes/deepxube.domains.cube3/Cube3.md`

### Module-level functions
- `_get_adj`
- `project_points`

## Imports

- `from typing import List, Dict, Tuple, Optional, cast`
- `from deepxube.base.domain import State, Action, Goal, GoalStartRevWalkableActsRev, NextStateNPActsEnumFixed, StateGoalVizable, StringToAct`
- `from deepxube.base.nnet_input import HasFlatSGActsEnumFixedIn, HasFlatSGAIn`
- `from deepxube.factories.domain_factory import domain_factory`
- `from matplotlib import pyplot as plt`
- `from matplotlib.figure import Figure`
- `import numpy as np`
- `from numpy.typing import NDArray`
