---
id: "func:deepxube.domains.npuzzle.NPuzzle.next_state"
kind: "method"
name: "next_state"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.next_state"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 97
line_end: 122
class: "NPuzzle"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[NPState]"
    default: null
  - name: "actions"
    annotation: "List[NPAction]"
    default: null
returns: "Tuple[List[NPState], List[float]]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [100]
  - target: null
    expr: "states_np.copy"
    call_sites: [101]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [105]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [107]
  - target: null
    expr: "len"
    call_sites: [107, 109]
  - target: null
    expr: "set"
    call_sites: [108]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [109, 116]
  - target: null
    expr: "range"
    call_sites: [109]
  - target: "func:deepxube.domains.npuzzle.NPuzzle._move_np"
    expr: "self._move_np"
    call_sites: [113]
  - target: "func:deepxube.domains.npuzzle.NPState"
    expr: "NPState"
    call_sites: [119]
  - target: null
    expr: "list"
    call_sites: [119, 120]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.next_state`

**File:** [deepxube/domains/npuzzle.py:97](../../../../deepxube/domains/npuzzle.py#L97)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def next_state(self, states: List[NPState], actions: List[NPAction]) -> Tuple[List[NPState], List[float]]
```

## Docstring

:return: Next states and transition costs (1.0 each) after applying ``actions``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[NPState]` | — |
| `actions` | `List[NPAction]` | — |

## Returns

`Tuple[List[NPState], List[float]]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 100)
- `np.where` → `func:numpy.where` (lines: 105)
- `np.zeros` → `func:numpy.zeros` (lines: 107)
- `np.array` → `func:numpy.array` (lines: 109, 116)
- `self._move_np` → `func:deepxube.domains.npuzzle.NPuzzle._move_np` (lines: 113)
- `NPState` → `func:deepxube.domains.npuzzle.NPState` (lines: 119)

### Unresolved
- `states_np.copy` (lines: 101)
- `len` (lines: 107, 109)
- `set` (lines: 108)
- `range` (lines: 109)
- `list` (lines: 119, 120)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def next_state(self, states: List[NPState], actions: List[NPAction]) -> Tuple[List[NPState], List[float]]:
        """ :return: Next states and transition costs (1.0 each) after applying ``actions``. """
        # initialize
        states_np: NDArray[int_t] = np.stack([x.tiles for x in states], axis=0)
        states_next_np: NDArray[int_t] = states_np.copy()

        # get zero indicies
        z_idxs: NDArray[np.int_]
        _, z_idxs = np.where(states_next_np == 0)

        tcs_np: NDArray[np.float64] = np.zeros(len(states))
        for action in set(actions):
            action_idxs: NDArray[np.int_] = np.array([idx for idx in range(len(actions)) if actions[idx] == action])
            states_np_act = states_np[action_idxs]
            z_idxs_act: NDArray[np.int_] = z_idxs[action_idxs]

            states_next_np_act, _, tcs_act = self._move_np(states_np_act, z_idxs_act, action.action)

            states_next_np[action_idxs] = states_next_np_act
            tcs_np[action_idxs] = np.array(tcs_act)

        # make states
        states_next: List[NPState] = [NPState(x) for x in list(states_next_np)]
        transition_costs = list(tcs_np)

        return states_next, transition_costs
```
