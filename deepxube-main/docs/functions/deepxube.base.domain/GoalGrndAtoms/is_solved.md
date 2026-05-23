---
id: "func:deepxube.base.domain.GoalGrndAtoms.is_solved"
kind: "method"
name: "is_solved"
qualified_name: "deepxube.base.domain.GoalGrndAtoms.is_solved"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 659
line_end: 673
class: "GoalGrndAtoms"
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
  - name: "goals"
    annotation: "List[G]"
    default: null
returns: "List[bool]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.GoalGrndAtoms.goal_to_model"
    expr: "self.goal_to_model"
    call_sites: [667]
  - target: "func:deepxube.base.domain.GoalGrndAtoms.state_to_model"
    expr: "self.state_to_model"
    call_sites: [669]
  - target: null
    expr: "zip"
    call_sites: [670]
  - target: null
    expr: "is_solved_l.append"
    call_sites: [671]
  - target: null
    expr: "model_goal.issubset"
    call_sites: [671]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.GoalGrndAtoms.is_solved`

**File:** [deepxube/base/domain.py:659](../../../../deepxube/base/domain.py#L659)
**Class:** `GoalGrndAtoms`
**Visibility:** public
**Kind:** method

## Signature

```python
def is_solved(self, states: List[S], goals: List[G]) -> List[bool]
```

## Docstring

Returns whether or not state is solved

:param states: List of states
:param goals: List of goals
:return: Boolean numpy array where the element at index i corresponds to whether or not the
state at index i is solved

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[S]` | — |
| `goals` | `List[G]` | — |

## Returns

`List[bool]`

## Calls

- `self.goal_to_model` → `func:deepxube.base.domain.GoalGrndAtoms.goal_to_model` (lines: 667)
- `self.state_to_model` → `func:deepxube.base.domain.GoalGrndAtoms.state_to_model` (lines: 669)

### Unresolved
- `zip` (lines: 670)
- `is_solved_l.append` (lines: 671)
- `model_goal.issubset` (lines: 671)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def is_solved(self, states: List[S], goals: List[G]) -> List[bool]:
        """ Returns whether or not state is solved

        :param states: List of states
        :param goals: List of goals
        :return: Boolean numpy array where the element at index i corresponds to whether or not the
        state at index i is solved
        """
        models_g: List[Model] = self.goal_to_model(goals)
        is_solved_l: List[bool] = []
        models_s: List[Model] = self.state_to_model(states)
        for model_state, model_goal in zip(models_s, models_g):
            is_solved_l.append(model_goal.issubset(model_state))

        return is_solved_l
```
