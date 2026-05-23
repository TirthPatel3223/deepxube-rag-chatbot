---
id: "func:deepxube.base.domain.GoalFixed.sample_goals"
kind: "method"
name: "sample_goals"
qualified_name: "deepxube.base.domain.GoalFixed.sample_goals"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 371
line_end: 373
class: "GoalFixed"
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
returns: "List[G]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.GoalFixed.get_goal"
    expr: "self.get_goal"
    call_sites: [373]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.GoalFixed.sample_goals`

**File:** [deepxube/base/domain.py:371](../../../../deepxube/base/domain.py#L371)
**Class:** `GoalFixed`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goals(self, num: int) -> List[G]
```

## Docstring

:return: ``num`` copies of the fixed goal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`List[G]`

## Calls

- `self.get_goal` → `func:deepxube.base.domain.GoalFixed.get_goal` (lines: 373)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_goals(self, num: int) -> List[G]:
        """ :return: ``num`` copies of the fixed goal. """
        return [self.get_goal()] * num
```
