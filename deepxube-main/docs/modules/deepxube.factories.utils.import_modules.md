---
id: "module:deepxube.factories.utils.import_modules"
kind: "module"
name: "import_modules"
qualified_name: "deepxube.factories.utils.import_modules"
file: "deepxube/factories/utils/import_modules.py"
line_count: 35
docstring_source: "present"
imports:
  - kind: "from"
    module: "importlib"
    names: [{"name": "import_module", "alias": null}]
  - kind: "import"
    module: "os"
    alias: null
classes: []
module_level_functions:
  - "func:deepxube.factories.utils.import_modules.import_local_modules"
module_level_constants: []
---

# Module `deepxube.factories.utils.import_modules`

**File:** [deepxube/factories/utils/import_modules.py](../../deepxube/factories/utils/import_modules.py)
**Lines:** 35

## Module docstring

Helper to import every Python module under a directory tree so that
side-effect registrations (``@factory.register_class``) fire.

Used by the CLI at startup to pick up user-defined ``domains/``,
``heuristics/``, and nnet inputs without requiring an explicit import list.

## Contents

### Module-level functions
- `import_local_modules`

## Imports

- `from importlib import import_module`
- `import os`
