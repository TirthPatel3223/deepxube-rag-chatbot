---
id: "func:deepxube._cli.plot_itr_data"
kind: "function"
name: "plot_itr_data"
qualified_name: "deepxube._cli.plot_itr_data"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 229
line_end: 245
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "axs"
    annotation: "List[Axes]"
    default: null
  - name: "step_slider"
    annotation: "Slider"
    default: null
  - name: "itr"
    annotation: "int"
    default: null
  - name: "itr_to_in_out"
    annotation: "Dict[int, Tuple[NDArray, NDArray]]"
    default: null
  - name: "itr_to_steps_to_pathfindstats"
    annotation: "Dict[int, Dict[int, Dict]]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "sorted"
    call_sites: [233]
  - target: null
    expr: "steps_to_pathfindperf.keys"
    call_sites: [233]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [237]
  - target: "func:deepxube._cli.plot_scatter"
    expr: "plot_scatter"
    call_sites: [239, 240, 241, 242, 243, 244]
  - target: null
    expr: "step_slider.valtext.set_text"
    call_sites: [245]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.plot_itr_data`

**File:** [deepxube/_cli.py:229](../../../../deepxube/_cli.py#L229)
**Visibility:** public
**Kind:** function

## Signature

```python
def plot_itr_data(axs: List[Axes], step_slider: Slider, itr: int, itr_to_in_out: Dict[int, Tuple[NDArray, NDArray]], itr_to_steps_to_pathfindstats: Dict[int, Dict[int, Dict]]) -> None
```

## Docstring

Populate the 6-panel training-summary figure for a single iteration. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `axs` | `List[Axes]` | — |
| `step_slider` | `Slider` | — |
| `itr` | `int` | — |
| `itr_to_in_out` | `Dict[int, Tuple[NDArray, NDArray]]` | — |
| `itr_to_steps_to_pathfindstats` | `Dict[int, Dict[int, Dict]]` | — |

## Returns

`None`

## Calls

- `np.mean` → `func:numpy.mean` (lines: 237)
- `plot_scatter` → `func:deepxube._cli.plot_scatter` (lines: 239, 240, 241, 242, 243, 244)

### Unresolved
- `sorted` (lines: 233)
- `steps_to_pathfindperf.keys` (lines: 233)
- `step_slider.valtext.set_text` (lines: 245)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def plot_itr_data(axs: List[Axes], step_slider: Slider, itr: int, itr_to_in_out: Dict[int, Tuple[NDArray, NDArray]],
                  itr_to_steps_to_pathfindstats: Dict[int, Dict[int, Dict]]) -> None:
    """ Populate the 6-panel training-summary figure for a single iteration. """
    steps_to_pathfindperf: Dict[int, Dict] = itr_to_steps_to_pathfindstats[itr]
    steps_at_itr: List[int] = sorted(steps_to_pathfindperf.keys())
    per_solved: List[float] = [steps_to_pathfindperf[step]["per_solved"] for step in steps_at_itr]
    path_costs: List[float] = [steps_to_pathfindperf[step]["path_costs"] for step in steps_at_itr]
    search_itrs: List[float] = [steps_to_pathfindperf[step]["search_itrs"] for step in steps_at_itr]
    targets: List[float] = [np.mean(steps_to_pathfindperf[step]["ctgs_backup"]) for step in steps_at_itr]
    num_instances: List[int] = [steps_to_pathfindperf[step]["num_instances"] for step in steps_at_itr]
    plot_scatter(axs[0], steps_at_itr, per_solved, "Step", "Percent Solved", False)
    plot_scatter(axs[1], steps_at_itr, path_costs, "Step", "Path Costs", False)
    plot_scatter(axs[2], steps_at_itr, search_itrs, "Step", "Search Iterations", False)
    plot_scatter(axs[3], steps_at_itr, targets, "Step", "Cost-to-Go Targets", False)
    plot_scatter(axs[4], steps_at_itr, num_instances, "Step", "# Instances", False)
    plot_scatter(axs[5], itr_to_in_out[itr][0], itr_to_in_out[itr][1], "Target", "Prediction", True, alpha=0.2)
    step_slider.valtext.set_text(f"Iteration {itr}")
```
