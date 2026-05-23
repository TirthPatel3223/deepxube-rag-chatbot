---
id: "module:deepxube.heuristics.resnet_2d"
kind: "module"
name: "resnet_2d"
qualified_name: "deepxube.heuristics.resnet_2d"
file: "deepxube/heuristics/resnet_2d.py"
line_count: 108
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Any", "alias": null}, {"name": "Type", "alias": null}]
  - kind: "import"
    module: "torch"
    alias: null
  - kind: "from"
    module: "torch"
    names: [{"name": "nn", "alias": null}, {"name": "Tensor", "alias": null}]
  - kind: "import"
    module: "re"
    alias: null
  - kind: "from"
    module: "deepxube.base.factory"
    names: [{"name": "Parser", "alias": null}]
  - kind: "from"
    module: "deepxube.base.nnet_input"
    names: [{"name": "TwoDIn", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNet", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.pytorch_models"
    names: [{"name": "Conv2dModel", "alias": null}, {"name": "ResnetModel", "alias": null}, {"name": "OneHot", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.heuristic_factory"
    names: [{"name": "heuristic_factory", "alias": null}]
classes:
  - "class:deepxube.heuristics.resnet_2d.Resnet2D"
  - "class:deepxube.heuristics.resnet_2d.ResnetFCParser"
module_level_functions: []
module_level_constants: []
---

# Module `deepxube.heuristics.resnet_2d`

**File:** [deepxube/heuristics/resnet_2d.py](../../deepxube/heuristics/resnet_2d.py)
**Lines:** 108

## Module docstring

2D convolutional ResNet heuristic for spatial NNet inputs (TwoDIn). Registered in the heuristic factory as
``resnet_2d``. 

## Contents

### Classes
- `Resnet2D` — see `../classes/deepxube.heuristics.resnet_2d/Resnet2D.md`
- `ResnetFCParser` — see `../classes/deepxube.heuristics.resnet_2d/ResnetFCParser.md`

## Imports

- `from typing import List, Dict, Any, Type`
- `import torch`
- `from torch import nn, Tensor`
- `import re`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.nnet_input import TwoDIn`
- `from deepxube.base.heuristic import HeurNNet`
- `from deepxube.nnet.pytorch_models import Conv2dModel, ResnetModel, OneHot`
- `from deepxube.factories.heuristic_factory import heuristic_factory`
