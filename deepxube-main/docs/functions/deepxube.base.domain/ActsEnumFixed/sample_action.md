---
id: "func:deepxube.base.domain.ActsEnumFixed.sample_action"
kind: "method"
name: "sample_action"
qualified_name: "deepxube.base.domain.ActsEnumFixed.sample_action"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 296
line_end: 299
class: "ActsEnumFixed"
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
returns: "List[A]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.ActsEnumFixed.get_actions_fixed"
    expr: "self.get_actions_fixed"
    call_sites: [298]
  - target: "func:random.choice"
    expr: "random.choice"
    call_sites: [299]
  - target: null
    expr: "range"
    call_sites: [299]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.ActsEnumFixed.sample_action`

**File:** [deepxube/base/domain.py:296](../../../../deepxube/base/domain.py#L296)
**Class:** `ActsEnumFixed`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_action(self, num: int) -> List[A]
```

## Docstring

:return: ``num`` actions sampled uniformly from the fixed action list. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`List[A]`

## Calls

- `self.get_actions_fixed` → `func:deepxube.base.domain.ActsEnumFixed.get_actions_fixed` (lines: 298)
- `random.choice` → `func:random.choice` (lines: 299)

### Unresolved
- `range` (lines: 299)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def sample_action(self, num: int) -> List[A]:
        """ :return: ``num`` actions sampled uniformly from the fixed action list. """
        actions_fixed: List[A] = self.get_actions_fixed()
        return [random.choice(actions_fixed) for _ in range(num)]
```
