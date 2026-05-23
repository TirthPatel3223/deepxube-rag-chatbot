---
id: "func:deepxube.domains.cube3.Cube3.visualize_state_goal"
kind: "method"
name: "visualize_state_goal"
qualified_name: "deepxube.domains.cube3.Cube3.visualize_state_goal"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 578
line_end: 581
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
  - name: "state"
    annotation: "Cube3State"
    default: null
  - name: "goal"
    annotation: "Cube3Goal"
    default: null
  - name: "fig"
    annotation: "Figure"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.InteractiveCube"
    expr: "InteractiveCube"
    call_sites: [580]
  - target: null
    expr: "fig.add_axes"
    call_sites: [581]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.visualize_state_goal`

**File:** [deepxube/domains/cube3.py:578](../../../../deepxube/domains/cube3.py#L578)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def visualize_state_goal(self, state: Cube3State, goal: Cube3Goal, fig: Figure) -> None
```

## Docstring

Render the cube state as an ``InteractiveCube`` on ``fig``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `state` | `Cube3State` | — |
| `goal` | `Cube3Goal` | — |
| `fig` | `Figure` | — |

## Returns

`None`

## Calls

- `InteractiveCube` → `func:deepxube.domains.cube3.InteractiveCube` (lines: 580)

### Unresolved
- `fig.add_axes` (lines: 581)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def visualize_state_goal(self, state: Cube3State, goal: Cube3Goal, fig: Figure) -> None:
        """ Render the cube state as an ``InteractiveCube`` on ``fig``. """
        interactive_cube: InteractiveCube = InteractiveCube(3, state.colors)
        fig.add_axes(interactive_cube)
```
