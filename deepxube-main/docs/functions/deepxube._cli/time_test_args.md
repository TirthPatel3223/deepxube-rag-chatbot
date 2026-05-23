---
id: "func:deepxube._cli.time_test_args"
kind: "function"
name: "time_test_args"
qualified_name: "deepxube._cli.time_test_args"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 217
line_end: 226
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "args"
    annotation: "argparse.Namespace"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_domain_from_arg"
    expr: "get_domain_from_arg"
    call_sites: [219]
  - target: "func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg"
    expr: "get_heur_nnet_par_from_arg"
    call_sites: [223]
  - target: "func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg"
    expr: "get_policy_nnet_par_from_arg"
    call_sites: [225]
  - target: "func:deepxube.tests.time_tests.time_test"
    expr: "time_test"
    call_sites: [226]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.time_test_args`

**File:** [deepxube/_cli.py:217](../../../../deepxube/_cli.py#L217)
**Visibility:** public
**Kind:** function

## Signature

```python
def time_test_args(args: argparse.Namespace) -> None
```

## Docstring

Parse CLI args and forward to :func:`~deepxube.tests.time_tests.time_test`. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `get_domain_from_arg` → `func:deepxube.utils.command_line_utils.get_domain_from_arg` (lines: 219)
- `get_heur_nnet_par_from_arg` → `func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg` (lines: 223)
- `get_policy_nnet_par_from_arg` → `func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg` (lines: 225)
- `time_test` → `func:deepxube.tests.time_tests.time_test` (lines: 226)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def time_test_args(args: argparse.Namespace) -> None:
    """ Parse CLI args and forward to :func:`~deepxube.tests.time_tests.time_test`. """
    domain, domain_name = get_domain_from_arg(args.domain)
    heur_nnet_par: Optional[HeurNNetPar] = None
    policy_nnet_par: Optional[PolicyNNetPar] = None
    if args.heur is not None:
        heur_nnet_par = get_heur_nnet_par_from_arg(domain, domain_name, args.heur, args.heur_type)[0]
    if args.policy is not None:
        policy_nnet_par = get_policy_nnet_par_from_arg(domain, domain_name, args.policy, args.policy_samp, args.policy_rand)[0]
    time_test(domain, heur_nnet_par, policy_nnet_par, args.num_insts, args.step_max)
```
