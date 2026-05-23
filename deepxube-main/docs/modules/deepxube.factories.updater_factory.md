---
id: "module:deepxube.factories.updater_factory"
kind: "module"
name: "updater_factory"
qualified_name: "deepxube.factories.updater_factory"
file: "deepxube/factories/updater_factory.py"
line_count: 101
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Type", "alias": null}, {"name": "List", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "PathFind", "alias": null}]
  - kind: "from"
    module: "deepxube.base.updater"
    names: [{"name": "Update", "alias": null}, {"name": "UpdateHER", "alias": null}, {"name": "UpdateHeur", "alias": null}, {"name": "UpdatePolicy", "alias": null}, {"name": "UpArgs", "alias": null}]
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Factory", "alias": null}]
  - kind: "from"
    module: "deepxube.utils.command_line_utils"
    names: [{"name": "get_pathfind_name_kwargs", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.pathfinding_factory"
    names: [{"name": "pathfinding_factory", "alias": null}]
classes: []
module_level_functions:
  - "func:deepxube.factories.updater_factory.get_updater"
module_level_constants:
  - name: "updater_factory"
    annotation: "Factory[Update]"
    value_expr: "Factory[Update]('Update')"
---

# Module `deepxube.factories.updater_factory`

**File:** [deepxube/factories/updater_factory.py](../../deepxube/factories/updater_factory.py)
**Lines:** 101

## Module docstring

Registry for ``Update`` subclasses (the training data generators).

Concrete ``Update`` subclasses in ``deepxube/updaters/`` register themselves
here via ``@updater_factory.register_class("key")``. The ``get_updater``
function resolves a ``(domain, pathfind, her, func_update)`` tuple to the
unique registered class that supports that combination and instantiates it.

## Contents

### Module-level functions
- `get_updater`

### Module-level constants / TypeVars
- `updater_factory`: `Factory[Update]` = `Factory[Update]('Update')`

## Imports

- `from typing import Type, List`
- `from deepxube.base.domain import Domain`
- `from deepxube.base.pathfinding import PathFind`
- `from deepxube.base.updater import Update, UpdateHER, UpdateHeur, UpdatePolicy, UpArgs`
- `from deepxube.base.factory import Factory`
- `from deepxube.utils.command_line_utils import get_pathfind_name_kwargs`
- `from deepxube.factories.pathfinding_factory import pathfinding_factory`
