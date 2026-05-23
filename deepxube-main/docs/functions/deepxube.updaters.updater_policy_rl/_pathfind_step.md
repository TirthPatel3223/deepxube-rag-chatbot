---
id: "func:deepxube.updaters.updater_policy_rl._pathfind_step"
kind: "function"
name: "_pathfind_step"
qualified_name: "deepxube.updaters.updater_policy_rl._pathfind_step"
module: "deepxube.updaters.updater_policy_rl"
file: "deepxube/updaters/updater_policy_rl.py"
line_start: 18
line_end: 22
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "pathfind"
    annotation: "PathFind"
    default: null
returns: "List[EdgeQ]"
docstring_source: "missing"
callees:
  - target: null
    expr: "pathfind.step"
    call_sites: [19]
  - target: "func:deepxube.updaters.updater_policy_rl.len"
    expr: "len"
    call_sites: [20]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_policy_rl._pathfind_step`

**File:** [deepxube/updaters/updater_policy_rl.py:18](../../../../deepxube/updaters/updater_policy_rl.py#L18)
**Visibility:** private
**Kind:** function

## Signature

```python
def _pathfind_step(pathfind: PathFind) -> List[EdgeQ]
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `pathfind` | `PathFind` | — |

## Returns

`List[EdgeQ]`

## Calls

- `len` → `func:deepxube.updaters.updater_policy_rl.len` (lines: 20)

### Unresolved
- `pathfind.step` (lines: 19)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _pathfind_step(pathfind: PathFind) -> List[EdgeQ]:
    edges_popped: List[EdgeQ] = pathfind.step()[1]
    assert len(edges_popped) == len(pathfind.instances), f"Values were {len(edges_popped)} and {len(pathfind.instances)}"

    return edges_popped
```
