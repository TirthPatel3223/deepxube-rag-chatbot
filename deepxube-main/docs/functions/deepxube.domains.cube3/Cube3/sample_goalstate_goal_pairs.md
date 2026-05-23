---
id: "func:deepxube.domains.cube3.Cube3.sample_goalstate_goal_pairs"
kind: "method"
name: "sample_goalstate_goal_pairs"
qualified_name: "deepxube.domains.cube3.Cube3.sample_goalstate_goal_pairs"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 550
line_end: 555
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
  - name: "num"
    annotation: "int"
    default: null
returns: "Tuple[List[Cube3State], List[Cube3Goal]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.Cube3State"
    expr: "Cube3State"
    call_sites: [552]
  - target: null
    expr: "self.goal_colors.copy"
    call_sites: [552, 553]
  - target: "func:deepxube.domains.cube3.Cube3Goal"
    expr: "Cube3Goal"
    call_sites: [553]
raises: []
reads_attrs:
  - "self.goal_colors"
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.sample_goalstate_goal_pairs`

**File:** [deepxube/domains/cube3.py:550](../../../../deepxube/domains/cube3.py#L550)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[Cube3State], List[Cube3Goal]]
```

## Docstring

:return: ``num`` pairs of the solved state and matching goal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`Tuple[List[Cube3State], List[Cube3Goal]]`

## Calls

- `Cube3State` → `func:deepxube.domains.cube3.Cube3State` (lines: 552)
- `Cube3Goal` → `func:deepxube.domains.cube3.Cube3Goal` (lines: 553)

### Unresolved
- `self.goal_colors.copy` (lines: 552, 553)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.goal_colors`

## Source

```python
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[Cube3State], List[Cube3Goal]]:
        """ :return: ``num`` pairs of the solved state and matching goal. """
        states_goal: List[Cube3State] = [Cube3State(self.goal_colors.copy())] * num
        goals: List[Cube3Goal] = [Cube3Goal(self.goal_colors.copy())] * num

        return states_goal, goals
```
