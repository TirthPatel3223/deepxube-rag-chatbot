---
id: "module:deepxube.base.nnet_input"
kind: "module"
name: "nnet_input"
qualified_name: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_count: 332
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Any", "alias": null}, {"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Generic", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Type", "alias": null}, {"name": "ClassVar", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Optional", "alias": null}]
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
classes:
  - "class:deepxube.base.nnet_input.NNetInput"
  - "class:deepxube.base.nnet_input.FlatIn"
  - "class:deepxube.base.nnet_input.TwoDIn"
  - "class:deepxube.base.nnet_input.StateGoalIn"
  - "class:deepxube.base.nnet_input.StateGoalActFixIn"
  - "class:deepxube.base.nnet_input.StateGoalActIn"
  - "class:deepxube.base.nnet_input.PolicyNNetIn"
  - "class:deepxube.base.nnet_input.FlatInPolicy"
  - "class:deepxube.base.nnet_input.DynamicNNetInput"
  - "class:deepxube.base.nnet_input.HasFlatSGIn"
  - "class:deepxube.base.nnet_input.HasActsEnumFixedIn"
  - "class:deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn"
  - "class:deepxube.base.nnet_input.HasFlatSGAIn"
  - "class:deepxube.base.nnet_input.HasTwoDSGIn"
  - "class:deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn"
module_level_functions: []
module_level_constants:
  - name: "D"
    annotation: null
    value_expr: "TypeVar('D', bound=Domain)"
  - name: "S"
    annotation: null
    value_expr: "TypeVar('S', bound=State)"
  - name: "A"
    annotation: null
    value_expr: "TypeVar('A', bound=Action)"
  - name: "G"
    annotation: null
    value_expr: "TypeVar('G', bound=Goal)"
---

# Module `deepxube.base.nnet_input`

**File:** [deepxube/base/nnet_input.py](../../deepxube/base/nnet_input.py)
**Lines:** 332

## Module docstring

Abstract ``NNetInput`` plus the ``Has*In`` mixins domains use to declare
which input shapes their states/goals/actions can be converted to.

A concrete ``NNetInput`` answers two questions: what tensor shapes does the
network see, and how do you convert (states[, goals[, actions]]) into those
tensors? The ``DynamicNNetInput`` machinery lets a domain register concrete
``NNetInput`` classes at class-definition time so the heuristic factory can
discover them. 

## Contents

### Classes
- `NNetInput` — see `../classes/deepxube.base.nnet_input/NNetInput.md`
- `FlatIn` — see `../classes/deepxube.base.nnet_input/FlatIn.md`
- `TwoDIn` — see `../classes/deepxube.base.nnet_input/TwoDIn.md`
- `StateGoalIn` — see `../classes/deepxube.base.nnet_input/StateGoalIn.md`
- `StateGoalActFixIn` — see `../classes/deepxube.base.nnet_input/StateGoalActFixIn.md`
- `StateGoalActIn` — see `../classes/deepxube.base.nnet_input/StateGoalActIn.md`
- `PolicyNNetIn` — see `../classes/deepxube.base.nnet_input/PolicyNNetIn.md`
- `FlatInPolicy` — see `../classes/deepxube.base.nnet_input/FlatInPolicy.md`
- `DynamicNNetInput` — see `../classes/deepxube.base.nnet_input/DynamicNNetInput.md`
- `HasFlatSGIn` — see `../classes/deepxube.base.nnet_input/HasFlatSGIn.md`
- `HasActsEnumFixedIn` — see `../classes/deepxube.base.nnet_input/HasActsEnumFixedIn.md`
- `HasFlatSGActsEnumFixedIn` — see `../classes/deepxube.base.nnet_input/HasFlatSGActsEnumFixedIn.md`
- `HasFlatSGAIn` — see `../classes/deepxube.base.nnet_input/HasFlatSGAIn.md`
- `HasTwoDSGIn` — see `../classes/deepxube.base.nnet_input/HasTwoDSGIn.md`
- `HasTwoDSGActsEnumFixedIn` — see `../classes/deepxube.base.nnet_input/HasTwoDSGActsEnumFixedIn.md`

### Module-level constants / TypeVars
- `D` = `TypeVar('D', bound=Domain)`
- `S` = `TypeVar('S', bound=State)`
- `A` = `TypeVar('A', bound=Action)`
- `G` = `TypeVar('G', bound=Goal)`

## Imports

- `from typing import Any, List, Tuple, Generic, TypeVar, Type, ClassVar, Dict, Optional`
- `from abc import ABC, abstractmethod`
- `from deepxube.base.domain import Domain, State, Action, Goal`
- `import numpy as np`
- `from numpy.typing import NDArray`
