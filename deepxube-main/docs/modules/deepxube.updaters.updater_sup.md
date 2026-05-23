---
id: "module:deepxube.updaters.updater_sup"
kind: "module"
name: "updater_sup"
qualified_name: "deepxube.updaters.updater_sup"
file: "deepxube/updaters/updater_sup.py"
line_count: 131
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Type", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "Node", "alias": null}, {"name": "EdgeQ", "alias": null}, {"name": "InstanceEdge", "alias": null}, {"name": "InstanceNode", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpdatePolicy", "alias": null}, {"name": "UpdateHeurV", "alias": null}, {"name": "UpdateHeurQ", "alias": null}, {"name": "UpdateSup", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.updater_factory"
    names: [{"name": "updater_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "from"
    module: "deepxube.pathfinding.supervised_v"
    names: [{"name": "PathFindNodeSup", "alias": null}]
  - kind: "from"
    module: "deepxube.pathfinding.supervised_q"
    names: [{"name": "PathFindEdgeSup", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
classes:
  - "class:deepxube.updaters.updater_sup.UpdatePolicySup"
  - "class:deepxube.updaters.updater_sup.UpdateHeurVSup"
  - "class:deepxube.updaters.updater_sup.UpdateHeurQSup"
module_level_functions: []
module_level_constants: []
---

# Module `deepxube.updaters.updater_sup`

**File:** [deepxube/updaters/updater_sup.py](../../deepxube/updaters/updater_sup.py)
**Lines:** 131

## Module docstring

Supervised-learning updaters: train targets are the path costs produced
by supervised random-walk pathfinders (see ``deepxube/pathfinding/supervised_*``).

Three concrete updaters — for policy, V-heuristic, and Q-heuristic networks —
all register with ``updater_factory`` so the CLI can pick them when
``--pathfind`` resolves to a supervised pathfinder.

## Contents

### Classes
- `UpdatePolicySup` — see `../classes/deepxube.updaters.updater_sup/UpdatePolicySup.md`
- `UpdateHeurVSup` — see `../classes/deepxube.updaters.updater_sup/UpdateHeurVSup.md`
- `UpdateHeurQSup` — see `../classes/deepxube.updaters.updater_sup/UpdateHeurQSup.md`

## Imports

- `from typing import List, Type, Any`
- `from numpy.typing import NDArray`
- `from deepxube.base.domain import Domain, State, Action, Goal`
- `from deepxube.base.pathfinding import Node, EdgeQ, InstanceEdge, InstanceNode`
- `from deepxube.base.updater import UpdatePolicy, UpdateHeurV, UpdateHeurQ, UpdateSup`
- `from deepxube.factories.updater_factory import updater_factory`
- `from deepxube.utils.timing_utils import Times`
- `from deepxube.pathfinding.supervised_v import PathFindNodeSup`
- `from deepxube.pathfinding.supervised_q import PathFindEdgeSup`
- `import numpy as np`
