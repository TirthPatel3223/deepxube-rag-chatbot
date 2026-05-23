---
id: "func:deepxube.domains.cube3.InteractiveCube.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.cube3.InteractiveCube.__init__"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 263
line_end: 341
class: "InteractiveCube"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "n"
    annotation: null
    default: null
  - name: "colors"
    annotation: "NDArray"
    default: null
  - name: "view"
    annotation: null
    default: "(0, 0, 10)"
  - name: "fig"
    annotation: null
    default: "None"
  - name: "**kwargs"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:numpy.eye"
    expr: "np.eye"
    call_sites: [268]
  - target: null
    expr: "Quaternion.from_v_theta"
    call_sites: [269, 270, 279]
  - target: "func:numpy.asarray"
    expr: "np.asarray"
    call_sites: [269, 270, 279]
  - target: "func:matplotlib.pyplot.gcf"
    expr: "plt.gcf"
    call_sites: [285]
  - target: null
    expr: "kwargs.update"
    call_sites: [292]
  - target: null
    expr: "dict"
    call_sites: [292]
  - target: null
    expr: "kwargs.get"
    call_sites: [292, 293, 294, 295, 296, 297]
  - target: null
    expr: "super(InteractiveCube, self).__init__"
    call_sites: [298]
  - target: null
    expr: "super"
    call_sites: [298]
  - target: null
    expr: "self.xaxis.set_major_formatter"
    call_sites: [299]
  - target: "func:matplotlib.pyplot.NullFormatter"
    expr: "plt.NullFormatter"
    call_sites: [299, 300]
  - target: null
    expr: "self.yaxis.set_major_formatter"
    call_sites: [300]
  - target: "func:deepxube.domains.cube3.InteractiveCube._initialize_arrays"
    expr: "self._initialize_arrays"
    call_sites: [332]
  - target: null
    expr: "self.figure.canvas.mpl_connect"
    call_sites: [334, 336, 338]
  - target: "func:deepxube.domains.cube3.InteractiveCube._draw_cube"
    expr: "self._draw_cube"
    call_sites: [341]
raises: []
reads_attrs:
  - "self.N"
  - "self._active"
  - "self._ax_LR"
  - "self._ax_LR_alt"
  - "self._ax_UD"
  - "self._black_stickers"
  - "self._button1"
  - "self._button2"
  - "self._current_rot"
  - "self._face_polys"
  - "self._grey_stickers"
  - "self._mouse_motion"
  - "self._mouse_press"
  - "self._mouse_release"
  - "self._move_list"
  - "self._prevStates"
  - "self._start_rot"
  - "self._start_xlim"
  - "self._start_ylim"
  - "self._step_LR"
  - "self._step_UD"
  - "self._sticker_polys"
  - "self._tab"
  - "self._view"
  - "self.colors"
  - "self.face_colors"
  - "self.figure"
  - "self.plastic_color"
  - "self.rots"
  - "self.xaxis"
  - "self.yaxis"
writes_attrs:
  - "self.N"
  - "self._active"
  - "self._ax_LR"
  - "self._ax_LR_alt"
  - "self._ax_UD"
  - "self._black_stickers"
  - "self._button1"
  - "self._button2"
  - "self._current_rot"
  - "self._face_polys"
  - "self._grey_stickers"
  - "self._move_list"
  - "self._prevStates"
  - "self._start_rot"
  - "self._start_xlim"
  - "self._start_ylim"
  - "self._step_LR"
  - "self._step_UD"
  - "self._sticker_polys"
  - "self._tab"
  - "self._view"
  - "self.colors"
  - "self.face_colors"
  - "self.plastic_color"
  - "self.rots"
---

# `deepxube.domains.cube3.InteractiveCube.__init__`

**File:** [deepxube/domains/cube3.py:263](../../../../deepxube/domains/cube3.py#L263)
**Class:** `InteractiveCube`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, n, colors: NDArray, view = (0, 0, 10), fig = None, **kwargs) -> None
```

## Docstring

Initialise the axes, precompute face geometry, and draw the cube in ``fig``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `n` | — | — |
| `colors` | `NDArray` | — |
| `view` | — | `(0, 0, 10)` |
| `fig` | — | `None` |
| `**kwargs` | — | — |

## Returns

`None`

## Calls

- `np.eye` → `func:numpy.eye` (lines: 268)
- `np.asarray` → `func:numpy.asarray` (lines: 269, 270, 279)
- `plt.gcf` → `func:matplotlib.pyplot.gcf` (lines: 285)
- `plt.NullFormatter` → `func:matplotlib.pyplot.NullFormatter` (lines: 299, 300)
- `self._initialize_arrays` → `func:deepxube.domains.cube3.InteractiveCube._initialize_arrays` (lines: 332)
- `self._draw_cube` → `func:deepxube.domains.cube3.InteractiveCube._draw_cube` (lines: 341)

### Unresolved
- `Quaternion.from_v_theta` (lines: 269, 270, 279)
- `kwargs.update` (lines: 292)
- `dict` (lines: 292)
- `kwargs.get` (lines: 292, 293, 294, 295, 296, 297)
- `super(InteractiveCube, self).__init__` (lines: 298)
- `super` (lines: 298)
- `self.xaxis.set_major_formatter` (lines: 299)
- `self.yaxis.set_major_formatter` (lines: 300)
- `self.figure.canvas.mpl_connect` (lines: 334, 336, 338)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.N`
- `self._active`
- `self._ax_LR`
- `self._ax_LR_alt`
- `self._ax_UD`
- `self._black_stickers`
- `self._button1`
- `self._button2`
- `self._current_rot`
- `self._face_polys`
- `self._grey_stickers`
- `self._move_list`
- `self._prevStates`
- `self._start_rot`
- `self._start_xlim`
- `self._start_ylim`
- `self._step_LR`
- `self._step_UD`
- `self._sticker_polys`
- `self._tab`
- `self._view`
- `self.colors`
- `self.face_colors`
- `self.plastic_color`
- `self.rots`

**Reads:**
- `self.N`
- `self._active`
- `self._ax_LR`
- `self._ax_LR_alt`
- `self._ax_UD`
- `self._black_stickers`
- `self._button1`
- `self._button2`
- `self._current_rot`
- `self._face_polys`
- `self._grey_stickers`
- `self._mouse_motion`
- `self._mouse_press`
- `self._mouse_release`
- `self._move_list`
- `self._prevStates`
- `self._start_rot`
- `self._start_xlim`
- `self._start_ylim`
- `self._step_LR`
- `self._step_UD`
- `self._sticker_polys`
- `self._tab`
- `self._view`
- `self.colors`
- `self.face_colors`
- `self.figure`
- `self.plastic_color`
- `self.rots`
- `self.xaxis`
- `self.yaxis`

## Source

```python
    def __init__(self, n, colors: NDArray, view=(0, 0, 10), fig=None, **kwargs) -> None:  # type: ignore
        """ Initialise the axes, precompute face geometry, and draw the cube in ``fig``. """
        self.colors: NDArray = colors

        # Define rotation angles and axes for the six sides of the cube
        x, y, z = np.eye(3)
        self.rots = [Quaternion.from_v_theta(x, np.asarray(theta)) for theta in (np.pi / 2, -np.pi / 2)]
        self.rots += [Quaternion.from_v_theta(y, np.asarray(theta)) for theta in (np.pi / 2, -np.pi / 2, np.pi, 2 * np.pi)]

        rect = [0, 0.16, 1, 0.84]
        self._move_list: List = []

        self.N = n
        self._prevStates: List = []

        self._view = view
        self._start_rot: Quaternion = Quaternion.from_v_theta(np.asarray((1, -1, 0)), np.asarray(-np.pi / 6))

        self._grey_stickers: List = []
        self._black_stickers: List = []

        if fig is None:
            fig = plt.gcf()

        # disable default key press events
        # callbacks = fig.canvas.callbacks.callbacks
        # del callbacks['key_press_event']

        # add some defaults, and draw axes
        kwargs.update(dict(aspect=kwargs.get('aspect', 'equal'),
                           xlim=kwargs.get('xlim', (-1.7, 1.5)),
                           ylim=kwargs.get('ylim', (-1.5, 1.7)),
                           frameon=kwargs.get('frameon', False),
                           xticks=kwargs.get('xticks', []),
                           yticks=kwargs.get('yticks', [])))
        super(InteractiveCube, self).__init__(fig, rect, **kwargs)
        self.xaxis.set_major_formatter(plt.NullFormatter())  # type: ignore
        self.yaxis.set_major_formatter(plt.NullFormatter())  # type: ignore

        self._start_xlim = kwargs['xlim']
        self._start_ylim = kwargs['ylim']

        self._active = False  # true when mouse is over axes
        self._button1 = False  # true when button 1 is pressed
        self._button2 = False  # true when button 2 is pressed
        self._tab = False  # tab key pressed

        # Define movement for up/down arrows or up/down mouse movement
        self._ax_UD = (1, 0, 0)
        self._step_UD = 0.01

        # Define movement for left/right arrows or left/right mouse movement
        self._ax_LR = (0, -1, 0)
        self._step_LR = 0.01

        self._ax_LR_alt = (0, 0, 1)

        self._current_rot: Quaternion = self._start_rot  # current rotation state
        self._face_polys: Optional[List] = None
        self._sticker_polys: Optional[List] = None

        self.plastic_color = 'black'

        # WHITE:0 - U, YELLOW:1 - D, BLUE:2 - L, GREEN:3 - R, ORANGE: 4 - B, RED: 5 - F
        self.face_colors = ["w", "#ffcf00",
                            "#ff6f00", "#cf0000",
                            "#00008f", "#009f0f",
                            "gray", "none"]

        self._initialize_arrays()

        self.figure.canvas.mpl_connect('button_press_event',
                                       self._mouse_press)
        self.figure.canvas.mpl_connect('button_release_event',
                                       self._mouse_release)
        self.figure.canvas.mpl_connect('motion_notify_event',
                                       self._mouse_motion)

        self._draw_cube()
```
