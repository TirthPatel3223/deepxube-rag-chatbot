---
id: "func:deepxube.utils.command_line_utils.get_name_args"
kind: "function"
name: "get_name_args"
qualified_name: "deepxube.utils.command_line_utils.get_name_args"
module: "deepxube.utils.command_line_utils"
file: "deepxube/utils/command_line_utils.py"
line_start: 21
line_end: 35
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "name_args"
    annotation: "str"
    default: null
returns: "Tuple[str, Optional[str]]"
docstring_source: "present"
callees:
  - target: null
    expr: "name_args.split"
    call_sites: [27]
  - target: null
    expr: "len"
    call_sites: [30, 33]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.command_line_utils.get_name_args`

**File:** [deepxube/utils/command_line_utils.py:21](../../../../deepxube/utils/command_line_utils.py#L21)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_name_args(name_args: str) -> Tuple[str, Optional[str]]
```

## Docstring

Split a CLI argument of the form ``<name>[.<args>]`` at the first dot.

:param name_args: Raw CLI argument, e.g. ``"grid.7"`` or ``"grid"``.
:return: ``(name, args)``; ``args`` is ``None`` if no dot is present.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `name_args` | `str` | — |

## Returns

`Tuple[str, Optional[str]]`

## Calls

*(No resolved calls.)*

### Unresolved
- `name_args.split` (lines: 27)
- `len` (lines: 30, 33)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_name_args(name_args: str) -> Tuple[str, Optional[str]]:
    """ Split a CLI argument of the form ``<name>[.<args>]`` at the first dot.

    :param name_args: Raw CLI argument, e.g. ``"grid.7"`` or ``"grid"``.
    :return: ``(name, args)``; ``args`` is ``None`` if no dot is present.
    """
    name_args_split: List[str] = name_args.split(".", 1)
    name: str = name_args_split[0]
    args: Optional[str]
    if len(name_args_split) == 1:
        args = None
    else:
        assert len(name_args_split) == 2
        args = name_args_split[1]
    return name, args
```
