---
id: "module:deepxube.logic.logic_objects"
kind: "module"
name: "logic_objects"
qualified_name: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_count: 434
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Set", "alias": null}, {"name": "Dict", "alias": null}, {"name": "FrozenSet", "alias": null}]
classes:
  - "class:deepxube.logic.logic_objects.Literal"
  - "class:deepxube.logic.logic_objects.VarNode"
  - "class:deepxube.logic.logic_objects.LitNode"
  - "class:deepxube.logic.logic_objects.Clause"
module_level_functions:
  - "func:deepxube.logic.logic_objects.prop_across"
  - "func:deepxube.logic.logic_objects.prune_lit"
  - "func:deepxube.logic.logic_objects.theta_sub_lits"
  - "func:deepxube.logic.logic_objects.theta_sub_args"
  - "func:deepxube.logic.logic_objects.make_subs_lit"
  - "func:deepxube.logic.logic_objects.make_subs"
  - "func:deepxube.logic.logic_objects.theta_sub_replace"
module_level_constants:
  - name: "Atom"
    annotation: null
    value_expr: "Tuple[str, ...]"
  - name: "Model"
    annotation: null
    value_expr: "FrozenSet[Atom]"
---

# Module `deepxube.logic.logic_objects`

**File:** [deepxube/logic/logic_objects.py](../../deepxube/logic/logic_objects.py)
**Lines:** 434

## Module docstring

First-order logic objects for DeepXube's ILP/ASP layer: Literals, Clauses, and theta-subsumption utilities.
``Atom`` and ``Model`` type aliases are also defined here for use throughout the logic subsystem. 

## Contents

### Classes
- `Literal` — see `../classes/deepxube.logic.logic_objects/Literal.md`
- `VarNode` — see `../classes/deepxube.logic.logic_objects/VarNode.md`
- `LitNode` — see `../classes/deepxube.logic.logic_objects/LitNode.md`
- `Clause` — see `../classes/deepxube.logic.logic_objects/Clause.md`

### Module-level functions
- `prop_across`
- `prune_lit`
- `theta_sub_lits`
- `theta_sub_args`
- `make_subs_lit`
- `make_subs`
- `theta_sub_replace`

### Module-level constants / TypeVars
- `Atom` = `Tuple[str, ...]`
- `Model` = `FrozenSet[Atom]`

## Imports

- `from typing import List, Tuple, Optional, Set, Dict, FrozenSet`
