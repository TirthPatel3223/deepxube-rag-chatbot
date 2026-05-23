---
id: "func:deepxube.factories.heuristic_factory.build_policy_nnet_par"
kind: "function"
name: "build_policy_nnet_par"
qualified_name: "deepxube.factories.heuristic_factory.build_policy_nnet_par"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 74
line_end: 96
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
  - name: "nnet_name"
    annotation: "str"
    default: null
  - name: "nnet_kwargs"
    annotation: "Dict[str, Any]"
    default: null
  - name: "num_samp"
    annotation: "int"
    default: null
  - name: "num_rand"
    annotation: "int"
    default: null
returns: "PolicyNNetPar"
docstring_source: "present"
callees:
  - target: null
    expr: "policy_factory.get_type(nnet_name).nnet_input_type"
    call_sites: [88]
  - target: null
    expr: "policy_factory.get_type"
    call_sites: [88]
  - target: "func:deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys"
    expr: "get_domain_nnet_input_keys"
    call_sites: [89]
  - target: "func:deepxube.factories.nnet_input_factory.get_nnet_input_t"
    expr: "get_nnet_input_t"
    call_sites: [91]
  - target: null
    expr: "issubclass"
    call_sites: [92]
  - target: "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete"
    expr: "PolicyNNetParConcrete"
    call_sites: [93]
  - target: null
    expr: "ValueError"
    call_sites: [95]
raises:
  - exception: "ValueError"
    call_sites: [95]
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.build_policy_nnet_par`

**File:** [deepxube/factories/heuristic_factory.py:74](../../../../deepxube/factories/heuristic_factory.py#L74)
**Visibility:** public
**Kind:** function

## Signature

```python
def build_policy_nnet_par(domain: Domain, domain_name: str, nnet_name: str, nnet_kwargs: Dict[str, Any], num_samp: int, num_rand: int) -> PolicyNNetPar
```

## Docstring

Build a ``PolicyNNetPar`` by pairing a registered policy network with
a ``PolicyNNetIn`` the domain supports and the network accepts.

:param domain: The instantiated domain the policy will act on.
:param domain_name: Registration key of the domain.
:param nnet_name: Registration key of the policy network.
:param nnet_kwargs: Keyword arguments to pass to the network constructor.
:param num_samp: Number of sampled actions per state for training.
:param num_rand: Number of random actions to mix in (mode-collapse guard).
:return: A ``PolicyNNetParConcrete``.
:raises ValueError: If no ``PolicyNNetIn``-compatible input is found for
    the domain and network.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `domain_name` | `str` | — |
| `nnet_name` | `str` | — |
| `nnet_kwargs` | `Dict[str, Any]` | — |
| `num_samp` | `int` | — |
| `num_rand` | `int` | — |

## Returns

`PolicyNNetPar`

## Calls

- `get_domain_nnet_input_keys` → `func:deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys` (lines: 89)
- `get_nnet_input_t` → `func:deepxube.factories.nnet_input_factory.get_nnet_input_t` (lines: 91)
- `PolicyNNetParConcrete` → `func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete` (lines: 93)

### Unresolved
- `policy_factory.get_type(nnet_name).nnet_input_type` (lines: 88)
- `policy_factory.get_type` (lines: 88)
- `issubclass` (lines: 92)
- `ValueError` (lines: 95)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 95)

## Source

```python
def build_policy_nnet_par(domain: Domain, domain_name: str, nnet_name: str, nnet_kwargs: Dict[str, Any], num_samp: int, num_rand: int) -> PolicyNNetPar:
    """ Build a ``PolicyNNetPar`` by pairing a registered policy network with
    a ``PolicyNNetIn`` the domain supports and the network accepts.

    :param domain: The instantiated domain the policy will act on.
    :param domain_name: Registration key of the domain.
    :param nnet_name: Registration key of the policy network.
    :param nnet_kwargs: Keyword arguments to pass to the network constructor.
    :param num_samp: Number of sampled actions per state for training.
    :param num_rand: Number of random actions to mix in (mode-collapse guard).
    :return: A ``PolicyNNetParConcrete``.
    :raises ValueError: If no ``PolicyNNetIn``-compatible input is found for
        the domain and network.
    """
    nnet_input_t: Type[NNetInput] = policy_factory.get_type(nnet_name).nnet_input_type()
    nnet_input_domain_keys: List[Tuple[str, str]] = get_domain_nnet_input_keys(domain_name)
    for nnet_input_domain_key in nnet_input_domain_keys:
        nnet_input_cls: Type[NNetInput] = get_nnet_input_t(nnet_input_domain_key)
        if issubclass(nnet_input_cls, PolicyNNetIn) and issubclass(nnet_input_cls, nnet_input_t):
            return PolicyNNetParConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs, num_samp, num_rand)

    raise ValueError(f"Cannot build policy nnet for domain: {domain_name}, and "
                     f"nnet_input type {nnet_input_t}.\nNNet inputs checked: {nnet_input_domain_keys}")
```
