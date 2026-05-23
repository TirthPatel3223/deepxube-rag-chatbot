---
id: "module:deepxube.domains.npuzzle"
kind: "module"
name: "npuzzle"
qualified_name: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_count: 365
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Union", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Parser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "ActsEnumFixed", "alias": null}, {"name": "GoalStartRevWalkableActsRev", "alias": null}, {"name": "StateGoalVizable", "alias": null}, {"name": "StringToAct", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "HasFlatSGIn", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "random"
    names: [{"name": "randrange", "alias": null}]
  - kind: "import"
    module: "matplotlib.patches"
    alias: "patches"
  - kind: "from"
    module: "matplotlib.figure"
    names: [{"name": "Figure", "alias": null}]
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
classes:
  - "class:deepxube.domains.npuzzle.NPState"
  - "class:deepxube.domains.npuzzle.NPGoal"
  - "class:deepxube.domains.npuzzle.NPAction"
  - "class:deepxube.domains.npuzzle.NPuzzle"
  - "class:deepxube.domains.npuzzle.GridParser"
module_level_functions: []
module_level_constants:
  - name: "int_t"
    annotation: null
    value_expr: "Union[np.uint8, np.int_]"
---

# Module `deepxube.domains.npuzzle`

**File:** [deepxube/domains/npuzzle.py](../../deepxube/domains/npuzzle.py)
**Lines:** 365

## Module docstring

N-puzzle (sliding tile) domain. Blank tile is 0; the goal configuration has tiles 1..(N²-1) followed by 0. 

## Contents

### Classes
- `NPState` — see `../classes/deepxube.domains.npuzzle/NPState.md`
- `NPGoal` — see `../classes/deepxube.domains.npuzzle/NPGoal.md`
- `NPAction` — see `../classes/deepxube.domains.npuzzle/NPAction.md`
- `NPuzzle` — see `../classes/deepxube.domains.npuzzle/NPuzzle.md`
- `GridParser` — see `../classes/deepxube.domains.npuzzle/GridParser.md`

### Module-level constants / TypeVars
- `int_t` = `Union[np.uint8, np.int_]`

## Imports

- `from typing import List, Tuple, Union, Optional, Dict, Any`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.domain import State, Action, Goal, ActsEnumFixed, GoalStartRevWalkableActsRev, StateGoalVizable, StringToAct`
- `from deepxube.factories.domain_factory import domain_factory`
- `from deepxube.base.nnet_input import HasFlatSGIn`
- `import numpy as np`
- `from random import randrange`
- `import matplotlib.patches as patches`
- `from matplotlib.figure import Figure`
- `from numpy.typing import NDArray`
