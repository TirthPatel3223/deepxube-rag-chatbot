---
id: "func:deepxube.domains.cube3.Quaternion.as_rotation_matrix"
kind: "method"
name: "as_rotation_matrix"
qualified_name: "deepxube.domains.cube3.Quaternion.as_rotation_matrix"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 156
line_end: 176
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
returns: "NDArray"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.Quaternion.as_v_theta"
    expr: "self.as_v_theta"
    call_sites: [158]
  - target: null
    expr: "theta.reshape"
    call_sites: [161]
  - target: null
    expr: "v.reshape"
    call_sites: [162]
  - target: "func:numpy.cos"
    expr: "np.cos"
    call_sites: [163]
  - target: "func:numpy.sin"
    expr: "np.sin"
    call_sites: [164]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [166]
  - target: null
    expr: "mat.reshape"
    call_sites: [176]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Quaternion.as_rotation_matrix`

**File:** [deepxube/domains/cube3.py:156](../../../../deepxube/domains/cube3.py#L156)
**Class:** `Quaternion`
**Visibility:** public
**Kind:** method

## Signature

```python
def as_rotation_matrix(self) -> NDArray
```

## Docstring

Return the rotation matrix of the (normalized) quaternion

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`NDArray`

## Calls

- `self.as_v_theta` → `func:deepxube.domains.cube3.Quaternion.as_v_theta` (lines: 158)
- `np.cos` → `func:numpy.cos` (lines: 163)
- `np.sin` → `func:numpy.sin` (lines: 164)
- `np.array` → `func:numpy.array` (lines: 166)

### Unresolved
- `theta.reshape` (lines: 161)
- `v.reshape` (lines: 162)
- `mat.reshape` (lines: 176)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def as_rotation_matrix(self) -> NDArray:
        """Return the rotation matrix of the (normalized) quaternion"""
        v, theta = self.as_v_theta()

        shape = theta.shape
        theta = theta.reshape(-1)
        v = v.reshape(-1, 3).T
        c = np.cos(theta)
        s = np.sin(theta)

        mat = np.array([[v[0] * v[0] * (1. - c) + c,
                         v[0] * v[1] * (1. - c) - v[2] * s,
                         v[0] * v[2] * (1. - c) + v[1] * s],
                        [v[1] * v[0] * (1. - c) + v[2] * s,
                         v[1] * v[1] * (1. - c) + c,
                         v[1] * v[2] * (1. - c) - v[0] * s],
                        [v[2] * v[0] * (1. - c) - v[1] * s,
                         v[2] * v[1] * (1. - c) + v[0] * s,
                         v[2] * v[2] * (1. - c) + c]],
                       order='F').T
        return mat.reshape(shape + (3, 3))
```
