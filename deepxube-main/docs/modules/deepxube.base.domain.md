---
id: "module:deepxube.base.domain"
kind: "module"
name: "domain"
qualified_name: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_count: 719
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Set", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Generic", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "clingo.solving"
    names: [{"name": "Model", "alias": "ModelCl"}]
  - kind: "from"
    module: "deepxube.logic.logic_objects"
    names: [{"name": "Atom", "alias": null}, {"name": "Model", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "misc_utils", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.nnet_utils"
    names: [{"name": "NNetPar", "alias": null}, {"name": "NNetCallable", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.timing_utils"
    names: [{"name": "Times", "alias": null}]
  - kind: "from"
    module: "matplotlib.figure"
    names: [{"name": "Figure", "alias": null}]
  - kind: "import"
    module: "random"
    alias: null
  - kind: "import"
    module: "time"
    alias: null
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
classes:
  - "class:deepxube.base.domain.State"
  - "class:deepxube.base.domain.Action"
  - "class:deepxube.base.domain.Goal"
  - "class:deepxube.base.domain.Domain"
  - "class:deepxube.base.domain.StateGoalVizable"
  - "class:deepxube.base.domain.StringToAct"
  - "class:deepxube.base.domain.ActsFixed"
  - "class:deepxube.base.domain.ActsRev"
  - "class:deepxube.base.domain.ActsEnum"
  - "class:deepxube.base.domain.ActsEnumFixed"
  - "class:deepxube.base.domain.GoalSampleable"
  - "class:deepxube.base.domain.GoalStateSampleable"
  - "class:deepxube.base.domain.GoalSampleableFromState"
  - "class:deepxube.base.domain.StateSampleableFromGoal"
  - "class:deepxube.base.domain.GoalFixed"
  - "class:deepxube.base.domain.GoalStateGoalPairSampleable"
  - "class:deepxube.base.domain.GoalStateSampGoalSamp"
  - "class:deepxube.base.domain.GoalSampGoalStateSamp"
  - "class:deepxube.base.domain.StartGoalWalkable"
  - "class:deepxube.base.domain.GoalStartRevWalkable"
  - "class:deepxube.base.domain.GoalStartRevWalkableActsRev"
  - "class:deepxube.base.domain.NextStateNP"
  - "class:deepxube.base.domain.NextStateNPActsEnum"
  - "class:deepxube.base.domain.NextStateNPActsFixed"
  - "class:deepxube.base.domain.NextStateNPActsEnumFixed"
  - "class:deepxube.base.domain.SupportsPDDL"
  - "class:deepxube.base.domain.GoalGrndAtoms"
module_level_functions: []
module_level_constants:
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

# Module `deepxube.base.domain`

**File:** [deepxube/base/domain.py](../../deepxube/base/domain.py)
**Lines:** 719

## Module docstring

Abstract domain interface plus the mixin tree that lets concrete domains
declare which capabilities they support (action enumeration, goal sampling,
random walks, PDDL/ASP integration, etc.).

A concrete ``Domain`` (e.g. ``Grid``, ``Cube3``) inherits from ``Domain[S, A, G]``
plus whichever mixins it implements. Other parts of DeepXube use ``isinstance``
/ ``issubclass`` against these mixins to decide which pathfinders, updaters,
and NNet inputs are compatible. 

## Contents

### Classes
- `State` — see `../classes/deepxube.base.domain/State.md`
- `Action` — see `../classes/deepxube.base.domain/Action.md`
- `Goal` — see `../classes/deepxube.base.domain/Goal.md`
- `Domain` — see `../classes/deepxube.base.domain/Domain.md`
- `StateGoalVizable` — see `../classes/deepxube.base.domain/StateGoalVizable.md`
- `StringToAct` — see `../classes/deepxube.base.domain/StringToAct.md`
- `ActsFixed` — see `../classes/deepxube.base.domain/ActsFixed.md`
- `ActsRev` — see `../classes/deepxube.base.domain/ActsRev.md`
- `ActsEnum` — see `../classes/deepxube.base.domain/ActsEnum.md`
- `ActsEnumFixed` — see `../classes/deepxube.base.domain/ActsEnumFixed.md`
- `GoalSampleable` — see `../classes/deepxube.base.domain/GoalSampleable.md`
- `GoalStateSampleable` — see `../classes/deepxube.base.domain/GoalStateSampleable.md`
- `GoalSampleableFromState` — see `../classes/deepxube.base.domain/GoalSampleableFromState.md`
- `StateSampleableFromGoal` — see `../classes/deepxube.base.domain/StateSampleableFromGoal.md`
- `GoalFixed` — see `../classes/deepxube.base.domain/GoalFixed.md`
- `GoalStateGoalPairSampleable` — see `../classes/deepxube.base.domain/GoalStateGoalPairSampleable.md`
- `GoalStateSampGoalSamp` — see `../classes/deepxube.base.domain/GoalStateSampGoalSamp.md`
- `GoalSampGoalStateSamp` — see `../classes/deepxube.base.domain/GoalSampGoalStateSamp.md`
- `StartGoalWalkable` — see `../classes/deepxube.base.domain/StartGoalWalkable.md`
- `GoalStartRevWalkable` — see `../classes/deepxube.base.domain/GoalStartRevWalkable.md`
- `GoalStartRevWalkableActsRev` — see `../classes/deepxube.base.domain/GoalStartRevWalkableActsRev.md`
- `NextStateNP` — see `../classes/deepxube.base.domain/NextStateNP.md`
- `NextStateNPActsEnum` — see `../classes/deepxube.base.domain/NextStateNPActsEnum.md`
- `NextStateNPActsFixed` — see `../classes/deepxube.base.domain/NextStateNPActsFixed.md`
- `NextStateNPActsEnumFixed` — see `../classes/deepxube.base.domain/NextStateNPActsEnumFixed.md`
- `SupportsPDDL` — see `../classes/deepxube.base.domain/SupportsPDDL.md`
- `GoalGrndAtoms` — see `../classes/deepxube.base.domain/GoalGrndAtoms.md`

### Module-level constants / TypeVars
- `S` = `TypeVar('S', bound=State)`
- `A` = `TypeVar('A', bound=Action)`
- `G` = `TypeVar('G', bound=Goal)`

## Imports

- `from abc import ABC, abstractmethod`
- `from typing import List, Tuple, Optional, Set, TypeVar, Generic, Dict, Any`
- `import numpy as np`
- `from clingo.solving import Model as ModelCl`
- `from deepxube.logic.logic_objects import Atom, Model`
- `from deepxube.utils import misc_utils`
- `from deepxube.nnet.nnet_utils import NNetPar, NNetCallable`
- `from deepxube.utils.timing_utils import Times`
- `from matplotlib.figure import Figure`
- `import random`
- `import time`
- `from numpy.typing import NDArray`
