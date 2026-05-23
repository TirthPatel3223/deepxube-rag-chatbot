---
id: "func:deepxube.domains.npuzzle.NPuzzle.sample_goalstate_goal_pairs"
kind: "method"
name: "sample_goalstate_goal_pairs"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.sample_goalstate_goal_pairs"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 90
line_end: 95
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
  - name: "num"
    annotation: "int"
    default: null
returns: "Tuple[List[NPState], List[NPGoal]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.npuzzle.NPState"
    expr: "NPState"
    call_sites: [92]
  - target: null
    expr: "self.goal_tiles.copy"
    call_sites: [92, 93]
  - target: "func:deepxube.domains.npuzzle.NPGoal"
    expr: "NPGoal"
    call_sites: [93]
raises: []
reads_attrs:
  - "self.goal_tiles"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.sample_goalstate_goal_pairs`

**File:** [deepxube/domains/npuzzle.py:90](../../../../deepxube/domains/npuzzle.py#L90)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[NPState], List[NPGoal]]
```

## Docstring

:return: ``num`` copies of the solved state and the corresponding goal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`Tuple[List[NPState], List[NPGoal]]`

## Calls

- `NPState` → `func:deepxube.domains.npuzzle.NPState` (lines: 92)
- `NPGoal` → `func:deepxube.domains.npuzzle.NPGoal` (lines: 93)

### Unresolved
- `self.goal_tiles.copy` (lines: 92, 93)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.goal_tiles`

## Source

```python
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[NPState], List[NPGoal]]:
        """ :return: ``num`` copies of the solved state and the corresponding goal. """
        states_goal: List[NPState] = [NPState(self.goal_tiles.copy())] * num
        goals: List[NPGoal] = [NPGoal(self.goal_tiles.copy())] * num

        return states_goal, goals
```
