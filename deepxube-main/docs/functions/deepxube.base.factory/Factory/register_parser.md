---
id: "func:deepxube.base.factory.Factory.register_parser"
kind: "method"
name: "register_parser"
qualified_name: "deepxube.base.factory.Factory.register_parser"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 92
line_end: 108
class: "Factory"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "name"
    annotation: "str"
    default: null
returns: "Callable[[Type[Parser]], Type[Parser]]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._parser_registry.keys"
    call_sites: [104]
  - target: null
    expr: "ValueError"
    call_sites: [105]
  - target: null
    expr: "self._class_type_str.capitalize"
    call_sites: [105]
raises:
  - exception: "ValueError"
    call_sites: [105]
reads_attrs:
  - "self._class_type_str"
  - "self._parser_registry"
writes_attrs: []
---

# `deepxube.base.factory.Factory.register_parser`

**File:** [deepxube/base/factory.py:92](../../../../deepxube/base/factory.py#L92)
**Class:** `Factory`
**Visibility:** public
**Kind:** method

## Signature

```python
def register_parser(self, name: str) -> Callable[[Type[Parser]], Type[Parser]]
```

## Docstring

Return a decorator that registers a ``Parser`` subclass under ``name``.

The ``name`` must match the name used when registering the corresponding
class, so ``get_kwargs`` can find both in tandem.

:param name: Unique string key matching a registered class.
    Registering the same name twice raises ``ValueError``.
:return: A decorator that records the parser in this factory's parser
    registry and returns the parser class unchanged.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `name` | `str` | — |

## Returns

`Callable[[Type[Parser]], Type[Parser]]`

## Calls

*(No resolved calls.)*

### Unresolved
- `self._parser_registry.keys` (lines: 104)
- `ValueError` (lines: 105)
- `self._class_type_str.capitalize` (lines: 105)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 105)

## Attribute access

**Reads:**
- `self._class_type_str`
- `self._parser_registry`

## Source

```python
    def register_parser(self, name: str) -> Callable[[Type[Parser]], Type[Parser]]:
        """ Return a decorator that registers a ``Parser`` subclass under ``name``.

        The ``name`` must match the name used when registering the corresponding
        class, so ``get_kwargs`` can find both in tandem.

        :param name: Unique string key matching a registered class.
            Registering the same name twice raises ``ValueError``.
        :return: A decorator that records the parser in this factory's parser
            registry and returns the parser class unchanged.
        """
        def deco(cls: Type[Parser]) -> Type[Parser]:
            if name in self._parser_registry.keys():
                raise ValueError(f"{self._class_type_str.capitalize()} parser {name!r} already registered")
            self._parser_registry[name] = cls
            return cls
        return deco
```
