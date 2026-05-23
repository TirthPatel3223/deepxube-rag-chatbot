---
id: "func:deepxube._solve.get_policy_fn"
kind: "function"
name: "get_policy_fn"
qualified_name: "deepxube._solve.get_policy_fn"
module: "deepxube._solve"
file: "deepxube/_solve.py"
line_start: 96
line_end: 117
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain"
    annotation: "Domain"
    default: null
  - name: "domain_name"
    annotation: "str"
    default: null
  - name: "policy_nnet_str"
    annotation: "Optional[str]"
    default: null
  - name: "policy_file"
    annotation: "Optional[str]"
    default: null
  - name: "policy_samp"
    annotation: "int"
    default: null
  - name: "policy_rand"
    annotation: "int"
    default: null
  - name: "nnet_batch_size"
    annotation: "Optional[int]"
    default: null
returns: "Optional[PolicyFn]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg"
    expr: "get_policy_nnet_par_from_arg"
    call_sites: [102]
  - target: "func:deepxube.nnet.nnet_utils.get_device"
    expr: "nnet_utils.get_device"
    call_sites: [103]
  - target: null
    expr: "print"
    call_sites: [104]
  - target: "func:deepxube.nnet.nnet_utils.load_nnet"
    expr: "nnet_utils.load_nnet"
    call_sites: [105]
  - target: null
    expr: "policy_nnet_par.get_nnet"
    call_sites: [105]
  - target: null
    expr: "nnet.eval"
    call_sites: [106]
  - target: null
    expr: "nnet.to"
    call_sites: [107]
  - target: "func:torch.nn.DataParallel"
    expr: "nn.DataParallel"
    call_sites: [108]
  - target: null
    expr: "policy_nnet_par.get_nnet_fn"
    call_sites: [109]
  - target: "func:deepxube.base.heuristic.policy_fn_rand"
    expr: "policy_fn_rand"
    call_sites: [113]
  - target: "func:deepxube._solve.PolicyFnRand"
    expr: "PolicyFnRand"
    call_sites: [115]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._solve.get_policy_fn`

**File:** [deepxube/_solve.py:96](../../../../deepxube/_solve.py#L96)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_policy_fn(domain: Domain, domain_name: str, policy_nnet_str: Optional[str], policy_file: Optional[str], policy_samp: int, policy_rand: int, nnet_batch_size: Optional[int]) -> Optional[PolicyFn]
```

## Docstring

:return: Loaded ``PolicyFn`` from file, or a uniform-random fallback if no policy is specified. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `domain_name` | `str` | — |
| `policy_nnet_str` | `Optional[str]` | — |
| `policy_file` | `Optional[str]` | — |
| `policy_samp` | `int` | — |
| `policy_rand` | `int` | — |
| `nnet_batch_size` | `Optional[int]` | — |

## Returns

`Optional[PolicyFn]`

## Calls

- `get_policy_nnet_par_from_arg` → `func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg` (lines: 102)
- `nnet_utils.get_device` → `func:deepxube.nnet.nnet_utils.get_device` (lines: 103)
- `nnet_utils.load_nnet` → `func:deepxube.nnet.nnet_utils.load_nnet` (lines: 105)
- `nn.DataParallel` → `func:torch.nn.DataParallel` (lines: 108)
- `policy_fn_rand` → `func:deepxube.base.heuristic.policy_fn_rand` (lines: 113)
- `PolicyFnRand` → `func:deepxube._solve.PolicyFnRand` (lines: 115)

### Unresolved
- `print` (lines: 104)
- `policy_nnet_par.get_nnet` (lines: 105)
- `nnet.eval` (lines: 106)
- `nnet.to` (lines: 107)
- `policy_nnet_par.get_nnet_fn` (lines: 109)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_policy_fn(domain: Domain, domain_name: str, policy_nnet_str: Optional[str], policy_file: Optional[str], policy_samp: int, policy_rand: int,
                  nnet_batch_size: Optional[int]) -> Optional[PolicyFn]:
    """ :return: Loaded ``PolicyFn`` from file, or a uniform-random fallback if no policy is specified. """
    policy_fn: Optional[PolicyFn]
    if policy_nnet_str is not None:
        assert policy_file is not None
        policy_nnet_par: PolicyNNetPar = get_policy_nnet_par_from_arg(domain, domain_name, policy_nnet_str, policy_samp, policy_rand)[0]
        device, devices, on_gpu = nnet_utils.get_device()
        print("device: %s, devices: %s, on_gpu: %s" % (device, devices, on_gpu))
        nnet: nn.Module = nnet_utils.load_nnet(policy_file, policy_nnet_par.get_nnet())
        nnet.eval()
        nnet.to(device)
        nnet = nn.DataParallel(nnet)
        policy_fn = policy_nnet_par.get_nnet_fn(nnet, nnet_batch_size, device, None)
    else:
        class PolicyFnRand(PolicyFn):
            def __call__(self, domain_in: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                return policy_fn_rand(domain, states, policy_samp + policy_rand)

        policy_fn = PolicyFnRand()

    return policy_fn
```
