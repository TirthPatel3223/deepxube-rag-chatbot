---
id: "func:deepxube.base.heuristic.PolicyNNetPar.get_nnet_fn"
kind: "method"
name: "get_nnet_fn"
qualified_name: "deepxube.base.heuristic.PolicyNNetPar.get_nnet_fn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 485
line_end: 500
class: "PolicyNNetPar"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nnet"
    annotation: "nn.Module"
    default: null
  - name: "batch_size"
    annotation: "Optional[int]"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "PolicyFn"
docstring_source: "present"
callees:
  - target: null
    expr: "nnet.eval"
    call_sites: [487]
  - target: null
    expr: "len"
    call_sites: [490, 497]
  - target: "func:deepxube.base.heuristic.policy_fn_rand"
    expr: "policy_fn_rand"
    call_sites: [491]
  - target: "func:deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep"
    expr: "self._get_nnet_inputs_rep"
    call_sites: [494]
  - target: "func:deepxube.nnet.nnet_utils.nnet_batched"
    expr: "nnet_batched"
    call_sites: [495]
  - target: "func:deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs"
    expr: "self._np_to_acts_and_pdfs"
    call_sites: [497]
  - target: "func:deepxube.base.heuristic._combine_nnet_with_rand"
    expr: "_combine_nnet_with_rand"
    call_sites: [498]
raises: []
reads_attrs:
  - "self.num_rand"
  - "self.num_samp"
writes_attrs: []
---

# `deepxube.base.heuristic.PolicyNNetPar.get_nnet_fn`

**File:** [deepxube/base/heuristic.py:485](../../../../deepxube/base/heuristic.py#L485)
**Class:** `PolicyNNetPar`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> PolicyFn
```

## Docstring

Build an in-process policy callable. On warmup (``update_num == 0``) returns purely random actions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet` | `nn.Module` | — |
| `batch_size` | `Optional[int]` | — |
| `device` | `torch.device` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`PolicyFn`

## Calls

- `policy_fn_rand` → `func:deepxube.base.heuristic.policy_fn_rand` (lines: 491)
- `self._get_nnet_inputs_rep` → `func:deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep` (lines: 494)
- `nnet_batched` → `func:deepxube.nnet.nnet_utils.nnet_batched` (lines: 495)
- `self._np_to_acts_and_pdfs` → `func:deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs` (lines: 497)
- `_combine_nnet_with_rand` → `func:deepxube.base.heuristic._combine_nnet_with_rand` (lines: 498)

### Unresolved
- `nnet.eval` (lines: 487)
- `len` (lines: 490, 497)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_rand`
- `self.num_samp`

## Source

```python
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> PolicyFn:
        """ Build an in-process policy callable. On warmup (``update_num == 0``) returns purely random actions. """
        nnet.eval()
        if (update_num is not None) and (update_num == 0):
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                assert len(states) == len(goals)  # to stop PyCharm from complaining
                return policy_fn_rand(domain, states, self.num_samp + self.num_rand)
        else:
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                inputs_nnet_rep: List[NDArray] = self._get_nnet_inputs_rep(states, goals, self.num_samp)
                nnet_out_np: List[NDArray[np.float64]] = nnet_batched(nnet, inputs_nnet_rep, batch_size, device)

                actions_l, pdfs_l = self._np_to_acts_and_pdfs(nnet_out_np[0:-1], nnet_out_np[-1], len(states), self.num_samp)
                return _combine_nnet_with_rand(domain, actions_l, pdfs_l, states, self.num_rand)

        return policy_fn
```
