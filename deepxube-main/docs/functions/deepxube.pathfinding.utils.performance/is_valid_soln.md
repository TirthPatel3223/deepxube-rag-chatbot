---
id: "func:deepxube.pathfinding.utils.performance.is_valid_soln"
kind: "function"
name: "is_valid_soln"
qualified_name: "deepxube.pathfinding.utils.performance.is_valid_soln"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 118
line_end: 124
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "state"
    annotation: "State"
    default: null
  - name: "goal"
    annotation: "Goal"
    default: null
  - name: "soln"
    annotation: "List[Action]"
    default: null
  - name: "domain"
    annotation: "Domain"
    default: null
returns: "bool"
docstring_source: "present"
callees:
  - target: null
    expr: "domain.next_state"
    call_sites: [122]
  - target: null
    expr: "domain.is_solved"
    call_sites: [124]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.is_valid_soln`

**File:** [deepxube/pathfinding/utils/performance.py:118](../../../../deepxube/pathfinding/utils/performance.py#L118)
**Visibility:** public
**Kind:** function

## Signature

```python
def is_valid_soln(state: State, goal: Goal, soln: List[Action], domain: Domain) -> bool
```

## Docstring

:return: True if applying ``soln`` actions from ``state`` reaches a state satisfying ``goal``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `state` | `State` | — |
| `goal` | `Goal` | — |
| `soln` | `List[Action]` | — |
| `domain` | `Domain` | — |

## Returns

`bool`

## Calls

*(No resolved calls.)*

### Unresolved
- `domain.next_state` (lines: 122)
- `domain.is_solved` (lines: 124)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def is_valid_soln(state: State, goal: Goal, soln: List[Action], domain: Domain) -> bool:
    """ :return: True if applying ``soln`` actions from ``state`` reaches a state satisfying ``goal``. """
    state_soln: State = state
    for action in soln:
        state_soln = domain.next_state([state_soln], [action])[0][0]

    return domain.is_solved([state_soln], [goal])[0]
```
