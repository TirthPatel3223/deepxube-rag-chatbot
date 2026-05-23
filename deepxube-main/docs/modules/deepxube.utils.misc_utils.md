---
id: "module:deepxube.utils.misc_utils"
kind: "module"
name: "misc_utils"
qualified_name: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_count: 137
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Any", "alias": null}, {"name": "Union", "alias": null}, {"name": "Set", "alias": null}, {"name": "cast", "alias": null}]
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "import"
    module: "math"
    alias: null
  - kind: "import"
    module: "re"
    alias: null
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}]
classes: []
module_level_functions:
  - "func:deepxube.utils.misc_utils.flatten"
  - "func:deepxube.utils.misc_utils.unflatten"
  - "func:deepxube.utils.misc_utils.split_evenly"
  - "func:deepxube.utils.misc_utils.split_evenly_w_max"
  - "func:deepxube.utils.misc_utils.remove_all_whitespace"
  - "func:deepxube.utils.misc_utils.random_subset"
  - "func:deepxube.utils.misc_utils.boltzmann"
module_level_constants: []
---

# Module `deepxube.utils.misc_utils`

**File:** [deepxube/utils/misc_utils.py](../../deepxube/utils/misc_utils.py)
**Lines:** 137

## Module docstring

Small numeric and collection utilities used throughout DeepXube.

Contents: flatten/unflatten list-of-lists with matching split indices, even
integer partitions, whitespace stripping, random set subsampling, and a
numerically-stable Boltzmann softmax.

## Contents

### Module-level functions
- `flatten`
- `unflatten`
- `split_evenly`
- `split_evenly_w_max`
- `remove_all_whitespace`
- `random_subset`
- `boltzmann`

## Imports

- `from typing import List, Tuple, Any, Union, Set, cast`
- `import numpy as np`
- `import math`
- `import re`
- `from numpy.typing import NDArray`
