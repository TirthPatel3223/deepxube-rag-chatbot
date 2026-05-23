---
id: "func:deepxube.domains.sokoban._get_train_states"
kind: "function"
name: "_get_train_states"
qualified_name: "deepxube.domains.sokoban._get_train_states"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 114
line_end: 122
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "List[SkState]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.sokoban.get_data_dir"
    expr: "get_data_dir"
    call_sites: [116]
  - target: "func:filelock.FileLock"
    expr: "FileLock"
    call_sites: [117]
  - target: "func:deepxube.domains.sokoban.load_states"
    expr: "load_states"
    call_sites: [120]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban._get_train_states`

**File:** [deepxube/domains/sokoban.py:114](../../../../deepxube/domains/sokoban.py#L114)
**Visibility:** private
**Kind:** function

## Signature

```python
def _get_train_states() -> List[SkState]
```

## Docstring

:return: Training states loaded under a file lock to prevent concurrent read/write corruption. 

## Parameters

*(No parameters.)*

## Returns

`List[SkState]`

## Calls

- `get_data_dir` → `func:deepxube.domains.sokoban.get_data_dir` (lines: 116)
- `FileLock` → `func:filelock.FileLock` (lines: 117)
- `load_states` → `func:deepxube.domains.sokoban.load_states` (lines: 120)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _get_train_states() -> List[SkState]:
    """ :return: Training states loaded under a file lock to prevent concurrent read/write corruption. """
    data_dir = get_data_dir()
    lock = FileLock(f"{data_dir}/file.lock")

    with lock:
        states_train: List[SkState] = load_states(data_dir)

    return states_train
```
