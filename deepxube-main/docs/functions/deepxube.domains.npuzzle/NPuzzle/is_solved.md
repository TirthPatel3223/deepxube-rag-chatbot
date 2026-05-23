---
id: "func:deepxube.domains.npuzzle.NPuzzle.is_solved"
kind: "method"
name: "is_solved"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.is_solved"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 177
line_end: 182
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
  - name: "goals"
    annotation: "List[NPGoal]"
    default: null
returns: "List[bool]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [179, 180]
  - target: "func:numpy.all"
    expr: "np.all"
    call_sites: [181]
  - target: "func:numpy.logical_or"
    expr: "np.logical_or"
    call_sites: [181]
  - target: null
    expr: "list"
    call_sites: [182]
raises: []
reads_attrs:
  - "self.num_tiles"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.is_solved`

**File:** [deepxube/domains/npuzzle.py:177](../../../../deepxube/domains/npuzzle.py#L177)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def is_solved(self, states: List[NPState], goals: List[NPGoal]) -> List[bool]
```

## Docstring

:return: True when state tiles match goal tiles (goal value ``num_tiles`` is a wildcard). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[NPState]` | — |
| `goals` | `List[NPGoal]` | — |

## Returns

`List[bool]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 179, 180)
- `np.all` → `func:numpy.all` (lines: 181)
- `np.logical_or` → `func:numpy.logical_or` (lines: 181)

### Unresolved
- `list` (lines: 182)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_tiles`

## Source

```python
    def is_solved(self, states: List[NPState], goals: List[NPGoal]) -> List[bool]:
        """ :return: True when state tiles match goal tiles (goal value ``num_tiles`` is a wildcard). """
        states_np = np.stack([x.tiles for x in states], axis=0)
        goals_np = np.stack([x.tiles for x in goals], axis=0)
        is_solved_np = np.all(np.logical_or(states_np == goals_np, goals_np == self.num_tiles), axis=1)
        return list(is_solved_np)
```
