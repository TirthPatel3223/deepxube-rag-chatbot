---
id: "module:deepxube.factories.domain_factory"
kind: "module"
name: "domain_factory"
qualified_name: "deepxube.factories.domain_factory"
file: "deepxube/factories/domain_factory.py"
line_count: 12
docstring_source: "present"
imports:
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Factory", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}]
classes: []
module_level_functions: []
module_level_constants:
  - name: "domain_factory"
    annotation: "Factory[Domain]"
    value_expr: "Factory[Domain]('domain')"
---

# Module `deepxube.factories.domain_factory`

**File:** [deepxube/factories/domain_factory.py](../../deepxube/factories/domain_factory.py)
**Lines:** 12

## Module docstring

Registry for ``Domain`` subclasses.

Concrete domains in ``deepxube/domains/`` (cube3, grid, lightsout, npuzzle,
sokoban) register themselves here via ``@domain_factory.register_class("key")``.
CLI tooling resolves arguments like ``--domain grid.7`` against this registry.

## Contents

### Module-level constants / TypeVars
- `domain_factory`: `Factory[Domain]` = `Factory[Domain]('domain')`

## Imports

- `from deepxube.base.factory import Factory`
- `from deepxube.base.domain import Domain`
