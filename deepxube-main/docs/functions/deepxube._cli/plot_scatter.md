---
id: "func:deepxube._cli.plot_scatter"
kind: "function"
name: "plot_scatter"
qualified_name: "deepxube._cli.plot_scatter"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 33
line_end: 42
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "ax"
    annotation: "Axes"
    default: null
  - name: "x"
    annotation: "Any"
    default: null
  - name: "y"
    annotation: "Any"
    default: null
  - name: "x_label"
    annotation: "str"
    default: null
  - name: "y_label"
    annotation: "str"
    default: null
  - name: "xy_line"
    annotation: "bool"
    default: null
  - name: "alpha"
    annotation: "float"
    default: "1.0"
  - name: "title"
    annotation: "str"
    default: "''"
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "ax.scatter"
    call_sites: [35]
  - target: null
    expr: "ax.set_xlabel"
    call_sites: [36]
  - target: null
    expr: "ax.set_ylabel"
    call_sites: [37]
  - target: "func:numpy.linspace"
    expr: "np.linspace"
    call_sites: [39]
  - target: null
    expr: "max"
    call_sites: [39]
  - target: null
    expr: "x.max"
    call_sites: [39]
  - target: null
    expr: "y.max"
    call_sites: [39]
  - target: null
    expr: "ax.plot"
    call_sites: [40]
  - target: null
    expr: "ax.set_title"
    call_sites: [41]
  - target: null
    expr: "ax.grid"
    call_sites: [42]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.plot_scatter`

**File:** [deepxube/_cli.py:33](../../../../deepxube/_cli.py#L33)
**Visibility:** public
**Kind:** function

## Signature

```python
def plot_scatter(ax: Axes, x: Any, y: Any, x_label: str, y_label: str, xy_line: bool, alpha: float = 1.0, title: str = '') -> None
```

## Docstring

Scatter-plot ``x`` vs ``y`` on ``ax`` with optional identity line and labels. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `ax` | `Axes` | — |
| `x` | `Any` | — |
| `y` | `Any` | — |
| `x_label` | `str` | — |
| `y_label` | `str` | — |
| `xy_line` | `bool` | — |
| `alpha` | `float` | `1.0` |
| `title` | `str` | `''` |

## Returns

`None`

## Calls

- `np.linspace` → `func:numpy.linspace` (lines: 39)

### Unresolved
- `ax.scatter` (lines: 35)
- `ax.set_xlabel` (lines: 36)
- `ax.set_ylabel` (lines: 37)
- `max` (lines: 39)
- `x.max` (lines: 39)
- `y.max` (lines: 39)
- `ax.plot` (lines: 40)
- `ax.set_title` (lines: 41)
- `ax.grid` (lines: 42)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def plot_scatter(ax: Axes, x: Any, y: Any, x_label: str, y_label: str, xy_line: bool, alpha: float = 1.0, title: str = "") -> None:
    """ Scatter-plot ``x`` vs ``y`` on ``ax`` with optional identity line and labels. """
    ax.scatter(x, y, s=10, alpha=alpha)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if xy_line:
        np.linspace(0, max(x.max(), y.max()), 100)
        ax.plot(x, x, color='k', ls="--")
    ax.set_title(title)
    ax.grid(True)
```
