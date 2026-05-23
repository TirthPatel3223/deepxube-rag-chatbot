---
id: "func:deepxube.domains.lightsout.LightsOut.sample_goalstate_goal_pairs"
kind: "method"
name: "sample_goalstate_goal_pairs"
qualified_name: "deepxube.domains.lightsout.LightsOut.sample_goalstate_goal_pairs"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 91
line_end: 96
class: "LightsOut"
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
returns: "Tuple[List[LOState], List[LOGoal]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.lightsout.LOState"
    expr: "LOState"
    call_sites: [93]
  - target: null
    expr: "self.goal_np.copy"
    call_sites: [93, 94]
  - target: "func:deepxube.domains.lightsout.LOGoal"
    expr: "LOGoal"
    call_sites: [94]
raises: []
reads_attrs:
  - "self.goal_np"
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut.sample_goalstate_goal_pairs`

**File:** [deepxube/domains/lightsout.py:91](../../../../deepxube/domains/lightsout.py#L91)
**Class:** `LightsOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[LOState], List[LOGoal]]
```

## Docstring

:return: ``num`` pairs of all-zeros goal states and matching goals. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`Tuple[List[LOState], List[LOGoal]]`

## Calls

- `LOState` → `func:deepxube.domains.lightsout.LOState` (lines: 93)
- `LOGoal` → `func:deepxube.domains.lightsout.LOGoal` (lines: 94)

### Unresolved
- `self.goal_np.copy` (lines: 93, 94)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.goal_np`

## Source

```python
    def sample_goalstate_goal_pairs(self, num: int) -> Tuple[List[LOState], List[LOGoal]]:
        """ :return: ``num`` pairs of all-zeros goal states and matching goals. """
        states_goal: List[LOState] = [LOState(self.goal_np.copy())] * num
        goals: List[LOGoal] = [LOGoal(self.goal_np.copy())] * num

        return states_goal, goals
```
