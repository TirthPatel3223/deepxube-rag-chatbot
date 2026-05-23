---
id: "func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg"
kind: "function"
name: "get_heur_nnet_par_from_arg"
qualified_name: "deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg"
module: "deepxube.utils.command_line_utils"
file: "deepxube/utils/command_line_utils.py"
line_start: 49
line_end: 63
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
  - name: "heur"
    annotation: "str"
    default: null
  - name: "heur_type"
    annotation: "str"
    default: null
returns: "Tuple[HeurNNetPar, str]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_name_args"
    expr: "get_name_args"
    call_sites: [59]
  - target: "func:deepxube.factories.heuristic_factory.heuristic_factory.get_type"
    expr: "heuristic_factory.get_type"
    call_sites: [60]
  - target: "func:deepxube.factories.heuristic_factory.heuristic_factory.get_kwargs"
    expr: "heuristic_factory.get_kwargs"
    call_sites: [61]
  - target: "func:deepxube.factories.heuristic_factory.build_heur_nnet_par"
    expr: "build_heur_nnet_par"
    call_sites: [62]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg`

**File:** [deepxube/utils/command_line_utils.py:49](../../../../deepxube/utils/command_line_utils.py#L49)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_heur_nnet_par_from_arg(domain: Domain, domain_name: str, heur: str, heur_type: str) -> Tuple[HeurNNetPar, str]
```

## Docstring

Resolve a ``--heur`` / ``--heur_type`` CLI argument pair into a
``HeurNNetPar`` for the given domain.

:param domain: Instantiated domain the network will run on.
:param domain_name: Domain registration key.
:param heur: CLI string for the network, e.g. ``"resnet_fc.100H_2B_bn"``.
:param heur_type: One of ``"V"``, ``"QFIX"``, ``"QIN"`` (case-insensitive).
:return: Tuple of (``HeurNNetPar``, network registration name).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `domain_name` | `str` | — |
| `heur` | `str` | — |
| `heur_type` | `str` | — |

## Returns

`Tuple[HeurNNetPar, str]`

## Calls

- `get_name_args` → `func:deepxube.utils.command_line_utils.get_name_args` (lines: 59)
- `heuristic_factory.get_type` → `func:deepxube.factories.heuristic_factory.heuristic_factory.get_type` (lines: 60)
- `heuristic_factory.get_kwargs` → `func:deepxube.factories.heuristic_factory.heuristic_factory.get_kwargs` (lines: 61)
- `build_heur_nnet_par` → `func:deepxube.factories.heuristic_factory.build_heur_nnet_par` (lines: 62)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_heur_nnet_par_from_arg(domain: Domain, domain_name: str, heur: str, heur_type: str) -> Tuple[HeurNNetPar, str]:
    """ Resolve a ``--heur`` / ``--heur_type`` CLI argument pair into a
    ``HeurNNetPar`` for the given domain.

    :param domain: Instantiated domain the network will run on.
    :param domain_name: Domain registration key.
    :param heur: CLI string for the network, e.g. ``"resnet_fc.100H_2B_bn"``.
    :param heur_type: One of ``"V"``, ``"QFIX"``, ``"QIN"`` (case-insensitive).
    :return: Tuple of (``HeurNNetPar``, network registration name).
    """
    nnet_name, nnet_args = get_name_args(heur)
    heuristic_factory.get_type(nnet_name)  # to ensure existence
    nnet_kwargs: Dict[str, Any] = heuristic_factory.get_kwargs(nnet_name, nnet_args)
    nnet_par: HeurNNetPar = build_heur_nnet_par(domain, domain_name, nnet_name, nnet_kwargs, heur_type)
    return nnet_par, nnet_name
```
