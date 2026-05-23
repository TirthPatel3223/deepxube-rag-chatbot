---
id: "module:deepxube.pathfinding.graph_search"
kind: "module"
name: "graph_search"
qualified_name: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_count: 348
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Any", "alias": null}, {"name": "Type", "alias": null}, {"name": "Optional", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Generic", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Dict", "alias": null}]
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Parser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "ActsEnum", "alias": null}, {"name": "State", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "Instance", "alias": null}, {"name": "InstanceNode", "alias": null}, {"name": "InstanceEdge", "alias": null}, {"name": "Node", "alias": null}, {"name": "EdgeQ", "alias": null}, {"name": "FNs", "alias": null}, {"name": "FNsHV", "alias": null}, {"name": "FNsHQ", "alias": null}, {"name": "FNsHeurQ", "alias": null}, {"name": "FNsHeurV", "alias": null}, {"name": "FNsHeurQPolicy", "alias": null}, {"name": "FNsHeurVPolicy", "alias": null}, {"name": "PathFind", "alias": null}, {"name": "PathFindNode", "alias": null}, {"name": "PathFindEdge", "alias": null}, {"name": "PathFindActsPolicy", "alias": null}, {"name": "PathFindSetHeurV", "alias": null}, {"name": "PathFindSetHeurQ", "alias": null}, {"name": "PathFindActsEnum", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "misc_utils", "alias": null}]
  - kind: "from"
    module: "heapq"
    names: [{"name": "heappush", "alias": null}, {"name": "heappop", "alias": null}, {"name": "heapify", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "random"
    alias: null
  - kind: "import"
    module: "time"
    alias: null
  - kind: "import"
    module: "re"
    alias: null
classes:
  - "class:deepxube.pathfinding.graph_search.InstanceGraph"
  - "class:deepxube.pathfinding.graph_search.GraphSearch"
  - "class:deepxube.pathfinding.graph_search.InstanceNodeGraph"
  - "class:deepxube.pathfinding.graph_search.InstanceEdgeGraph"
  - "class:deepxube.pathfinding.graph_search.GraphSearchHeurNode"
  - "class:deepxube.pathfinding.graph_search.GraphSearchHeurEdge"
  - "class:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum"
  - "class:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum"
  - "class:deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy"
  - "class:deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy"
  - "class:deepxube.pathfinding.graph_search.GraphSearchParser"
  - "class:deepxube.pathfinding.graph_search.GraphSearchNodeParser"
  - "class:deepxube.pathfinding.graph_search.GraphSearchEdgeParser"
  - "class:deepxube.pathfinding.graph_search.GraphSearchNodeHasPolicyParser"
  - "class:deepxube.pathfinding.graph_search.GraphSearchEdgeHasPolicyParser"
module_level_functions: []
module_level_constants:
  - name: "SchOver"
    annotation: null
    value_expr: "TypeVar('SchOver')"
  - name: "D"
    annotation: null
    value_expr: "TypeVar('D', bound=Domain)"
  - name: "IGraph"
    annotation: null
    value_expr: "TypeVar('IGraph', bound=InstanceGraph)"
---

# Module `deepxube.pathfinding.graph_search`

**File:** [deepxube/pathfinding/graph_search.py](../../deepxube/pathfinding/graph_search.py)
**Lines:** 348

## Module docstring

Weighted best-first graph-search variants (A*, GBFS, and hybrids). Supports node-based V heuristics and
edge-based Q heuristics, batch expansion, and epsilon-random pop. Parsers at the bottom enable CLI flags like
``graph_v.10B_0.5W_0.1E``. 

## Contents

### Classes
- `InstanceGraph` — see `../classes/deepxube.pathfinding.graph_search/InstanceGraph.md`
- `GraphSearch` — see `../classes/deepxube.pathfinding.graph_search/GraphSearch.md`
- `InstanceNodeGraph` — see `../classes/deepxube.pathfinding.graph_search/InstanceNodeGraph.md`
- `InstanceEdgeGraph` — see `../classes/deepxube.pathfinding.graph_search/InstanceEdgeGraph.md`
- `GraphSearchHeurNode` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchHeurNode.md`
- `GraphSearchHeurEdge` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchHeurEdge.md`
- `GraphSearchHeurNodeActsEnum` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchHeurNodeActsEnum.md`
- `GraphSearchHeurEdgeActsEnum` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchHeurEdgeActsEnum.md`
- `GraphSearchHeurNodeActsPolicy` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchHeurNodeActsPolicy.md`
- `GraphSearchHeurEdgeActsPolicy` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchHeurEdgeActsPolicy.md`
- `GraphSearchParser` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchParser.md`
- `GraphSearchNodeParser` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchNodeParser.md`
- `GraphSearchEdgeParser` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchEdgeParser.md`
- `GraphSearchNodeHasPolicyParser` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchNodeHasPolicyParser.md`
- `GraphSearchEdgeHasPolicyParser` — see `../classes/deepxube.pathfinding.graph_search/GraphSearchEdgeHasPolicyParser.md`

### Module-level constants / TypeVars
- `SchOver` = `TypeVar('SchOver')`
- `D` = `TypeVar('D', bound=Domain)`
- `IGraph` = `TypeVar('IGraph', bound=InstanceGraph)`

## Imports

- `from abc import ABC, abstractmethod`
- `from typing import List, Any, Type, Optional, TypeVar, Generic, Tuple, Dict`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.domain import Domain, ActsEnum, State, Goal`
- `from deepxube.base.pathfinding import Instance, InstanceNode, InstanceEdge, Node, EdgeQ, FNs, FNsHV, FNsHQ, FNsHeurQ, FNsHeurV, FNsHeurQPolicy, FNsHeurVPolicy, PathFind, PathFindNode, PathFindEdge, PathFindActsPolicy, PathFindSetHeurV, PathFindSetHeurQ, PathFindActsEnum`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory`
- `from deepxube.utils import misc_utils`
- `from heapq import heappush, heappop, heapify`
- `import numpy as np`
- `import random`
- `import time`
- `import re`
