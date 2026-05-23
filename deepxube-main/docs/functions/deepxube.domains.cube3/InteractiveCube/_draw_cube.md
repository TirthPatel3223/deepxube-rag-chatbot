---
id: "func:deepxube.domains.cube3.InteractiveCube._draw_cube"
kind: "method"
name: "_draw_cube"
qualified_name: "deepxube.domains.cube3.InteractiveCube._draw_cube"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 412
line_end: 455
class: "InteractiveCube"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.InteractiveCube._project"
    expr: "self._project"
    call_sites: [414, 415, 416, 417]
  - target: "func:numpy.asarray"
    expr: "np.asarray"
    call_sites: [421]
  - target: null
    expr: "range"
    call_sites: [435, 446]
  - target: null
    expr: "len"
    call_sites: [435, 446]
  - target: "func:matplotlib.pyplot.Polygon"
    expr: "plt.Polygon"
    call_sites: [436, 437]
  - target: null
    expr: "self._face_polys.append"
    call_sites: [439]
  - target: null
    expr: "self._sticker_polys.append"
    call_sites: [440]
  - target: "func:deepxube.domains.cube3.InteractiveCube.add_patch"
    expr: "self.add_patch"
    call_sites: [441, 442]
  - target: null
    expr: "self._face_polys[i].set_xy"
    call_sites: [447]
  - target: null
    expr: "self._face_polys[i].set_zorder"
    call_sites: [448]
  - target: null
    expr: "self._face_polys[i].set_facecolor"
    call_sites: [449]
  - target: null
    expr: "self._sticker_polys[i].set_xy"
    call_sites: [451]
  - target: null
    expr: "self._sticker_polys[i].set_zorder"
    call_sites: [452]
  - target: null
    expr: "self._sticker_polys[i].set_facecolor"
    call_sites: [453]
  - target: null
    expr: "self.figure.canvas.draw"
    call_sites: [455]
raises: []
reads_attrs:
  - "self._black_stickers"
  - "self._face_centroids"
  - "self._face_polys"
  - "self._faces"
  - "self._grey_stickers"
  - "self._sticker_centroids"
  - "self._sticker_polys"
  - "self._stickers"
  - "self.colors"
  - "self.face_colors"
  - "self.figure"
  - "self.plastic_color"
writes_attrs:
  - "self._face_polys"
  - "self._sticker_polys"
---

# `deepxube.domains.cube3.InteractiveCube._draw_cube`

**File:** [deepxube/domains/cube3.py:412](../../../../deepxube/domains/cube3.py#L412)
**Class:** `InteractiveCube`
**Visibility:** private
**Kind:** method

## Signature

```python
def _draw_cube(self) -> None
```

## Docstring

Project all faces and stickers and update (or create) their matplotlib Polygon patches. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

- `self._project` → `func:deepxube.domains.cube3.InteractiveCube._project` (lines: 414, 415, 416, 417)
- `np.asarray` → `func:numpy.asarray` (lines: 421)
- `plt.Polygon` → `func:matplotlib.pyplot.Polygon` (lines: 436, 437)
- `self.add_patch` → `func:deepxube.domains.cube3.InteractiveCube.add_patch` (lines: 441, 442)

### Unresolved
- `range` (lines: 435, 446)
- `len` (lines: 435, 446)
- `self._face_polys.append` (lines: 439)
- `self._sticker_polys.append` (lines: 440)
- `self._face_polys[i].set_xy` (lines: 447)
- `self._face_polys[i].set_zorder` (lines: 448)
- `self._face_polys[i].set_facecolor` (lines: 449)
- `self._sticker_polys[i].set_xy` (lines: 451)
- `self._sticker_polys[i].set_zorder` (lines: 452)
- `self._sticker_polys[i].set_facecolor` (lines: 453)
- `self.figure.canvas.draw` (lines: 455)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._face_polys`
- `self._sticker_polys`

**Reads:**
- `self._black_stickers`
- `self._face_centroids`
- `self._face_polys`
- `self._faces`
- `self._grey_stickers`
- `self._sticker_centroids`
- `self._sticker_polys`
- `self._stickers`
- `self.colors`
- `self.face_colors`
- `self.figure`
- `self.plastic_color`

## Source

```python
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
```
