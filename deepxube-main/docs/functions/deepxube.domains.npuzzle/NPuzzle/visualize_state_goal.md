---
id: "func:deepxube.domains.npuzzle.NPuzzle.visualize_state_goal"
kind: "method"
name: "visualize_state_goal"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.visualize_state_goal"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 191
line_end: 222
class: "NPuzzle"
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
    annotation: "NPState"
    default: null
  - name: "goal"
    annotation: "NPGoal"
    default: null
  - name: "fig"
    annotation: "Figure"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "fig.add_subplot"
    call_sites: [193]
  - target: null
    expr: "enumerate"
    call_sites: [200]
  - target: null
    expr: "int"
    call_sites: [202]
  - target: "func:numpy.floor"
    expr: "np.floor"
    call_sites: [202]
  - target: null
    expr: "float"
    call_sites: [205, 206, 207, 208]
  - target: null
    expr: "ax.add_patch"
    call_sites: [210]
  - target: "func:matplotlib.patches.Rectangle"
    expr: "patches.Rectangle"
    call_sites: [210]
  - target: null
    expr: "str"
    call_sites: [218]
  - target: null
    expr: "ax.text"
    call_sites: [219]
  - target: null
    expr: "fig.canvas.draw"
    call_sites: [222]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.visualize_state_goal`

**File:** [deepxube/domains/npuzzle.py:191](../../../../deepxube/domains/npuzzle.py#L191)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def visualize_state_goal(self, state: NPState, goal: NPGoal, fig: Figure) -> None
```

## Docstring

Draw the tile grid on ``fig`` with tile numbers; the blank tile is left empty. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `state` | `NPState` | — |
| `goal` | `NPGoal` | — |
| `fig` | `Figure` | — |

## Returns

`None`

## Calls

- `np.floor` → `func:numpy.floor` (lines: 202)
- `patches.Rectangle` → `func:matplotlib.patches.Rectangle` (lines: 210)

### Unresolved
- `fig.add_subplot` (lines: 193)
- `enumerate` (lines: 200)
- `int` (lines: 202)
- `float` (lines: 205, 206, 207, 208)
- `ax.add_patch` (lines: 210)
- `str` (lines: 218)
- `ax.text` (lines: 219)
- `fig.canvas.draw` (lines: 222)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def visualize_state_goal(self, state: NPState, goal: NPGoal, fig: Figure) -> None:
        """ Draw the tile grid on ``fig`` with tile numbers; the blank tile is left empty. """
        ax = fig.add_subplot(111)
        # fig = plt.figure(figsize=(.64, .64))
        # ax = fig.gca()
        # fig.add_axes(ax)

        state_np: NDArray[int_t] = state.tiles

        for square_idx, square in enumerate(state_np):
            color = 'white'
            x_pos = int(np.floor(square_idx / self.dim))
            y_pos = square_idx % self.dim

            left = y_pos / float(self.dim)
            right = left + 1.0 / float(self.dim)
            top = (self.dim - x_pos - 1) / float(self.dim)
            bottom = top + 1.0 / float(self.dim)

            ax.add_patch(patches.Rectangle((left, top), 1.0 / self.dim, 1.0 / self.dim, linewidth=1,
                                           edgecolor='k', facecolor=color))

            if square != 0:
                sqr_txt: str
                if square == (self.dim ** 2):
                    sqr_txt = "-"
                else:
                    sqr_txt = str(square)
                ax.text(0.5 * (left + right), 0.5 * (bottom + top), sqr_txt, horizontalalignment='center',
                        verticalalignment='center', fontsize=12, color='black', transform=ax.transAxes)

        fig.canvas.draw()
```
