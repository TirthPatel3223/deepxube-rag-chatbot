---
id: "func:deepxube.domains.sokoban._get_surfaces"
kind: "function"
name: "_get_surfaces"
qualified_name: "deepxube.domains.sokoban._get_surfaces"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 98
line_end: 111
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "Dict[str, NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.sokoban.get_data_dir"
    expr: "get_data_dir"
    call_sites: [101]
  - target: "func:filelock.FileLock"
    expr: "FileLock"
    call_sites: [104]
  - target: null
    expr: "dict"
    call_sites: [107]
  - target: null
    expr: "imageio.imread"
    call_sites: [109]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban._get_surfaces`

**File:** [deepxube/domains/sokoban.py:98](../../../../deepxube/domains/sokoban.py#L98)
**Visibility:** private
**Kind:** function

## Signature

```python
def _get_surfaces() -> Dict[str, NDArray]
```

## Docstring

:return: Dict mapping surface name to its RGB image array, loaded from the sokoban data directory. 

## Parameters

*(No parameters.)*

## Returns

`Dict[str, NDArray]`

## Calls

- `get_data_dir` → `func:deepxube.domains.sokoban.get_data_dir` (lines: 101)
- `FileLock` → `func:filelock.FileLock` (lines: 104)

### Unresolved
- `dict` (lines: 107)
- `imageio.imread` (lines: 109)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _get_surfaces() -> Dict[str, NDArray]:
    """ :return: Dict mapping surface name to its RGB image array, loaded from the sokoban data directory. """
    import imageio.v2 as imageio
    data_dir = get_data_dir()
    img_dir = f"{data_dir}/sokoban/"

    lock = FileLock(f"{data_dir}/file.lock")
    with lock:
        # Load images, representing the corresponding situation
        surface_dict: Dict[str, NDArray] = dict()
        for img_name in ["box", "box_on_target", "box_target", "floor", "player", "player_on_target", "wall"]:
            surface_dict[img_name] = imageio.imread(f"{img_dir}/surface/{img_name}.png")

    return surface_dict
```
