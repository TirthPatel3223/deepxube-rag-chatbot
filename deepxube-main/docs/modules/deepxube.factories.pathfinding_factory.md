---
id: "module:deepxube.factories.pathfinding_factory"
kind: "module"
name: "pathfinding_factory"
qualified_name: "deepxube.factories.pathfinding_factory"
file: "deepxube/factories/pathfinding_factory.py"
line_count: 80
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Type", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Any", "alias": null}]
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Factory", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurFn", "alias": null}, {"name": "HeurFnV", "alias": null}, {"name": "HeurFnQ", "alias": null}, {"name": "PolicyFn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.pathfinding"
    names: [{"name": "PathFind", "alias": null}, {"name": "FNsHeurV", "alias": null}, {"name": "FNsHeurQ", "alias": null}, {"name": "FNsPolicy", "alias": null}, {"name": "FNsHeurVPolicy", "alias": null}, {"name": "FNsHeurQPolicy", "alias": null}]
classes: []
module_level_functions:
  - "func:deepxube.factories.pathfinding_factory.get_pathfind_functions"
  - "func:deepxube.factories.pathfinding_factory.get_domain_compat_pathfind_names"
module_level_constants:
  - name: "pathfinding_factory"
    annotation: "Factory[PathFind]"
    value_expr: "Factory[PathFind]('PathFind')"
---

# Module `deepxube.factories.pathfinding_factory`

**File:** [deepxube/factories/pathfinding_factory.py](../../deepxube/factories/pathfinding_factory.py)
**Lines:** 80

## Module docstring

Registry for ``PathFind`` subclasses and helpers to assemble their
functions bundles.

Concrete pathfinders in ``deepxube/pathfinding/`` register themselves here via
``@pathfinding_factory.register_class("key")``. Two helpers resolve what each
pathfinder needs: ``get_pathfind_functions`` bundles the heuristic/policy
callables into the expected ``FNs*`` dataclass, and
``get_domain_compat_pathfind_names`` lists the pathfinders a given domain can
use.

## Contents

### Module-level functions
- `get_pathfind_functions`
- `get_domain_compat_pathfind_names`

### Module-level constants / TypeVars
- `pathfinding_factory`: `Factory[PathFind]` = `Factory[PathFind]('PathFind')`

## Imports

- `from typing import List, Type, Optional, Any`
- `from deepxube.base.factory import Factory`
- `from deepxube.base.domain import Domain`
- `from deepxube.base.heuristic import HeurFn, HeurFnV, HeurFnQ, PolicyFn`
- `from deepxube.base.pathfinding import PathFind, FNsHeurV, FNsHeurQ, FNsPolicy, FNsHeurVPolicy, FNsHeurQPolicy`
