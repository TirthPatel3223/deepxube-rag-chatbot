---
id: "class:deepxube.base.heuristic.HeurNNetParV"
kind: "class"
name: "HeurNNetParV"
qualified_name: "deepxube.base.heuristic.HeurNNetParV"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 259
line_end: 295
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HeurNNetPar[HeurFnV]"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.HeurNNetParV._get_output"
  - "func:deepxube.base.heuristic.HeurNNetParV.get_nnet_fn"
  - "func:deepxube.base.heuristic.HeurNNetParV.get_nnet_par_fn"
  - "func:deepxube.base.heuristic.HeurNNetParV.to_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.HeurNNetParV`

**File:** [deepxube/base/heuristic.py:259](../../../deepxube/base/heuristic.py#L259)
**Abstract:** yes

## Docstring

V-type heuristic ``Par``: scalar cost-to-go output, clamped non-negative. 

## Inheritance

**Direct bases:**
- `HeurNNetPar[HeurFnV]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_get_output`
- `get_nnet_fn`
- `get_nnet_par_fn`
- `to_np` *(trivial, skipped)*

## Source

```python
class HeurNNetParV(HeurNNetPar[HeurFnV]):
    """ V-type heuristic ``Par``: scalar cost-to-go output, clamped non-negative. """

    @staticmethod
    def _get_output(heurs: NDArray[np.float64], update_num: Optional[int]) -> List[float]:
        """ Clamp to non-negative; on ``update_num == 0`` return all zeros (warmup). """
        heurs = np.maximum(heurs[:, 0], 0)
        if (update_num is not None) and (update_num == 0):
            heurs = heurs * 0
        return cast(List[float], heurs.astype(np.float64).tolist())

    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device,
                    update_num: Optional[int]) -> HeurFnV:
        """ Build an in-process V-heuristic callable that batches through ``nnet``. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal]) -> List[float]:
            inputs_nnet: List[NDArray] = self.to_np(states, goals)
            heurs: NDArray[np.float64] = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]

            return self._get_output(heurs, update_num)
        return heuristic_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnV:
        """ Build a V-heuristic callable that delegates to a worker NNet runner. """
        def heuristic_fn(states: List[State], goals: List[Goal]) -> List[float]:
            inputs_nnet: List[NDArray] = self.to_np(states, goals)
            heurs: NDArray[np.float64] = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]

            return self._get_output(heurs, update_num)

        return heuristic_fn

    @abstractmethod
    def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]:
        """ Convert state/goal lists into per-tensor numpy inputs. """
        pass
```
