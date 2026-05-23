---
id: "module:deepxube.utils.command_line_utils"
kind: "module"
name: "command_line_utils"
qualified_name: "deepxube.utils.command_line_utils"
file: "deepxube/utils/command_line_utils.py"
line_count: 112
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNetPar", "alias": null}, {"name": "PolicyNNetPar", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "PathFind", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.heuristic_factory"
    names: [{"name": "heuristic_factory", "alias": null}, {"name": "policy_factory", "alias": null}, {"name": "build_heur_nnet_par", "alias": null}, {"name": "build_policy_nnet_par", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}]
classes: []
module_level_functions:
  - "func:deepxube.utils.command_line_utils.get_name_args"
  - "func:deepxube.utils.command_line_utils.get_domain_from_arg"
  - "func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg"
  - "func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg"
  - "func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs"
  - "func:deepxube.utils.command_line_utils.get_pathfind_from_arg"
module_level_constants: []
---

# Module `deepxube.utils.command_line_utils`

**File:** [deepxube/utils/command_line_utils.py](../../deepxube/utils/command_line_utils.py)
**Lines:** 112

## Module docstring

CLI-argument parsing helpers that resolve dotted strings like ``grid.7``
or ``resnet_fc.100H_2B_bn`` into fully-constructed domain, heuristic, policy,
or pathfinding objects via the factory registries.

The convention is ``<name>.<parser-args>``: the part before the first dot is
the factory registration key; the part after is handed to the registered
``Parser`` for that key.

## Contents

### Module-level functions
- `get_name_args`
- `get_domain_from_arg`
- `get_heur_nnet_par_from_arg`
- `get_policy_nnet_par_from_arg`
- `get_pathfind_name_kwargs`
- `get_pathfind_from_arg`

## Imports

- `from typing import Tuple, Optional, List, Dict, Any`
- `from deepxube.base.domain import Domain`
- `from deepxube.base.heuristic import HeurNNetPar, PolicyNNetPar`
- `from deepxube.base.pathfinding import PathFind`
- `from deepxube.factories.domain_factory import domain_factory`
- `from deepxube.factories.heuristic_factory import heuristic_factory, policy_factory, build_heur_nnet_par, build_policy_nnet_par`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory`
