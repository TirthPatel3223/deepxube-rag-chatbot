---
id: "func:deepxube.domains.npuzzle.NPuzzle.expand"
kind: "method"
name: "expand"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.expand"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 124
line_end: 158
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
returns: "Tuple[List[List[NPState]], List[List[NPAction]], List[List[float]]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [127, 129, 130, 151]
  - target: null
    expr: "range"
    call_sites: [129, 130, 142, 151, 156]
  - target: "func:numpy.empty"
    expr: "np.empty"
    call_sites: [132]
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [135]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [139]
  - target: "func:deepxube.domains.npuzzle.NPuzzle._move_np"
    expr: "self._move_np"
    call_sites: [146]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [149]
  - target: null
    expr: "states_exp[idx].append"
    call_sites: [152]
  - target: "func:deepxube.domains.npuzzle.NPState"
    expr: "NPState"
    call_sites: [152]
  - target: null
    expr: "actions_exp_l[idx].append"
    call_sites: [153]
  - target: "func:deepxube.domains.npuzzle.NPAction"
    expr: "NPAction"
    call_sites: [153]
  - target: null
    expr: "list"
    call_sites: [156]
raises: []
reads_attrs:
  - "self.num_actions"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.expand`

**File:** [deepxube/domains/npuzzle.py:124](../../../../deepxube/domains/npuzzle.py#L124)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def expand(self, states: List[NPState]) -> Tuple[List[List[NPState]], List[List[NPAction]], List[List[float]]]
```

## Docstring

:return: ``(children, actions, costs)`` for all 4 slide directions applied to each state. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[NPState]` | — |

## Returns

`Tuple[List[List[NPState]], List[List[NPAction]], List[List[float]]]`

## Calls

- `np.empty` → `func:numpy.empty` (lines: 132)
- `np.stack` → `func:numpy.stack` (lines: 135)
- `np.where` → `func:numpy.where` (lines: 139)
- `self._move_np` → `func:deepxube.domains.npuzzle.NPuzzle._move_np` (lines: 146)
- `np.array` → `func:numpy.array` (lines: 149)
- `NPState` → `func:deepxube.domains.npuzzle.NPState` (lines: 152)
- `NPAction` → `func:deepxube.domains.npuzzle.NPAction` (lines: 153)

### Unresolved
- `len` (lines: 127, 129, 130, 151)
- `range` (lines: 129, 130, 142, 151, 156)
- `states_exp[idx].append` (lines: 152)
- `actions_exp_l[idx].append` (lines: 153)
- `list` (lines: 156)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_actions`

## Source

```python
    def expand(self, states: List[NPState]) -> Tuple[List[List[NPState]], List[List[NPAction]], List[List[float]]]:
        """ :return: ``(children, actions, costs)`` for all 4 slide directions applied to each state. """
        # initialize
        num_states: int = len(states)

        states_exp: List[List[NPState]] = [[] for _ in range(len(states))]
        actions_exp_l: List[List[NPAction]] = [[] for _ in range(len(states))]

        tc: NDArray[np.float64] = np.empty([num_states, self.num_actions])

        # numpy states
        states_np: NDArray[int_t] = np.stack([state.tiles for state in states])

        # Get z_idxs
        z_idxs: NDArray[np.int_]
        _, z_idxs = np.where(states_np == 0)

        # for each move, get next states, transition costs, and if solved
        for action in range(self.num_actions):
            # next state
            states_next_np: NDArray[int_t]
            tc_move: List[float]
            states_next_np, _, tc_move = self._move_np(states_np, z_idxs, action)

            # transition cost
            tc[:, action] = np.array(tc_move)

            for idx in range(len(states)):
                states_exp[idx].append(NPState(states_next_np[idx]))
                actions_exp_l[idx].append(NPAction(action))

        # make lists
        tc_l: List[List[float]] = [list(tc[i]) for i in range(num_states)]

        return states_exp, actions_exp_l, tc_l
```
