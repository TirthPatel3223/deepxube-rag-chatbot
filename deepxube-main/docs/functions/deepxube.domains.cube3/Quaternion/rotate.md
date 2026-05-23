---
id: "func:deepxube.domains.cube3.Quaternion.rotate"
kind: "method"
name: "rotate"
qualified_name: "deepxube.domains.cube3.Quaternion.rotate"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 178
line_end: 181
class: "Quaternion"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "points"
    annotation: null
    default: null
returns: null
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.Quaternion.as_rotation_matrix"
    expr: "self.as_rotation_matrix"
    call_sites: [180]
  - target: "func:numpy.dot"
    expr: "np.dot"
    call_sites: [181]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Quaternion.rotate`

**File:** [deepxube/domains/cube3.py:178](../../../../deepxube/domains/cube3.py#L178)
**Class:** `Quaternion`
**Visibility:** public
**Kind:** method

## Signature

```python
def rotate(self, points)
```

## Docstring

:return: ``points`` rotated by this quaternion's rotation matrix. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `points` | — | — |

## Returns

*(Not annotated.)*

## Calls

- `self.as_rotation_matrix` → `func:deepxube.domains.cube3.Quaternion.as_rotation_matrix` (lines: 180)
- `np.dot` → `func:numpy.dot` (lines: 181)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def rotate(self, points):  # type: ignore
        """ :return: ``points`` rotated by this quaternion's rotation matrix. """
        rot_mat = self.as_rotation_matrix()
        return np.dot(points, rot_mat.T)
```
