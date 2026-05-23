---
id: "func:deepxube.base.factory.Factory.get_parser"
kind: "method"
name: "get_parser"
qualified_name: "deepxube.base.factory.Factory.get_parser"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 110
line_end: 121
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
returns: "Optional[Parser]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._parser_registry.get"
    call_sites: [117]
  - target: "func:deepxube.base.factory.cls_parser"
    expr: "cls_parser"
    call_sites: [119]
raises: []
reads_attrs:
  - "self._parser_registry"
writes_attrs: []
---

# `deepxube.base.factory.Factory.get_parser`

**File:** [deepxube/base/factory.py:110](../../../../deepxube/base/factory.py#L110)
**Class:** `Factory`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_parser(self, name: str) -> Optional[Parser]
```

## Docstring

Return a fresh instance of the ``Parser`` registered under ``name``.

:param name: The registered class name.
:return: A new ``Parser`` instance, or ``None`` if no parser is
    registered for that name.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `name` | `str` | — |

## Returns

`Optional[Parser]`

## Calls

- `cls_parser` → `func:deepxube.base.factory.cls_parser` (lines: 119)

### Unresolved
- `self._parser_registry.get` (lines: 117)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self._parser_registry`

## Source

```python
    def get_parser(self, name: str) -> Optional[Parser]:
        """ Return a fresh instance of the ``Parser`` registered under ``name``.

        :param name: The registered class name.
        :return: A new ``Parser`` instance, or ``None`` if no parser is
            registered for that name.
        """
        cls_parser: Optional[Type[Parser]] = self._parser_registry.get(name)
        if cls_parser is not None:
            return cls_parser()
        else:
            return None
```
