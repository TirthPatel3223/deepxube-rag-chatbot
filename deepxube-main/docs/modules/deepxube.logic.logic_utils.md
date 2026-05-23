---
id: "module:deepxube.logic.logic_utils"
kind: "module"
name: "logic_utils"
qualified_name: "deepxube.logic.logic_utils"
file: "deepxube/logic/logic_utils.py"
line_count: 109
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Set", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Dict", "alias": null}]
  - kind: "from"
    module: "deepxube.logic.logic_objects"
    names: [{"name": "Clause", "alias": null}, {"name": "Literal", "alias": null}, {"name": "Atom", "alias": null}]
  - kind: "from"
    module: "deepxube.utils"
    names: [{"name": "misc_utils", "alias": null}]
  - kind: "import"
    module: "re"
    alias: null
classes: []
module_level_functions:
  - "func:deepxube.logic.logic_utils.parse_literal"
  - "func:deepxube.logic.logic_utils.replace_anon_vars"
  - "func:deepxube.logic.logic_utils.parse_clause"
  - "func:deepxube.logic.logic_utils.copy_clause_with_new_head"
  - "func:deepxube.logic.logic_utils.atom_to_str"
module_level_constants: []
---

# Module `deepxube.logic.logic_utils`

**File:** [deepxube/logic/logic_utils.py](../../deepxube/logic/logic_utils.py)
**Lines:** 109

## Module docstring

Parsing and manipulation utilities for first-order logic objects: literals, clauses, and atoms. Used internally
by the ILP/ASP layer of DeepXube. 

## Contents

### Module-level functions
- `parse_literal`
- `replace_anon_vars`
- `parse_clause`
- `copy_clause_with_new_head`
- `atom_to_str` *(trivial, skipped)*

## Imports

- `from typing import List, Set, Tuple, Dict`
- `from deepxube.logic.logic_objects import Clause, Literal, Atom`
- `from deepxube.utils import misc_utils`
- `import re`
