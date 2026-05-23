---
id: "module:deepxube.pathfinding.utils.performance"
kind: "module"
name: "performance"
qualified_name: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_count: 124
docstring_source: "present"
imports:
  - kind: "from"
    module: "dataclasses"
    names: [{"name": "dataclass", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Dict", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Goal", "alias": null}, {"name": "Action", "alias": null}, {"name": "Domain", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "Instance", "alias": null}]
classes:
  - "class:deepxube.pathfinding.utils.performance.PathFindPerf"
module_level_functions:
  - "func:deepxube.pathfinding.utils.performance.get_eq_weighted_perf"
  - "func:deepxube.pathfinding.utils.performance.print_pathfindperf"
  - "func:deepxube.pathfinding.utils.performance.is_valid_soln"
module_level_constants: []
---

# Module `deepxube.pathfinding.utils.performance`

**File:** [deepxube/pathfinding/utils/performance.py](../../deepxube/pathfinding/utils/performance.py)
**Lines:** 124

## Module docstring

Per-step pathfinding performance bookkeeping (solve rate, path cost,
search iters, root cost-to-go), plus a helper to validate a solution. 

## Contents

### Classes
- `PathFindPerf` — see `../classes/deepxube.pathfinding.utils.performance/PathFindPerf.md`

### Module-level functions
- `get_eq_weighted_perf`
- `print_pathfindperf`
- `is_valid_soln`

## Imports

- `from dataclasses import dataclass`
- `from typing import List, Tuple, Dict`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `from deepxube.base.domain import State, Goal, Action, Domain`
- `from deepxube.base.pathfinding import Instance`
