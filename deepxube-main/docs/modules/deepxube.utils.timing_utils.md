---
id: "module:deepxube.utils.timing_utils"
kind: "module"
name: "timing_utils"
qualified_name: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_count: 191
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Optional", "alias": null}]
  - kind: "from"
    module: "collections"
    names: [{"name": "OrderedDict", "alias": null}]
classes:
  - "class:deepxube.utils.timing_utils.Times"
module_level_functions:
  - "func:deepxube.utils.timing_utils.add_times"
  - "func:deepxube.utils.timing_utils.add_counts"
  - "func:deepxube.utils.timing_utils.init_times"
  - "func:deepxube.utils.timing_utils.init_counts"
module_level_constants: []
---

# Module `deepxube.utils.timing_utils`

**File:** [deepxube/utils/timing_utils.py](../../deepxube/utils/timing_utils.py)
**Lines:** 191

## Module docstring

Hierarchical wall-clock timer used across DeepXube for performance
diagnostics.

``Times`` is a named-bucket accumulator with optional nested sub-timers.
Each bucket tracks cumulative elapsed time and call count. Training loops
use it to report per-phase breakdowns (e.g. ``steps_gen``, ``inst_add``,
``backup``, ``to_np``).

## Contents

### Classes
- `Times` — see `../classes/deepxube.utils.timing_utils/Times.md`

### Module-level functions
- `add_times`
- `add_counts`
- `init_times`
- `init_counts`

## Imports

- `from typing import List, Dict, Optional`
- `from collections import OrderedDict`
