---
id: "func:deepxube.domains.lightsout.LightsOut._next_state_np"
kind: "method"
name: "_next_state_np"
qualified_name: "deepxube.domains.lightsout.LightsOut._next_state_np"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 139
line_end: 151
class: "LightsOut"
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
    annotation: "List[NDArray]"
    default: null
  - name: "actions"
    annotation: "List[LOAction]"
    default: null
returns: "Tuple[List[NDArray], List[float]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [141, 151]
  - target: null
    expr: "states_np_l[0].copy"
    call_sites: [142]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [144]
  - target: "func:numpy.expand_dims"
    expr: "np.expand_dims"
    call_sites: [145]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [147]
raises: []
reads_attrs:
  - "self.move_matrix"
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut._next_state_np`

**File:** [deepxube/domains/lightsout.py:139](../../../../deepxube/domains/lightsout.py#L139)
**Class:** `LightsOut`
**Visibility:** private
**Kind:** method

## Signature

```python
def _next_state_np(self, states_np_l: List[NDArray], actions: List[LOAction]) -> Tuple[List[NDArray], List[float]]
```

## Docstring

:return: States after toggling each action's tile and its neighbours. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np_l` | `List[NDArray]` | — |
| `actions` | `List[LOAction]` | — |

## Returns

`Tuple[List[NDArray], List[float]]`

## Calls

- `np.arange` → `func:numpy.arange` (lines: 144)
- `np.expand_dims` → `func:numpy.expand_dims` (lines: 145)
- `np.array` → `func:numpy.array` (lines: 147)

### Unresolved
- `len` (lines: 141, 151)
- `states_np_l[0].copy` (lines: 142)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.move_matrix`

## Source

```python
    def _next_state_np(self, states_np_l: List[NDArray], actions: List[LOAction]) -> Tuple[List[NDArray], List[float]]:
        """ :return: States after toggling each action's tile and its neighbours. """
        assert len(states_np_l) == 1
        tiles_next_np: NDArray = states_np_l[0].copy()

        state_idxs: NDArray = np.arange(0, tiles_next_np.shape[0])
        state_idxs = np.expand_dims(state_idxs, 1)

        actions_np: NDArray = np.array([action.action for action in actions])
        move_matrix = self.move_matrix[actions_np]
        tiles_next_np[state_idxs, move_matrix] = (tiles_next_np[state_idxs, move_matrix] + 1) % 2

        return [tiles_next_np], [1.0] * len(actions)
```
