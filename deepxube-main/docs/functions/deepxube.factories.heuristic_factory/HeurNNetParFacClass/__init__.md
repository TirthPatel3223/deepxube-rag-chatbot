---
id: "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParFacClass.__init__"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 108
line_end: 128
class: "HeurNNetParFacClass"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "domain"
    annotation: "Domain"
    default: null
  - name: "nnet_input_name"
    annotation: "Tuple[str, str]"
    default: null
  - name: "nnet_name"
    annotation: "str"
    default: null
  - name: "nnet_kwargs"
    annotation: "Dict[str, Any]"
    default: null
  - name: "q_fix"
    annotation: "bool"
    default: null
  - name: "out_dim"
    annotation: "int"
    default: null
returns: null
docstring_source: "present"
callees: []
raises: []
reads_attrs:
  - "self.domain"
  - "self.nnet_input"
  - "self.nnet_input_name"
  - "self.nnet_kwargs"
  - "self.nnet_name"
  - "self.out_dim"
  - "self.q_fix"
writes_attrs:
  - "self.domain"
  - "self.nnet_input"
  - "self.nnet_input_name"
  - "self.nnet_kwargs"
  - "self.nnet_name"
  - "self.out_dim"
  - "self.q_fix"
---

# `deepxube.factories.heuristic_factory.HeurNNetParFacClass.__init__`

**File:** [deepxube/factories/heuristic_factory.py:108](../../../../deepxube/factories/heuristic_factory.py#L108)
**Class:** `HeurNNetParFacClass`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], q_fix: bool, out_dim: int)
```

## Docstring

Store the domain, input key, and network parameters for later
lazy construction.

:param domain: The domain the input and network operate on.
:param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
    the nnet-input registry.
:param nnet_name: Registration key of the heuristic network.
:param nnet_kwargs: Keyword arguments for the network constructor.
:param q_fix: ``True`` for a fixed-output-dim Q-network
    (one output per action).
:param out_dim: Number of heuristic outputs (1 for V, ``num_acts``
    for fixed Q).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `domain` | `Domain` | — |
| `nnet_input_name` | `Tuple[str, str]` | — |
| `nnet_name` | `str` | — |
| `nnet_kwargs` | `Dict[str, Any]` | — |
| `q_fix` | `bool` | — |
| `out_dim` | `int` | — |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.domain`
- `self.nnet_input`
- `self.nnet_input_name`
- `self.nnet_kwargs`
- `self.nnet_name`
- `self.out_dim`
- `self.q_fix`

**Reads:**
- `self.domain`
- `self.nnet_input`
- `self.nnet_input_name`
- `self.nnet_kwargs`
- `self.nnet_name`
- `self.out_dim`
- `self.q_fix`

## Source

```python
    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], q_fix: bool, out_dim: int):
        """ Store the domain, input key, and network parameters for later
        lazy construction.

        :param domain: The domain the input and network operate on.
        :param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
            the nnet-input registry.
        :param nnet_name: Registration key of the heuristic network.
        :param nnet_kwargs: Keyword arguments for the network constructor.
        :param q_fix: ``True`` for a fixed-output-dim Q-network
            (one output per action).
        :param out_dim: Number of heuristic outputs (1 for V, ``num_acts``
            for fixed Q).
        """
        self.domain: Domain = domain
        self.nnet_input_name: Tuple[str, str] = nnet_input_name
        self.nnet_input: Optional[NNetInput] = None
        self.nnet_name: str = nnet_name
        self.nnet_kwargs: Dict[str, Any] = nnet_kwargs
        self.q_fix: bool = q_fix
        self.out_dim: int = out_dim
```
