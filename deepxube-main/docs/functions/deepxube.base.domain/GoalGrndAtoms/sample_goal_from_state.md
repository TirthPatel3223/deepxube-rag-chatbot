---
id: "func:deepxube.base.domain.GoalGrndAtoms.sample_goal_from_state"
kind: "method"
name: "sample_goal_from_state"
qualified_name: "deepxube.base.domain.GoalGrndAtoms.sample_goal_from_state"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 675
line_end: 685
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
  - name: "states_start"
    annotation: "Optional[List[S]]"
    default: null
  - name: "states_goal"
    annotation: "List[S]"
    default: null
returns: "List[G]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.GoalGrndAtoms.state_to_model"
    expr: "self.state_to_model"
    call_sites: [679]
  - target: null
    expr: "np.random.rand"
    call_sites: [680]
  - target: null
    expr: "len"
    call_sites: [680]
  - target: null
    expr: "zip"
    call_sites: [681]
  - target: "func:deepxube.utils.misc_utils.random_subset"
    expr: "misc_utils.random_subset"
    call_sites: [682]
  - target: null
    expr: "models_g.append"
    call_sites: [683]
  - target: null
    expr: "frozenset"
    call_sites: [683]
  - target: "func:deepxube.base.domain.GoalGrndAtoms.model_to_goal"
    expr: "self.model_to_goal"
    call_sites: [685]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.GoalGrndAtoms.sample_goal_from_state`

**File:** [deepxube/base/domain.py:675](../../../../deepxube/base/domain.py#L675)
**Class:** `GoalGrndAtoms`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goal_from_state(self, states_start: Optional[List[S]], states_goal: List[S]) -> List[G]
```

## Docstring

Build a goal by randomly subsetting the state's ground-atom model (HER-style relabelling). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_start` | `Optional[List[S]]` | — |
| `states_goal` | `List[S]` | — |

## Returns

`List[G]`

## Calls

- `self.state_to_model` → `func:deepxube.base.domain.GoalGrndAtoms.state_to_model` (lines: 679)
- `misc_utils.random_subset` → `func:deepxube.utils.misc_utils.random_subset` (lines: 682)
- `self.model_to_goal` → `func:deepxube.base.domain.GoalGrndAtoms.model_to_goal` (lines: 685)

### Unresolved
- `np.random.rand` (lines: 680)
- `len` (lines: 680)
- `zip` (lines: 681)
- `models_g.append` (lines: 683)
- `frozenset` (lines: 683)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_goal_from_state(self, states_start: Optional[List[S]], states_goal: List[S]) -> List[G]:
        """ Build a goal by randomly subsetting the state's ground-atom model (HER-style relabelling). """
        models_g: List[Model] = []

        models_s: List[Model] = self.state_to_model(states_goal)
        keep_probs: NDArray[np.float64] = np.random.rand(len(states_goal))
        for model_s, keep_prob in zip(models_s, keep_probs):
            rand_subset: Set[Atom] = misc_utils.random_subset(model_s, keep_prob)
            models_g.append(frozenset(rand_subset))

        return self.model_to_goal(models_g)
```
