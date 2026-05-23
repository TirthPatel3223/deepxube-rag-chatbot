---
id: "module:deepxube.domains.lightsout"
kind: "module"
name: "lightsout"
qualified_name: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_count: 165
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Any", "alias": null}, {"name": "cast", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Parser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "HasFlatSGAIn", "alias": null}, {"name": "HasFlatSGActsEnumFixedIn", "alias": null}, {"name": "HasTwoDSGActsEnumFixedIn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "GoalStartRevWalkableActsRev", "alias": null}, {"name": "NextStateNPActsEnumFixed", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
classes:
  - "class:deepxube.domains.lightsout.LOState"
  - "class:deepxube.domains.lightsout.LOGoal"
  - "class:deepxube.domains.lightsout.LOAction"
  - "class:deepxube.domains.lightsout.LightsOut"
  - "class:deepxube.domains.lightsout.LightsOutParser"
module_level_functions: []
module_level_constants: []
---

# Module `deepxube.domains.lightsout`

**File:** [deepxube/domains/lightsout.py](../../deepxube/domains/lightsout.py)
**Lines:** 165

## Module docstring

Lights Out puzzle domain: toggling a cell flips it and its 4 cardinal neighbours; the goal is all lights off. 

## Contents

### Classes
- `LOState` — see `../classes/deepxube.domains.lightsout/LOState.md`
- `LOGoal` — see `../classes/deepxube.domains.lightsout/LOGoal.md`
- `LOAction` — see `../classes/deepxube.domains.lightsout/LOAction.md`
- `LightsOut` — see `../classes/deepxube.domains.lightsout/LightsOut.md`
- `LightsOutParser` — see `../classes/deepxube.domains.lightsout/LightsOutParser.md`

## Imports

- `from typing import List, Tuple, Dict, Optional, Any, cast`
- `import numpy as np`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.nnet_input import HasFlatSGAIn, HasFlatSGActsEnumFixedIn, HasTwoDSGActsEnumFixedIn`
- `from deepxube.base.domain import State, Action, Goal, GoalStartRevWalkableActsRev, NextStateNPActsEnumFixed`
- `from deepxube.factories.domain_factory import domain_factory`
- `from numpy.typing import NDArray`
