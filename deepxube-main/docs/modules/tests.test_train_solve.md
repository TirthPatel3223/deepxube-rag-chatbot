---
id: "module:tests.test_train_solve"
kind: "module"
name: "test_train_solve"
qualified_name: "tests.test_train_solve"
file: "tests/test_train_solve.py"
line_count: 110
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "import"
    module: "pytest"
    alias: null
  - kind: "from"
    module: "deepxube.factories.updater_factory"
    names: [{"name": "get_updater", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNetPar", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "Node", "alias": null}, {"name": "Instance", "alias": null}, {"name": "get_path", "alias": null}]
  - kind: "from"
    module: "deepxube.pathfinding.utils.performance"
    names: [{"name": "is_valid_soln", "alias": null}, {"name": "PathFindPerf", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "PathFind", "alias": null}, {"name": "FNsHeurV", "alias": null}, {"name": "FNsHeurQ", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.command_line_utils"
    names: [{"name": "get_domain_from_arg", "alias": null}, {"name": "get_heur_nnet_par_from_arg", "alias": null}, {"name": "get_pathfind_from_arg", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "UpArgs", "alias": null}, {"name": "Update", "alias": null}, {"name": "UpdateHeur", "alias": null}]
  - kind: "from"
    module: "deepxube.base.trainer"
    names: [{"name": "TrainArgs", "alias": null}]
  - kind: "from"
    module: "deepxube.trainers.utils.train_loop"
    names: [{"name": "train", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet"
    names: [{"name": "nnet_utils", "alias": null}]
  - kind: "from"
    module: "itertools"
    names: [{"name": "product", "alias": null}]
  - kind: "import"
    module: "shutil"
    alias: null
  - kind: "from"
    module: "torch"
    names: [{"name": "nn", "alias": null}]
  - kind: "import"
    module: "os"
    alias: null
classes: []
module_level_functions:
  - "func:tests.test_train_solve.test_train_solve_heur"
module_level_constants:
  - name: "cases"
    annotation: null
    value_expr: "[pytest.param(a, b, c, d, e, f, g, 85.0, id='graph_v') for a, b, c, d, e, f, g in product(['graph_v'], ['graph_v'], ['V'], [True, False], [False], [1, -1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 85.0, id='beam_v') for a, b, c, d, e, f, g in product(['beam_v.1T'], ['beam_v'], ['V'], [True, False], [True, False], [1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 85.0, id='sup_v_rw') for a, b, c, d, e, f, g in product(['sup_v_rw'], ['graph_v'], ['V'], [False], [False], [1], [False])] + [pytest.param(a, b, c, d, e, f, g, 80.0, id='graph_q') for a, b, c, d, e, f, g in product(['graph_q'], ['graph_q'], ['QFix', 'QIn'], [True, False], [False], [1, -1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 80.0, id='beam_q') for a, b, c, d, e, f, g in product(['beam_q.1T'], ['beam_q'], ['QFix', 'QIn'], [True, False], [True, False], [1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 80.0, id='sup_q_rw') for a, b, c, d, e, f, g in product(['sup_q_rw'], ['graph_q'], ['QFix', 'QIn'], [False], [False], [1], [False])]"
---

# Module `tests.test_train_solve`

**File:** [tests/test_train_solve.py](../../tests/test_train_solve.py)
**Lines:** 110

## Module docstring

Integration tests: train a heuristic on a small Grid domain and verify solve rate meets a threshold. 

## Contents

### Module-level functions
- `test_train_solve_heur`

### Module-level constants / TypeVars
- `cases` = `[pytest.param(a, b, c, d, e, f, g, 85.0, id='graph_v') for a, b, c, d, e, f, g in product(['graph_v'], ['graph_v'], ['V'], [True, False], [False], [1, -1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 85.0, id='beam_v') for a, b, c, d, e, f, g in product(['beam_v.1T'], ['beam_v'], ['V'], [True, False], [True, False], [1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 85.0, id='sup_v_rw') for a, b, c, d, e, f, g in product(['sup_v_rw'], ['graph_v'], ['V'], [False], [False], [1], [False])] + [pytest.param(a, b, c, d, e, f, g, 80.0, id='graph_q') for a, b, c, d, e, f, g in product(['graph_q'], ['graph_q'], ['QFix', 'QIn'], [True, False], [False], [1, -1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 80.0, id='beam_q') for a, b, c, d, e, f, g in product(['beam_q.1T'], ['beam_q'], ['QFix', 'QIn'], [True, False], [True, False], [1], [True, False])] + [pytest.param(a, b, c, d, e, f, g, 80.0, id='sup_q_rw') for a, b, c, d, e, f, g in product(['sup_q_rw'], ['graph_q'], ['QFix', 'QIn'], [False], [False], [1], [False])]`

## Imports

- `from typing import List, Optional, Any`
- `import pytest`
- `from deepxube.factories.updater_factory import get_updater`
- `from deepxube.base.heuristic import HeurNNetPar`
- `from deepxube.base.pathfinding import Node, Instance, get_path`
- `from deepxube.pathfinding.utils.performance import is_valid_soln, PathFindPerf`
- `from deepxube.base.pathfinding import PathFind, FNsHeurV, FNsHeurQ`
- `from deepxube.utils.command_line_utils import get_domain_from_arg, get_heur_nnet_par_from_arg, get_pathfind_from_arg`
- `from deepxube.base.updater import UpArgs, Update, UpdateHeur`
- `from deepxube.base.trainer import TrainArgs`
- `from deepxube.trainers.utils.train_loop import train`
- `from deepxube.nnet import nnet_utils`
- `from itertools import product`
- `import shutil`
- `from torch import nn`
- `import os`
