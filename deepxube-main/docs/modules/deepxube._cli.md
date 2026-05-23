---
id: "module:deepxube._cli"
kind: "module"
name: "_cli"
qualified_name: "deepxube._cli"
file: "deepxube/_cli.py"
line_count: 424
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "cast", "alias": null}, {"name": "Type", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "import"
    module: "argparse"
    alias: null
  - kind: "from"
    module: "argparse"
    names: [{"name": "ArgumentParser", "alias": null}]
  - kind: "from"
    module: "deepxube._train_cli"
    names: [{"name": "parser_train", "alias": null}]
  - kind: "from"
    module: "deepxube._solve"
    names: [{"name": "parse_solve", "alias": null}]
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Parser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "StateGoalVizable", "alias": null}, {"name": "StringToAct", "alias": null}, {"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNet", "alias": null}, {"name": "HeurNNetPar", "alias": null}, {"name": "PolicyNNetPar", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "PathFind", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.nnet_input_factory"
    names: [{"name": "get_domain_nnet_input_keys", "alias": null}, {"name": "get_nnet_input_t", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.heuristic_factory"
    names: [{"name": "heuristic_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}, {"name": "get_domain_compat_pathfind_names", "alias": null}]
  - kind: "from"
    module: "deepxube.base.trainer"
    names: [{"name": "TrainSummary", "alias": null}]
  - kind: "from"
    module: "deepxube.tests.time_tests"
    names: [{"name": "time_test", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.command_line_utils"
    names: [{"name": "get_domain_from_arg", "alias": null}, {"name": "get_heur_nnet_par_from_arg", "alias": null}, {"name": "get_policy_nnet_par_from_arg", "alias": null}]
  - kind: "import"
    module: "matplotlib.pyplot"
    alias: "plt"
  - kind: "from"
    module: "matplotlib.axes"
    names: [{"name": "Axes", "alias": null}]
  - kind: "from"
    module: "matplotlib.widgets"
    names: [{"name": "Slider", "alias": null}]
  - kind: "from"
    module: "matplotlib.figure"
    names: [{"name": "Figure", "alias": null}]
  - kind: "import"
    module: "pickle"
    alias: null
  - kind: "import"
    module: "textwrap"
    alias: null
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "time"
    alias: null
classes: []
module_level_functions:
  - "func:deepxube._cli.plot_scatter"
  - "func:deepxube._cli.get_immediate_mixins"
  - "func:deepxube._cli.domain_info"
  - "func:deepxube._cli.heur_info"
  - "func:deepxube._cli.pathfinding_info"
  - "func:deepxube._cli.viz"
  - "func:deepxube._cli._viz_state_goal_update"
  - "func:deepxube._cli.time_test_args"
  - "func:deepxube._cli.plot_itr_data"
  - "func:deepxube._cli.train_summary"
  - "func:deepxube._cli.problem_inst_gen"
  - "func:deepxube._cli.main"
  - "func:deepxube._cli._parser_domain_info"
  - "func:deepxube._cli._parser_heur_info"
  - "func:deepxube._cli._parser_pathfind_info"
  - "func:deepxube._cli._parse_viz_info"
  - "func:deepxube._cli._parse_time"
  - "func:deepxube._cli._parse_problem_instance"
  - "func:deepxube._cli._parse_train_summary"
module_level_constants: []
---

# Module `deepxube._cli`

**File:** [deepxube/_cli.py](../../deepxube/_cli.py)
**Lines:** 424

## Module docstring

Top-level CLI: registers all subcommands (domain_info, viz, train, solve, …) and dispatches via argparse. 

## Contents

### Module-level functions
- `plot_scatter`
- `get_immediate_mixins` *(trivial, skipped)*
- `domain_info`
- `heur_info`
- `pathfinding_info`
- `viz`
- `_viz_state_goal_update` *(trivial, skipped)*
- `time_test_args`
- `plot_itr_data`
- `train_summary`
- `problem_inst_gen`
- `main`
- `_parser_domain_info` *(trivial, skipped)*
- `_parser_heur_info` *(trivial, skipped)*
- `_parser_pathfind_info` *(trivial, skipped)*
- `_parse_viz_info`
- `_parse_time`
- `_parse_problem_instance`
- `_parse_train_summary` *(trivial, skipped)*

## Imports

- `from typing import List, Optional, Tuple, cast, Type, Dict, Any`
- `import argparse`
- `from argparse import ArgumentParser`
- `from deepxube._train_cli import parser_train`
- `from deepxube._solve import parse_solve`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.domain import Domain, StateGoalVizable, StringToAct, State, Action, Goal`
- `from deepxube.base.heuristic import HeurNNet, HeurNNetPar, PolicyNNetPar`
- `from deepxube.base.pathfinding import PathFind`
- `from deepxube.factories.domain_factory import domain_factory`
- `from deepxube.factories.nnet_input_factory import get_domain_nnet_input_keys, get_nnet_input_t`
- `from deepxube.factories.heuristic_factory import heuristic_factory`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory, get_domain_compat_pathfind_names`
- `from deepxube.base.trainer import TrainSummary`
- `from deepxube.tests.time_tests import time_test`
- `from deepxube.utils.command_line_utils import get_domain_from_arg, get_heur_nnet_par_from_arg, get_policy_nnet_par_from_arg`
- `import matplotlib.pyplot as plt`
- `from matplotlib.axes import Axes`
- `from matplotlib.widgets import Slider`
- `from matplotlib.figure import Figure`
- `import pickle`
- `import textwrap`
- `import numpy as np`
- `from numpy.typing import NDArray`
- `import os`
- `import time`
