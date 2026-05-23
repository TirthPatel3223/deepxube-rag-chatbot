---
id: "func:deepxube.base.domain.NextStateNPActsFixed._sample_state_np_action"
kind: "method"
name: "_sample_state_np_action"
qualified_name: "deepxube.base.domain.NextStateNPActsFixed._sample_state_np_action"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 592
line_end: 594
class: "NextStateNPActsFixed"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_np"
    annotation: "List[NDArray]"
    default: null
returns: "List[A]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.domain.NextStateNPActsFixed.sample_action"
    expr: "self.sample_action"
    call_sites: [594]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.domain.NextStateNPActsFixed._sample_state_np_action`

**File:** [deepxube/base/domain.py:592](../../../../deepxube/base/domain.py#L592)
**Class:** `NextStateNPActsFixed`
**Visibility:** private
**Kind:** method

## Signature

```python
def _sample_state_np_action(self, states_np: List[NDArray]) -> List[A]
```

## Docstring

Sample one action per row from the fixed action set. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `List[NDArray]` | — |

## Returns

`List[A]`

## Calls

- `self.sample_action` → `func:deepxube.base.domain.NextStateNPActsFixed.sample_action` (lines: 594)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _sample_state_np_action(self, states_np: List[NDArray]) -> List[A]:
        """ Sample one action per row from the fixed action set. """
        return self.sample_action(states_np[0].shape[0])
```
