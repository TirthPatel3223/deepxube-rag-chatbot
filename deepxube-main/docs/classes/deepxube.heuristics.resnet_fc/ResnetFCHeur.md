---
id: "class:deepxube.heuristics.resnet_fc.ResnetFCHeur"
kind: "class"
name: "ResnetFCHeur"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCHeur"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 19
line_end: 58
is_abstract: false
is_dataclass: false
decorators:
  - "@heuristic_factory.register_class('resnet_fc')"
generic_parameters: []
bases:
  - name: "HeurNNet[FlatIn]"
    resolved_id: null
methods:
  - "func:deepxube.heuristics.resnet_fc.ResnetFCHeur.nnet_input_type"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCHeur.__init__"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCHeur._forward"
attributes:
  - name: "self.heur"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.one_hots"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.res_dim"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.heuristic_factory.heuristic_factory"
    key: "resnet_fc"
docstring_source: "present"
---

# `deepxube.heuristics.resnet_fc.ResnetFCHeur`

**File:** [deepxube/heuristics/resnet_fc.py:19](../../../deepxube/heuristics/resnet_fc.py#L19)
**Abstract:** no
**Decorators:** `@heuristic_factory.register_class('resnet_fc')`

## Docstring

FC-ResNet heuristic for flat (FlatIn) inputs; one-hot encodes, concatenates, and regresses to ``out_dim`` values. 

## Inheritance

**Direct bases:**
- `HeurNNet[FlatIn]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.heuristic_factory.heuristic_factory` under key `resnet_fc`

## Methods

- `nnet_input_type` *(trivial, skipped)*
- `__init__`
- `_forward`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.heur` | — | __init__ |
| `self.one_hots` | — | __init__ |
| `self.res_dim` | — | __init__ |

## Source

```python
class ResnetFCHeur(HeurNNet[FlatIn]):
    """ FC-ResNet heuristic for flat (FlatIn) inputs; one-hot encodes, concatenates, and regresses to ``out_dim`` values. """

    @staticmethod
    def nnet_input_type() -> Type[FlatIn]:
        """ :return: ``FlatIn``. """
        return FlatIn

    def __init__(self, nnet_input: FlatIn, out_dim: int, q_fix: bool, res_dim: int = 1000, num_blocks: int = 4,
                 batch_norm: bool = False, weight_norm: bool = False, group_norm: int = -1, act_fn: str = "RELU"):
        """ Build one-hot encoders, residual body, and linear output layer from ``nnet_input`` metadata. """
        super().__init__(nnet_input, out_dim, q_fix)
        # one hots
        self.one_hots: nn.ModuleList = nn.ModuleList()
        input_dim_tot: int = 0
        input_dims, one_hot_depths = self.nnet_input.get_input_info()
        for input_dim, one_hot_depth in zip(input_dims, one_hot_depths, strict=True):
            assert one_hot_depth >= 1
            self.one_hots.append(OneHot(one_hot_depth, True))
            input_dim_tot += input_dim * one_hot_depth

        # res net
        self.res_dim: int = res_dim

        def res_block_init() -> nn.Module:
            return FullyConnectedModel(res_dim, [res_dim] * 2, [act_fn, "LINEAR"],
                                       batch_norms=[batch_norm] * 2, weight_norms=[weight_norm] * 2,
                                       group_norms=[group_norm] * 2)

        self.heur = nn.Sequential(
            nn.Linear(input_dim_tot, res_dim),
            ResnetModel(res_block_init, num_blocks, act_fn),
            nn.Linear(res_dim, self.out_dim)
        )

    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ One-hot encode each input, concatenate, and run through the residual network. """
        inputs_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(inputs, self.one_hots)]
        x: Tensor = self.heur(torch.cat(inputs_oh, dim=1))
        return x
```
