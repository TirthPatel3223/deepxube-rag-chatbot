---
id: "class:deepxube.nnet.nnet_utils.NNetPar"
kind: "class"
name: "NNetPar"
qualified_name: "deepxube.nnet.nnet_utils.NNetPar"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 233
line_end: 253
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "NNetFn"
bases:
  - name: "ABC"
    resolved_id: null
  - name: "Generic[NNetFn]"
    resolved_id: null
methods:
  - "func:deepxube.nnet.nnet_utils.NNetPar.get_nnet_fn"
  - "func:deepxube.nnet.nnet_utils.NNetPar.get_nnet_par_fn"
  - "func:deepxube.nnet.nnet_utils.NNetPar.get_nnet"
  - "func:deepxube.nnet.nnet_utils.NNetPar.__repr__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.nnet_utils.NNetPar`

**File:** [deepxube/nnet/nnet_utils.py:233](../../../deepxube/nnet/nnet_utils.py#L233)
**Abstract:** yes
**Generic parameters:** `NNetFn`

## Docstring

Abstract interface for obtaining nnet callables — either local (direct) or via an inter-process queue. 

## Inheritance

**Direct bases:**
- `ABC`
- `Generic[NNetFn]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_nnet_fn` *(trivial, skipped)*
- `get_nnet_par_fn` *(trivial, skipped)*
- `get_nnet` *(trivial, skipped)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class NNetPar(ABC, Generic[NNetFn]):
    """ Abstract interface for obtaining nnet callables — either local (direct) or via an inter-process queue. """

    @abstractmethod
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device,
                    update_num: Optional[int]) -> NNetFn:
        """ :return: A callable that runs the nnet locally on ``device``. """
        pass

    @abstractmethod
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> NNetFn:
        """ :return: A callable that routes inference through the parallel worker described by ``nnet_par_info``. """
        pass

    @abstractmethod
    def get_nnet(self) -> nn.Module:
        """ :return: The underlying ``nn.Module``. """
        pass

    def __repr__(self) -> str:
        return f"{self.get_nnet()}"
```
