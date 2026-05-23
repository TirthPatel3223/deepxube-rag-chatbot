---
id: "func:deepxube.domains.sokoban.Sokoban._get_next_idx"
kind: "method"
name: "_get_next_idx"
qualified_name: "deepxube.domains.sokoban.Sokoban._get_next_idx"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 315
line_end: 335
class: "Sokoban"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "curr_idxs"
    annotation: "NDArray[np.int_]"
    default: null
  - name: "actions"
    annotation: "List[SkAction]"
    default: null
returns: "NDArray[np.int_]"
docstring_source: "present"
callees:
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [317]
  - target: null
    expr: "curr_idxs.copy"
    call_sites: [318]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [320, 323, 326, 329]
  - target: "func:numpy.maximum"
    expr: "np.maximum"
    call_sites: [332]
  - target: "func:numpy.minimum"
    expr: "np.minimum"
    call_sites: [333]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.sokoban.Sokoban._get_next_idx`

**File:** [deepxube/domains/sokoban.py:315](../../../../deepxube/domains/sokoban.py#L315)
**Class:** `Sokoban`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_next_idx(self, curr_idxs: NDArray[np.int_], actions: List[SkAction]) -> NDArray[np.int_]
```

## Docstring

:return: Candidate next ``(row, col)`` positions after applying each action, clamped to grid bounds. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `curr_idxs` | `NDArray[np.int_]` | — |
| `actions` | `List[SkAction]` | — |

## Returns

`NDArray[np.int_]`

## Calls

- `np.array` → `func:numpy.array` (lines: 317)
- `np.where` → `func:numpy.where` (lines: 320, 323, 326, 329)
- `np.maximum` → `func:numpy.maximum` (lines: 332)
- `np.minimum` → `func:numpy.minimum` (lines: 333)

### Unresolved
- `curr_idxs.copy` (lines: 318)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def _get_next_idx(self, curr_idxs: NDArray[np.int_], actions: List[SkAction]) -> NDArray[np.int_]:
        """ :return: Candidate next ``(row, col)`` positions after applying each action, clamped to grid bounds. """
        actions_np: NDArray[np.int_] = np.array([action.action for action in actions])
        next_idxs: NDArray[np.int_] = curr_idxs.copy()

        action_idxs: NDArray[np.int_] = np.where(actions_np == 0)[0]
        next_idxs[action_idxs, 0] = next_idxs[action_idxs, 0] - 1

        action_idxs = np.where(actions_np == 1)[0]
        next_idxs[action_idxs, 0] = next_idxs[action_idxs, 0] + 1

        action_idxs = np.where(actions_np == 2)[0]
        next_idxs[action_idxs, 1] = next_idxs[action_idxs, 1] - 1

        action_idxs = np.where(actions_np == 3)[0]
        next_idxs[action_idxs, 1] = next_idxs[action_idxs, 1] + 1

        next_idxs = np.maximum(next_idxs, 0)
        next_idxs = np.minimum(next_idxs, self.dim - 1)

        return next_idxs
```
