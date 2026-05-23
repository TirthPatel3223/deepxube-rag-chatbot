---
id: "func:deepxube.base.factory.Factory.register_class"
kind: "method"
name: "register_class"
qualified_name: "deepxube.base.factory.Factory.register_class"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 77
line_end: 90
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
returns: "Callable[[Type[T]], Type[T]]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._class_registry.keys"
    call_sites: [86]
  - target: null
    expr: "ValueError"
    call_sites: [87]
  - target: null
    expr: "self._class_type_str.capitalize"
    call_sites: [87]
raises:
  - exception: "ValueError"
    call_sites: [87]
reads_attrs:
  - "self._class_registry"
  - "self._class_type_str"
writes_attrs: []
---

# `deepxube.base.factory.Factory.register_class`

**File:** [deepxube/base/factory.py:77](../../../../deepxube/base/factory.py#L77)
**Class:** `Factory`
**Visibility:** public
**Kind:** method

## Signature

```python
def register_class(self, name: str) -> Callable[[Type[T]], Type[T]]
```

## Docstring

Return a decorator that registers a class under ``name``.

:param name: Unique string key under which to register the class.
    Registering the same name twice raises ``ValueError``.
:return: A decorator that records the class in this factory's class
    registry and returns the class unchanged.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `name` | `str` | — |

## Returns

`Callable[[Type[T]], Type[T]]`

## Calls

*(No resolved calls.)*

### Unresolved
- `self._class_registry.keys` (lines: 86)
- `ValueError` (lines: 87)
- `self._class_type_str.capitalize` (lines: 87)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 87)

## Attribute access

**Reads:**
- `self._class_registry`
- `self._class_type_str`

## Source

```python
    def register_class(self, name: str) -> Callable[[Type[T]], Type[T]]:
        """ Return a decorator that registers a class under ``name``.

        :param name: Unique string key under which to register the class.
            Registering the same name twice raises ``ValueError``.
        :return: A decorator that records the class in this factory's class
            registry and returns the class unchanged.
        """
        def deco(cls: Type[T]) -> Type[T]:
            if name in self._class_registry.keys():
                raise ValueError(f"{self._class_type_str.capitalize()} {name!r} already registered")
            self._class_registry[name] = cls
            return cls
        return deco
```
