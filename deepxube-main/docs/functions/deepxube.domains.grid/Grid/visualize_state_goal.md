---
id: "func:deepxube.domains.grid.Grid.visualize_state_goal"
kind: "method"
name: "visualize_state_goal"
qualified_name: "deepxube.domains.grid.Grid.visualize_state_goal"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 126
line_end: 133
class: "Grid"
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
    annotation: "GridState"
    default: null
  - name: "goal"
    annotation: "GridGoal"
    default: null
  - name: "fig"
    annotation: "Figure"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:matplotlib.pyplot.axes"
    expr: "plt.axes"
    call_sites: [128]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [129]
  - target: null
    expr: "ax.imshow"
    call_sites: [132]
  - target: "func:matplotlib.colors.ListedColormap"
    expr: "ListedColormap"
    call_sites: [132]
  - target: null
    expr: "fig.add_axes"
    call_sites: [133]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.grid.Grid.visualize_state_goal`

**File:** [deepxube/domains/grid.py:126](../../../../deepxube/domains/grid.py#L126)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def visualize_state_goal(self, state: GridState, goal: GridGoal, fig: Figure) -> None
```

## Docstring

Draw the grid with robot (1=black) and goal (2=green) on ``fig``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `state` | `GridState` | — |
| `goal` | `GridGoal` | — |
| `fig` | `Figure` | — |

## Returns

`None`

## Calls

- `plt.axes` → `func:matplotlib.pyplot.axes` (lines: 128)
- `np.zeros` → `func:numpy.zeros` (lines: 129)
- `ListedColormap` → `func:matplotlib.colors.ListedColormap` (lines: 132)

### Unresolved
- `ax.imshow` (lines: 132)
- `fig.add_axes` (lines: 133)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def visualize_state_goal(self, state: GridState, goal: GridGoal, fig: Figure) -> None:
        """ Draw the grid with robot (1=black) and goal (2=green) on ``fig``. """
        ax = plt.axes()
        grid: NDArray = np.zeros((self.dim, self.dim))
        grid[goal.robot_x, goal.robot_y] = 2
        grid[state.robot_x, state.robot_y] = 1
        ax.imshow(grid, cmap=ListedColormap(["white", "black", "green"]), origin="upper")
        fig.add_axes(ax)
```
