---
id: "class:deepxube.domains.grid.GridNet"
kind: "class"
name: "GridNet"
qualified_name: "deepxube.domains.grid.GridNet"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 181
line_end: 205
is_abstract: false
is_dataclass: false
decorators:
  - "@heuristic_factory.register_class('gridnet')"
generic_parameters: []
bases:
  - name: "HeurNNet[GridNNetInput]"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.GridNet.nnet_input_type"
  - "func:deepxube.domains.grid.GridNet.__init__"
  - "func:deepxube.domains.grid.GridNet._forward"
attributes:
  - name: "self.heur"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.one_hots"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.heuristic_factory.heuristic_factory"
    key: "gridnet"
docstring_source: "present"
---

# `deepxube.domains.grid.GridNet`

**File:** [deepxube/domains/grid.py:181](../../../deepxube/domains/grid.py#L181)
**Abstract:** no
**Decorators:** `@heuristic_factory.register_class('gridnet')`

## Docstring

CNN heuristic for the Grid domain, registered as ``gridnet``; uses Conv2d + FC layers. 

## Inheritance

**Direct bases:**
- `HeurNNet[GridNNetInput]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.heuristic_factory.heuristic_factory` under key `gridnet`

## Methods

- `nnet_input_type` *(trivial, skipped)* — *(no docstring)*
- `__init__`
- `_forward`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.heur` | — | __init__ |
| `self.one_hots` | — | __init__ |

## Source

```python
class GridNet(HeurNNet[GridNNetInput]):
    """ CNN heuristic for the Grid domain, registered as ``gridnet``; uses Conv2d + FC layers. """

    @staticmethod
    def nnet_input_type() -> Type[GridNNetInput]:
        return GridNNetInput

    def __init__(self, nnet_input: GridNNetInput, out_dim: int, q_fix: bool, chan_size: int = 8, fc_size: int = 100):
        """ Build the Conv2d and FC layers from grid dimensions. """
        super().__init__(nnet_input, out_dim, q_fix)
        # one hots
        self.one_hots: nn.ModuleList = nn.ModuleList()
        grid_dim: int = self.nnet_input.get_input_info()

        self.heur: nn.Module = nn.Sequential(
            Conv2dModel(2, [chan_size, chan_size], [3, 3], [1, 1], ["RELU", "RELU"], batch_norms=[True, True]),
            nn.Flatten(),
            FullyConnectedModel(grid_dim * grid_dim * chan_size, [fc_size], ["RELU"], batch_norms=[True]),
            nn.Linear(fc_size, self.out_dim)
        )

    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ :return: Heuristic value from the 2-channel spatial input. """
        x: Tensor = self.heur(inputs[0])
        return x
```
