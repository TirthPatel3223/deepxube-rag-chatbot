---
id: "module:deepxube.heuristics.resnet_fc"
kind: "module"
name: "resnet_fc"
qualified_name: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_count: 193
docstring_source: "present"
imports:
  - kind: "from"
    module: "typing"
    names: [{"name": "List", "alias": null}, {"name": "Dict", "alias": null}, {"name": "Any", "alias": null}, {"name": "Type", "alias": null}, {"name": "Tuple", "alias": null}]
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
    names: [{"name": "FlatIn", "alias": null}, {"name": "FlatInPolicy", "alias": null}]
  - kind: "from"
    module: "deepxube.base.heuristic"
    names: [{"name": "HeurNNet", "alias": null}, {"name": "PolicyVAE", "alias": null}]
  - kind: "from"
    module: "deepxube.nnet.pytorch_models"
    names: [{"name": "FullyConnectedModel", "alias": null}, {"name": "ResnetModel", "alias": null}, {"name": "OneHot", "alias": null}, {"name": "make_onehots", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.heuristic_factory"
    names: [{"name": "heuristic_factory", "alias": null}]
  - kind: "from"
    module: "deepxube.factories.heuristic_factory"
    names: [{"name": "policy_factory", "alias": null}]
classes:
  - "class:deepxube.heuristics.resnet_fc.ResnetFCHeur"
  - "class:deepxube.heuristics.resnet_fc.ResnetFCPolicy"
  - "class:deepxube.heuristics.resnet_fc.ResnetFCParserHeur"
  - "class:deepxube.heuristics.resnet_fc.ResnetFCParserPolicy"
module_level_functions: []
module_level_constants: []
---

# Module `deepxube.heuristics.resnet_fc`

**File:** [deepxube/heuristics/resnet_fc.py](../../deepxube/heuristics/resnet_fc.py)
**Lines:** 193

## Module docstring

Fully-connected ResNet heuristic and VAE policy for flat NNet inputs. Both are registered in their respective
factories as ``resnet_fc``. 

## Contents

### Classes
- `ResnetFCHeur` — see `../classes/deepxube.heuristics.resnet_fc/ResnetFCHeur.md`
- `ResnetFCPolicy` — see `../classes/deepxube.heuristics.resnet_fc/ResnetFCPolicy.md`
- `ResnetFCParserHeur` — see `../classes/deepxube.heuristics.resnet_fc/ResnetFCParserHeur.md`
- `ResnetFCParserPolicy` — see `../classes/deepxube.heuristics.resnet_fc/ResnetFCParserPolicy.md`

## Imports

- `from typing import List, Dict, Any, Type, Tuple`
- `import torch`
- `from torch import nn, Tensor`
- `import re`
- `from deepxube.base.factory import Parser`
- `from deepxube.base.nnet_input import FlatIn, FlatInPolicy`
- `from deepxube.base.heuristic import HeurNNet, PolicyVAE`
- `from deepxube.nnet.pytorch_models import FullyConnectedModel, ResnetModel, OneHot, make_onehots`
- `from deepxube.factories.heuristic_factory import heuristic_factory`
- `from deepxube.factories.heuristic_factory import policy_factory`
