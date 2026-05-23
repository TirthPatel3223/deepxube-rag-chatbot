---
id: "func:deepxube.updaters.updater_q_rl._pathfind_q_step"
kind: "function"
name: "_pathfind_q_step"
qualified_name: "deepxube.updaters.updater_q_rl._pathfind_q_step"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 17
line_end: 21
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "pathfind"
    annotation: "PathFindSetHeurQ"
    default: null
returns: "List[EdgeQ]"
docstring_source: "missing"
callees:
  - target: null
    expr: "pathfind.step"
    call_sites: [18]
  - target: "func:deepxube.updaters.updater_q_rl.len"
    expr: "len"
    call_sites: [19]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl._pathfind_q_step`

**File:** [deepxube/updaters/updater_q_rl.py:17](../../../../deepxube/updaters/updater_q_rl.py#L17)
**Visibility:** private
**Kind:** function

## Signature

```python
def _pathfind_q_step(pathfind: PathFindSetHeurQ) -> List[EdgeQ]
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `pathfind` | `PathFindSetHeurQ` | — |

## Returns

`List[EdgeQ]`

## Calls

- `len` → `func:deepxube.updaters.updater_q_rl.len` (lines: 19)

### Unresolved
- `pathfind.step` (lines: 18)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _pathfind_q_step(pathfind: PathFindSetHeurQ) -> List[EdgeQ]:
    edges_popped: List[EdgeQ] = pathfind.step()[1]
    assert len(edges_popped) == len(pathfind.instances), f"Values were {len(edges_popped)} and {len(pathfind.instances)}"

    return edges_popped
```
