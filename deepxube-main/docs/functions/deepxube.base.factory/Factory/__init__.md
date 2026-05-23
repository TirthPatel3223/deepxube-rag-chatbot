---
id: "func:deepxube.base.factory.Factory.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.factory.Factory.__init__"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 20
line_end: 23
class: "Factory"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "class_type_str"
    annotation: "str"
    default: null
returns: null
docstring_source: "missing"
callees:
  - target: "func:deepxube.base.factory.dict"
    expr: "dict"
    call_sites: [21, 22]
raises: []
reads_attrs:
  - "self._class_registry"
  - "self._class_type_str"
  - "self._parser_registry"
writes_attrs:
  - "self._class_registry"
  - "self._class_type_str"
  - "self._parser_registry"
---

# `deepxube.base.factory.Factory.__init__`

**File:** [deepxube/base/factory.py:20](../../../../deepxube/base/factory.py#L20)
**Class:** `Factory`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, class_type_str: str)
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `class_type_str` | `str` | — |

## Returns

*(Not annotated.)*

## Calls

- `dict` → `func:deepxube.base.factory.dict` (lines: 21, 22)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._class_registry`
- `self._class_type_str`
- `self._parser_registry`

**Reads:**
- `self._class_registry`
- `self._class_type_str`
- `self._parser_registry`

## Source

```python
    def __init__(self, class_type_str: str):
        self._class_registry: Dict[str, Type[T]] = dict()
        self._parser_registry: Dict[str, Type[Parser]] = dict()
        self._class_type_str: str = class_type_str
```
