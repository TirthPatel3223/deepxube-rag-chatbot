---
id: "func:deepxube.utils.command_line_utils.get_pathfind_from_arg"
kind: "function"
name: "get_pathfind_from_arg"
qualified_name: "deepxube.utils.command_line_utils.get_pathfind_from_arg"
module: "deepxube.utils.command_line_utils"
file: "deepxube/utils/command_line_utils.py"
line_start: 96
line_end: 112
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain"
    annotation: "Domain"
    default: null
  - name: "functions"
    annotation: "Any"
    default: null
  - name: "pathfind"
    annotation: "str"
    default: null
returns: "Tuple[PathFind, str]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_name_args"
    expr: "get_name_args"
    call_sites: [108]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_kwargs"
    expr: "pathfinding_factory.get_kwargs"
    call_sites: [109]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.build_class"
    expr: "pathfinding_factory.build_class"
    call_sites: [112]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.command_line_utils.get_pathfind_from_arg`

**File:** [deepxube/utils/command_line_utils.py:96](../../../../deepxube/utils/command_line_utils.py#L96)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_pathfind_from_arg(domain: Domain, functions: Any, pathfind: str) -> Tuple[PathFind, str]
```

## Docstring

Resolve a ``--pathfind`` CLI argument into a constructed ``PathFind``.

Injects ``domain`` and ``functions`` into the pathfinder kwargs before
instantiation.

:param domain: Instantiated domain the pathfinder will run over.
:param functions: An ``FNs*`` dataclass (heuristic / policy bundle), or
    ``None`` for supervised pathfinders.
:param pathfind: CLI string, e.g. ``"graph_v.1B_1.0W"``.
:return: Tuple of (instantiated ``PathFind``, registration name).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `functions` | `Any` | — |
| `pathfind` | `str` | — |

## Returns

`Tuple[PathFind, str]`

## Calls

- `get_name_args` → `func:deepxube.utils.command_line_utils.get_name_args` (lines: 108)
- `pathfinding_factory.get_kwargs` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_kwargs` (lines: 109)
- `pathfinding_factory.build_class` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.build_class` (lines: 112)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_pathfind_from_arg(domain: Domain, functions: Any, pathfind: str) -> Tuple[PathFind, str]:
    """ Resolve a ``--pathfind`` CLI argument into a constructed ``PathFind``.

    Injects ``domain`` and ``functions`` into the pathfinder kwargs before
    instantiation.

    :param domain: Instantiated domain the pathfinder will run over.
    :param functions: An ``FNs*`` dataclass (heuristic / policy bundle), or
        ``None`` for supervised pathfinders.
    :param pathfind: CLI string, e.g. ``"graph_v.1B_1.0W"``.
    :return: Tuple of (instantiated ``PathFind``, registration name).
    """
    pathfind_name, args_str = get_name_args(pathfind)
    pathfind_kwargs: Dict[str, Any] = pathfinding_factory.get_kwargs(pathfind_name, args_str)
    pathfind_kwargs["domain"] = domain
    pathfind_kwargs["functions"] = functions
    return pathfinding_factory.build_class(pathfind_name, pathfind_kwargs), pathfind_name
```
