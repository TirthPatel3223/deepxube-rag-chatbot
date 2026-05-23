---
id: "func:deepxube.base.heuristic.PolicyNNetPar.get_nnet_par_fn"
kind: "method"
name: "get_nnet_par_fn"
qualified_name: "deepxube.base.heuristic.PolicyNNetPar.get_nnet_par_fn"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 502
line_end: 516
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
  - name: "nnet_par_info"
    annotation: "NNetParInfo"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "PolicyFn"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [506, 513]
  - target: "func:deepxube.base.heuristic.policy_fn_rand"
    expr: "policy_fn_rand"
    call_sites: [507]
  - target: "func:deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep"
    expr: "self._get_nnet_inputs_rep"
    call_sites: [510]
  - target: "func:deepxube.nnet.nnet_utils.get_nnet_par_out"
    expr: "get_nnet_par_out"
    call_sites: [511]
  - target: "func:deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs"
    expr: "self._np_to_acts_and_pdfs"
    call_sites: [513]
  - target: "func:deepxube.base.heuristic._combine_nnet_with_rand"
    expr: "_combine_nnet_with_rand"
    call_sites: [514]
raises: []
reads_attrs:
  - "self.num_rand"
  - "self.num_samp"
writes_attrs: []
---

# `deepxube.base.heuristic.PolicyNNetPar.get_nnet_par_fn`

**File:** [deepxube/base/heuristic.py:502](../../../../deepxube/base/heuristic.py#L502)
**Class:** `PolicyNNetPar`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> PolicyFn
```

## Docstring

Worker-queue-routed variant of ``get_nnet_fn``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_par_info` | `NNetParInfo` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`PolicyFn`

## Calls

- `policy_fn_rand` → `func:deepxube.base.heuristic.policy_fn_rand` (lines: 507)
- `self._get_nnet_inputs_rep` → `func:deepxube.base.heuristic.PolicyNNetPar._get_nnet_inputs_rep` (lines: 510)
- `get_nnet_par_out` → `func:deepxube.nnet.nnet_utils.get_nnet_par_out` (lines: 511)
- `self._np_to_acts_and_pdfs` → `func:deepxube.base.heuristic.PolicyNNetPar._np_to_acts_and_pdfs` (lines: 513)
- `_combine_nnet_with_rand` → `func:deepxube.base.heuristic._combine_nnet_with_rand` (lines: 514)

### Unresolved
- `len` (lines: 506, 513)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_rand`
- `self.num_samp`

## Source

```python
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> PolicyFn:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        if (update_num is not None) and (update_num == 0):
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                assert len(states) == len(goals)  # to stop PyCharm from complaining
                return policy_fn_rand(domain, states, self.num_samp + self.num_rand)
        else:
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                inputs_nnet_rep: List[NDArray] = self._get_nnet_inputs_rep(states, goals, self.num_samp)
                nnet_out_np: List[NDArray[np.float64]] = get_nnet_par_out(inputs_nnet_rep, nnet_par_info)

                actions_l, pdfs_l = self._np_to_acts_and_pdfs(nnet_out_np[0:-1], nnet_out_np[-1], len(states), self.num_samp)
                return _combine_nnet_with_rand(domain, actions_l, pdfs_l, states, self.num_rand)

        return policy_fn
```
