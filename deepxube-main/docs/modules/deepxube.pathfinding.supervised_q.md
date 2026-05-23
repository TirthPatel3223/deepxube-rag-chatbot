---
id: "module:deepxube.pathfinding.supervised_q"
kind: "module"
name: "supervised_q"
qualified_name: "deepxube.pathfinding.supervised_q"
file: "deepxube/pathfinding/supervised_q.py"
line_count: 163
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Any", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Type", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Tuple", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}, {"name": "StartGoalWalkable", "alias": null}, {"name": "GoalStartRevWalkableActsRev", "alias": null}, {"name": "Action", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "InstanceEdge", "alias": null}, {"name": "Node", "alias": null}, {"name": "EdgeQ", "alias": null}, {"name": "PathFindEdge", "alias": null}, {"name": "PathFindSup", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.pathfinding.supervised_q.InstanceEdgeSup"
  - "class:deepxube.pathfinding.supervised_q.PathFindEdgeSup"
  - "class:deepxube.pathfinding.supervised_q.PathFindEdgeSupRW"
  - "class:deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev"
module_level_functions: []
module_level_constants:
  - name: "D"
    annotation: null
    value_expr: "TypeVar('D', bound=Domain)"
---

# Module `deepxube.pathfinding.supervised_q`

**File:** [deepxube/pathfinding/supervised_q.py](../../deepxube/pathfinding/supervised_q.py)
**Lines:** 163

## Module docstring

Supervised Q-pathfinder: each "step" emits a single edge whose Q-value is
the random-walk path cost, used by ``UpdateHeurQSup`` to generate
(state, goal, action, q_target) training tuples without an actual search. 

## Contents

### Classes
- `InstanceEdgeSup` — see `../classes/deepxube.pathfinding.supervised_q/InstanceEdgeSup.md`
- `PathFindEdgeSup` — see `../classes/deepxube.pathfinding.supervised_q/PathFindEdgeSup.md`
- `PathFindEdgeSupRW` — see `../classes/deepxube.pathfinding.supervised_q/PathFindEdgeSupRW.md`
- `PathFindEdgeSupRWRev` — see `../classes/deepxube.pathfinding.supervised_q/PathFindEdgeSupRWRev.md`

### Module-level constants / TypeVars
- `D` = `TypeVar('D', bound=Domain)`

## Imports

- `from abc import ABC`
- `from typing import List, Any, Optional, Type, TypeVar, Tuple`
- `from deepxube.base.domain import Domain, State, Goal, StartGoalWalkable, GoalStartRevWalkableActsRev, Action`
- `from deepxube.base.pathfinding import InstanceEdge, Node, EdgeQ, PathFindEdge, PathFindSup`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory`
- `import numpy as np`
- `import time`
