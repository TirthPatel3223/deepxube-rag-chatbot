---
id: "func:deepxube.base.updater.Update.get_pathfind"
kind: "method"
name: "get_pathfind"
qualified_name: "deepxube.base.updater.Update.get_pathfind"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 363
line_end: 368
class: "Update"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "P"
docstring_source: "present"
callees:
  - target: null
    expr: "self.pathfind_kwargs.copy"
    call_sites: [365]
  - target: "func:deepxube.base.updater.Update._get_pathfind_functions"
    expr: "self._get_pathfind_functions"
    call_sites: [367]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [368]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.build_class"
    expr: "pathfinding_factory.build_class"
    call_sites: [368]
raises: []
reads_attrs:
  - "self.domain"
  - "self.pathfind_kwargs"
  - "self.pathfind_name"
writes_attrs: []
---

# `deepxube.base.updater.Update.get_pathfind`

**File:** [deepxube/base/updater.py:363](../../../../deepxube/base/updater.py#L363)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_pathfind(self) -> P
```

## Docstring

Build a fresh pathfinder with this updater's domain and current function bundle. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`P`

## Calls

- `self._get_pathfind_functions` → `func:deepxube.base.updater.Update._get_pathfind_functions` (lines: 367)
- `cast` → `func:typing.cast` (lines: 368)
- `pathfinding_factory.build_class` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.build_class` (lines: 368)

### Unresolved
- `self.pathfind_kwargs.copy` (lines: 365)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.pathfind_kwargs`
- `self.pathfind_name`

## Source

```python
    def get_pathfind(self) -> P:
        """ Build a fresh pathfinder with this updater's domain and current function bundle. """
        pathfind_kwargs: Dict[str, Any] = self.pathfind_kwargs.copy()
        pathfind_kwargs["domain"] = self.domain
        pathfind_kwargs["functions"] = self._get_pathfind_functions()
        return cast(P, pathfinding_factory.build_class(self.pathfind_name, pathfind_kwargs))
```
