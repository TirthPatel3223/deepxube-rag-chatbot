---
id: "func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs"
kind: "function"
name: "get_pathfind_name_kwargs"
qualified_name: "deepxube.utils.command_line_utils.get_pathfind_name_kwargs"
module: "deepxube.utils.command_line_utils"
file: "deepxube/utils/command_line_utils.py"
line_start: 84
line_end: 93
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "pathfind"
    annotation: "str"
    default: null
returns: "Tuple[str, Dict[str, Any]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_name_args"
    expr: "get_name_args"
    call_sites: [91]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_kwargs"
    expr: "pathfinding_factory.get_kwargs"
    call_sites: [92]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.command_line_utils.get_pathfind_name_kwargs`

**File:** [deepxube/utils/command_line_utils.py:84](../../../../deepxube/utils/command_line_utils.py#L84)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_pathfind_name_kwargs(pathfind: str) -> Tuple[str, Dict[str, Any]]
```

## Docstring

Resolve a ``--pathfind`` CLI argument into its registration name and
constructor kwargs, without instantiating it.

:param pathfind: CLI string, e.g. ``"graph_v.1B_1.0W"``.
:return: Tuple of (pathfinder registration name, constructor kwargs).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `pathfind` | `str` | — |

## Returns

`Tuple[str, Dict[str, Any]]`

## Calls

- `get_name_args` → `func:deepxube.utils.command_line_utils.get_name_args` (lines: 91)
- `pathfinding_factory.get_kwargs` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_kwargs` (lines: 92)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_pathfind_name_kwargs(pathfind: str) -> Tuple[str, Dict[str, Any]]:
    """ Resolve a ``--pathfind`` CLI argument into its registration name and
    constructor kwargs, without instantiating it.

    :param pathfind: CLI string, e.g. ``"graph_v.1B_1.0W"``.
    :return: Tuple of (pathfinder registration name, constructor kwargs).
    """
    name, args_str = get_name_args(pathfind)
    pathfind_kwargs: Dict[str, Any] = pathfinding_factory.get_kwargs(name, args_str)
    return name, pathfind_kwargs
```
