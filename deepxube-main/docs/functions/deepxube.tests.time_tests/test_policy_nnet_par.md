---
id: "func:deepxube.tests.time_tests.test_policy_nnet_par"
kind: "function"
name: "test_policy_nnet_par"
qualified_name: "deepxube.tests.time_tests.test_policy_nnet_par"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 188
line_end: 232
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
  - name: "policy_nnet_par"
    annotation: "PolicyNNetPar"
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "actions"
    annotation: "List[Action]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [191, 193, 208, 210, 214, 217, 227, 230]
  - target: null
    expr: "policy_nnet_par.to_np_train"
    call_sites: [192]
  - target: null
    expr: "len"
    call_sites: [194, 196, 211, 212, 218, 220, 231, 232]
  - target: null
    expr: "print"
    call_sites: [195, 201, 212, 219, 232]
  - target: "func:deepxube.tests.time_tests.init_nnet"
    expr: "init_nnet"
    call_sites: [199]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [200]
  - target: "func:deepxube.nnet.nnet_utils.to_pytorch_input"
    expr: "nnet_utils.to_pytorch_input"
    call_sites: [204]
  - target: null
    expr: "nnet.train"
    call_sites: [205]
  - target: null
    expr: "nnet.train_fprop"
    call_sites: [206, 209]
  - target: null
    expr: "nnet.eval"
    call_sites: [215]
  - target: null
    expr: "policy_nnet_par.to_np_fn"
    call_sites: [216]
  - target: null
    expr: "policy_nnet_par.get_nnet_fn"
    call_sites: [222]
  - target: "func:deepxube.tests.time_tests.policy_fn"
    expr: "policy_fn"
    call_sites: [224, 228]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.test_policy_nnet_par`

**File:** [deepxube/tests/time_tests.py:188](../../../../deepxube/tests/time_tests.py#L188)
**Visibility:** public
**Kind:** function

## Signature

```python
def test_policy_nnet_par(domain: Domain, policy_nnet_par: PolicyNNetPar, states: List[State], goals: List[Goal], actions: List[Action]) -> None
```

## Docstring

Time training forward pass and policy sampling for a loaded policy nnet. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `policy_nnet_par` | `PolicyNNetPar` | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `actions` | `List[Action]` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 191, 193, 208, 210, 214, 217, 227, 230)
- `init_nnet` → `func:deepxube.tests.time_tests.init_nnet` (lines: 199)
- `cast` → `func:typing.cast` (lines: 200)
- `nnet_utils.to_pytorch_input` → `func:deepxube.nnet.nnet_utils.to_pytorch_input` (lines: 204)
- `policy_fn` → `func:deepxube.tests.time_tests.policy_fn` (lines: 224, 228)

### Unresolved
- `policy_nnet_par.to_np_train` (lines: 192)
- `len` (lines: 194, 196, 211, 212, 218, 220, 231, 232)
- `print` (lines: 195, 201, 212, 219, 232)
- `nnet.train` (lines: 205)
- `nnet.train_fprop` (lines: 206, 209)
- `nnet.eval` (lines: 215)
- `policy_nnet_par.to_np_fn` (lines: 216)
- `policy_nnet_par.get_nnet_fn` (lines: 222)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def test_policy_nnet_par(domain: Domain, policy_nnet_par: PolicyNNetPar, states: List[State], goals: List[Goal], actions: List[Action]) -> None:
    """ Time training forward pass and policy sampling for a loaded policy nnet. """
    # nnet format
    start_time = time.time()
    train_data_np: List[NDArray] = policy_nnet_par.to_np_train(states, goals, actions)
    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Converted %i states, goals, actions for training to nnet format in "
          "%s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # initialize nnet
    nnet_ret, device = init_nnet(policy_nnet_par)
    nnet: PolicyNNet = cast(PolicyNNet, nnet_ret)
    print("")

    # train fprop
    train_data: List[Tensor] = nnet_utils.to_pytorch_input(train_data_np, device)
    nnet.train()
    nnet.train_fprop(train_data)

    start_time = time.time()
    nnet.train_fprop(train_data)
    nnet_train_out_time = time.time() - start_time
    states_per_sec = len(states) / nnet_train_out_time
    print("Computed policy output for training for %i states in %s seconds (%.2f/second)" % (len(states), nnet_train_out_time, states_per_sec))

    start_time = time.time()
    nnet.eval()
    policy_nnet_par.to_np_fn(states, goals)
    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Converted %i states, goals for sampling to nnet format in "
          "%s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    policy_fn: PolicyFn = policy_nnet_par.get_nnet_fn(nnet, None, device, None)

    policy_fn(domain, states, goals)

    # nnet heuristic
    start_time = time.time()
    policy_fn(domain, states, goals)

    nnet_time = time.time() - start_time
    states_per_sec = len(states) / nnet_time
    print("Computed policy for %i states in %s seconds (%.2f/second)" % (len(states), nnet_time, states_per_sec))
```
