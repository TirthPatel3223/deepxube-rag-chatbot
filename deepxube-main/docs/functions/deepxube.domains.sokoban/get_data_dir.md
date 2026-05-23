---
id: "func:deepxube.domains.sokoban.get_data_dir"
kind: "function"
name: "get_data_dir"
qualified_name: "deepxube.domains.sokoban.get_data_dir"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 125
line_end: 130
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "str"
docstring_source: "present"
callees:
  - target: null
    expr: "str"
    call_sites: [127]
  - target: null
    expr: "pathlib.Path(__file__).parent.resolve"
    call_sites: [127]
  - target: "func:pathlib.Path"
    expr: "pathlib.Path"
    call_sites: [127]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban.get_data_dir`

**File:** [deepxube/domains/sokoban.py:125](../../../../deepxube/domains/sokoban.py#L125)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_data_dir() -> str
```

## Docstring

:return: Absolute path to the sokoban data directory adjacent to this source file. 

## Parameters

*(No parameters.)*

## Returns

`str`

## Calls

- `pathlib.Path` → `func:pathlib.Path` (lines: 127)

### Unresolved
- `str` (lines: 127)
- `pathlib.Path(__file__).parent.resolve` (lines: 127)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_data_dir() -> str:
    """ :return: Absolute path to the sokoban data directory adjacent to this source file. """
    parent_dir: str = str(pathlib.Path(__file__).parent.resolve())
    data_dir: str = f"{parent_dir}/data/sokoban/"

    return data_dir
```
