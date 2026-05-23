---
id: "class:deepxube.base.heuristic.DeepXubeNNet"
kind: "class"
name: "DeepXubeNNet"
qualified_name: "deepxube.base.heuristic.DeepXubeNNet"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 31
line_end: 62
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "In"
bases:
  - name: "nn.Module"
    resolved_id: null
  - name: "Generic[In]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.DeepXubeNNet.nnet_input_type"
  - "func:deepxube.base.heuristic.DeepXubeNNet.__init__"
  - "func:deepxube.base.heuristic.DeepXubeNNet.forward"
  - "func:deepxube.base.heuristic.DeepXubeNNet.get_optimizer"
  - "func:deepxube.base.heuristic.DeepXubeNNet.update_optimizer"
attributes:
  - name: "self.lr"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.lr_d"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_input"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.DeepXubeNNet`

**File:** [deepxube/base/heuristic.py:31](../../../deepxube/base/heuristic.py#L31)
**Abstract:** yes
**Generic parameters:** `In`

## Docstring

Common base for heuristic and policy networks. Holds the ``NNetInput``,
declares the LR schedule, and asserts type compatibility on construction. 

## Inheritance

**Direct bases:**
- `nn.Module`
- `Generic[In]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `nnet_input_type` *(trivial, skipped)*
- `__init__`
- `forward` *(trivial, skipped)*
- `get_optimizer`
- `update_optimizer`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.lr` | — | __init__ |
| `self.lr_d` | — | __init__ |
| `self.nnet_input` | — | __init__ |

## Source

```python
class DeepXubeNNet(nn.Module, Generic[In], ABC):
    """ Common base for heuristic and policy networks. Holds the ``NNetInput``,
    declares the LR schedule, and asserts type compatibility on construction. """

    @staticmethod
    @abstractmethod
    def nnet_input_type() -> Type[In]:
        """ :return: The ``NNetInput`` subclass this network expects. """
        pass

    def __init__(self, nnet_input: In):
        """ Bind the ``NNetInput`` and initialise default learning-rate parameters. """
        super().__init__()
        assert isinstance(nnet_input, self.nnet_input_type()), f"NNetInput {nnet_input} must be an instance of {self.nnet_input_type()}."
        self.nnet_input: In = nnet_input
        self.lr: float = 0.001
        self.lr_d: float = 0.9999993

    @abstractmethod
    def forward(self, inputs: List[Tensor]) -> List[Tensor]:
        """ Standard PyTorch forward pass over the per-input tensor list. """
        pass

    def get_optimizer(self) -> Optimizer:
        """ :return: Default Adam optimiser at lr=0.001. """
        return optim.Adam(self.parameters(), lr=0.001)

    def update_optimizer(self, optimizer: Optimizer, train_itr: int) -> None:
        """ Apply geometric LR decay ``lr * lr_d ** train_itr`` to every param group. """
        lr_itr: float = self.lr * (self.lr_d ** train_itr)
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr_itr
```
