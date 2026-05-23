---
id: "func:deepxube.domains.lightsout.LightsOut.is_solved"
kind: "method"
name: "is_solved"
qualified_name: "deepxube.domains.lightsout.LightsOut.is_solved"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 84
line_end: 89
class: "LightsOut"
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
    annotation: "List[LOState]"
    default: null
  - name: "goals"
    annotation: "List[LOGoal]"
    default: null
returns: "List[bool]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [86, 87]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [89]
  - target: null
    expr: "np.all(states_np == goals_np, axis=1).tolist"
    call_sites: [89]
  - target: "func:numpy.all"
    expr: "np.all"
    call_sites: [89]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut.is_solved`

**File:** [deepxube/domains/lightsout.py:84](../../../../deepxube/domains/lightsout.py#L84)
**Class:** `LightsOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def is_solved(self, states: List[LOState], goals: List[LOGoal]) -> List[bool]
```

## Docstring

:return: True for each state whose tile array exactly matches the goal tile array. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[LOState]` | — |
| `goals` | `List[LOGoal]` | — |

## Returns

`List[bool]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 86, 87)
- `cast` → `func:typing.cast` (lines: 89)
- `np.all` → `func:numpy.all` (lines: 89)

### Unresolved
- `np.all(states_np == goals_np, axis=1).tolist` (lines: 89)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def is_solved(self, states: List[LOState], goals: List[LOGoal]) -> List[bool]:
        """ :return: True for each state whose tile array exactly matches the goal tile array. """
        states_np = np.stack([state.tiles for state in states], axis=0)
        goals_np = np.stack([goal.tiles for goal in goals], axis=0)

        return cast(List[bool], np.all(states_np == goals_np, axis=1).tolist())
```
