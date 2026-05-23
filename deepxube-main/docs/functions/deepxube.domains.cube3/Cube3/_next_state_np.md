---
id: "func:deepxube.domains.cube3.Cube3._next_state_np"
kind: "method"
name: "_next_state_np"
qualified_name: "deepxube.domains.cube3.Cube3._next_state_np"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 619
line_end: 633
class: "Cube3"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_np_l"
    annotation: "List[NDArray[np.uint8]]"
    default: null
  - name: "actions"
    annotation: "List[Cube3Action]"
    default: null
returns: "Tuple[List[NDArray], List[float]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [622, 624, 633]
  - target: null
    expr: "states_np_l[0].copy"
    call_sites: [623]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [626]
  - target: "func:numpy.expand_dims"
    expr: "np.expand_dims"
    call_sites: [627]
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [629, 630]
raises: []
reads_attrs:
  - "self.atomic_actions"
  - "self.rotate_idxs_new"
  - "self.rotate_idxs_old"
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3._next_state_np`

**File:** [deepxube/domains/cube3.py:619](../../../../deepxube/domains/cube3.py#L619)
**Class:** `Cube3`
**Visibility:** private
**Kind:** method

## Signature

```python
def _next_state_np(self, states_np_l: List[NDArray[np.uint8]], actions: List[Cube3Action]) -> Tuple[List[NDArray], List[float]]
```

## Docstring

:return: States after applying each action's sticker permutation. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np_l` | `List[NDArray[np.uint8]]` | — |
| `actions` | `List[Cube3Action]` | — |

## Returns

`Tuple[List[NDArray], List[float]]`

## Calls

- `np.arange` → `func:numpy.arange` (lines: 626)
- `np.expand_dims` → `func:numpy.expand_dims` (lines: 627)
- `np.stack` → `func:numpy.stack` (lines: 629, 630)

### Unresolved
- `len` (lines: 622, 624, 633)
- `states_np_l[0].copy` (lines: 623)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.atomic_actions`
- `self.rotate_idxs_new`
- `self.rotate_idxs_old`

## Source

```python
    def _next_state_np(self, states_np_l: List[NDArray[np.uint8]],
                       actions: List[Cube3Action]) -> Tuple[List[NDArray], List[float]]:
        """ :return: States after applying each action's sticker permutation. """
        assert len(states_np_l) == 1
        colors_next_np: NDArray[np.uint8] = states_np_l[0].copy()
        assert colors_next_np.shape[0] == len(actions), f"#states {colors_next_np.shape[0]} != #actions {len(actions)}"

        state_idxs: NDArray = np.arange(0, colors_next_np.shape[0])
        state_idxs = np.expand_dims(state_idxs, 1)

        rotate_idxs_new: NDArray = np.stack([self.rotate_idxs_new[self.atomic_actions[action.action]] for action in actions])
        rotate_idxs_old: NDArray = np.stack([self.rotate_idxs_old[self.atomic_actions[action.action]] for action in actions])
        colors_next_np[state_idxs, rotate_idxs_new] = colors_next_np[state_idxs, rotate_idxs_old]

        return [colors_next_np], [1.0] * len(actions)
```
