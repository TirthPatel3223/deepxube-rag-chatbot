---
id: "func:deepxube.base.domain.GoalStartRevWalkableActsRev.random_walk_rev"
kind: "method"
name: "random_walk_rev"
qualified_name: "deepxube.base.domain.GoalStartRevWalkableActsRev.random_walk_rev"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 475
line_end: 477
class: "GoalStartRevWalkableActsRev"
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
returns: "List[S]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.GoalStartRevWalkableActsRev.random_walk"
    expr: "self.random_walk"
    call_sites: [477]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.GoalStartRevWalkableActsRev.random_walk_rev`

**File:** [deepxube/base/domain.py:475](../../../../deepxube/base/domain.py#L475)
**Class:** `GoalStartRevWalkableActsRev`
**Visibility:** public
**Kind:** method

## Signature

```python
def random_walk_rev(self, states: List[S], num_steps_l: List[int]) -> List[S]
```

## Docstring

Forward random walk that doubles as a reverse walk via action reversibility. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |
| `num_steps_l` | `List[int]` | — |

## Returns

`List[S]`

## Calls

- `self.random_walk` → `func:deepxube.base.domain.GoalStartRevWalkableActsRev.random_walk` (lines: 477)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def random_walk_rev(self, states: List[S], num_steps_l: List[int]) -> List[S]:
        """ Forward random walk that doubles as a reverse walk via action reversibility. """
        return self.random_walk(states, num_steps_l)[0]
```
