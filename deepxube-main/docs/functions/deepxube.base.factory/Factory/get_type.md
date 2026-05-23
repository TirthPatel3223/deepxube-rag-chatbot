---
id: "func:deepxube.base.factory.Factory.get_type"
kind: "method"
name: "get_type"
qualified_name: "deepxube.base.factory.Factory.get_type"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 150
line_end: 161
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
returns: "Type[T]"
docstring_source: "present"
callees:
  - target: null
    expr: "ValueError"
    call_sites: [161]
  - target: null
    expr: "sorted"
    call_sites: [161]
raises:
  - exception: "ValueError"
    call_sites: [161]
reads_attrs:
  - "self._class_registry"
  - "self._class_type_str"
writes_attrs: []
---

# `deepxube.base.factory.Factory.get_type`

**File:** [deepxube/base/factory.py:150](../../../../deepxube/base/factory.py#L150)
**Class:** `Factory`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_type(self, name: str) -> Type[T]
```

## Docstring

Return the class registered under ``name``.

:param name: The registered class name.
:return: The concrete class type.
:raises ValueError: If no class is registered under ``name``; the error
    message lists the available names.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `name` | `str` | — |

## Returns

`Type[T]`

## Calls

*(No resolved calls.)*

### Unresolved
- `ValueError` (lines: 161)
- `sorted` (lines: 161)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 161)

## Attribute access

**Reads:**
- `self._class_registry`
- `self._class_type_str`

## Source

```python
    def get_type(self, name: str) -> Type[T]:
        """ Return the class registered under ``name``.

        :param name: The registered class name.
        :return: The concrete class type.
        :raises ValueError: If no class is registered under ``name``; the error
            message lists the available names.
        """
        try:
            return self._class_registry[name]
        except KeyError:
            raise ValueError(f"Unknown {self._class_type_str} {name!r}. Available: {sorted(self._class_registry)}")
```
