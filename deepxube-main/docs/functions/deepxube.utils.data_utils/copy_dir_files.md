---
id: "func:deepxube.utils.data_utils.copy_dir_files"
kind: "function"
name: "copy_dir_files"
qualified_name: "deepxube.utils.data_utils.copy_dir_files"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 113
line_end: 125
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "src_dir"
    annotation: "str"
    default: null
  - name: "dest_dir"
    annotation: "str"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:os.listdir"
    expr: "os.listdir"
    call_sites: [121]
  - target: null
    expr: "os.path.join"
    call_sites: [123]
  - target: null
    expr: "os.path.isfile"
    call_sites: [124]
  - target: "func:shutil.copy"
    expr: "shutil.copy"
    call_sites: [125]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.data_utils.copy_dir_files`

**File:** [deepxube/utils/data_utils.py:113](../../../../deepxube/utils/data_utils.py#L113)
**Visibility:** public
**Kind:** function

## Signature

```python
def copy_dir_files(src_dir: str, dest_dir: str) -> None
```

## Docstring

Copy every regular file from ``src_dir`` into ``dest_dir``.

Subdirectories are ignored. Destination must already exist.

:param src_dir: Source directory path.
:param dest_dir: Destination directory path.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `src_dir` | `str` | — |
| `dest_dir` | `str` | — |

## Returns

`None`

## Calls

- `os.listdir` → `func:os.listdir` (lines: 121)
- `shutil.copy` → `func:shutil.copy` (lines: 125)

### Unresolved
- `os.path.join` (lines: 123)
- `os.path.isfile` (lines: 124)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def copy_dir_files(src_dir: str, dest_dir: str) -> None:
    """ Copy every regular file from ``src_dir`` into ``dest_dir``.

    Subdirectories are ignored. Destination must already exist.

    :param src_dir: Source directory path.
    :param dest_dir: Destination directory path.
    """
    src_files: List[str] = os.listdir(src_dir)
    for file_name in src_files:
        full_file_name: str = os.path.join(src_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)
```
