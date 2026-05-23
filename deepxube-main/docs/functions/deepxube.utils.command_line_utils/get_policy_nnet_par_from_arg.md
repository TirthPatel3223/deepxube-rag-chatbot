---
id: "func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg"
kind: "function"
name: "get_policy_nnet_par_from_arg"
qualified_name: "deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg"
module: "deepxube.utils.command_line_utils"
file: "deepxube/utils/command_line_utils.py"
line_start: 66
line_end: 81
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
  - name: "policy"
    annotation: "str"
    default: null
  - name: "num_samp"
    annotation: "int"
    default: null
  - name: "num_int"
    annotation: "int"
    default: null
returns: "Tuple[PolicyNNetPar, str]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_name_args"
    expr: "get_name_args"
    call_sites: [77]
  - target: "func:deepxube.factories.heuristic_factory.policy_factory.get_type"
    expr: "policy_factory.get_type"
    call_sites: [78]
  - target: "func:deepxube.factories.heuristic_factory.policy_factory.get_kwargs"
    expr: "policy_factory.get_kwargs"
    call_sites: [79]
  - target: "func:deepxube.factories.heuristic_factory.build_policy_nnet_par"
    expr: "build_policy_nnet_par"
    call_sites: [80]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg`

**File:** [deepxube/utils/command_line_utils.py:66](../../../../deepxube/utils/command_line_utils.py#L66)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_policy_nnet_par_from_arg(domain: Domain, domain_name: str, policy: str, num_samp: int, num_int: int) -> Tuple[PolicyNNetPar, str]
```

## Docstring

Resolve a ``--policy`` CLI argument into a ``PolicyNNetPar`` for the
given domain.

:param domain: Instantiated domain the policy will act on.
:param domain_name: Domain registration key.
:param policy: CLI string for the policy network.
:param num_samp: Number of sampled actions per state at training time.
:param num_int: Number of random (mode-collapse guard) actions to mix in.
:return: Tuple of (``PolicyNNetPar``, network registration name).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `domain_name` | `str` | — |
| `policy` | `str` | — |
| `num_samp` | `int` | — |
| `num_int` | `int` | — |

## Returns

`Tuple[PolicyNNetPar, str]`

## Calls

- `get_name_args` → `func:deepxube.utils.command_line_utils.get_name_args` (lines: 77)
- `policy_factory.get_type` → `func:deepxube.factories.heuristic_factory.policy_factory.get_type` (lines: 78)
- `policy_factory.get_kwargs` → `func:deepxube.factories.heuristic_factory.policy_factory.get_kwargs` (lines: 79)
- `build_policy_nnet_par` → `func:deepxube.factories.heuristic_factory.build_policy_nnet_par` (lines: 80)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_policy_nnet_par_from_arg(domain: Domain, domain_name: str, policy: str, num_samp: int, num_int: int) -> Tuple[PolicyNNetPar, str]:
    """ Resolve a ``--policy`` CLI argument into a ``PolicyNNetPar`` for the
    given domain.

    :param domain: Instantiated domain the policy will act on.
    :param domain_name: Domain registration key.
    :param policy: CLI string for the policy network.
    :param num_samp: Number of sampled actions per state at training time.
    :param num_int: Number of random (mode-collapse guard) actions to mix in.
    :return: Tuple of (``PolicyNNetPar``, network registration name).
    """
    nnet_name, nnet_args = get_name_args(policy)
    policy_factory.get_type(nnet_name)  # to ensure existence
    nnet_kwargs: Dict[str, Any] = policy_factory.get_kwargs(nnet_name, nnet_args)
    nnet_par: PolicyNNetPar = build_policy_nnet_par(domain, domain_name, nnet_name, nnet_kwargs, num_samp, num_int)
    return nnet_par, nnet_name
```
