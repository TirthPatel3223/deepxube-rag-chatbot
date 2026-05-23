---
id: "func:deepxube.base.factory.Factory.build_class"
kind: "method"
name: "build_class"
qualified_name: "deepxube.base.factory.Factory.build_class"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 163
line_end: 172
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
  - name: "kwargs"
    annotation: "Dict[str, Any]"
    default: null
returns: "T"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.factory.Factory.get_type"
    expr: "self.get_type"
    call_sites: [171]
  - target: "func:deepxube.base.factory.cls"
    expr: "cls"
    call_sites: [172]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.factory.Factory.build_class`

**File:** [deepxube/base/factory.py:163](../../../../deepxube/base/factory.py#L163)
**Class:** `Factory`
**Visibility:** public
**Kind:** method

## Signature

```python
def build_class(self, name: str, kwargs: Dict[str, Any]) -> T
```

## Docstring

Look up the class registered under ``name`` and instantiate it.

:param name: The registered class name.
:param kwargs: Keyword arguments to pass to the class constructor,
    typically produced by ``get_kwargs``.
:return: A newly-constructed instance of the registered class.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `name` | `str` | — |
| `kwargs` | `Dict[str, Any]` | — |

## Returns

`T`

## Calls

- `self.get_type` → `func:deepxube.base.factory.Factory.get_type` (lines: 171)
- `cls` → `func:deepxube.base.factory.cls` (lines: 172)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def build_class(self, name: str, kwargs: Dict[str, Any]) -> T:
        """ Look up the class registered under ``name`` and instantiate it.

        :param name: The registered class name.
        :param kwargs: Keyword arguments to pass to the class constructor,
            typically produced by ``get_kwargs``.
        :return: A newly-constructed instance of the registered class.
        """
        cls: Type[T] = self.get_type(name)
        return cls(**kwargs)
```
