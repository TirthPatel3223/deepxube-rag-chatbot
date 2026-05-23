---
id: "class:deepxube.base.heuristic.HeurNNet"
kind: "class"
name: "HeurNNet"
qualified_name: "deepxube.base.heuristic.HeurNNet"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 67
line_end: 94
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "DeepXubeNNet[In]"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.HeurNNet.__init__"
  - "func:deepxube.base.heuristic.HeurNNet.forward"
  - "func:deepxube.base.heuristic.HeurNNet._forward"
attributes:
  - name: "self.out_dim"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.q_fix"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurNNet`

**File:** [deepxube/base/heuristic.py:67](../../../deepxube/base/heuristic.py#L67)
**Abstract:** yes

## Docstring

Heuristic network. With ``q_fix=True``, the last input tensor is treated
as action indices and only those columns of the output are returned. 

## Inheritance

**Direct bases:**
- `DeepXubeNNet[In]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `forward`
- `_forward` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.out_dim` | — | __init__ |
| `self.q_fix` | — | __init__ |

## Source

```python
class HeurNNet(DeepXubeNNet[In]):
    """ Heuristic network. With ``q_fix=True``, the last input tensor is treated
    as action indices and only those columns of the output are returned. """

    def __init__(self, nnet_input: In, out_dim: int, q_fix: bool, **kwargs: Any):
        """ Store output dimension and fixed-Q flag.

        :param out_dim: Number of network outputs (1 for V; ``num_acts`` for fixed Q).
        :param q_fix: If True, the network returns one output per fixed action and
            ``forward`` indexes the requested columns.
        """
        super().__init__(nnet_input)
        self.out_dim: int = out_dim
        self.q_fix: bool = q_fix

    def forward(self, inputs: List[Tensor]) -> List[Tensor]:
        """ Run the body and, if ``q_fix``, gather only the requested action columns. """
        if self.q_fix:
            action_idxs: Tensor = inputs[-1].long()
            x: Tensor = self._forward(inputs[:-1])
            return [torch.gather(x, 1, action_idxs)]
        else:
            return [self._forward(inputs)]

    @abstractmethod
    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ Subclass forward body returning a single output tensor. """
        pass
```
