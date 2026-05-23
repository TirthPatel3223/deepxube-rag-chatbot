---
id: "module:deepxube.updaters.utils.replay_buffer_utils"
kind: "module"
name: "replay_buffer_utils"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_count: 146
docstring_source: "present"
imports:
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "from"
    module: "typing"
    names: [{"name": "Deque", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "List", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Generic", "alias": null}, {"name": "TypeVar", "alias": null}]
  - kind: "from"
    module: "collections"
    names: [{"name": "deque", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
classes:
  - "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer"
  - "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV"
  - "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ"
  - "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP"
module_level_functions: []
module_level_constants:
  - name: "ReplayVElem"
    annotation: null
    value_expr: "Tuple[State, Goal, bool]"
  - name: "ReplayQElem"
    annotation: null
    value_expr: "Tuple[State, Goal, bool, Action, float, State]"
  - name: "ReplayPElem"
    annotation: null
    value_expr: "Tuple[State, Goal, Action]"
  - name: "ReplayVRet"
    annotation: null
    value_expr: "Tuple[List[State], List[Goal], List[bool]]"
  - name: "ReplayQRet"
    annotation: null
    value_expr: "Tuple[List[State], List[Goal], List[bool], List[Action], List[float], List[State]]"
  - name: "ReplayPRet"
    annotation: null
    value_expr: "Tuple[List[State], List[Goal], List[Action]]"
  - name: "Elem"
    annotation: null
    value_expr: "TypeVar('Elem')"
  - name: "SampRet"
    annotation: null
    value_expr: "TypeVar('SampRet')"
---

# Module `deepxube.updaters.utils.replay_buffer_utils`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py](../../deepxube/updaters/utils/replay_buffer_utils.py)
**Lines:** 146

## Module docstring

Fixed-capacity replay buffers used by the RL updaters.

Three typed variants store the tuples needed by each training regime:
``ReplayBufferV`` for value-based learning (state, goal, is_solved),
``ReplayBufferQ`` for Q-learning (state, goal, is_solved, action, tc, next_state),
and ``ReplayBufferP`` for policy learning (state, goal, action).
All use a ``collections.deque`` bounded by ``max_size`` with uniform
random sampling.

## Contents

### Classes
- `ReplayBuffer` — see `../classes/deepxube.updaters.utils.replay_buffer_utils/ReplayBuffer.md`
- `ReplayBufferV` — see `../classes/deepxube.updaters.utils.replay_buffer_utils/ReplayBufferV.md`
- `ReplayBufferQ` — see `../classes/deepxube.updaters.utils.replay_buffer_utils/ReplayBufferQ.md`
- `ReplayBufferP` — see `../classes/deepxube.updaters.utils.replay_buffer_utils/ReplayBufferP.md`

### Module-level constants / TypeVars
- `ReplayVElem` = `Tuple[State, Goal, bool]`
- `ReplayQElem` = `Tuple[State, Goal, bool, Action, float, State]`
- `ReplayPElem` = `Tuple[State, Goal, Action]`
- `ReplayVRet` = `Tuple[List[State], List[Goal], List[bool]]`
- `ReplayQRet` = `Tuple[List[State], List[Goal], List[bool], List[Action], List[float], List[State]]`
- `ReplayPRet` = `Tuple[List[State], List[Goal], List[Action]]`
- `Elem` = `TypeVar('Elem')`
- `SampRet` = `TypeVar('SampRet')`

## Imports

- `from abc import ABC, abstractmethod`
- `from typing import Deque, Tuple, List, Optional, Generic, TypeVar`
- `from collections import deque`
- `from deepxube.base.domain import State, Action, Goal`
- `import numpy as np`
