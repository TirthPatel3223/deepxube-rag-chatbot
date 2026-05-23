---
id: "func:deepxube.domains.grid.GridNNetInput.to_np"
kind: "method"
name: "to_np"
qualified_name: "deepxube.domains.grid.GridNNetInput.to_np"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 170
line_end: 177
class: "GridNNetInput"
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
    annotation: "List[GridState]"
    default: null
  - name: "goals"
    annotation: "List[GridGoal]"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [172]
  - target: null
    expr: "len"
    call_sites: [172]
  - target: null
    expr: "enumerate"
    call_sites: [173]
  - target: null
    expr: "zip"
    call_sites: [173]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.domains.grid.GridNNetInput.to_np`

**File:** [deepxube/domains/grid.py:170](../../../../deepxube/domains/grid.py#L170)
**Class:** `GridNNetInput`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np(self, states: List[GridState], goals: List[GridGoal]) -> List[NDArray]
```

## Docstring

:return: Shape ``(N, 2, dim, dim)`` array with binary robot and goal position maps. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[GridState]` | — |
| `goals` | `List[GridGoal]` | — |

## Returns

`List[NDArray]`

## Calls

- `np.zeros` → `func:numpy.zeros` (lines: 172)

### Unresolved
- `len` (lines: 172)
- `enumerate` (lines: 173)
- `zip` (lines: 173)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def to_np(self, states: List[GridState], goals: List[GridGoal]) -> List[NDArray]:
        """ :return: Shape ``(N, 2, dim, dim)`` array with binary robot and goal position maps. """
        np_rep: NDArray = np.zeros((len(states), 2, self.domain.dim, self.domain.dim))
        for idx, (state, goal) in enumerate(zip(states, goals)):
            np_rep[idx, 0, state.robot_x, state.robot_y] = 1
            np_rep[idx, 1, goal.robot_x, goal.robot_y] = 1

        return [np_rep]
```
