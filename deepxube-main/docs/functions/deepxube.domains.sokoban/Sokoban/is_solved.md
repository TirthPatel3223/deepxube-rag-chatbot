---
id: "func:deepxube.domains.sokoban.Sokoban.is_solved"
kind: "method"
name: "is_solved"
qualified_name: "deepxube.domains.sokoban.Sokoban.is_solved"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 231
line_end: 235
class: "Sokoban"
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
    annotation: "List[SkState]"
    default: null
  - name: "goals"
    annotation: "List[SkGoal]"
    default: null
returns: "List[bool]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [233, 234]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [235]
  - target: null
    expr: "np.all(boxes_states == targets, axis=(1, 2)).tolist"
    call_sites: [235]
  - target: "func:numpy.all"
    expr: "np.all"
    call_sites: [235]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban.Sokoban.is_solved`

**File:** [deepxube/domains/sokoban.py:231](../../../../deepxube/domains/sokoban.py#L231)
**Class:** `Sokoban`
**Visibility:** public
**Kind:** method

## Signature

```python
def is_solved(self, states: List[SkState], goals: List[SkGoal]) -> List[bool]
```

## Docstring

:return: True for each state whose box map exactly matches the goal box map. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[SkState]` | — |
| `goals` | `List[SkGoal]` | — |

## Returns

`List[bool]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 233, 234)
- `cast` → `func:typing.cast` (lines: 235)
- `np.all` → `func:numpy.all` (lines: 235)

### Unresolved
- `np.all(boxes_states == targets, axis=(1, 2)).tolist` (lines: 235)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def is_solved(self, states: List[SkState], goals: List[SkGoal]) -> List[bool]:
        """ :return: True for each state whose box map exactly matches the goal box map. """
        boxes_states: NDArray = np.stack([state.boxes for state in states], axis=0)
        targets: NDArray = np.stack([goal.boxes for goal in goals], axis=0)
        return cast(List[bool], np.all(boxes_states == targets, axis=(1, 2)).tolist())
```
