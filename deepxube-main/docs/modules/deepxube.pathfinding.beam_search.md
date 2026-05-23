---
id: "module:deepxube.pathfinding.beam_search"
kind: "module"
name: "beam_search"
qualified_name: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_count: 369
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Any", "alias": null}, {"name": "Type", "alias": null}, {"name": "Optional", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Dict", "alias": null}]
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Parser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "ActsEnum", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "Instance", "alias": null}, {"name": "InstanceNode", "alias": null}, {"name": "InstanceEdge", "alias": null}, {"name": "Node", "alias": null}, {"name": "EdgeQ", "alias": null}, {"name": "FNs", "alias": null}, {"name": "FNsHV", "alias": null}, {"name": "FNsHQ", "alias": null}, {"name": "FNsPolicy", "alias": null}, {"name": "FNsHeurQ", "alias": null}, {"name": "FNsHeurV", "alias": null}, {"name": "FNsHeurQPolicy", "alias": null}, {"name": "FNsHeurVPolicy", "alias": null}, {"name": "PathFind", "alias": null}, {"name": "PathFindNode", "alias": null}, {"name": "PathFindEdge", "alias": null}, {"name": "PathFindActsPolicy", "alias": null}, {"name": "PathFindSetPolicy", "alias": null}, {"name": "PathFindSetHeurV", "alias": null}, {"name": "PathFindSetHeurQ", "alias": null}, {"name": "PathFindActsEnum", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.misc_utils"
    names: [{"name": "boltzmann", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "time"
    alias: null
  - kind: "import"
    module: "re"
    alias: null
classes:
  - "class:deepxube.pathfinding.beam_search.InstanceBeam"
  - "class:deepxube.pathfinding.beam_search.BeamSearch"
  - "class:deepxube.pathfinding.beam_search.InstanceNodeBeam"
  - "class:deepxube.pathfinding.beam_search.InstanceEdgeBeam"
  - "class:deepxube.pathfinding.beam_search.BeamSearchPolicy"
  - "class:deepxube.pathfinding.beam_search.BeamSearchHeurNode"
  - "class:deepxube.pathfinding.beam_search.BeamSearchHeurEdge"
  - "class:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum"
  - "class:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum"
  - "class:deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy"
  - "class:deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy"
  - "class:deepxube.pathfinding.beam_search.BeamSearchParser"
  - "class:deepxube.pathfinding.beam_search.BeamSearchPolicyParser"
  - "class:deepxube.pathfinding.beam_search.BeamSearchNodeParser"
  - "class:deepxube.pathfinding.beam_search.BeamSearchEdgeParser"
  - "class:deepxube.pathfinding.beam_search.BeamSearchNodeHasPolicyParser"
  - "class:deepxube.pathfinding.beam_search.BeamSearchEdgeHasPolicyParser"
module_level_functions: []
module_level_constants:
  - name: "D"
    annotation: null
    value_expr: "TypeVar('D', bound=Domain)"
  - name: "IBeam"
    annotation: null
    value_expr: "TypeVar('IBeam', bound=InstanceBeam)"
---

# Module `deepxube.pathfinding.beam_search`

**File:** [deepxube/pathfinding/beam_search.py](../../deepxube/pathfinding/beam_search.py)
**Lines:** 369

## Module docstring

Batch beam search variants. Each iteration keeps the top ``beam_size``
children (selected greedily, by Boltzmann sampling at temperature ``temp``,
or with ``eps`` random replacements). Variants exist for V/Q heuristics,
policy-only, and combined V/Q + policy. Parsers live at the bottom so CLI
arguments like ``beam_v.10B_1.0T_0.1E`` work. 

## Contents

### Classes
- `InstanceBeam` — see `../classes/deepxube.pathfinding.beam_search/InstanceBeam.md`
- `BeamSearch` — see `../classes/deepxube.pathfinding.beam_search/BeamSearch.md`
- `InstanceNodeBeam` — see `../classes/deepxube.pathfinding.beam_search/InstanceNodeBeam.md`
- `InstanceEdgeBeam` — see `../classes/deepxube.pathfinding.beam_search/InstanceEdgeBeam.md`
- `BeamSearchPolicy` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchPolicy.md`
- `BeamSearchHeurNode` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchHeurNode.md`
- `BeamSearchHeurEdge` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchHeurEdge.md`
- `BeamSearchHeurNodeActsEnum` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchHeurNodeActsEnum.md`
- `BeamSearchHeurEdgeActsEnum` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchHeurEdgeActsEnum.md`
- `BeamSearchHeurNodeActsPolicy` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchHeurNodeActsPolicy.md`
- `BeamSearchHeurEdgeActsPolicy` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchHeurEdgeActsPolicy.md`
- `BeamSearchParser` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchParser.md`
- `BeamSearchPolicyParser` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchPolicyParser.md`
- `BeamSearchNodeParser` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchNodeParser.md`
- `BeamSearchEdgeParser` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchEdgeParser.md`
- `BeamSearchNodeHasPolicyParser` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchNodeHasPolicyParser.md`
- `BeamSearchEdgeHasPolicyParser` — see `../classes/deepxube.pathfinding.beam_search/BeamSearchEdgeHasPolicyParser.md`

### Module-level constants / TypeVars
- `D` = `TypeVar('D', bound=Domain)`
- `IBeam` = `TypeVar('IBeam', bound=InstanceBeam)`

## Imports

- `from abc import ABC, abstractmethod`
- `from typing import List, Any, Type, Optional, TypeVar, Dict`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.domain import Domain, ActsEnum, State, Goal`
- `from deepxube.base.pathfinding import Instance, InstanceNode, InstanceEdge, Node, EdgeQ, FNs, FNsHV, FNsHQ, FNsPolicy, FNsHeurQ, FNsHeurV, FNsHeurQPolicy, FNsHeurVPolicy, PathFind, PathFindNode, PathFindEdge, PathFindActsPolicy, PathFindSetPolicy, PathFindSetHeurV, PathFindSetHeurQ, PathFindActsEnum`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory`
- `from deepxube.utils.misc_utils import boltzmann`
- `import numpy as np`
- `import time`
- `import re`
