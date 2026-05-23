---
id: "func:deepxube.updaters.updater_v_rl._pathfind_v_step"
kind: "function"
name: "_pathfind_v_step"
qualified_name: "deepxube.updaters.updater_v_rl._pathfind_v_step"
module: "deepxube.updaters.updater_v_rl"
file: "deepxube/updaters/updater_v_rl.py"
line_start: 18
line_end: 23
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "pathfind"
    annotation: "PathFindSetHeurV"
    default: null
returns: "List[Node]"
docstring_source: "missing"
callees:
  - target: null
    expr: "pathfind.step"
    call_sites: [20]
  - target: "func:deepxube.updaters.updater_v_rl.len"
    expr: "len"
    call_sites: [21]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_v_rl._pathfind_v_step`

**File:** [deepxube/updaters/updater_v_rl.py:18](../../../../deepxube/updaters/updater_v_rl.py#L18)
**Visibility:** private
**Kind:** function

## Signature

```python
def _pathfind_v_step(pathfind: PathFindSetHeurV) -> List[Node]
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `pathfind` | `PathFindSetHeurV` | — |

## Returns

`List[Node]`

## Calls

- `len` → `func:deepxube.updaters.updater_v_rl.len` (lines: 21)

### Unresolved
- `pathfind.step` (lines: 20)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _pathfind_v_step(pathfind: PathFindSetHeurV) -> List[Node]:
    # take a step
    nodes_popped: List[Node] = pathfind.step()[0]
    assert len(nodes_popped) == len(pathfind.instances), f"Values were {len(nodes_popped)} and {len(pathfind.instances)}"

    return nodes_popped
```
