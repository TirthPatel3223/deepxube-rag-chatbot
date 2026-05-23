---
id: "func:deepxube.base.factory.Factory.get_all_class_names"
kind: "method"
name: "get_all_class_names"
qualified_name: "deepxube.base.factory.Factory.get_all_class_names"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 72
line_end: 73
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
returns: "List[str]"
docstring_source: "missing"
callees:
  - target: "func:deepxube.base.factory.list"
    expr: "list"
    call_sites: [73]
  - target: null
    expr: "self._class_registry.keys"
    call_sites: [73]
raises: []
reads_attrs:
  - "self._class_registry"
writes_attrs: []
---

# `deepxube.base.factory.Factory.get_all_class_names`

**File:** [deepxube/base/factory.py:72](../../../../deepxube/base/factory.py#L72)
**Class:** `Factory`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_all_class_names(self) -> List[str]
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`List[str]`

## Calls

- `list` → `func:deepxube.base.factory.list` (lines: 73)

### Unresolved
- `self._class_registry.keys` (lines: 73)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self._class_registry`

## Source

```python
    def get_all_class_names(self) -> List[str]:
        return list(self._class_registry.keys())
```
