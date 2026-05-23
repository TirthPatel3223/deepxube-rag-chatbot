---
id: "class:deepxube.domains.cube3.InteractiveCube"
kind: "class"
name: "InteractiveCube"
qualified_name: "deepxube.domains.cube3.InteractiveCube"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 239
line_end: 507
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "plt.Axes"
    resolved_id: null
methods:
  - "func:deepxube.domains.cube3.InteractiveCube.__init__"
  - "func:deepxube.domains.cube3.InteractiveCube.set_rot"
  - "func:deepxube.domains.cube3.InteractiveCube._initialize_arrays"
  - "func:deepxube.domains.cube3.InteractiveCube.rotate"
  - "func:deepxube.domains.cube3.InteractiveCube._project"
  - "func:deepxube.domains.cube3.InteractiveCube._draw_cube"
  - "func:deepxube.domains.cube3.InteractiveCube._mouse_press"
  - "func:deepxube.domains.cube3.InteractiveCube._mouse_release"
  - "func:deepxube.domains.cube3.InteractiveCube._mouse_motion"
attributes:
  - name: "self.N"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._active"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._ax_LR"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._ax_LR_alt"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._ax_UD"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._black_stickers"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._button1"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._button2"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._current_rot"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._face_polys"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._grey_stickers"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._move_list"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._prevStates"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._start_rot"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._start_xlim"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._start_ylim"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._step_LR"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._step_UD"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._sticker_polys"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._tab"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._view"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.colors"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.face_colors"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.plastic_color"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.rots"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.cube3.InteractiveCube`

**File:** [deepxube/domains/cube3.py:239](../../../deepxube/domains/cube3.py#L239)
**Abstract:** no

## Docstring

Matplotlib Axes subclass that renders a 3D Rubik's Cube with mouse-driven rotation. 

## Inheritance

**Direct bases:**
- `plt.Axes`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `set_rot`
- `_initialize_arrays`
- `rotate` *(trivial, skipped)*
- `_project`
- `_draw_cube`
- `_mouse_press`
- `_mouse_release`
- `_mouse_motion`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.N` | — | __init__ |
| `self._active` | — | __init__ |
| `self._ax_LR` | — | __init__ |
| `self._ax_LR_alt` | — | __init__ |
| `self._ax_UD` | — | __init__ |
| `self._black_stickers` | — | __init__ |
| `self._button1` | — | __init__ |
| `self._button2` | — | __init__ |
| `self._current_rot` | — | __init__ |
| `self._face_polys` | — | __init__ |
| `self._grey_stickers` | — | __init__ |
| `self._move_list` | — | __init__ |
| `self._prevStates` | — | __init__ |
| `self._start_rot` | — | __init__ |
| `self._start_xlim` | — | __init__ |
| `self._start_ylim` | — | __init__ |
| `self._step_LR` | — | __init__ |
| `self._step_UD` | — | __init__ |
| `self._sticker_polys` | — | __init__ |
| `self._tab` | — | __init__ |
| `self._view` | — | __init__ |
| `self.colors` | — | __init__ |
| `self.face_colors` | — | __init__ |
| `self.plastic_color` | — | __init__ |
| `self.rots` | — | __init__ |

## Source

```python
class InteractiveCube(plt.Axes):  # type: ignore
    """ Matplotlib Axes subclass that renders a 3D Rubik's Cube with mouse-driven rotation. """

    # Define some attributes
    base_face = np.array([[1, 1, 1],
                          [1, -1, 1],
                          [-1, -1, 1],
                          [-1, 1, 1],
                          [1, 1, 1]], dtype=float)
    stickerwidth = 0.9
    stickermargin = 0.5 * (1. - stickerwidth)
    stickerthickness = 0.001
    (d1, d2, d3) = (1 - stickermargin,
                    1 - 2 * stickermargin,
                    1 + stickerthickness)
    base_sticker = np.array([[d1, d2, d3], [d2, d1, d3],
                             [-d2, d1, d3], [-d1, d2, d3],
                             [-d1, -d2, d3], [-d2, -d1, d3],
                             [d2, -d1, d3], [d1, -d2, d3],
                             [d1, d2, d3]], dtype=float)

    base_face_centroid = np.array([[0, 0, 1]])
    base_sticker_centroid = np.array([[0, 0, 1 + stickerthickness]])

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
        # self._initialize_widgets()

    def set_rot(self, rot: int) -> None:
        """ Set a preset camera orientation (``rot=0`` or ``rot=1``) and redraw. """
        if rot == 0:
            self._current_rot = Quaternion.from_v_theta(np.asarray((-0.53180525, 0.83020462, 0.16716299)), np.asarray(0.95063829))
        elif rot == 1:
            self._current_rot = Quaternion.from_v_theta(np.asarray((0.9248325, 0.14011997, -0.35362584)), np.asarray(2.49351394))

        self._draw_cube()

    def _initialize_arrays(self) -> None:
        """ Precompute face, sticker, and centroid geometry for all 6 faces and N² cubies per face. """
        # initialize centroids, faces, and stickers.  We start with a
        # base for each one, and then translate & rotate them into position.

        # Define N^2 translations for each face of the cube
        cubie_width = 2. / self.N
        translations = np.array([[[-1 + (i + 0.5) * cubie_width,
                                   -1 + (j + 0.5) * cubie_width, 0]]
                                 for i in range(self.N)
                                 for j in range(self.N)])

        # Create arrays for centroids, faces, stickers
        face_centroids = []
        faces = []
        sticker_centroids = []
        stickers = []
        colors = []

        factor = np.array([1. / self.N, 1. / self.N, 1])

        for i in range(6):
            rot_mat = self.rots[i].as_rotation_matrix()
            faces_t = np.dot(factor * self.base_face
                             + translations, rot_mat.T)
            stickers_t = np.dot(factor * self.base_sticker
                                + translations, rot_mat.T)
            face_centroids_t = np.dot(self.base_face_centroid
                                      + translations, rot_mat.T)
            sticker_centroids_t = np.dot(self.base_sticker_centroid
                                         + translations, rot_mat.T)
            # colors_i = i + np.zeros(face_centroids_t.shape[0], dtype=int)
            colors_i = np.arange(i * face_centroids_t.shape[0], (i + 1) * face_centroids_t.shape[0])

            # append face ID to the face centroids for lex-sorting
            face_centroids_t = np.hstack([face_centroids_t.reshape(-1, 3),
                                          colors_i[:, None]])
            sticker_centroids_t = sticker_centroids_t.reshape((-1, 3))

            faces.append(faces_t)
            face_centroids.append(face_centroids_t)
            stickers.append(stickers_t)
            sticker_centroids.append(sticker_centroids_t)

            colors.append(colors_i)

        self._face_centroids = np.vstack(face_centroids)
        self._faces = np.vstack(faces)
        self._sticker_centroids = np.vstack(sticker_centroids)
        self._stickers = np.vstack(stickers)

    def rotate(self, rot) -> None:  # type: ignore
        """ Compose ``rot`` onto the current view rotation. """
        self._current_rot = self._current_rot * rot

    def _project(self, pts):  # type: ignore
        """ :return: Projected 2D coordinates of ``pts`` under the current view rotation. """
        return project_points(pts, self._current_rot, self._view, [0, 1, 0])

    def _draw_cube(self) -> None:
        """ Project all faces and stickers and update (or create) their matplotlib Polygon patches. """
        stickers = self._project(self._stickers)[:, :, :2]
        faces = self._project(self._faces)[:, :, :2]
        face_centroids = self._project(self._face_centroids[:, :3])
        sticker_centroids = self._project(self._sticker_centroids[:, :3])

        plastic_color = self.plastic_color
        # self._colors[np.ravel_multi_index((0,1,2),(6,N,N))] = 10
        colors = np.asarray(self.face_colors)[self.colors]
        for idx in self._grey_stickers:
            colors[idx] = "grey"
        for idx in self._black_stickers:
            colors[idx] = "k"

        face_zorders = -face_centroids[:, 2]
        sticker_zorders = -sticker_centroids[:, 2]

        if self._face_polys is None:
            # initial call: create polygon objects and add to axes
            self._face_polys = []
            self._sticker_polys = []

            for i in range(len(colors)):
                fp = plt.Polygon(faces[i], facecolor=plastic_color, zorder=face_zorders[i])  # type: ignore
                sp = plt.Polygon(stickers[i], facecolor=colors[i], zorder=sticker_zorders[i])  # type: ignore

                self._face_polys.append(fp)
                self._sticker_polys.append(sp)
                self.add_patch(fp)
                self.add_patch(sp)
        else:
            assert self._sticker_polys is not None
            # subsequent call: updater the polygon objects
            for i in range(len(colors)):
                self._face_polys[i].set_xy(faces[i])
                self._face_polys[i].set_zorder(face_zorders[i])
                self._face_polys[i].set_facecolor(plastic_color)

                self._sticker_polys[i].set_xy(stickers[i])
                self._sticker_polys[i].set_zorder(sticker_zorders[i])
                self._sticker_polys[i].set_facecolor(colors[i])

        self.figure.canvas.draw()

    def _mouse_press(self, event, event_x=None, event_y=None):  # type: ignore
        """ Record the mouse position and which button was pressed to start a drag. """
        if event_x is not None and event_y is not None:
            self._event_xy = (event_x, event_y)
            self._button1 = True
        else:
            self._event_xy = (event.x, event.y)
            if event.button == 1:
                self._button1 = True
            elif event.button == 3:
                self._button2 = True

    def _mouse_release(self, event):  # type: ignore
        """ Clear drag state when a mouse button is released. """
        self._event_xy = None  # type: ignore
        if event.button == 1:
            self._button1 = False
        elif event.button == 3:
            self._button2 = False

    def _mouse_motion(self, event, event_x=None, event_y=None):  # type: ignore
        """ Rotate the view (button 1) or zoom (button 2) in response to mouse drag. """
        if self._button1 or self._button2:
            if event_x is not None and event_y is not None:
                dx = event_x - self._event_xy[0]
                dy = event_y - self._event_xy[1]
                self._event_xy = (event_x, event_y)
            else:
                dx = event.x - self._event_xy[0]
                dy = event.y - self._event_xy[1]
                self._event_xy = (event.x, event.y)

            if self._button1:
                if self._tab:
                    ax_lr = self._ax_LR_alt
                else:
                    ax_lr = self._ax_LR
                rot1 = Quaternion.from_v_theta(self._ax_UD, self._step_UD * dy)
                rot2 = Quaternion.from_v_theta(ax_lr, self._step_LR * dx)
                self.rotate(rot1 * rot2)

                self._draw_cube()

            if self._button2:
                factor = 1 - 0.003 * (dx + dy)
                xlim = self.get_xlim()
                ylim = self.get_ylim()
                self.set_xlim(factor * xlim[0], factor * xlim[1])
                self.set_ylim(factor * ylim[0], factor * ylim[1])

                self.figure.canvas.draw()
```
