---
id: "func:deepxube.base.domain.NextStateNP.random_walk"
kind: "method"
name: "random_walk"
qualified_name: "deepxube.base.domain.NextStateNP.random_walk"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 494
line_end: 519
class: "NextStateNP"
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
  - target: "func:deepxube.base.domain.NextStateNP._states_to_np"
    expr: "self._states_to_np"
    call_sites: [496]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [499]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [500]
  - target: null
    expr: "len"
    call_sites: [500, 509]
  - target: "func:numpy.any"
    expr: "np.any"
    call_sites: [502]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [503]
  - target: "func:deepxube.base.domain.NextStateNP._sample_state_np_action"
    expr: "self._sample_state_np_action"
    call_sites: [505]
  - target: "func:deepxube.base.domain.NextStateNP._next_state_np"
    expr: "self._next_state_np"
    call_sites: [507]
  - target: null
    expr: "range"
    call_sites: [509]
  - target: null
    expr: "enumerate"
    call_sites: [512]
  - target: "func:deepxube.base.domain.NextStateNP._np_to_states"
    expr: "self._np_to_states"
    call_sites: [519]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.NextStateNP.random_walk`

**File:** [deepxube/base/domain.py:494](../../../../deepxube/base/domain.py#L494)
**Class:** `NextStateNP`
**Visibility:** public
**Kind:** method

## Signature

```python
def random_walk(self, states: List[S], num_steps_l: List[int]) -> Tuple[List[S], List[float]]
```

## Docstring

Vectorised numpy random walk; semantics match ``Domain.random_walk``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |
| `num_steps_l` | `List[int]` | — |

## Returns

`Tuple[List[S], List[float]]`

## Calls

- `self._states_to_np` → `func:deepxube.base.domain.NextStateNP._states_to_np` (lines: 496)
- `np.array` → `func:numpy.array` (lines: 499)
- `np.zeros` → `func:numpy.zeros` (lines: 500)
- `np.any` → `func:numpy.any` (lines: 502)
- `np.where` → `func:numpy.where` (lines: 503)
- `self._sample_state_np_action` → `func:deepxube.base.domain.NextStateNP._sample_state_np_action` (lines: 505)
- `self._next_state_np` → `func:deepxube.base.domain.NextStateNP._next_state_np` (lines: 507)
- `self._np_to_states` → `func:deepxube.base.domain.NextStateNP._np_to_states` (lines: 519)

### Unresolved
- `len` (lines: 500, 509)
- `range` (lines: 509)
- `enumerate` (lines: 512)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def random_walk(self, states: List[S], num_steps_l: List[int]) -> Tuple[List[S], List[float]]:
        """ Vectorised numpy random walk; semantics match ``Domain.random_walk``. """
        states_np = self._states_to_np(states)
        path_costs: List[float] = [0.0 for _ in states]

        num_steps: NDArray[np.int_] = np.array(num_steps_l)
        num_steps_curr: NDArray[np.int_] = np.zeros(len(states), dtype=int)
        steps_lt: NDArray[np.bool_] = num_steps_curr < num_steps
        while np.any(steps_lt):
            idxs: NDArray[np.int_] = np.where(steps_lt)[0]
            states_np_tomove: List[NDArray] = [states_np_i[idxs] for states_np_i in states_np]
            actions_rand: List[A] = self._sample_state_np_action(states_np_tomove)

            states_moved, tcs = self._next_state_np(states_np_tomove, actions_rand)

            for l_idx in range(len(states_np)):
                states_np[l_idx][idxs] = states_moved[l_idx]
            idx: int
            for act_idx, idx in enumerate(idxs):
                path_costs[idx] += tcs[act_idx]

            num_steps_curr[idxs] = num_steps_curr[idxs] + 1

            steps_lt[idxs] = num_steps_curr[idxs] < num_steps[idxs]

        return self._np_to_states(states_np), path_costs
```
