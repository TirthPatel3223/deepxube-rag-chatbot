---
id: "module:deepxube.logic.asp"
kind: "module"
name: "asp"
qualified_name: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_count: 286
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Set", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Callable", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "from"
    module: "deepxube.logic.logic_objects"
    names: [{"name": "Clause", "alias": null}, {"name": "Literal", "alias": null}, {"name": "Atom", "alias": null}, {"name": "Model", "alias": null}]
  - kind: "from"
    module: "deepxube.logic.logic_utils"
    names: [{"name": "copy_clause_with_new_head", "alias": null}, {"name": "atom_to_str", "alias": null}]
  - kind: "from"
    module: "clingo.solving"
    names: [{"name": "SolveHandle", "alias": null}]
  - kind: "from"
    module: "clingo.solving"
    names: [{"name": "Model", "alias": "ModelCl"}]
  - kind: "import"
    module: "random"
    alias: null
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "clingo"
    alias: null
  - kind: "from"
    module: "clingo"
    names: [{"name": "Control", "alias": null}, {"name": "parse_term", "alias": null}, {"name": "Symbol", "alias": null}]
  - kind: "import"
    module: "re"
    alias: null
classes:
  - "class:deepxube.logic.asp.Spec"
  - "class:deepxube.logic.asp.Solver"
module_level_functions:
  - "func:deepxube.logic.asp.model_to_body"
  - "func:deepxube.logic.asp.on_model_var_vals"
  - "func:deepxube.logic.asp.parse_clingo_line"
module_level_constants: []
---

# Module `deepxube.logic.asp`

**File:** [deepxube/logic/asp.py](../../deepxube/logic/asp.py)
**Lines:** 286

## Module docstring

Answer-set programming (ASP) interface for DeepXube, wrapping the Clingo solver. Provides ``Spec`` for
declarative goal/constraint specifications and ``Solver`` for sampling and checking stable models. 

## Contents

### Classes
- `Spec` — see `../classes/deepxube.logic.asp/Spec.md`
- `Solver` — see `../classes/deepxube.logic.asp/Solver.md`

### Module-level functions
- `model_to_body`
- `on_model_var_vals` *(trivial, skipped)*
- `parse_clingo_line`

## Imports

- `from typing import List, Optional, Set, Tuple, Dict, Callable, Any`
- `from deepxube.logic.logic_objects import Clause, Literal, Atom, Model`
- `from deepxube.logic.logic_utils import copy_clause_with_new_head, atom_to_str`
- `from clingo.solving import SolveHandle`
- `from clingo.solving import Model as ModelCl`
- `import random`
- `import os`
- `import clingo`
- `from clingo import Control, parse_term, Symbol`
- `import re`
