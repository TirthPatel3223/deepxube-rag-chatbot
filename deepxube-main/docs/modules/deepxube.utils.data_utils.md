---
id: "module:deepxube.utils.data_utils"
kind: "module"
name: "data_utils"
qualified_name: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_count: 253
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Any", "alias": null}, {"name": "Tuple", "alias": null}, {"name": "Optional", "alias": null}, {"name": "Type", "alias": null}, {"name": "cast", "alias": null}]
  - kind: "import"
    module: "sys"
    alias: null
  - kind: "from"
    module: "multiprocessing"
    names: [{"name": "Queue", "alias": null}]
  - kind: "import"
    module: "queue"
    alias: null
  - kind: "import"
    module: "os"
    alias: null
  - kind: "import"
    module: "shutil"
    alias: null
  - kind: "import"
    module: "numpy"
    alias: "np"
  - kind: "from"
    module: "numpy.typing"
    names: [{"name": "NDArray", "alias": null}, {"name": "ArrayLike", "alias": null}]
  - kind: "from"
    module: "multiprocessing"
    names: [{"name": "shared_memory", "alias": null}]
  - kind: "from"
    module: "multiprocessing.shared_memory"
    names: [{"name": "SharedMemory", "alias": null}]
classes:
  - "class:deepxube.utils.data_utils.Logger"
  - "class:deepxube.utils.data_utils.SharedNDArray"
module_level_functions:
  - "func:deepxube.utils.data_utils.get_nowait_noerr"
  - "func:deepxube.utils.data_utils.get_while_not_empty"
  - "func:deepxube.utils.data_utils.get_in_order"
  - "func:deepxube.utils.data_utils.copy_dir_files"
  - "func:deepxube.utils.data_utils.sel_l"
  - "func:deepxube.utils.data_utils.combine_l_l"
  - "func:deepxube.utils.data_utils.np_to_shnd"
module_level_constants: []
---

# Module `deepxube.utils.data_utils`

**File:** [deepxube/utils/data_utils.py](../../deepxube/utils/data_utils.py)
**Lines:** 253

## Module docstring

IO, multiprocessing-queue, and numpy-array plumbing used across DeepXube.

Includes: a ``Logger`` that tees stdout to a file, non-blocking queue helpers,
list-of-ndarray indexing and concatenation, and a pickleable ``SharedNDArray``
that lets worker processes share numpy buffers via POSIX/Windows shared memory.

## Contents

### Classes
- `Logger` — see `../classes/deepxube.utils.data_utils/Logger.md`
- `SharedNDArray` — see `../classes/deepxube.utils.data_utils/SharedNDArray.md`

### Module-level functions
- `get_nowait_noerr`
- `get_while_not_empty`
- `get_in_order`
- `copy_dir_files`
- `sel_l`
- `combine_l_l`
- `np_to_shnd`

## Imports

- `from typing import List, Any, Tuple, Optional, Type, cast`
- `import sys`
- `from multiprocessing import Queue`
- `import queue`
- `import os`
- `import shutil`
- `import numpy as np`
- `from numpy.typing import NDArray, ArrayLike`
- `from multiprocessing import shared_memory`
- `from multiprocessing.shared_memory import SharedMemory`
