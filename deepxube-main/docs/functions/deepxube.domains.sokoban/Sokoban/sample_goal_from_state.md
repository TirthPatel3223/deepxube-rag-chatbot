---
id: "func:deepxube.domains.sokoban.Sokoban.sample_goal_from_state"
kind: "method"
name: "sample_goal_from_state"
qualified_name: "deepxube.domains.sokoban.Sokoban.sample_goal_from_state"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 253
line_end: 259
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
  - name: "states_start"
    annotation: "Optional[List[SkState]]"
    default: null
  - name: "states_goal"
    annotation: "List[SkState]"
    default: null
returns: "List[SkGoal]"
docstring_source: "present"
callees:
  - target: null
    expr: "goals.append"
    call_sites: [257]
  - target: "func:deepxube.domains.sokoban.SkGoal"
    expr: "SkGoal"
    call_sites: [257]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban.Sokoban.sample_goal_from_state`

**File:** [deepxube/domains/sokoban.py:253](../../../../deepxube/domains/sokoban.py#L253)
**Class:** `Sokoban`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goal_from_state(self, states_start: Optional[List[SkState]], states_goal: List[SkState]) -> List[SkGoal]
```

## Docstring

:return: Goals derived from the box positions of each state in ``states_goal``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_start` | `Optional[List[SkState]]` | — |
| `states_goal` | `List[SkState]` | — |

## Returns

`List[SkGoal]`

## Calls

- `SkGoal` → `func:deepxube.domains.sokoban.SkGoal` (lines: 257)

### Unresolved
- `goals.append` (lines: 257)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_goal_from_state(self, states_start: Optional[List[SkState]], states_goal: List[SkState]) -> List[SkGoal]:
        """ :return: Goals derived from the box positions of each state in ``states_goal``. """
        goals: List[SkGoal] = []
        for state_goal in states_goal:
            goals.append(SkGoal(state_goal.boxes))

        return goals
```
