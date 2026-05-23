---
id: "module:deepxube.factories.heuristic_factory"
kind: "module"
name: "heuristic_factory"
qualified_name: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_count: 363
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "Dict", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Type", "alias": null}, {"name": "List", "alias": null}, {"name": "Any", "alias": null}, {"name": "Optional", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Factory", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "ActsEnumFixed", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "NNetInput", "alias": null}, {"name": "StateGoalIn", "alias": null}, {"name": "StateGoalActFixIn", "alias": null}, {"name": "StateGoalActIn", "alias": null}, {"name": "PolicyNNetIn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNet", "alias": null}, {"name": "PolicyNNet", "alias": null}, {"name": "HeurNNetPar", "alias": null}, {"name": "PolicyNNetPar", "alias": null}, {"name": "HeurNNetParV", "alias": null}, {"name": "HeurNNetParQIn", "alias": null}, {"name": "HeurNNetParQFixOut", "alias": null}]
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.nnet_input_factory"
    names: [{"name": "get_domain_nnet_input_keys", "alias": null}, {"name": "get_nnet_input_t", "alias": null}]
classes:
  - "class:deepxube.factories.heuristic_factory.HeurNNetParFacClass"
  - "class:deepxube.factories.heuristic_factory.PolicyNNetParFacClass"
  - "class:deepxube.factories.heuristic_factory.HeurNNetParVConcrete"
  - "class:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete"
  - "class:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete"
  - "class:deepxube.factories.heuristic_factory.PolicyNNetParConcrete"
module_level_functions:
  - "func:deepxube.factories.heuristic_factory.build_heur_nnet_par"
  - "func:deepxube.factories.heuristic_factory.build_policy_nnet_par"
module_level_constants:
  - name: "heuristic_factory"
    annotation: "Factory[HeurNNet]"
    value_expr: "Factory[HeurNNet]('HeurNNet')"
  - name: "policy_factory"
    annotation: "Factory[PolicyNNet]"
    value_expr: "Factory[PolicyNNet]('PolicyNNet')"
---

# Module `deepxube.factories.heuristic_factory`

**File:** [deepxube/factories/heuristic_factory.py](../../deepxube/factories/heuristic_factory.py)
**Lines:** 363

## Module docstring

Registries for heuristic and policy neural networks, plus builders that
pair a registered network with a compatible per-domain ``NNetInput``.

The factories here are used to turn a CLI pair like
``(--domain grid.7, --heur resnet_fc.100H_2B_bn, --heur_type V)`` into a
fully-wired ``HeurNNetPar`` that knows how to convert states/goals into numpy
arrays and then into a network. The concrete ``*Concrete`` subclasses at the
bottom of this file plug the right ``NNetInput`` into the right
``HeurNNetPar`` / ``PolicyNNetPar`` variant.

## Contents

### Classes
- `HeurNNetParFacClass` — see `../classes/deepxube.factories.heuristic_factory/HeurNNetParFacClass.md`
- `PolicyNNetParFacClass` — see `../classes/deepxube.factories.heuristic_factory/PolicyNNetParFacClass.md`
- `HeurNNetParVConcrete` — see `../classes/deepxube.factories.heuristic_factory/HeurNNetParVConcrete.md`
- `HeurNNetParQFixOutConcrete` — see `../classes/deepxube.factories.heuristic_factory/HeurNNetParQFixOutConcrete.md`
- `HeurNNetParQActInConcrete` — see `../classes/deepxube.factories.heuristic_factory/HeurNNetParQActInConcrete.md`
- `PolicyNNetParConcrete` — see `../classes/deepxube.factories.heuristic_factory/PolicyNNetParConcrete.md`

### Module-level functions
- `build_heur_nnet_par`
- `build_policy_nnet_par`

### Module-level constants / TypeVars
- `heuristic_factory`: `Factory[HeurNNet]` = `Factory[HeurNNet]('HeurNNet')`
- `policy_factory`: `Factory[PolicyNNet]` = `Factory[PolicyNNet]('PolicyNNet')`

## Imports

- `from abc import ABC`
- `from typing import Dict, Tuple, Type, List, Any, Optional`
- `import numpy as np`
- `from deepxube.base.factory import Factory`
- `from deepxube.base.domain import Domain, State, Action, Goal, ActsEnumFixed`
- `from deepxube.base.nnet_input import NNetInput, StateGoalIn, StateGoalActFixIn, StateGoalActIn, PolicyNNetIn`
- `from deepxube.base.heuristic import HeurNNet, PolicyNNet, HeurNNetPar, PolicyNNetPar, HeurNNetParV, HeurNNetParQIn, HeurNNetParQFixOut`
- `from numpy.typing import NDArray`
- `from deepxube.factories.nnet_input_factory import get_domain_nnet_input_keys, get_nnet_input_t`
