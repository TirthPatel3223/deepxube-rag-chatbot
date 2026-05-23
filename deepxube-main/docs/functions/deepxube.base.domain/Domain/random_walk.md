---
id: "func:deepxube.base.domain.Domain.random_walk"
kind: "method"
name: "random_walk"
qualified_name: "deepxube.base.domain.Domain.random_walk"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 139
line_end: 167
class: "Domain"
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
    annotation: "List[S]"
    default: null
  - name: "num_steps_l"
    annotation: "List[int]"
    default: null
returns: "Tuple[List[S], List[float]]"
docstring_source: "present"
callees:
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [149]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [150]
  - target: null
    expr: "len"
    call_sites: [150]
  - target: "func:numpy.any"
    expr: "np.any"
    call_sites: [152]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [153]
  - target: "func:deepxube.base.domain.Domain.sample_next_state"
    expr: "self.sample_next_state"
    call_sites: [156]
  - target: null
    expr: "enumerate"
    call_sites: [159]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.Domain.random_walk`

**File:** [deepxube/base/domain.py:139](../../../../deepxube/base/domain.py#L139)
**Class:** `Domain`
**Visibility:** public
**Kind:** method

## Signature

```python
def random_walk(self, states: List[S], num_steps_l: List[int]) -> Tuple[List[S], List[float]]
```

## Docstring

Perform a random walk on the given states for the given number of steps

:param states: List of states
:param num_steps_l: number of steps to take for each state
:return: The resulting state and the path cost for each random walk

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |
| `num_steps_l` | `List[int]` | — |

## Returns

`Tuple[List[S], List[float]]`

## Calls

- `np.array` → `func:numpy.array` (lines: 149)
- `np.zeros` → `func:numpy.zeros` (lines: 150)
- `np.any` → `func:numpy.any` (lines: 152)
- `np.where` → `func:numpy.where` (lines: 153)
- `self.sample_next_state` → `func:deepxube.base.domain.Domain.sample_next_state` (lines: 156)

### Unresolved
- `len` (lines: 150)
- `enumerate` (lines: 159)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def random_walk(self, states: List[S], num_steps_l: List[int]) -> Tuple[List[S], List[float]]:
        """ Perform a random walk on the given states for the given number of steps

        :param states: List of states
        :param num_steps_l: number of steps to take for each state
        :return: The resulting state and the path cost for each random walk
        """
        states_walk: List[S] = [state for state in states]
        path_costs: List[float] = [0.0 for _ in states]

        num_steps: NDArray[np.int_] = np.array(num_steps_l)
        num_steps_curr: NDArray[np.int_] = np.zeros(len(states), dtype=int)
        steps_lt: NDArray[np.bool_] = num_steps_curr < num_steps
        while np.any(steps_lt):
            idxs: NDArray[np.int_] = np.where(steps_lt)[0]
            states_to_move = [states_walk[idx] for idx in idxs]

            states_moved, tcs = self.sample_next_state(states_to_move)

            idx: int
            for move_idx, idx in enumerate(idxs):
                states_walk[idx] = states_moved[move_idx]
                path_costs[idx] += tcs[move_idx]

            num_steps_curr[idxs] = num_steps_curr[idxs] + 1

            steps_lt[idxs] = num_steps_curr[idxs] < num_steps[idxs]

        return states_walk, path_costs
```
