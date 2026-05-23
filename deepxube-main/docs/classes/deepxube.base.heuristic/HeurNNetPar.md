---
id: "class:deepxube.base.heuristic.HeurNNetPar"
kind: "class"
name: "HeurNNetPar"
qualified_name: "deepxube.base.heuristic.HeurNNetPar"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 238
line_end: 256
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "NNetPar[H]"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.HeurNNetPar.get_nnet"
  - "func:deepxube.base.heuristic.HeurNNetPar.get_nnet_fn"
  - "func:deepxube.base.heuristic.HeurNNetPar.get_nnet_par_fn"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurNNetPar`

**File:** [deepxube/base/heuristic.py:238](../../../deepxube/base/heuristic.py#L238)
**Abstract:** yes

## Docstring

Parallelisable wrapper for a heuristic network: pairs the network's
construction recipe with a per-state numpy converter so callables can be
handed to worker processes. 

## Inheritance

**Direct bases:**
- `NNetPar[H]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_nnet` *(trivial, skipped)*
- `get_nnet_fn` *(trivial, skipped)*
- `get_nnet_par_fn` *(trivial, skipped)*

## Source

```python
class HeurNNetPar(NNetPar[H]):
    """ Parallelisable wrapper for a heuristic network: pairs the network's
    construction recipe with a per-state numpy converter so callables can be
    handed to worker processes. """

    @abstractmethod
    def get_nnet(self) -> HeurNNet:
        """ :return: A freshly-constructed heuristic network. """
        pass

    @abstractmethod
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> H:
        """ :return: An in-process callable that runs ``nnet`` on (state, goal[, actions]) lists. """
        pass

    @abstractmethod
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> H:
        """ :return: A callable that routes inference through the worker queue triple. """
        pass
```
