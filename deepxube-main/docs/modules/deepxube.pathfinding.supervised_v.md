---
id: "module:deepxube.pathfinding.supervised_v"
kind: "module"
name: "supervised_v"
qualified_name: "deepxube.pathfinding.supervised_v"
file: "deepxube/pathfinding/supervised_v.py"
line_count: 133
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
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}, {"name": "StartGoalWalkable", "alias": null}, {"name": "GoalStartRevWalkable", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "InstanceNode", "alias": null}, {"name": "Node", "alias": null}, {"name": "EdgeQ", "alias": null}, {"name": "PathFindNode", "alias": null}, {"name": "PathFindSup", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}]
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.pathfinding.supervised_v.InstanceNodeSup"
  - "class:deepxube.pathfinding.supervised_v.PathFindNodeSup"
  - "class:deepxube.pathfinding.supervised_v.PathFindNodeSupRW"
  - "class:deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev"
module_level_functions: []
module_level_constants:
  - name: "D"
    annotation: null
    value_expr: "TypeVar('D', bound=Domain)"
---

# Module `deepxube.pathfinding.supervised_v`

**File:** [deepxube/pathfinding/supervised_v.py](../../deepxube/pathfinding/supervised_v.py)
**Lines:** 133

## Module docstring

Supervised V-pathfinder: each "step" emits a single node carrying the
random-walk path cost as its heuristic target. Used by ``UpdateHeurVSup`` to
generate (state, goal, ctg) training tuples without running an actual search. 

## Contents

### Classes
- `InstanceNodeSup` — see `../classes/deepxube.pathfinding.supervised_v/InstanceNodeSup.md`
- `PathFindNodeSup` — see `../classes/deepxube.pathfinding.supervised_v/PathFindNodeSup.md`
- `PathFindNodeSupRW` — see `../classes/deepxube.pathfinding.supervised_v/PathFindNodeSupRW.md`
- `PathFindNodeSupRWRev` — see `../classes/deepxube.pathfinding.supervised_v/PathFindNodeSupRWRev.md`

### Module-level constants / TypeVars
- `D` = `TypeVar('D', bound=Domain)`

## Imports

- `from abc import ABC`
- `from typing import List, Any, Optional, Type, TypeVar, Tuple`
- `from deepxube.base.domain import Domain, State, Goal, StartGoalWalkable, GoalStartRevWalkable`
- `from deepxube.base.pathfinding import InstanceNode, Node, EdgeQ, PathFindNode, PathFindSup`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory`
- `import time`
