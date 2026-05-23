---
id: "module:deepxube.base.pathfinding"
kind: "module"
name: "pathfinding"
qualified_name: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_count: 872
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Generic", "alias": null}, {"name": "List", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Any", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Callable", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Type", "alias": null}, {"name": "Union", "alias": null}]
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}, {"name": "Action", "alias": null}, {"name": "ActsEnum", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurFnV", "alias": null}, {"name": "HeurFnQ", "alias": null}, {"name": "PolicyFn", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "misc_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "from"
    module: "dataclasses"
    names: [{"name": "dataclass", "alias": null}]
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "time"
    alias: null
classes:
  - "class:deepxube.base.pathfinding.Node"
  - "class:deepxube.base.pathfinding.EdgeQ"
  - "class:deepxube.base.pathfinding.Instance"
  - "class:deepxube.base.pathfinding.FNsHeurV"
  - "class:deepxube.base.pathfinding.FNsHeurQ"
  - "class:deepxube.base.pathfinding.FNsPolicy"
  - "class:deepxube.base.pathfinding.FNsHeurVPolicy"
  - "class:deepxube.base.pathfinding.FNsHeurQPolicy"
  - "class:deepxube.base.pathfinding.PathFind"
  - "class:deepxube.base.pathfinding.InstanceNode"
  - "class:deepxube.base.pathfinding.InstanceEdge"
  - "class:deepxube.base.pathfinding.PathFindNode"
  - "class:deepxube.base.pathfinding.PathFindEdge"
  - "class:deepxube.base.pathfinding.PathFindSetPolicy"
  - "class:deepxube.base.pathfinding.PathFindSetHeurV"
  - "class:deepxube.base.pathfinding.PathFindSetHeurQ"
  - "class:deepxube.base.pathfinding.PathFindActsEnum"
  - "class:deepxube.base.pathfinding.PathFindActsPolicy"
  - "class:deepxube.base.pathfinding.PathFindSup"
module_level_functions:
  - "func:deepxube.base.pathfinding.get_path"
module_level_constants:
  - name: "FNsHeur"
    annotation: null
    value_expr: "Union[FNsHeurV, FNsHeurQ]"
  - name: "I"
    annotation: null
    value_expr: "TypeVar('I', bound=Instance)"
  - name: "D"
    annotation: null
    value_expr: "TypeVar('D', bound=Domain)"
  - name: "FNs"
    annotation: null
    value_expr: "TypeVar('FNs')"
  - name: "INode"
    annotation: null
    value_expr: "TypeVar('INode', bound=InstanceNode)"
  - name: "IEdge"
    annotation: null
    value_expr: "TypeVar('IEdge', bound=InstanceEdge)"
  - name: "FNsP"
    annotation: null
    value_expr: "TypeVar('FNsP', bound=FNsPolicy)"
  - name: "FNsHV"
    annotation: null
    value_expr: "TypeVar('FNsHV', bound=FNsHeurV)"
  - name: "FNsHQ"
    annotation: null
    value_expr: "TypeVar('FNsHQ', bound=FNsHeurQ)"
  - name: "DActsEnum"
    annotation: null
    value_expr: "TypeVar('DActsEnum', bound=ActsEnum)"
---

# Module `deepxube.base.pathfinding`

**File:** [deepxube/base/pathfinding.py](../../deepxube/base/pathfinding.py)
**Lines:** 872

## Module docstring

Abstract pathfinding base classes plus shared search-tree data structures.

A ``PathFind`` runs a batch of ``Instance`` objects in lockstep: at each
``step()`` it pops nodes (or edges) from the open set across all instances,
checks goal/expand/score, and pushes children. The ``FNs*`` dataclasses bundle
the heuristic / policy callables a pathfinder needs. Concrete pathfinders in
``deepxube/pathfinding/`` plug specific open-set policies into this skeleton. 

## Contents

### Classes
- `Node` — see `../classes/deepxube.base.pathfinding/Node.md`
- `EdgeQ` — see `../classes/deepxube.base.pathfinding/EdgeQ.md`
- `Instance` — see `../classes/deepxube.base.pathfinding/Instance.md`
- `FNsHeurV` — see `../classes/deepxube.base.pathfinding/FNsHeurV.md`
- `FNsHeurQ` — see `../classes/deepxube.base.pathfinding/FNsHeurQ.md`
- `FNsPolicy` — see `../classes/deepxube.base.pathfinding/FNsPolicy.md`
- `FNsHeurVPolicy` — see `../classes/deepxube.base.pathfinding/FNsHeurVPolicy.md`
- `FNsHeurQPolicy` — see `../classes/deepxube.base.pathfinding/FNsHeurQPolicy.md`
- `PathFind` — see `../classes/deepxube.base.pathfinding/PathFind.md`
- `InstanceNode` — see `../classes/deepxube.base.pathfinding/InstanceNode.md`
- `InstanceEdge` — see `../classes/deepxube.base.pathfinding/InstanceEdge.md`
- `PathFindNode` — see `../classes/deepxube.base.pathfinding/PathFindNode.md`
- `PathFindEdge` — see `../classes/deepxube.base.pathfinding/PathFindEdge.md`
- `PathFindSetPolicy` — see `../classes/deepxube.base.pathfinding/PathFindSetPolicy.md`
- `PathFindSetHeurV` — see `../classes/deepxube.base.pathfinding/PathFindSetHeurV.md`
- `PathFindSetHeurQ` — see `../classes/deepxube.base.pathfinding/PathFindSetHeurQ.md`
- `PathFindActsEnum` — see `../classes/deepxube.base.pathfinding/PathFindActsEnum.md`
- `PathFindActsPolicy` — see `../classes/deepxube.base.pathfinding/PathFindActsPolicy.md`
- `PathFindSup` — see `../classes/deepxube.base.pathfinding/PathFindSup.md`

### Module-level functions
- `get_path`

### Module-level constants / TypeVars
- `FNsHeur` = `Union[FNsHeurV, FNsHeurQ]`
- `I` = `TypeVar('I', bound=Instance)`
- `D` = `TypeVar('D', bound=Domain)`
- `FNs` = `TypeVar('FNs')`
- `INode` = `TypeVar('INode', bound=InstanceNode)`
- `IEdge` = `TypeVar('IEdge', bound=InstanceEdge)`
- `FNsP` = `TypeVar('FNsP', bound=FNsPolicy)`
- `FNsHV` = `TypeVar('FNsHV', bound=FNsHeurV)`
- `FNsHQ` = `TypeVar('FNsHQ', bound=FNsHeurQ)`
- `DActsEnum` = `TypeVar('DActsEnum', bound=ActsEnum)`

## Imports

- `from typing import Generic, List, Optional, Any, Tuple, Callable, TypeVar, Dict, Type, Union`
- `from numpy.typing import NDArray`
- `from deepxube.base.domain import Domain, State, Goal, Action, ActsEnum`
- `from deepxube.base.heuristic import HeurFnV, HeurFnQ, PolicyFn`
- `from deepxube.utils import misc_utils`
- `from deepxube.utils.timing_utils import Times`
- `from dataclasses import dataclass`
- `from abc import ABC, abstractmethod`
- `import numpy as np`
- `import time`
