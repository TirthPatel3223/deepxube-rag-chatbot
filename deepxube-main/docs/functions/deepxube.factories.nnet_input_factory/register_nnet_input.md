---
id: "func:deepxube.factories.nnet_input_factory.register_nnet_input"
kind: "function"
name: "register_nnet_input"
qualified_name: "deepxube.factories.nnet_input_factory.register_nnet_input"
module: "deepxube.factories.nnet_input_factory"
file: "deepxube/factories/nnet_input_factory.py"
line_start: 20
line_end: 37
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain_name"
    annotation: "str"
    default: null
  - name: "nnet_input_name"
    annotation: "str"
    default: null
returns: "Callable[[Type[NNetInput]], Type[NNetInput]]"
docstring_source: "present"
callees:
  - target: null
    expr: "_nnet_input_registry.keys"
    call_sites: [33]
  - target: null
    expr: "ValueError"
    call_sites: [34]
raises:
  - exception: "ValueError"
    call_sites: [34]
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.nnet_input_factory.register_nnet_input`

**File:** [deepxube/factories/nnet_input_factory.py:20](../../../../deepxube/factories/nnet_input_factory.py#L20)
**Visibility:** public
**Kind:** function

## Signature

```python
def register_nnet_input(domain_name: str, nnet_input_name: str) -> Callable[[Type[NNetInput]], Type[NNetInput]]
```

## Docstring

Return a decorator that registers an ``NNetInput`` class under the
``(domain_name, nnet_input_name)`` pair.

:param domain_name: Registration key of the domain this input belongs to.
:param nnet_input_name: Short name identifying the input shape (e.g.
    ``"flat_sg"`` for flat state/goal inputs).
:return: A decorator that records the class in the registry and returns it
    unchanged.
:raises ValueError: If the key is already registered (via the decorator).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain_name` | `str` | — |
| `nnet_input_name` | `str` | — |

## Returns

`Callable[[Type[NNetInput]], Type[NNetInput]]`

## Calls

*(No resolved calls.)*

### Unresolved
- `_nnet_input_registry.keys` (lines: 33)
- `ValueError` (lines: 34)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 34)

## Source

```python
def register_nnet_input(domain_name: str, nnet_input_name: str) -> Callable[[Type[NNetInput]], Type[NNetInput]]:
    """ Return a decorator that registers an ``NNetInput`` class under the
    ``(domain_name, nnet_input_name)`` pair.

    :param domain_name: Registration key of the domain this input belongs to.
    :param nnet_input_name: Short name identifying the input shape (e.g.
        ``"flat_sg"`` for flat state/goal inputs).
    :return: A decorator that records the class in the registry and returns it
        unchanged.
    :raises ValueError: If the key is already registered (via the decorator).
    """
    def deco(cls: Type[NNetInput]) -> Type[NNetInput]:
        key: Tuple[str, str] = (domain_name, nnet_input_name)
        if key in _nnet_input_registry.keys():
            raise ValueError(f"{key!r} already registered for nnet inputs")
        _nnet_input_registry[key] = cls
        return cls
    return deco
```
