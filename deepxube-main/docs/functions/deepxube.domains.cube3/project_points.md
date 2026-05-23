---
id: "func:deepxube.domains.cube3.project_points"
kind: "function"
name: "project_points"
qualified_name: "deepxube.domains.cube3.project_points"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 184
line_end: 236
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "points"
    annotation: null
    default: null
  - name: "q"
    annotation: "Quaternion"
    default: null
  - name: "view"
    annotation: null
    default: null
  - name: "vertical"
    annotation: null
    default: null
returns: "NDArray"
docstring_source: "present"
callees:
  - target: "func:numpy.asarray"
    expr: "np.asarray"
    call_sites: [206, 207]
  - target: null
    expr: "np.cross(vertical, view).astype"
    call_sites: [209]
  - target: "func:numpy.cross"
    expr: "np.cross"
    call_sites: [209, 217]
  - target: "func:numpy.all"
    expr: "np.all"
    call_sites: [211]
  - target: null
    expr: "ValueError"
    call_sites: [212]
  - target: "func:numpy.sqrt"
    expr: "np.sqrt"
    call_sites: [214, 218, 222]
  - target: "func:numpy.dot"
    expr: "np.dot"
    call_sites: [214, 218, 221, 226, 230, 234, 235, 236]
  - target: null
    expr: "q.as_rotation_matrix"
    call_sites: [225]
  - target: null
    expr: "np.dot(dpoint, view).reshape"
    call_sites: [230]
  - target: null
    expr: "list"
    call_sites: [233]
  - target: null
    expr: "range"
    call_sites: [233]
  - target: null
    expr: "np.array([np.dot(dproj, xdir), np.dot(dproj, ydir), -np.dot(dpoint, zdir)]).transpose"
    call_sites: [234]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [234]
raises:
  - exception: "ValueError"
    call_sites: [212]
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.project_points`

**File:** [deepxube/domains/cube3.py:184](../../../../deepxube/domains/cube3.py#L184)
**Visibility:** public
**Kind:** function

## Signature

```python
def project_points(points, q: Quaternion, view, vertical) -> NDArray
```

## Docstring

Project points using a quaternion q and a view v

Parameters
----------
points : array_like
    array of last-dimension 3
q : utils.viz_utils.Quaternion
    quaternion representation of the rotation
view : array_like
    length-3 vector giving the point of view
vertical : array_like
    direction of y-axis for view.  An error will be raised if it
    is parallel to the view.

Returns
-------
proj: array_like
    array of projected points: same shape as points.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `points` | — | — |
| `q` | `Quaternion` | — |
| `view` | — | — |
| `vertical` | — | — |

## Returns

`NDArray`

## Calls

- `np.asarray` → `func:numpy.asarray` (lines: 206, 207)
- `np.cross` → `func:numpy.cross` (lines: 209, 217)
- `np.all` → `func:numpy.all` (lines: 211)
- `np.sqrt` → `func:numpy.sqrt` (lines: 214, 218, 222)
- `np.dot` → `func:numpy.dot` (lines: 214, 218, 221, 226, 230, 234, 235, 236)
- `np.array` → `func:numpy.array` (lines: 234)

### Unresolved
- `np.cross(vertical, view).astype` (lines: 209)
- `ValueError` (lines: 212)
- `q.as_rotation_matrix` (lines: 225)
- `np.dot(dpoint, view).reshape` (lines: 230)
- `list` (lines: 233)
- `range` (lines: 233)
- `np.array([np.dot(dproj, xdir), np.dot(dproj, ydir), -np.dot(dpoint, zdir)]).transpose` (lines: 234)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 212)

## Source

```python
def project_points(points, q: Quaternion, view, vertical) -> NDArray:  # type: ignore
    """Project points using a quaternion q and a view v

    Parameters
    ----------
    points : array_like
        array of last-dimension 3
    q : utils.viz_utils.Quaternion
        quaternion representation of the rotation
    view : array_like
        length-3 vector giving the point of view
    vertical : array_like
        direction of y-axis for view.  An error will be raised if it
        is parallel to the view.

    Returns
    -------
    proj: array_like
        array of projected points: same shape as points.
    """
    if vertical is None:
        vertical = [0, 1, 0]
    points = np.asarray(points)
    view = np.asarray(view)

    xdir = np.cross(vertical, view).astype(float)

    if np.all(xdir == 0):
        raise ValueError("vertical is parallel to v")

    xdir /= np.sqrt(np.dot(xdir, xdir))

    # get the unit vector corresponing to vertical
    ydir = np.cross(view, xdir)
    ydir /= np.sqrt(np.dot(ydir, ydir))

    # normalize the viewer location: this is the z-axis
    v2 = np.dot(view, view)
    zdir = view / np.sqrt(v2)

    # rotate the points
    rot_mat = q.as_rotation_matrix()
    r_pts = np.dot(points, rot_mat.T)

    # project the points onto the view
    dpoint = r_pts - view
    dpoint_view = np.dot(dpoint, view).reshape(dpoint.shape[:-1] + (1,))
    dproj = -dpoint * v2 / dpoint_view

    trans = list(range(1, dproj.ndim)) + [0]
    return np.array([np.dot(dproj, xdir),
                     np.dot(dproj, ydir),
                     -np.dot(dpoint, zdir)]).transpose(trans)
```
