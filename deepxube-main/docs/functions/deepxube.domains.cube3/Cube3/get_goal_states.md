---
id: "func:deepxube.domains.cube3.Cube3.get_goal_states"
kind: "method"
name: "get_goal_states"
qualified_name: "deepxube.domains.cube3.Cube3.get_goal_states"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 546
line_end: 548
class: "Cube3"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num_states"
    annotation: "int"
    default: null
returns: "List[Cube3State]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.Cube3State"
    expr: "Cube3State"
    call_sites: [548]
  - target: null
    expr: "self.goal_colors.copy"
    call_sites: [548]
  - target: null
    expr: "range"
    call_sites: [548]
raises: []
reads_attrs:
  - "self.goal_colors"
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.get_goal_states`

**File:** [deepxube/domains/cube3.py:546](../../../../deepxube/domains/cube3.py#L546)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_goal_states(self, num_states: int) -> List[Cube3State]
```

## Docstring

:return: ``num_states`` copies of the solved cube state. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_states` | `int` | — |

## Returns

`List[Cube3State]`

## Calls

- `Cube3State` → `func:deepxube.domains.cube3.Cube3State` (lines: 548)

### Unresolved
- `self.goal_colors.copy` (lines: 548)
- `range` (lines: 548)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.goal_colors`

## Source

```python
    def get_goal_states(self, num_states: int) -> List[Cube3State]:
        """ :return: ``num_states`` copies of the solved cube state. """
        return [Cube3State(self.goal_colors.copy()) for _ in range(num_states)]
```
