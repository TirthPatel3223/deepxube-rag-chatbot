---
id: "func:deepxube.factories.updater_factory.get_updater"
kind: "function"
name: "get_updater"
qualified_name: "deepxube.factories.updater_factory.get_updater"
module: "deepxube.factories.updater_factory"
file: "deepxube/factories/updater_factory.py"
line_start: 22
line_end: 63
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
  - name: "pathfind_arg"
    annotation: "str"
    default: null
  - name: "up_args"
    annotation: "UpArgs"
    default: null
  - name: "her"
    annotation: "bool"
    default: null
  - name: "func_update"
    annotation: "str"
    default: null
returns: "Update"
docstring_source: "present"
callees:
  - target: "func:deepxube.factories.updater_factory.get_all_class_names"
    expr: "updater_factory.get_all_class_names"
    call_sites: [41]
  - target: "func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs"
    expr: "get_pathfind_name_kwargs"
    call_sites: [42]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_type"
    expr: "pathfinding_factory.get_type"
    call_sites: [43]
  - target: null
    expr: "isinstance"
    call_sites: [45]
  - target: null
    expr: "updater_factory.get_type(up_cls_name).domain_type"
    call_sites: [45]
  - target: "func:deepxube.factories.updater_factory.get_type"
    expr: "updater_factory.get_type"
    call_sites: [45, 46, 47, 48, 51, 53, 62]
  - target: null
    expr: "issubclass"
    call_sites: [46, 47, 51, 53]
  - target: null
    expr: "updater_factory.get_type(up_cls_name).pathfind_type"
    call_sites: [46]
  - target: null
    expr: "updater_factory.get_type(up_cls_name).functions_type"
    call_sites: [48]
  - target: null
    expr: "pathfind_t.functions_type"
    call_sites: [48]
  - target: null
    expr: "func_update.upper"
    call_sites: [50, 52]
  - target: null
    expr: "ValueError"
    call_sites: [55, 58, 60]
  - target: null
    expr: "len"
    call_sites: [57, 59]
  - target: "func:deepxube.factories.updater_factory.up_cls"
    expr: "up_cls"
    call_sites: [63]
raises:
  - exception: "ValueError"
    call_sites: [55, 58, 60]
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.updater_factory.get_updater`

**File:** [deepxube/factories/updater_factory.py:22](../../../../deepxube/factories/updater_factory.py#L22)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_updater(domain: Domain, pathfind_arg: str, up_args: UpArgs, her: bool, func_update: str) -> Update
```

## Docstring

Resolve and instantiate the unique ``Update`` that matches the inputs.

Filters the updater registry by (1) domain type compatibility via
``isinstance``, (2) pathfinding type compatibility via ``issubclass``,
(3) whether the updater uses Hindsight Experience Replay, (4) matching
pathfinding ``functions_type``, and (5) whether ``func_update`` asks for
a heuristic or policy updater. Exactly one updater must match.

:param domain: The domain instance being trained on.
:param pathfind_arg: CLI pathfinding argument, e.g. ``"graph_v.1B_1.0W"``.
:param up_args: Shared updater arguments used by all subclasses.
:param her: ``True`` to select a Hindsight-Experience-Replay variant.
:param func_update: Either ``"HEUR"`` or ``"POLICY"`` (case-insensitive).
:return: A freshly-constructed ``Update`` instance.
:raises ValueError: If ``func_update`` is neither ``"HEUR"`` nor
    ``"POLICY"``, if zero updaters match the filter tuple, or if more
    than one matches.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `pathfind_arg` | `str` | — |
| `up_args` | `UpArgs` | — |
| `her` | `bool` | — |
| `func_update` | `str` | — |

## Returns

`Update`

## Calls

- `updater_factory.get_all_class_names` → `func:deepxube.factories.updater_factory.get_all_class_names` (lines: 41)
- `get_pathfind_name_kwargs` → `func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs` (lines: 42)
- `pathfinding_factory.get_type` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_type` (lines: 43)
- `updater_factory.get_type` → `func:deepxube.factories.updater_factory.get_type` (lines: 45, 46, 47, 48, 51, 53, 62)
- `up_cls` → `func:deepxube.factories.updater_factory.up_cls` (lines: 63)

### Unresolved
- `isinstance` (lines: 45)
- `updater_factory.get_type(up_cls_name).domain_type` (lines: 45)
- `issubclass` (lines: 46, 47, 51, 53)
- `updater_factory.get_type(up_cls_name).pathfind_type` (lines: 46)
- `updater_factory.get_type(up_cls_name).functions_type` (lines: 48)
- `pathfind_t.functions_type` (lines: 48)
- `func_update.upper` (lines: 50, 52)
- `ValueError` (lines: 55, 58, 60)
- `len` (lines: 57, 59)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 55, 58, 60)

## Source

```python
def get_updater(domain: Domain, pathfind_arg: str, up_args: UpArgs, her: bool, func_update: str) -> Update:
    """ Resolve and instantiate the unique ``Update`` that matches the inputs.

    Filters the updater registry by (1) domain type compatibility via
    ``isinstance``, (2) pathfinding type compatibility via ``issubclass``,
    (3) whether the updater uses Hindsight Experience Replay, (4) matching
    pathfinding ``functions_type``, and (5) whether ``func_update`` asks for
    a heuristic or policy updater. Exactly one updater must match.

    :param domain: The domain instance being trained on.
    :param pathfind_arg: CLI pathfinding argument, e.g. ``"graph_v.1B_1.0W"``.
    :param up_args: Shared updater arguments used by all subclasses.
    :param her: ``True`` to select a Hindsight-Experience-Replay variant.
    :param func_update: Either ``"HEUR"`` or ``"POLICY"`` (case-insensitive).
    :return: A freshly-constructed ``Update`` instance.
    :raises ValueError: If ``func_update`` is neither ``"HEUR"`` nor
        ``"POLICY"``, if zero updaters match the filter tuple, or if more
        than one matches.
    """
    up_cls_names: List[str] = updater_factory.get_all_class_names()
    pathfind_name: str = get_pathfind_name_kwargs(pathfind_arg)[0]
    pathfind_t: Type[PathFind] = pathfinding_factory.get_type(pathfind_name)

    up_cls_names = [up_cls_name for up_cls_name in up_cls_names if isinstance(domain, updater_factory.get_type(up_cls_name).domain_type())]
    up_cls_names = [up_cls_name for up_cls_name in up_cls_names if issubclass(pathfind_t, updater_factory.get_type(up_cls_name).pathfind_type())]
    up_cls_names = [up_cls_name for up_cls_name in up_cls_names if issubclass(updater_factory.get_type(up_cls_name), UpdateHER) == her]
    up_cls_names = [up_cls_name for up_cls_name in up_cls_names if updater_factory.get_type(up_cls_name).functions_type() is pathfind_t.functions_type()]

    if func_update.upper() == "HEUR":
        up_cls_names = [up_cls_name for up_cls_name in up_cls_names if issubclass(updater_factory.get_type(up_cls_name), UpdateHeur)]
    elif func_update.upper() == "POLICY":
        up_cls_names = [up_cls_name for up_cls_name in up_cls_names if issubclass(updater_factory.get_type(up_cls_name), UpdatePolicy)]
    else:
        raise ValueError(f"Unknown func to update {func_update}")

    if len(up_cls_names) == 0:
        raise ValueError(f"No updaters for Domain: {domain}, PathFind: {pathfind_t}, HER: {her}, Update func: {func_update}")
    if len(up_cls_names) > 1:
        raise ValueError(f"More than one updater option: {up_cls_names} for Domain: {domain}, PathFind: {pathfind_t}, HER: {her}, Update func: {func_update}")

    up_cls: Type[Update] = updater_factory.get_type(up_cls_names[0])
    return up_cls(domain, pathfind_arg, up_args)
```
