---
id: "func:deepxube.factories.pathfinding_factory.get_domain_compat_pathfind_names"
kind: "function"
name: "get_domain_compat_pathfind_names"
qualified_name: "deepxube.factories.pathfinding_factory.get_domain_compat_pathfind_names"
module: "deepxube.factories.pathfinding_factory"
file: "deepxube/factories/pathfinding_factory.py"
line_start: 65
line_end: 80
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain_t"
    annotation: "Type[Domain]"
    default: null
returns: "List[str]"
docstring_source: "present"
callees:
  - target: "func:deepxube.factories.pathfinding_factory.get_all_class_names"
    expr: "pathfinding_factory.get_all_class_names"
    call_sites: [75]
  - target: "func:deepxube.factories.pathfinding_factory.get_type"
    expr: "pathfinding_factory.get_type"
    call_sites: [76]
  - target: null
    expr: "issubclass"
    call_sites: [77]
  - target: null
    expr: "pathfind_t.domain_type"
    call_sites: [77]
  - target: null
    expr: "pathfind_names.append"
    call_sites: [78]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.pathfinding_factory.get_domain_compat_pathfind_names`

**File:** [deepxube/factories/pathfinding_factory.py:65](../../../../deepxube/factories/pathfinding_factory.py#L65)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_domain_compat_pathfind_names(domain_t: Type[Domain]) -> List[str]
```

## Docstring

Return the registered pathfinder names that accept ``domain_t``.

A pathfinder is compatible if ``domain_t`` is a subclass of the pathfinder's
declared ``domain_type()``.

:param domain_t: The concrete domain class to check compatibility for.
:return: List of pathfinder registration keys compatible with the domain.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain_t` | `Type[Domain]` | — |

## Returns

`List[str]`

## Calls

- `pathfinding_factory.get_all_class_names` → `func:deepxube.factories.pathfinding_factory.get_all_class_names` (lines: 75)
- `pathfinding_factory.get_type` → `func:deepxube.factories.pathfinding_factory.get_type` (lines: 76)

### Unresolved
- `issubclass` (lines: 77)
- `pathfind_t.domain_type` (lines: 77)
- `pathfind_names.append` (lines: 78)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_domain_compat_pathfind_names(domain_t: Type[Domain]) -> List[str]:
    """ Return the registered pathfinder names that accept ``domain_t``.

    A pathfinder is compatible if ``domain_t`` is a subclass of the pathfinder's
    declared ``domain_type()``.

    :param domain_t: The concrete domain class to check compatibility for.
    :return: List of pathfinder registration keys compatible with the domain.
    """
    pathfind_names: List[str] = []
    for pathfind_name in pathfinding_factory.get_all_class_names():
        pathfind_t: Type[PathFind] = pathfinding_factory.get_type(pathfind_name)
        if issubclass(domain_t, pathfind_t.domain_type()):
            pathfind_names.append(pathfind_name)

    return pathfind_names
```
