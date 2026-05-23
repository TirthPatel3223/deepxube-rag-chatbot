---
id: "func:deepxube.domains.cube3.InteractiveCube._initialize_arrays"
kind: "method"
name: "_initialize_arrays"
qualified_name: "deepxube.domains.cube3.InteractiveCube._initialize_arrays"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 353
line_end: 402
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
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [360, 372]
  - target: null
    expr: "range"
    call_sites: [362, 363, 374]
  - target: null
    expr: "self.rots[i].as_rotation_matrix"
    call_sites: [375]
  - target: "func:numpy.dot"
    expr: "np.dot"
    call_sites: [376, 378, 380, 382]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [385]
  - target: "func:numpy.hstack"
    expr: "np.hstack"
    call_sites: [388]
  - target: null
    expr: "face_centroids_t.reshape"
    call_sites: [388]
  - target: null
    expr: "sticker_centroids_t.reshape"
    call_sites: [390]
  - target: null
    expr: "faces.append"
    call_sites: [392]
  - target: null
    expr: "face_centroids.append"
    call_sites: [393]
  - target: null
    expr: "stickers.append"
    call_sites: [394]
  - target: null
    expr: "sticker_centroids.append"
    call_sites: [395]
  - target: null
    expr: "colors.append"
    call_sites: [397]
  - target: "func:numpy.vstack"
    expr: "np.vstack"
    call_sites: [399, 400, 401, 402]
raises: []
reads_attrs:
  - "self.N"
  - "self._face_centroids"
  - "self._faces"
  - "self._sticker_centroids"
  - "self._stickers"
  - "self.base_face"
  - "self.base_face_centroid"
  - "self.base_sticker"
  - "self.base_sticker_centroid"
  - "self.rots"
writes_attrs:
  - "self._face_centroids"
  - "self._faces"
  - "self._sticker_centroids"
  - "self._stickers"
---

# `deepxube.domains.cube3.InteractiveCube._initialize_arrays`

**File:** [deepxube/domains/cube3.py:353](../../../../deepxube/domains/cube3.py#L353)
**Class:** `InteractiveCube`
**Visibility:** private
**Kind:** method

## Signature

```python
def _initialize_arrays(self) -> None
```

## Docstring

Precompute face, sticker, and centroid geometry for all 6 faces and N² cubies per face. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

- `np.array` → `func:numpy.array` (lines: 360, 372)
- `np.dot` → `func:numpy.dot` (lines: 376, 378, 380, 382)
- `np.arange` → `func:numpy.arange` (lines: 385)
- `np.hstack` → `func:numpy.hstack` (lines: 388)
- `np.vstack` → `func:numpy.vstack` (lines: 399, 400, 401, 402)

### Unresolved
- `range` (lines: 362, 363, 374)
- `self.rots[i].as_rotation_matrix` (lines: 375)
- `face_centroids_t.reshape` (lines: 388)
- `sticker_centroids_t.reshape` (lines: 390)
- `faces.append` (lines: 392)
- `face_centroids.append` (lines: 393)
- `stickers.append` (lines: 394)
- `sticker_centroids.append` (lines: 395)
- `colors.append` (lines: 397)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._face_centroids`
- `self._faces`
- `self._sticker_centroids`
- `self._stickers`

**Reads:**
- `self.N`
- `self._face_centroids`
- `self._faces`
- `self._sticker_centroids`
- `self._stickers`
- `self.base_face`
- `self.base_face_centroid`
- `self.base_sticker`
- `self.base_sticker_centroid`
- `self.rots`

## Source

```python
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
```
