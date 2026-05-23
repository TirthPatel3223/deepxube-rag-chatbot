---
id: "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParFacClass.__init__"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 170
line_end: 187
class: "PolicyNNetParFacClass"
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
  - name: "num_samp"
    annotation: "int"
    default: null
  - name: "num_rand"
    annotation: "int"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [182]
  - target: null
    expr: "super"
    call_sites: [182]
raises: []
reads_attrs:
  - "self.domain"
  - "self.nnet_input"
  - "self.nnet_input_name"
  - "self.nnet_kwargs"
  - "self.nnet_name"
writes_attrs:
  - "self.domain"
  - "self.nnet_input"
  - "self.nnet_input_name"
  - "self.nnet_kwargs"
  - "self.nnet_name"
---

# `deepxube.factories.heuristic_factory.PolicyNNetParFacClass.__init__`

**File:** [deepxube/factories/heuristic_factory.py:170](../../../../deepxube/factories/heuristic_factory.py#L170)
**Class:** `PolicyNNetParFacClass`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], num_samp: int, num_rand: int)
```

## Docstring

Store the domain, input key, and network parameters for later
lazy construction.

:param domain: The domain the policy operates on.
:param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
    the nnet-input registry; must resolve to a ``PolicyNNetIn``.
:param nnet_name: Registration key of the policy network.
:param nnet_kwargs: Keyword arguments for the network constructor.
:param num_samp: Number of sampled actions per state for training.
:param num_rand: Number of random actions mixed in.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `domain` | `Domain` | — |
| `nnet_input_name` | `Tuple[str, str]` | — |
| `nnet_name` | `str` | — |
| `nnet_kwargs` | `Dict[str, Any]` | — |
| `num_samp` | `int` | — |
| `num_rand` | `int` | — |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

### Unresolved
- `super().__init__` (lines: 182)
- `super` (lines: 182)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.domain`
- `self.nnet_input`
- `self.nnet_input_name`
- `self.nnet_kwargs`
- `self.nnet_name`

**Reads:**
- `self.domain`
- `self.nnet_input`
- `self.nnet_input_name`
- `self.nnet_kwargs`
- `self.nnet_name`

## Source

```python
    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], num_samp: int, num_rand: int):
        """ Store the domain, input key, and network parameters for later
        lazy construction.

        :param domain: The domain the policy operates on.
        :param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
            the nnet-input registry; must resolve to a ``PolicyNNetIn``.
        :param nnet_name: Registration key of the policy network.
        :param nnet_kwargs: Keyword arguments for the network constructor.
        :param num_samp: Number of sampled actions per state for training.
        :param num_rand: Number of random actions mixed in.
        """
        super().__init__(num_samp, num_rand)
        self.domain: Domain = domain
        self.nnet_input_name: Tuple[str, str] = nnet_input_name
        self.nnet_input: Optional[PolicyNNetIn] = None
        self.nnet_name: str = nnet_name
        self.nnet_kwargs: Dict[str, Any] = nnet_kwargs
```
