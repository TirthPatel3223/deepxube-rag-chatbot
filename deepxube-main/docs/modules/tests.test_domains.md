---
id: "module:tests.test_domains"
kind: "module"
name: "test_domains"
qualified_name: "tests.test_domains"
file: "tests/test_domains.py"
line_count: 149
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "cast", "alias": null}]
  - kind: "import"
    module: "pytest"
    alias: null
  - kind: "from"
    module: "deepxube.factories.domain_factory"
    names: [{"name": "domain_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.base.domain"
    names: [{"name": "Domain", "alias": null}, {"name": "State", "alias": null}, {"name": "Action", "alias": null}, {"name": "Goal", "alias": null}, {"name": "GoalSampleableFromState", "alias": null}, {"name": "GoalSampleable", "alias": null}, {"name": "ActsRev", "alias": null}]
classes: []
module_level_functions:
  - "func:tests.test_domains.build_domain_from_name"
  - "func:tests.test_domains.domain_name"
  - "func:tests.test_domains.domain"
  - "func:tests.test_domains.domain_goalsamp"
  - "func:tests.test_domains.domain_goalsamp_fromstate"
  - "func:tests.test_domains.domain_actsrev"
  - "func:tests.test_domains.test_get_start_goal_pairs"
  - "func:tests.test_domains.test_get_start_goal_pairs_0steps"
  - "func:tests.test_domains.test_goalsamp"
  - "func:tests.test_domains.test_actsrev"
module_level_constants:
  - name: "DOMAIN_NAMES"
    annotation: "List[str]"
    value_expr: "[cls_name for cls_name in domain_factory.get_all_class_names() if cls_name != 'sokoban']"
---

# Module `tests.test_domains`

**File:** [tests/test_domains.py](../../tests/test_domains.py)
**Lines:** 149

## Module docstring

Pytest suite verifying core domain contracts: problem-instance generation, goal sampling, and action reversibility. 

## Contents

### Module-level functions
- `build_domain_from_name`
- `domain_name`
- `domain`
- `domain_goalsamp`
- `domain_goalsamp_fromstate`
- `domain_actsrev`
- `test_get_start_goal_pairs` *(trivial, skipped)*
- `test_get_start_goal_pairs_0steps` *(trivial, skipped)*
- `test_goalsamp` *(trivial, skipped)*
- `test_actsrev`

### Module-level constants / TypeVars
- `DOMAIN_NAMES`: `List[str]` = `[cls_name for cls_name in domain_factory.get_all_class_names() if cls_name != 'sokoban']`

## Imports

- `from typing import List, cast`
- `import pytest`
- `from deepxube.factories.domain_factory import domain_factory`
- `from deepxube.base.domain import Domain, State, Action, Goal, GoalSampleableFromState, GoalSampleable, ActsRev`
