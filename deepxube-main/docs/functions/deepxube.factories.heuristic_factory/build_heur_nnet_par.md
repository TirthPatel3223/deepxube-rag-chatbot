---
id: "func:deepxube.factories.heuristic_factory.build_heur_nnet_par"
kind: "function"
name: "build_heur_nnet_par"
qualified_name: "deepxube.factories.heuristic_factory.build_heur_nnet_par"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 31
line_end: 71
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
  - name: "heur_type"
    annotation: "str"
    default: null
returns: "HeurNNetPar"
docstring_source: "present"
callees:
  - target: null
    expr: "heuristic_factory.get_type(nnet_name).nnet_input_type"
    call_sites: [53]
  - target: "func:deepxube.factories.heuristic_factory.get_type"
    expr: "heuristic_factory.get_type"
    call_sites: [53]
  - target: "func:deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys"
    expr: "get_domain_nnet_input_keys"
    call_sites: [54]
  - target: "func:deepxube.factories.nnet_input_factory.get_nnet_input_t"
    expr: "get_nnet_input_t"
    call_sites: [57]
  - target: null
    expr: "heur_type.upper"
    call_sites: [58, 61, 65]
  - target: null
    expr: "issubclass"
    call_sites: [59, 63, 66]
  - target: "func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete"
    expr: "HeurNNetParVConcrete"
    call_sites: [60]
  - target: null
    expr: "isinstance"
    call_sites: [62]
  - target: "func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete"
    expr: "HeurNNetParQFixOutConcrete"
    call_sites: [64]
  - target: null
    expr: "domain.get_num_acts"
    call_sites: [64]
  - target: "func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete"
    expr: "HeurNNetParQActInConcrete"
    call_sites: [67]
  - target: null
    expr: "ValueError"
    call_sites: [69, 70]
raises:
  - exception: "ValueError"
    call_sites: [69, 70]
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.build_heur_nnet_par`

**File:** [deepxube/factories/heuristic_factory.py:31](../../../../deepxube/factories/heuristic_factory.py#L31)
**Visibility:** public
**Kind:** function

## Signature

```python
def build_heur_nnet_par(domain: Domain, domain_name: str, nnet_name: str, nnet_kwargs: Dict[str, Any], heur_type: str) -> HeurNNetPar
```

## Docstring

Build a ``HeurNNetPar`` by pairing a registered heuristic network with
an ``NNetInput`` the domain supports and the network accepts.

Walks every ``NNetInput`` registered under ``domain_name`` and returns the
first one that is simultaneously a subclass of the heuristic network's
expected input type and of the input mixin required by ``heur_type``
(``StateGoalIn`` for ``V``, ``StateGoalActFixIn`` for ``QFIX``,
``StateGoalActIn`` for ``QIN``).

:param domain: The instantiated domain the network will run against.
:param domain_name: Registration key of the domain.
:param nnet_name: Registration key of the heuristic network (e.g.
    ``"resnet_fc"``).
:param nnet_kwargs: Keyword arguments to pass to the network constructor.
:param heur_type: One of ``"V"``, ``"QFIX"``, ``"QIN"``
    (case-insensitive). Selects the output shape.
:return: A concrete ``HeurNNetPar`` (``HeurNNetParVConcrete``,
    ``HeurNNetParQFixOutConcrete``, or ``HeurNNetParQActInConcrete``).
:raises ValueError: If ``heur_type`` is unrecognised, or if no compatible
    ``NNetInput`` is found for the given domain, heur type, and network.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `domain_name` | `str` | — |
| `nnet_name` | `str` | — |
| `nnet_kwargs` | `Dict[str, Any]` | — |
| `heur_type` | `str` | — |

## Returns

`HeurNNetPar`

## Calls

- `heuristic_factory.get_type` → `func:deepxube.factories.heuristic_factory.get_type` (lines: 53)
- `get_domain_nnet_input_keys` → `func:deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys` (lines: 54)
- `get_nnet_input_t` → `func:deepxube.factories.nnet_input_factory.get_nnet_input_t` (lines: 57)
- `HeurNNetParVConcrete` → `func:deepxube.factories.heuristic_factory.HeurNNetParVConcrete` (lines: 60)
- `HeurNNetParQFixOutConcrete` → `func:deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete` (lines: 64)
- `HeurNNetParQActInConcrete` → `func:deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete` (lines: 67)

### Unresolved
- `heuristic_factory.get_type(nnet_name).nnet_input_type` (lines: 53)
- `heur_type.upper` (lines: 58, 61, 65)
- `issubclass` (lines: 59, 63, 66)
- `isinstance` (lines: 62)
- `domain.get_num_acts` (lines: 64)
- `ValueError` (lines: 69, 70)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 69, 70)

## Source

```python
def build_heur_nnet_par(domain: Domain, domain_name: str, nnet_name: str, nnet_kwargs: Dict[str, Any], heur_type: str) -> HeurNNetPar:
    """ Build a ``HeurNNetPar`` by pairing a registered heuristic network with
    an ``NNetInput`` the domain supports and the network accepts.

    Walks every ``NNetInput`` registered under ``domain_name`` and returns the
    first one that is simultaneously a subclass of the heuristic network's
    expected input type and of the input mixin required by ``heur_type``
    (``StateGoalIn`` for ``V``, ``StateGoalActFixIn`` for ``QFIX``,
    ``StateGoalActIn`` for ``QIN``).

    :param domain: The instantiated domain the network will run against.
    :param domain_name: Registration key of the domain.
    :param nnet_name: Registration key of the heuristic network (e.g.
        ``"resnet_fc"``).
    :param nnet_kwargs: Keyword arguments to pass to the network constructor.
    :param heur_type: One of ``"V"``, ``"QFIX"``, ``"QIN"``
        (case-insensitive). Selects the output shape.
    :return: A concrete ``HeurNNetPar`` (``HeurNNetParVConcrete``,
        ``HeurNNetParQFixOutConcrete``, or ``HeurNNetParQActInConcrete``).
    :raises ValueError: If ``heur_type`` is unrecognised, or if no compatible
        ``NNetInput`` is found for the given domain, heur type, and network.
    """
    nnet_input_t: Type[NNetInput] = heuristic_factory.get_type(nnet_name).nnet_input_type()
    nnet_input_domain_keys: List[Tuple[str, str]] = get_domain_nnet_input_keys(domain_name)

    for nnet_input_domain_key in nnet_input_domain_keys:
        nnet_input_cls: Type[NNetInput] = get_nnet_input_t(nnet_input_domain_key)
        if heur_type.upper() == "V":
            if issubclass(nnet_input_cls, StateGoalIn) and issubclass(nnet_input_cls, nnet_input_t):
                return HeurNNetParVConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs)
        elif heur_type.upper() == "QFIX":
            assert isinstance(domain, ActsEnumFixed)
            if issubclass(nnet_input_cls, StateGoalActFixIn) and issubclass(nnet_input_cls, nnet_input_t):
                return HeurNNetParQFixOutConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs, domain.get_num_acts())
        elif heur_type.upper() == "QIN":
            if issubclass(nnet_input_cls, StateGoalActIn) and issubclass(nnet_input_cls, nnet_input_t):
                return HeurNNetParQActInConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs)
        else:
            raise ValueError(f"Unknown heur type {heur_type}")
    raise ValueError(f"Cannot build heur nnet for domain: {domain_name}, heur type {heur_type}, and "
                     f"nnet_input type {nnet_input_t}.\nNNet inputs checked: {nnet_input_domain_keys}")
```
