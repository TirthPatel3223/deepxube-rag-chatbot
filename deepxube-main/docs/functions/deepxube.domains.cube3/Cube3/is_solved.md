---
id: "func:deepxube.domains.cube3.Cube3.is_solved"
kind: "method"
name: "is_solved"
qualified_name: "deepxube.domains.cube3.Cube3.is_solved"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 540
line_end: 544
class: "Cube3"
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
    annotation: "List[Cube3State]"
    default: null
  - name: "goals"
    annotation: "List[Cube3Goal]"
    default: null
returns: "List[bool]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [542, 543]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [544]
  - target: null
    expr: "np.all(states_np == goals_np, axis=1).tolist"
    call_sites: [544]
  - target: "func:numpy.all"
    expr: "np.all"
    call_sites: [544]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.is_solved`

**File:** [deepxube/domains/cube3.py:540](../../../../deepxube/domains/cube3.py#L540)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def is_solved(self, states: List[Cube3State], goals: List[Cube3Goal]) -> List[bool]
```

## Docstring

:return: True for each state whose colour array exactly matches the goal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[Cube3State]` | — |
| `goals` | `List[Cube3Goal]` | — |

## Returns

`List[bool]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 542, 543)
- `cast` → `func:typing.cast` (lines: 544)
- `np.all` → `func:numpy.all` (lines: 544)

### Unresolved
- `np.all(states_np == goals_np, axis=1).tolist` (lines: 544)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def is_solved(self, states: List[Cube3State], goals: List[Cube3Goal]) -> List[bool]:
        """ :return: True for each state whose colour array exactly matches the goal. """
        states_np: NDArray = np.stack([x.colors for x in states], axis=0)
        goals_np: NDArray = np.stack([x.colors for x in goals], axis=0)
        return cast(List[bool], np.all(states_np == goals_np, axis=1).tolist())
```
