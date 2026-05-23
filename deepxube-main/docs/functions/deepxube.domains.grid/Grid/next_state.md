---
id: "func:deepxube.domains.grid.Grid.next_state"
kind: "method"
name: "next_state"
qualified_name: "deepxube.domains.grid.Grid.next_state"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 88
line_end: 101
class: "Grid"
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
  - name: "actions"
    annotation: "List[GridAction]"
    default: null
returns: "Tuple[List[GridState], List[float]]"
docstring_source: "present"
callees:
  - target: null
    expr: "zip"
    call_sites: [91]
  - target: null
    expr: "states_next.append"
    call_sites: [93, 95, 97, 99]
  - target: "func:deepxube.domains.grid.GridState"
    expr: "GridState"
    call_sites: [93, 95, 97, 99]
  - target: null
    expr: "min"
    call_sites: [93, 97]
  - target: null
    expr: "max"
    call_sites: [95, 99]
  - target: null
    expr: "len"
    call_sites: [101]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.grid.Grid.next_state`

**File:** [deepxube/domains/grid.py:88](../../../../deepxube/domains/grid.py#L88)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def next_state(self, states: List[GridState], actions: List[GridAction]) -> Tuple[List[GridState], List[float]]
```

## Docstring

:return: States after applying ``actions``; movement is clamped to grid boundaries. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[GridState]` | — |
| `actions` | `List[GridAction]` | — |

## Returns

`Tuple[List[GridState], List[float]]`

## Calls

- `GridState` → `func:deepxube.domains.grid.GridState` (lines: 93, 95, 97, 99)

### Unresolved
- `zip` (lines: 91)
- `states_next.append` (lines: 93, 95, 97, 99)
- `min` (lines: 93, 97)
- `max` (lines: 95, 99)
- `len` (lines: 101)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def next_state(self, states: List[GridState], actions: List[GridAction]) -> Tuple[List[GridState], List[float]]:
        """ :return: States after applying ``actions``; movement is clamped to grid boundaries. """
        states_next: List[GridState] = []
        for state, action in zip(states, actions):
            if action.action == 0:  # up
                states_next.append(GridState(min(state.robot_x + 1, self.dim - 1), state.robot_y))
            elif action.action == 1:  # down
                states_next.append(GridState(max(state.robot_x - 1, 0), state.robot_y))
            elif action.action == 2:  # left
                states_next.append(GridState(state.robot_x, min(state.robot_y + 1, self.dim - 1)))
            elif action.action == 3:  # right
                states_next.append(GridState(state.robot_x, max(state.robot_y - 1, 0)))

        return states_next, [1.0] * len(states_next)
```
