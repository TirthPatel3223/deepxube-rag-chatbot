---
id: "func:deepxube.domains.sokoban.Sokoban.visualize_state_goal"
kind: "method"
name: "visualize_state_goal"
qualified_name: "deepxube.domains.sokoban.Sokoban.visualize_state_goal"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 272
line_end: 277
class: "Sokoban"
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
    annotation: "SkState"
    default: null
  - name: "goal"
    annotation: "SkGoal"
    default: null
  - name: "fig"
    annotation: "Figure"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.sokoban.Sokoban.to_img"
    expr: "self.to_img"
    call_sites: [274]
  - target: null
    expr: "fig.add_subplot"
    call_sites: [276]
  - target: null
    expr: "ax.imshow"
    call_sites: [277]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban.Sokoban.visualize_state_goal`

**File:** [deepxube/domains/sokoban.py:272](../../../../deepxube/domains/sokoban.py#L272)
**Class:** `Sokoban`
**Visibility:** public
**Kind:** method

## Signature

```python
def visualize_state_goal(self, state: SkState, goal: SkGoal, fig: Figure) -> None
```

## Docstring

Render the board as an RGB image and display it on ``fig``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `state` | `SkState` | — |
| `goal` | `SkGoal` | — |
| `fig` | `Figure` | — |

## Returns

`None`

## Calls

- `self.to_img` → `func:deepxube.domains.sokoban.Sokoban.to_img` (lines: 274)

### Unresolved
- `fig.add_subplot` (lines: 276)
- `ax.imshow` (lines: 277)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def visualize_state_goal(self, state: SkState, goal: SkGoal, fig: Figure) -> None:
        """ Render the board as an RGB image and display it on ``fig``. """
        room_rgb = self.to_img(state, goal)

        ax = fig.add_subplot(111)
        ax.imshow(room_rgb)
```
