---
id: "module:deepxube.base.factory"
kind: "module"
name: "factory"
qualified_name: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_count: 179
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Dict", "alias": null}, {"name": "Any", "alias": null}, {"name": "Generic", "alias": null}, {"name": "TypeVar", "alias": null}, {"name": "Type", "alias": null}, {"name": "Callable", "alias": null}, {"name": "Optional", "alias": null}, {"name": "List", "alias": null}]
  - kind: "from"
    module: "abc"
    names: [{"name": "ABC", "alias": null}, {"name": "abstractmethod", "alias": null}]
  - kind: "import"
    module: "logging"
    alias: null
classes:
  - "class:deepxube.base.factory.Parser"
  - "class:deepxube.base.factory.Factory"
module_level_functions: []
module_level_constants:
  - name: "T"
    annotation: null
    value_expr: "TypeVar('T')"
---

# Module `deepxube.base.factory`

**File:** [deepxube/base/factory.py](../../deepxube/base/factory.py)
**Lines:** 179

## Module docstring

Generic registry + argument-parser plumbing for DeepXube's factories.

A ``Factory[T]`` instance holds two registries keyed by string names:

- a class registry (``@factory.register_class("name")``) mapping each name to a
  concrete subclass of ``T`` (e.g. a domain, heuristic, updater, pathfinder).
- a parser registry (``@factory.register_parser("name")``) mapping each name to
  a ``Parser`` subclass that turns a dotted argument string (e.g. the ``7`` in
  ``grid.7``) into keyword arguments for the class constructor.

Command-line tooling in ``deepxube.utils.command_line_utils`` uses these
registries to resolve CLI arguments like ``--domain grid.7`` or
``--pathfind graph_v.1B_1.0W`` into fully-constructed objects.

## Contents

### Classes
- `Parser` — see `../classes/deepxube.base.factory/Parser.md`
- `Factory` — see `../classes/deepxube.base.factory/Factory.md`

### Module-level constants / TypeVars
- `T` = `TypeVar('T')`

## Imports

- `from typing import Dict, Any, Generic, TypeVar, Type, Callable, Optional, List`
- `from abc import ABC, abstractmethod`
- `import logging`
