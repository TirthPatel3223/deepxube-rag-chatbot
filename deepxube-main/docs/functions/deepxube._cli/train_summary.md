---
id: "func:deepxube._cli.train_summary"
kind: "function"
name: "train_summary"
qualified_name: "deepxube._cli.train_summary"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 248
line_end: 280
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "args"
    annotation: "argparse.Namespace"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:pickle.load"
    expr: "pickle.load"
    call_sites: [251]
  - target: null
    expr: "open"
    call_sites: [251]
  - target: null
    expr: "sorted"
    call_sites: [254]
  - target: null
    expr: "itr_to_in_out.keys"
    call_sites: [254]
  - target: "func:matplotlib.pyplot.subplots"
    expr: "plt.subplots"
    call_sites: [255]
  - target: null
    expr: "axs_np.flatten().tolist"
    call_sites: [256]
  - target: null
    expr: "axs_np.flatten"
    call_sites: [256]
  - target: "func:matplotlib.pyplot.subplots_adjust"
    expr: "plt.subplots_adjust"
    call_sites: [257]
  - target: null
    expr: "fig.add_axes"
    call_sites: [258]
  - target: "func:matplotlib.widgets.Slider"
    expr: "Slider"
    call_sites: [259]
  - target: null
    expr: "len"
    call_sites: [263]
  - target: null
    expr: "min"
    call_sites: [268]
  - target: "func:deepxube._cli.plot_itr_data"
    expr: "plot_itr_data"
    call_sites: [269, 275]
  - target: null
    expr: "int"
    call_sites: [272]
  - target: null
    expr: "ax.cla"
    call_sites: [274]
  - target: null
    expr: "fig.canvas.draw"
    call_sites: [276]
  - target: null
    expr: "step_slider.on_changed"
    call_sites: [278]
  - target: null
    expr: "fig.tight_layout"
    call_sites: [279]
  - target: "func:matplotlib.pyplot.show"
    expr: "plt.show"
    call_sites: [280]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.train_summary`

**File:** [deepxube/_cli.py:248](../../../../deepxube/_cli.py#L248)
**Visibility:** public
**Kind:** function

## Signature

```python
def train_summary(args: argparse.Namespace) -> None
```

## Docstring

Load a training summary pickle and show an interactive 6-panel matplotlib figure with an iteration slider. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `pickle.load` → `func:pickle.load` (lines: 251)
- `plt.subplots` → `func:matplotlib.pyplot.subplots` (lines: 255)
- `plt.subplots_adjust` → `func:matplotlib.pyplot.subplots_adjust` (lines: 257)
- `Slider` → `func:matplotlib.widgets.Slider` (lines: 259)
- `plot_itr_data` → `func:deepxube._cli.plot_itr_data` (lines: 269, 275)
- `plt.show` → `func:matplotlib.pyplot.show` (lines: 280)

### Unresolved
- `open` (lines: 251)
- `sorted` (lines: 254)
- `itr_to_in_out.keys` (lines: 254)
- `axs_np.flatten().tolist` (lines: 256)
- `axs_np.flatten` (lines: 256)
- `fig.add_axes` (lines: 258)
- `len` (lines: 263)
- `min` (lines: 268)
- `int` (lines: 272)
- `ax.cla` (lines: 274)
- `fig.canvas.draw` (lines: 276)
- `step_slider.on_changed` (lines: 278)
- `fig.tight_layout` (lines: 279)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def train_summary(args: argparse.Namespace) -> None:
    """ Load a training summary pickle and show an interactive 6-panel matplotlib figure with an iteration slider. """
    status_file: str = f"{args.dir}/{args.type}_train_summary.pkl"
    train_summ: TrainSummary = pickle.load(open(status_file, "rb"))
    itr_to_in_out: Dict[int, Tuple[NDArray, NDArray]] = train_summ.itr_to_in_out
    itr_to_steps_to_pathfindperf: Dict[int, Dict[int, Dict]] = train_summ.itr_to_steps_to_pathfindstats
    itrs: List[int] = sorted(itr_to_in_out.keys())
    fig, axs_np = plt.subplots(3, 2)
    axs: List[Axes] = axs_np.flatten().tolist()
    plt.subplots_adjust(bottom=0.2)
    axstep = fig.add_axes((0.2, 0.01, 0.65, 0.03))
    step_slider: Slider = Slider(
        ax=axstep,
        label='',
        valmin=0,
        valmax=len(itrs) - 1,
        valinit=0,
        valstep=1,
    )

    itr_init: int = min(itrs)
    plot_itr_data(axs, step_slider, itr_init, itr_to_in_out, itr_to_steps_to_pathfindperf)

    def update(idx: float) -> None:
        itr: int = itrs[int(idx)]
        for ax in axs:
            ax.cla()
        plot_itr_data(axs, step_slider, itr, itr_to_in_out, itr_to_steps_to_pathfindperf)
        fig.canvas.draw()

    step_slider.on_changed(update)
    fig.tight_layout()
    plt.show()
```
