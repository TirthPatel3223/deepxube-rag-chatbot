---
id: "module:deepxube.factories.nnet_input_factory"
kind: "module"
name: "nnet_input_factory"
qualified_name: "deepxube.factories.nnet_input_factory"
file: "deepxube/factories/nnet_input_factory.py"
line_count: 74
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "Dict", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Type", "alias": null}, {"name": "Callable", "alias": null}, {"name": "List", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "NNetInput", "alias": null}, {"name": "DynamicNNetInput", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
classes: []
module_level_functions:
  - "func:deepxube.factories.nnet_input_factory.register_nnet_input"
  - "func:deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys"
  - "func:deepxube.factories.nnet_input_factory.get_nnet_input_t"
  - "func:deepxube.factories.nnet_input_factory.register_nnet_input_dynamic"
module_level_constants:
  - name: "_nnet_input_registry"
    annotation: "Dict[Tuple[str, str], Type[NNetInput]]"
    value_expr: "{}"
---

# Module `deepxube.factories.nnet_input_factory`

**File:** [deepxube/factories/nnet_input_factory.py](../../deepxube/factories/nnet_input_factory.py)
**Lines:** 74

## Module docstring

Registry of per-(domain, nnet-input-name) ``NNetInput`` classes.

Unlike the class-only factories, ``NNetInput`` classes are keyed by the pair
``(domain_name, nnet_input_name)`` so the same input shape (e.g. ``flat_sg``)
can have different implementations per domain. Domains that implement
``DynamicNNetInput`` register their mixin-derived ``NNetInput`` classes at
module load via ``register_nnet_input_dynamic``.

## Contents

### Module-level functions
- `register_nnet_input`
- `get_domain_nnet_input_keys` *(trivial, skipped)*
- `get_nnet_input_t` *(trivial, skipped)*
- `register_nnet_input_dynamic`

### Module-level constants / TypeVars
- `_nnet_input_registry`: `Dict[Tuple[str, str], Type[NNetInput]]` = `{}`

## Imports

- `from typing import Dict, Tuple, Type, Callable, List`
- `from deepxube.base.nnet_input import NNetInput, DynamicNNetInput`
- `from deepxube.base.domain import Domain`
- `from deepxube.factories.domain_factory import domain_factory`
