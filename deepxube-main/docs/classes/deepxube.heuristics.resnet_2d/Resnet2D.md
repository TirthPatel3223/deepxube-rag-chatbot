---
id: "class:deepxube.heuristics.resnet_2d.Resnet2D"
kind: "class"
name: "Resnet2D"
qualified_name: "deepxube.heuristics.resnet_2d.Resnet2D"
module: "deepxube.heuristics.resnet_2d"
file: "deepxube/heuristics/resnet_2d.py"
line_start: 18
line_end: 77
is_abstract: false
is_dataclass: false
decorators:
  - "@heuristic_factory.register_class('resnet_2d')"
generic_parameters: []
bases:
  - name: "HeurNNet[TwoDIn]"
    resolved_id: null
methods:
  - "func:deepxube.heuristics.resnet_2d.Resnet2D.nnet_input_type"
  - "func:deepxube.heuristics.resnet_2d.Resnet2D.__init__"
  - "func:deepxube.heuristics.resnet_2d.Resnet2D._forward"
attributes:
  - name: "self.heur"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.one_hots"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.out"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.heuristic_factory.heuristic_factory"
    key: "resnet_2d"
docstring_source: "present"
---

# `deepxube.heuristics.resnet_2d.Resnet2D`

**File:** [deepxube/heuristics/resnet_2d.py:18](../../../deepxube/heuristics/resnet_2d.py#L18)
**Abstract:** no
**Decorators:** `@heuristic_factory.register_class('resnet_2d')`

## Docstring

Conv-ResNet heuristic for 2-D spatial inputs; one-hot encodes each channel, applies residual blocks, and
collapses to ``out_dim`` scalars. 

## Inheritance

**Direct bases:**
- `HeurNNet[TwoDIn]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.heuristic_factory.heuristic_factory` under key `resnet_2d`

## Methods

- `nnet_input_type` *(trivial, skipped)*
- `__init__`
- `_forward`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.heur` | — | __init__ |
| `self.one_hots` | — | __init__ |
| `self.out` | — | __init__ |

## Source

```python
class Resnet2D(HeurNNet[TwoDIn]):
    """ Conv-ResNet heuristic for 2-D spatial inputs; one-hot encodes each channel, applies residual blocks, and
    collapses to ``out_dim`` scalars. """

    @staticmethod
    def nnet_input_type() -> Type[TwoDIn]:
        """ :return: ``TwoDIn``. """
        return TwoDIn

    def __init__(self, nnet_input: TwoDIn, out_dim: int, q_fix: bool, num_chan: int = 64, num_blocks: int = 4,
                 batch_norm: bool = False, weight_norm: bool = False, act_fn: str = "RELU"):
        """ Build one-hot encoders, residual body, and output head from ``nnet_input`` metadata. """
        super().__init__(nnet_input, out_dim, q_fix)

        chan_dims, (height, width), one_hot_depths, q_fix_1x1 = self.nnet_input.get_input_info()

        # one hots
        self.one_hots: nn.ModuleList = nn.ModuleList()
        chan_in_tot: int = 0
        for chan_dim, one_hot_depth in zip(chan_dims, one_hot_depths, strict=True):
            assert one_hot_depth >= 1
            self.one_hots.append(OneHot(one_hot_depth, False))
            chan_in_tot += chan_dim * one_hot_depth

        # res net
        def res_block_init() -> nn.Module:
            return Conv2dModel(num_chan, [num_chan] * 2, [3] * 2, [1] * 2, [act_fn, "LINEAR"],
                               batch_norms=[batch_norm] * 2, weight_norms=[weight_norm] * 2)

        self.heur = nn.Sequential(
            Conv2dModel(chan_in_tot, [num_chan], [1], [0], ["LINEAR"]),
            ResnetModel(res_block_init, num_blocks, act_fn),
        )

        if self.q_fix and (q_fix_1x1 is not None):
            assert (height * width * q_fix_1x1) == out_dim
            self.out = nn.Sequential(
                Conv2dModel(num_chan, [q_fix_1x1], [1], [0], ["LINEAR"]),
                nn.Flatten(),
            )
        else:
            self.out = nn.Sequential(
                Conv2dModel(num_chan, [1], [1], [0], ["LINEAR"]),
                nn.Flatten(),
                nn.Linear(height * width, out_dim)
            )

    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ One-hot encode each input channel, concatenate spatially, run the ResNet body, and apply the output head. """
        inputs_oh: List[Tensor] = []
        for input_i, one_hot in zip(inputs, self.one_hots):
            input_i_oh: Tensor = one_hot(input_i)
            if len(input_i_oh.shape) == 5:
                input_i_oh = input_i_oh.permute((0, 1, 4, 2, 3)).flatten(1, 2)
            inputs_oh.append(input_i_oh)

        # inputs_oh: List[Tensor] = [one_hot(input_i).permute((0, 1, 4, 2, 3)).flatten(1, 2) for input_i, one_hot in zip(inputs, self.one_hots)]
        x: Tensor = self.heur(torch.cat(inputs_oh, dim=1))
        x = self.out(x)
        return x
```
